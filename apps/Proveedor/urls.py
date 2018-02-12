from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.Proveedor.views import index_proveedor, proveedor_list, ProveedorList, ProveedorCreate, ProveedorUpdate, ProveedorDelete
urlpatterns = [
    url(r'^$', index_proveedor, name='index_proveedor'),
    url(r'^nuevo$', login_required(ProveedorCreate.as_view()) , name='proveedor_crear'),
 	url(r'^listar', login_required(ProveedorList.as_view()), name='proveedor_listar'),
 	url(r'^editar/(?P<pk>\d+)/$', login_required(ProveedorUpdate.as_view()), name='proveedor_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(ProveedorDelete.as_view()), name='proveedor_eliminar'),
         
]