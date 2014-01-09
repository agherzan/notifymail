#!/usr/bin/env python

from distutils.core import setup
setup(name='notifmail',
      version='1.0b',
      scripts=['notifmail'],
      py_modules=['notifmail_utils'],
      description='IMAP email notifier',
      long_description='IMAP email notifier',
      platforms=['linux'],
      author='Andrei Gherzan',
      author_email='andrei@gherzan.ro',
      url='https://github.com/agherzan/notifmail',
      license='MIT',
     )
