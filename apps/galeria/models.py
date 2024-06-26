from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


#representa uma tabela no banco de dados
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta")
    ]

    nome = models.CharField(max_length=100,null=False,blank=False) #campo string,nao pode ser vazio. blank é como se fosse uma String vazia
    legenda = models.CharField(max_length=150,null=False,blank=False) 
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False,blank=False) #campo para texto como paragrafo...longo
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True ) # y=ano,m=mes,d=dia
    publicada = models.BooleanField(default=True) #item começa não publicada
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(#um usuario pra cada fotografia nova
        to=User,#associou a tabela de usuario
        on_delete= models.SET_NULL,#caso o usuario for deletado, define ele como null
        null=True,
        blank=False,
        related_name="user", #localiza melhor a tabela
    )

    #boa prática
    #função que devolve um nome dos cada itens
    def __str__(self):
        return self.nome