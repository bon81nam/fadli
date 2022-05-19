import django_filters
from .models import InputFormModel


class ActivityFilter(django_filters.FilterSet):
#    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = InputFormModel
        fields = ['JABATAN', 'Tempoh', 'tahun']
