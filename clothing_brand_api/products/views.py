from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from brands.models import Brand
from .permissions import IsProductOwner

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        brand = Brand.objects.get(pk=self.kwargs['brand_id'])
        if brand.owner != self.request.user:
            raise PermissionError("You are not allowed to add products to this brand.")
        serializer.save(brand=brand)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsProductOwner()]
        return [permissions.AllowAny()]


