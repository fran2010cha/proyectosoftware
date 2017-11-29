from django.conf.urls import url, include
from apps.Plato.views import index_plato, plato_view, plato_list, PlatoList, PlatoCreate, PlatoUpdate, PlatoDelete
urlpatterns = [
    url(r'^$', index_plato, name='index_plato'),
    url(r'^nuevo$', PlatoCreate.as_view() , name='plato_crear'),
 	url(r'^listar$', PlatoList.as_view(), name='plato_listar'),
 	url(r'^editar/(?P<pk>\d+)/$', PlatoUpdate.as_view(), name='plato_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', PlatoDelete.as_view(), name='plato_eliminar'),
         
]