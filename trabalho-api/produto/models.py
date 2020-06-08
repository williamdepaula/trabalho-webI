from django.db import models
from categoria.models import Categoria

class Produto(models.Model):

    class Meta:
        db_table = 'produto'

    nome = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    descricao = models.TextField()
    custo = models.DecimalField(max_digits=6, decimal_places=2)
    valor_venda = models.DecimalField(max_digits=6, decimal_places=2)
    url_img = models.URLField(max_length=200)

    def __str__(self):
        return self.nome
