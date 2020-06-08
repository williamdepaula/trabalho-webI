from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    tipo_categoria = serializers.ChoiceField(
        choices= Categoria.TIPO_CATEGORIA
    )

    class Meta:

        model = Categoria
        fields = '__all__'

    