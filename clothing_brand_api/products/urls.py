from django.urls import path
from .views import ProductListCreateView, ProductDetailView




urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('brand/<int:brand_id>/add/', ProductListCreateView.as_view(), name='product-create'),
]
