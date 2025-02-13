from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers  # Importa serializers

class ProductoSerializer(serializers.Serializer):  # Serializador Manual
    id = serializers.IntegerField()
    nombre = serializers.CharField(max_length=200)
    descripcion = serializers.CharField()
    precio = serializers.DecimalField(max_digits=10, decimal_places=2)
    imagen = serializers.URLField()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lista_productos(request):
    """
    Retorna un catálogo predefinido de 4 productos diferentes.
    """
    productos = [
        {
            'id': 1,
            'nombre': 'Camiseta Algodón Orgánico',
            'descripcion': 'Camiseta suave y cómoda hecha de algodón 100% orgánico.',
            'precio': 25.99,
            'imagen': 'https://ejemplo.com/camiseta.jpg',
        },
        {
            'id': 2,
            'nombre': 'Pantalón Vaquero Slim Fit',
            'descripcion': 'Pantalón vaquero moderno con corte ajustado y tejido resistente.',
            'precio': 59.99,
            'imagen': 'https://ejemplo.com/pantalon.jpg',
        },
        {
            'id': 3,
            'nombre': 'Zapatillas Deportivas Running',
            'descripcion': 'Zapatillas ligeras y transpirables ideales para correr y entrenar.',
            'precio': 89.99,
            'imagen': 'https://ejemplo.com/zapatillas.jpg',
        },
        {
            'id': 4,
            'nombre': 'Bolso Bandolera de Cuero',
            'descripcion': 'Bolso elegante y práctico para llevar tus objetos esenciales.',
            'precio': 45.50,
            'imagen': 'https://ejemplo.com/bolso.jpg',
        },
    ]

    serializer = ProductoSerializer(productos, many=True)  # Serializa la lista
    return Response(serializer.data)  # Retorna los datos serializados