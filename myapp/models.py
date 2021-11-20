from django.db import models


class Formulario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.nome
