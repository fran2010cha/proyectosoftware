from django.conf.urls import url, include 
from django.contrib.auth.decorators import login_required
from apps.Empleado.views import index_empleado, EmpleadoList, EmpleadoCreate, EmpleadoUpdate, EmpleadoDelete 

urlpatterns = [
	url(r'^$', index_empleado, name='index_empleado'),
	url(r'^nuevo$',login_required(EmpleadoCreate.as_view()), name='empleado_crear'),
	url(r'^listar$', login_required(EmpleadoList.as_view()), name='empleado_listar'), 
	url(r'^editar/(?P<pk>\d+)/$',login_required(EmpleadoUpdate.as_view()), name='empleado_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(EmpleadoDelete.as_view()), name='empleado_eliminar'),
]