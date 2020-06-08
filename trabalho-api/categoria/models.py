from django.db import models

class Categoria(models.Model):

    TIPO_CATEGORIA = (
        ('P', 'Produto'),
        ('S', 'Servico'),
    )

    class Meta:

        db_table = 'categoria'

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    tipo_categoria = models.CharField(max_length=1, choices=TIPO_CATEGORIA)

    def __str__(self):
        return self.nome