run:
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

shell:
	python manage.py shell

show_sql:
	python manage.py sqlmigrate $(app) $(num)

startproject:
	django-admin startproject $(name)

startapp:
	python manage.py startapp $(name)

collectstatic:
	python manage.py collectstatic

createsu:
	python manage.py createsuperuser