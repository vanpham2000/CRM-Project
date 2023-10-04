# filters.py
import django_filters
from .models import CustomerAccount

class CustomerAccountFilter(django_filters.FilterSet):
    firstname = django_filters.CharFilter(lookup_expr='icontains')
    lastname = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CustomerAccount
        fields = ['firstname', 'lastname']