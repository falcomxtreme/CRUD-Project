 O projeto ainda está em desenvolvimento.
 Para instalar e rodar esse projeto, você deverá o Python 3.12.1 ou versão superior, todos os links estarão no final da descrição.

 Será necessário criar um ambiente virtual com o comando " python -m venv venv ", e instalar o django >= 5.0.1 ou superior,
a escolha do Django se deve ao fato de eu ter conhecido ela recentemente(e ser a que mais conheço de forma geral), além de todas as informações
positivas que eu li sobre ela enquanto pesquisava, o proximo download é o  dj-database-url >= 2.1.0 e o python-decouple => 3.8  os quais ajudam a manter as a Scret_Key,
o Debug, Allowed_host e a Database mais seguras, deixando os dados das mesmas fora do f12/inspensionar do navegador, quanto ao bootstrap >= 2023.10 foi uma escolha para
fazer um front mais clear, e aprender de maneira mais tranquila sobre o fron-end, assim como no django-crispy-forms => 2.1 que teve o mesmo proposito. Já o filter 
django-filter foi um dos meios que achei de filtrar sem precisar pegar o código pronto, e assim aprender um pouco mais!

Para executar a aplicação basta(após entrar no ambiente virtual com o Set-ExecutionPolicy -Scope Process -ExecutionPolicy ByPass(pra liberar a politica de execução) e python -m .\.venv\Scripts\activate pra entrar de fato no ambiente virtual), basta
usar o python manage.py runserver para rodar a aplicação e clicar no link para entrar, lá você poderá cadastrar tarefas na opção
"Nova Tarefa", Concluir, Editar, Excluir e até mesmo consultar filtrando por Status ou não! No futuro poderá até ordenar por data crescente ou ascendente!
 

https://www.python.org/downloads/
https://www.djangoproject.com/download/
pip install Django 5.0
https://pypi.org/project/dj-database-url/
pip install dj-database-url
https://pypi.org/project/python-decouple/
pip install python-decouple
https://django-crispy-forms.readthedocs.io/en/latest/install.html
pip install django-crispy-forms
https://getbootstrap.com/docs/5.3/getting-started/introduction/
pip install crispy-bootstrap5
https://django-filter.readthedocs.io/en/stable/
23.5 pip install django-filter
