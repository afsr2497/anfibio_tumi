from django.db import models
import datetime

# Create your models here.

class usr_anfibio(models.Model):
    nombre = models.CharField(max_length=64,default='')
    apellido = models.CharField(max_length=64,default='')
    rol_usr = models.CharField(max_length=32,default='')
    codigo_usr = models.CharField(max_length=32,default='')
    nro_celular = models.CharField(max_length=32,default='')
    email_usr = models.CharField(max_length=64,default='')
    fecha_registro = models.DateField(default=datetime.date.today)
    cod_verificacion = models.CharField(max_length=64,default='')
    usr_password = models.CharField(max_length=64,default='')

class barcos_anfibio(models.Model):
    nombre_barco = models.CharField(max_length=64,default='')
    codigo_barco = models.CharField(max_length=32,default='')
    ruta_foto = models.CharField(max_length=64,default='')
    fabricante_barco = models.CharField(max_length=64,default='')
    ubicacion = models.CharField(max_length=64,default='')

class operacion_anfibio(models.Model):
    fecha_operacion = models.DateField(default=datetime.date.today)
    distancia_operacion = models.CharField(max_length=64,default='')
    duracion_operacion = models.CharField(max_length=64,default='')
    codigo_embarcacion = models.CharField(max_length=64,default='')
    codigo_usuario = models.CharField(max_length=64,default='')


class img_anfibio(models.Model):
    ruta_img = models.CharField(max_length=64,default='')
    codigo_img = models.CharField(max_length=64,default='')
    res_img = models.CharField(max_length=64,default='')
    fecha_img = models.DateField(default=datetime.date.today)
    peso_img = models.CharField(max_length=64,default='')
    codigo_operacion = models.CharField(max_length=64,default='')


class video_anfibio(models.Model):
    ruta_video = models.CharField(max_length=64,default='')
    codigo_video = models.CharField(max_length=64,default='')
    res_video = models.CharField(max_length=64,default='')
    fecha_video = models.DateField(default=datetime.date.today)
    duracion_video = models.CharField(max_length=64,default='')
    peso_video = models.CharField(max_length=64,default='')
    codigo_operacion = models.CharField(max_length=64,default='')