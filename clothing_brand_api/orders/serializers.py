from rest_framework import serializers
from .models import Cart, Order
from products.models import Product




class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_field = ['customer', 'total_price']
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

        read_only_fields = ['customer', 'total_price', 'date_ordered']
