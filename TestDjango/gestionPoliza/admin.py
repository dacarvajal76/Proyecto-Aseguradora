from django.contrib import admin
from gestionPoliza.models import Agente, BandaSalarial, CategoriaAccidente, CategoriaVehiculo, Estado, Financiadora, Pais, Municipio, Parroquia, Ciudad, Perfil, RolUsuario, Sucursal, Empleado, TipoCobertura, Trabaja, Usuario

# Register your models here.

class PaisAdmin(admin.ModelAdmin):
    list_display=('id_pais', 'nb_pais')
    
class EstadoAdmin(admin.ModelAdmin):
    list_display=('id_estado', 'nb_estado','id_pais') 
    
class MunicipioAdmin(admin.ModelAdmin):
    list_display=('id_municipio', 'nb_municipio', 'id_estado')
    
class ParroquiaAdmin(admin.ModelAdmin):
    list_display=('id_parroquia', 'nb_parroquia', 'id_municipio') 
    
class CiudadAdmin(admin.ModelAdmin):
    list_display=('id_ciudad','nb_ciudad','id_municipio')
    
class SucursalAdmin(admin.ModelAdmin):
    list_display=('id_sucursal','nb_sucursal','id_ciudad', 'activos', 'id_director')     
    
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('id_empleado',"fecha_inicio_empresa")
    
class BandaSalarialAdmin(admin.ModelAdmin):
    list_display=('id_banda','banda_min', 'banda_max')
    
class TrabajaAdmin(admin.ModelAdmin):
    list_display=('id_empleado','id_sucursal', 'id_banda', 'fecha_inicio_sucursal', 'acumulado_salario')
    
class UsuarioAdmin(admin.ModelAdmin):
    list_display=('id_usuario','nombre_usuario', 'email', 'contrasena', 'nombre', 'apellido', 'edad', 'genero', 'id_ciudad')
    
class PerfilAdmin(admin.ModelAdmin):
    list_display=('id_perfil','nombre_perfil')  

class RolUsuarioAdmin(admin.ModelAdmin):
    list_display=('id_perfil','id_usuario')                                  
                      
class AgenteAdmin(admin.ModelAdmin):
    list_display=('id_agente','direc_agente', 'tipo_agente', 'id_sucursal')
    
class FinanciadoraAdmin(admin.ModelAdmin):
    list_display=('id_financiadora','direc_financiadora', 'tlf_financiadora') 
    
class TipoCoberturaAdmin(admin.ModelAdmin):
    list_display=('id_tipo_cobertura','descrip_tipo_cobertura')
    
class CategoriaVehiculoAdmin(admin.ModelAdmin):
    list_display=('id_categoria','descrip_categoria_veh')
    
class CategoriaAccidenteAdmin(admin.ModelAdmin):
    list_display=('id_categoria_acc','descrip_categ','descrip_sub_categ')                                    

admin.site.register(Pais, PaisAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(BandaSalarial, BandaSalarialAdmin)
admin.site.register(Trabaja, TrabajaAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(RolUsuario, RolUsuarioAdmin)
admin.site.register(Agente, AgenteAdmin)
admin.site.register(Financiadora, FinanciadoraAdmin)
admin.site.register(TipoCobertura, TipoCoberturaAdmin)
admin.site.register(CategoriaVehiculo, CategoriaVehiculoAdmin)
admin.site.register(CategoriaAccidente, CategoriaAccidenteAdmin)
