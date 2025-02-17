# api/serializers.py
from rest_framework import serializers  # Correct import
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio']  # Fields from your Producto model


