
.PHONY: clean python-packages install test run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

python packages:
	pip install -r requirements.txt

install: python-packages

set-environment:
	ENVIRONMENT=$(ENVIRONMENT)
	DATABASE_URI=$(DATABASE_URI)
	SECRET_KEY=$(SECRET_KEY)

test: set-environment
	python manage.py test

run: set-environment
	python manage.py run

all: set-environment clean install test run
