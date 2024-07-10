import django_filters

from .models import  Tarefa

#Filtro a ser aperfeiçoado!
class FiltoDeStatus(django_filters.FilterSet):         

    class Meta:
        model = Tarefa
        fields = {
            'Status',
        }
