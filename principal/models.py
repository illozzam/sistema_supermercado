from django.db import models

class Supermercado(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    supermercado = models.ForeignKey(Supermercado, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Preco(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return '{} - R$ {}'.format(
            self.produto.nome,
            self.preco
        )

class Compra(models.Model):
    supermercado = models.ForeignKey(Supermercado, on_delete=models.DO_NOTHING)
    data_hora = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto)
    quantidade = models.IntegerField()
    preco = models.ForeignKey(Preco, on_delete=models.DO_NOTHING)

    def __str__(self):
        return 'Compra em {}'.format(self.data_hora)
