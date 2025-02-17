from rest_framework import generics
from .models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


class ProductoList(generics.ListAPIView):  # Tu vista para listar productos
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveAPIView):  # Nueva vista para detalles
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


 
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Or your custom registration form
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})