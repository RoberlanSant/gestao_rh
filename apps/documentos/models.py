from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.

class Documento(models.Model):
    discricao = models.CharField(max_length=100)
    pertece = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return  self.discricao