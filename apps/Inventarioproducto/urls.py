from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.Inventarioproducto.views import Inventariopinicio, InventariopList, InventariopCreate, InventariopUpdate, InventariopDelete, product_list
urlpatterns = [
    url(r'^index$',Inventariopinicio , name='inventariop_inicio'),
    url(r'^search$', product_list, name='inventario_search'),
 	url(r'^nuevo$',login_required(InventariopCreate.as_view()) , name='inventariop_crear'),
 	url(r'^listar$', login_required(InventariopList.as_view()), name='inventariop_listar'),
 	url(r'^editar/(?P<pk>\d+)/$', login_required(InventariopUpdate.as_view()), name='inventariop_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(InventariopDelete.as_view()), name='inventariop_eliminar'),
         
]