from django.db import models

class Tarea(models.Model):
    descripcion = models.TextField(default="")
    eliminada = models.BooleanField(default=False)


class SubTarea(models.Model):
    descripcion = models.TextField(default="")
    eliminada = models.BooleanField(default=False)
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE, null=False)
