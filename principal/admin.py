from django.contrib import admin
from .models import Supermercado, Produto, Preco, Compra

class CompraInline(admin.TabularInline):
    model = Compra
    extra = 0

class PrecoInline(admin.TabularInline):
    model = Preco
    extra = 0

@admin.register(Supermercado)
class SupermercadoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    inlines = [CompraInline]

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['supermercado', 'nome']
    inlines = [PrecoInline]
