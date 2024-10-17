from django.db import models
from django.utils import timezone

class Notice(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    tempo = models.DurationField()

    def __str__(self):
        return f'{self.nome} - {self.data} {self.hora}, Tempo: {self.tempo}'