from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.Inventario.views import Inventarioinicio, InventarioList, InventarioCreate, InventarioUpdate, InventarioDelete
urlpatterns = [
    url(r'^index$',Inventarioinicio , name='inventario_inicio'),
 	url(r'^nuevo$',login_required(InventarioCreate.as_view()) , name='inventario_crear'),
 	url(r'^listar$', login_required(InventarioList.as_view()), name='inventario_listar'),
 	url(r'^editar/(?P<pk>\d+)/$', login_required(InventarioUpdate.as_view()), name='inventario_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(InventarioDelete.as_view()), name='inventario_eliminar'),
         
]