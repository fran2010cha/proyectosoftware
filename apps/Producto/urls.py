from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.Producto.views import index_producto, producto_list, ProductoList, ProductoCreate, ProductoUpdate, ProductoDelete
urlpatterns = [
    url(r'^$', index_producto, name='index_producto'),
    url(r'^nuevo$',login_required(ProductoCreate.as_view()) , name='producto_crear'),
 	url(r'^listar$', login_required(ProductoList.as_view()), name='producto_listar'),
 	url(r'^editar/(?P<pk>\d+)/$', login_required(ProductoUpdate.as_view()), name='producto_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(ProductoDelete.as_view()), name='producto_eliminar'),
]