
from apps.Inventarioproducto.models import Inventarioproducto
import django_filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Inventarioproducto
        fields = ['inventario',]