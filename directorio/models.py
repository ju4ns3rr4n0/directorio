from django.db import models

class Directorio(models.Model):
    persona = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

    def __str__(self):
        return self.persona
