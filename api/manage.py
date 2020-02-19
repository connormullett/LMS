#!/usr/bin/env python

import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db

from app import blueprint

# register models for migrate command
from app.main.model import user
from app.main.model import lesson
from app.main.model import module
from app.main.model import course
from app.main.model import assessment
from app.main.model import question
from app.main.model import link

app = create_app(os.getenv('ENVIRONMENT'))
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
  app.run()

@manager.command
def test():
  tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
  result = unittest.TextTestRunner(verbosity=2).run(tests)
  if result.wasSuccessful():
    return 0
  return 1


if __name__ == '__main__':
  manager.run()