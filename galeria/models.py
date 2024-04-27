from datetime import datetime

from django.db import models


# Create your models here.

class Fotografia(models.Model):
    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galaxia'),
        ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(choices=OPCOES_CATEGORIA, default='', max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', null=True, blank=True)
    publicada = models.BooleanField(default=False, null=False, blank=False)
    data_fotografia = models.DateTimeField(blank=False, default=datetime.now())

    def __str__(self):
        return self.nome
