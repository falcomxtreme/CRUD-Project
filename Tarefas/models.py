from django.db import models

from datetime import date


#Modelo da tarefa.
class Tarefa(models.Model):
   OPCOES_STATUS = [
      ('Em Andamento', 'Em Andamento'),
      ('Pendente', 'Pendente'),
      ('Concluída', 'Concluída'),
   ]

   titulo = models.CharField(verbose_name="Título", max_length=100,
   null=False, blank=False)
   #Automáticamente atribui a data de criação à tarefa
   data_de_criacao = models.DateTimeField(verbose_name="Data da criação",
      auto_now_add=True)
   descricao = models.CharField(verbose_name="Breve descrição",
      max_length=400, null=True, blank=True)
   data_de_vencimento = models.DateField(verbose_name="Data de vencimento",
   null=False, blank=False)
   data_de_finalizacao = models.DateField(null=True)
   status = models.CharField(max_length=20, choices=OPCOES_STATUS)
   
   #Function para marcar tarfa como completa caso não esteja.
   def marcar_como_completa(self):
      #Verifica se a data de finalização não está settada. 
      if not self.data_de_finalizacao:
         #Adiciona a data de finalização como o dia que a function foi chamada.
         self.data_de_finalizacao = date.today()
         #Altera o status da tarefa para "Concluída"
         self.status = 'Concluída'
         #Salva as alterações na tarefa.
         self.save()
