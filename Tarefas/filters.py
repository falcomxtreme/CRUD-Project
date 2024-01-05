import django_filters
from .models import Tarefa

#Filtro a ser aperfeiçoado!

class FiltroDeTarefas(django_filters.FilterSet):         

    class Meta:
        model = Tarefa
        fields = {
            'Status',
            'DataDeVencimento'
        }
