from django.db import models

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

class Producto(models.Model): #Esto es PRODUCTOS
    id = models.AutoField(primary_key = True)
    nombre_producto = models.CharField(max_length = 200, blank = False, null = False)
    cantidad = models.CharField(max_length = 200, blank = False, null = False)
    proveedor = models.ForeignKey('Proveedor' , on_delete=models.SET_NULL, null=True, blank=False)
    descripcion = models.TextField(blank = False, null = False)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre_producto']
        
    def __str__(self):
        return self.nombre_producto


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


class Proveedor(models.Model): #Esto es PROVEEDOR
    id = models.AutoField(primary_key = True)
    nombre_proveedor = models.CharField('Nombre proveedor', max_length = 255, blank = False, null = True)
    correo_proveedor = models.EmailField('Correo proveedor', max_length=255, blank = False, null = True)
    telefono_proveedor = models.CharField('Teléfono proveedor', max_length=12, blank = False, null = True)
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']
        
    def __str__(self):
        return self.nombre_proveedor


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


class Mesa(models.Model):
    id = models.AutoField(primary_key = True)
    numero_mesa = models.CharField('Número de la mesa', max_length = 2, blank = False, null = True)
    descripcion_mesa = models.CharField('Descripción mesa', max_length = 255, blank = False, null = True)
    cantidad_personas = models.CharField('Cantidad de personas', max_length=2, blank = False, null = True)
    
    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
        ordering = ['numero_mesa']
        
    def __str__(self):
        return f'Mesa N°{self.numero_mesa}, {self.descripcion_mesa} para {self.cantidad_personas} personas'


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


class Receta(models.Model):
    id = models.AutoField(primary_key = True)
    nombre_receta = models.CharField('Nombre de la receta o bebestible', max_length = 255, db_index=True)
    precio_receta = models.FloatField('Precio de la receta o bebestible', max_length=10)
    image = models.ImageField(upload_to = "recetas y bebestibles", blank=True, null=False)
    tiempo_preparacion = models.CharField('Tiempo de preparación', max_length=2, blank = False, null = True)
    
    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
        ordering = ['id']
        
    def __str__(self):
        return self.nombre_receta


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------


class Bodega(models.Model):
    id = models.AutoField(primary_key = True)
    proveedor = models.ForeignKey('Proveedor' , on_delete=models.SET_NULL, null=True, blank=False)
    productos = models.ForeignKey('Producto' , on_delete=models.SET_NULL, null=True, blank=False)
    cantidad = models.CharField('Cantidad' , max_length = 2, blank = False, null = True)

    class Meta:
        verbose_name = 'Bodega'
        verbose_name_plural = 'Bodegas'
        ordering = ['proveedor']

    def __str__(self):
        return self.cantidad
