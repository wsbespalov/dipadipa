ДЛЯ ЗАПУСКА 
1. cd project folder там где папка env
2. запуск окружения  source env/bin/activate
3. cd app folder там где есть manage.py {cd stopmusor/}
4. ./manage.py runserver 0.0.0.0:8000

если были обновлены пакеты, то нужно из папки где есть requirements.txt
при активированном окружении вызвать команду
pip install -r requirements.txt


Если МЕНЯЕТСЯ МОДЕЛЬ то сначала
./manage.py makemigrations
	Выдаст чтото типа 
	Migrations for 'server':
  	server/migrations/0003_papers.py
    	- Create model Papers
Далее		
./manage.py migrate
	Выдаст чтото типа
	Running migrations:
  		Applying server.0003_papers... OK

Добавляем данные в модель 
./manage.py shell
from server.models import News	{или другое имя вместо News}

Смотрим какие поля есть в dipadipa/stopmusor/server/models.py и пишем данные в модель следующей строкой:
n = News.objects.create(title="New service", slug="New is good!!!", author="admin", body="lorem ipsum blah-blah-blah")

Проверяем 
n 	{или другая буква которую использовал}
Выдаст:
	<Papers: 2. News> 	{Заголовок title}
Сохраняем: 
n.save()

q = Question.objects.create(title="New Question", fio="Putin VV", email="vovka@gov.ru", body="WTF?")
q.save()

Выходим:
exit()