from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Cart, Order
from .serializers import CartSerializer, OrderSerializer
from products.models import Product

# Create your views here.


class CartView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(customer=self.request.user)
        return cart



    def delete(self, request, *args, **kwargs):
        cart = self.get_object()
        cart.products.clear()
        cart.update_total()
        return Response({"message":"Cart cleared."}, status=status.HTTP_204_NO_CONTENT)
    
class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)
    
    def perform_create(self, serializer):
        cart = Cart.objects.get(customer=self.request.user)
        serializer.save(customer=self.request.user, total_price=cart.total_price)
        cart.products.clear()
        cart.update_total()


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


    def patch(self, request, *args, **kwargs):
        order = self.get_object()
        if request.user.role != 'brand_owner':
            return Response({"error": "Only brand owners can update status"}, status=403)
        return super().patch(request, *args, **kwargs)
    


class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


    def delete(self, request, *args, **kwargs):
        order = self.get_object()
        if order.customer !=request.user:
            return Response({"error":"You can only cancel your own orders."}, status=403)
        return super().delete(request, *args, **kwargs)
    