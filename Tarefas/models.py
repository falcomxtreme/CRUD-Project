from django.db import models

from datetime import date


#Modelo da tarefa, com suas informações e, algumas informações para o
#administrador(Data de criação e finaliqzação).

class Tarefa(models.Model):
    
     Titulo = models.CharField(verbose_name="Título", max_length=100,
     null=False, blank=False)
     DataDeCriacao = models.DateTimeField(verbose_name="teste", auto_now_add=True)
     Descricao = models.CharField(verbose_name="Descrição breve",
     max_length=400, null=True, blank=True)
     DataDeVencimento = models.DateField(verbose_name="Data de vencimento",
     null=False, blank=False)
     DataDeFinalizacao = models.DateField(null=True)
     Status = models.CharField(max_length=50, choices= (
        ("Em Andamento", "Em Andamento"),("Pendente", "Pendente")
        )
       )
     
     #Definição para marcara tarfa como completa

     def MarcarComoCompleta(self):
         if not self.DataDeFinalizacao:
            self.DataDeFinalizacao = date.today()
            self.Status = "Concluída"
            self.save()
   