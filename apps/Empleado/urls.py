from django.conf.urls import url, include 
from apps.Empleado.views import index_empleado, EmpleadoList, EmpleadoCreate, EmpleadoUpdate, EmpleadoDelete 

urlpatterns = [
	url(r'^$', index_empleado, name='index_empleado'),
	url(r'^nuevo$', EmpleadoCreate.as_view(), name='empleado_crear'),
	url(r'^listar$', EmpleadoList.as_view(), name='empleado_listar'), 
	url(r'^editar/(?P<pk>\d+)/$', EmpleadoUpdate.as_view(), name='empleado_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', EmpleadoDelete.as_view(), name='empleado_eliminar'),
]