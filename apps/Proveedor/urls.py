from django.conf.urls import url, include
from apps.Proveedor.views import index_proveedor, proveedor_list, ProveedorList, ProveedorCreate, ProveedorUpdate, ProveedorDelete
urlpatterns = [
    url(r'^$', index_proveedor, name='index_proveedor'),
    url(r'^nuevo$', ProveedorCreate.as_view() , name='proveedor_crear'),
 	url(r'^listar', ProveedorList.as_view(), name='proveedor_listar'),
 	url(r'^editar/(?P<pk>\d+)/$', ProveedorUpdate.as_view(), name='proveedor_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', ProveedorDelete.as_view(), name='proveedor_eliminar'),
         
]