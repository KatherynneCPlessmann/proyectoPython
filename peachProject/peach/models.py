from django.db import models

class Proveedor(models.Model):
    nombres= models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=250)
    direccion= models.CharField(max_length=200)
    telefono= models.CharField(max_length=10)
    correo = models.EmailField()

    def __str__(self):
        return self.empresa

class Cliente(models.Model):
    nombres= models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=250)
    direccion= models.CharField(max_length=200)
    telefono= models.CharField(max_length=10)
    correo = models.EmailField()
    referencia = models.CharField(max_length=100)

    def __str__(self):
        return  self.empresa

class TipoArticulo(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return  self.nombre

class TipoServicio(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return  self.nombre

class Comentario(models.Model):
    nombre= models.CharField(max_length=50)
    fecha= models.DateField()
    descripcion= models.TextField(max_length=250)

    def __str__(self):
        return  self.nombre

class Contacto(models.Model):
    nombres= models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=250)
    direccion= models.CharField(max_length=200)
    telefono= models.CharField(max_length=10)
    correo = models.EmailField()
    interes = models.CharField(max_length=200)

    def __str__(self):
        return  self.empresa

class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    precio = models.FloatField()
    Tipo = models.ForeignKey(TipoArticulo, on_delete=models.CASCADE) #llave foranea

    def __str__(self):
        return  self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    costo = models.FloatField()
    Tipo = models.ForeignKey(TipoServicio, on_delete=models.CASCADE) #llave foranea

    def __str__(self):
        return  self.nombre

class Compra(models.Model):
    numero = models.IntegerField()
    fecha= models.DateTimeField()
    recibido = models.BooleanField()
    proveedor= models.ForeignKey(Proveedor, on_delete=models.CASCADE)  # llave foranea
    articuloCompra = models.ManyToManyField(Articulo) #muchos a muchos


class Venta(models.Model):
    numero = models.IntegerField()
    fecha = models.DateTimeField()
    costoAdicional = models.FloatField()
    cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)  # llave foranea
    servicioVenta = models.ManyToManyField(Servicio) #muchos a muchos

class Estado(models.Model):
    estado= models.CharField(max_length=70)

    def __str__(self):
        return  self.estado

class Encuesta(models.Model):
    ocupacion = models.CharField(max_length=80)
    experiencia = models.IntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE) #llave foranea

    def __str__(self):
        return  self.ocupacion



