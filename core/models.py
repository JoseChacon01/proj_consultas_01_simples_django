from django.db import models

class Area(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Publico(models.Model):
    nome = models.CharField('Nome', max_length=100)

class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100)
    data_inicio = models.DateField('Data de Início')
    vagas = models.IntegerField('Vagas')
    area = models.ForeignKey(Area, on_delete=models.PROTECT)
    publicos = models.ManyToManyField(Publico)

