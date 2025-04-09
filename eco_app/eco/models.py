from django.db import models

class EcoHabit(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cumplido = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
