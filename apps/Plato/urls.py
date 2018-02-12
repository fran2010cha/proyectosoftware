from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.Plato.views import index_plato, plato_view, plato_list, PlatoList, PlatoCreate, PlatoUpdate, PlatoDelete
urlpatterns = [
    url(r'^$', index_plato, name='index_plato'),
    url(r'^nuevo$',login_required(PlatoCreate.as_view()) , name='plato_crear'),
 	url(r'^listar$', login_required(PlatoList.as_view()), name='plato_listar'),
 	url(r'^editar/(?P<pk>\d+)/$', login_required(PlatoUpdate.as_view()), name='plato_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(PlatoDelete.as_view()), name='plato_eliminar'),
         
]