from django.db import models


# Create your models here.
class Padawan(models.Model):
    idUser = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    def __str__(self):
        txt = "nombre: {0} / usuario: {1}"
        return txt.format(self.nombre, self.username)


class Area(models.Model):
    id_Areas = models.AutoField(primary_key=True)
    area = models.CharField(max_length=30, default='Ejemplo: Back / Front / Devs')
    orientado = models.CharField(max_length=100, null=False, blank=True)
    descripcion = models.CharField(max_length=100, null=False, blank=True)
    conocimiento = models.CharField(max_length=100, null=False, blank=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.area)

class Jedi(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    area = models.ForeignKey(Area, null=False, blank=False, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        txt = "Jedi: {0} / Area: {1}"
        return txt.format(self.nombre, self.area)

class Erona(models.Model):
    usuario = models.ForeignKey(Padawan, null=False, blank=False, on_delete=models.CASCADE)
    id_Jedi = models.ForeignKey(Jedi, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        txt = "[Padawan: {0}] de [{1}]"
        return txt.format(self.usuario, self.id_Jedi)
