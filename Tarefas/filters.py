import django_filters
from .models import Tarefa


class FiltroDeTarefas(django_filters.FilterSet):

    CHOICES = (
        ('Crescente', 'Crescente'),
        ('Decrescente', 'Decrescente'),
    )
    
    ordering = django_filters.ChoiceFilter(
        label='Ordenar por Data de Vencimento', 
    choices= CHOICES, method='filter_by_order'
    )
    

    def filter_by_order(self, queryset, name, value):
        expression = 'DataDeVencimento' if value == 'Crescente' else '-DataDeVencimento'
        return queryset.order_by(expression)