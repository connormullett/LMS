
.PHONY: clean python-packages install migrate test run all

clean:
	find . -type d -name '__pycache__' -delete
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

python-packages:
	pip install -r requirements.txt

install: python-packages

test:
	python manage.py test

run:
	python manage.py run

migrate:
	python manage.py db migrate
	python manage.py db upgrade

all: clean install test run
