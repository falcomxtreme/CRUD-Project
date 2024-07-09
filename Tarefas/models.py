from django.db import models

from datetime import date


#Modelo da tarefa.
class Tarefa(models.Model):
    
   Titulo = models.CharField(verbose_name="Título", max_length=100,
   null=False, blank=False)
   #Automáticamente atribui a data de criação à tarefa
   DataDeCriacao = models.DateTimeField(verbose_name="teste",
      auto_now_add=True)
   Descricao = models.CharField(verbose_name="Descrição breve",
      max_length=400, null=True, blank=True)
   DataDeVencimento = models.DateField(verbose_name="Data de vencimento",
   null=False, blank=False)
   DataDeFinalizacao = models.DateField(null=True)
   Status = models.CharField(max_length=20, choices={
      ('Em Andamento', 'Em Andamento'),('Pendente', 'Pendente'),
      ('Concluída', 'Concluída'),
      }
   )
   
   #Function para marcar tarfa como completa caso não esteja.
   def marcar_como_completa(self):
      #Verifica se a data de finalização não está settada. 
      if not self.DataDeFinalizacao:
         #Adiciona a data de finalização como o dia que a function foi chamada.
         self.DataDeFinalizacao = date.today()
         #Altera o status da tarefa para "Concluída"
         self.Status = 'Concluída'
         #Salva as alterações na tarefa.
         self.save()
