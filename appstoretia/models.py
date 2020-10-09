from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        usuario = self.model(username = username,
                             email=self.normalize_email(email),
                             nombres= nombres,
                             apellidos = apellidos
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    def create_superuser(self,email,username,nombres,apellidos,password):
        usuario = self.create_user(
            email,
            username = username,
            nombres = nombres,
            apellidos = apellidos,
            password= password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de Usuario', unique=True, max_length=20)
    email = models.EmailField('Email', unique=True, max_length=254)
    objects = UsuarioManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'Usuario {self.nombres}{self.apellidos}'
    def has_perm(self, perm, obj = None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.usuario_administrador


class Tiendas(models.Model):
    store = models.IntegerField(primary_key=True,default=None)
    type = models.CharField(max_length=1,default=None)
    size = models.DecimalField(max_digits=10, decimal_places=2, default=None)

    def __str__(self):
        return str(self.store)

class Caracteristicas(models.Model):
    store = models.ForeignKey(Tiendas, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField()
    temperature = models.DecimalField(max_digits=6, decimal_places=2, default=None)
    fuel_price = models.DecimalField(max_digits=8, decimal_places=3, default=None)
    markdown1 = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    markdown2 = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    markdown3 = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    markdown4 = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    markdown5 = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    cpi = models.DecimalField(max_digits=16, decimal_places=2, default=None)
    unemployme = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    isholiday = models.BooleanField(default=False)

    def __str__(self):
        return str(self.store_id)

class Ventas(models.Model):
    store = models.ForeignKey(Tiendas, on_delete=models.SET_NULL, blank=True, null=True)
    departamento = models.IntegerField(default=None)
    date = models.DateField()
    weekly_sales = models.DecimalField(max_digits=8, decimal_places=2, default=None)
    isholiday = models.BooleanField(default=False)

    def __str__(self):
        return str(self.store_id)