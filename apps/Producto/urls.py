from django.conf.urls import url, include
from apps.Producto.views import index_producto, producto_list, ProductoList, ProductoCreate, ProductoUpdate, ProductoDelete
urlpatterns = [
    url(r'^$', index_producto, name='index_producto'),
    url(r'^nuevo$', ProductoCreate.as_view() , name='producto_crear'),
 	url(r'^listar', ProductoList.as_view(), name='producto_listar'),
 	url(r'^editar/(?P<pk>\d+)/$', ProductoUpdate.as_view(), name='producto_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', ProductoDelete.as_view(), name='producto_eliminar'),
         
]