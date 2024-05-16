from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name='aiogram3_calendar',
  packages=['aiogram_calendar'],
  version='0.2',
  license='MIT',
  description='Simple Inline Calendar & Date Selection tool for Aiogram Telegram bots',
  long_description=long_description,
  author='Kataev Nikita (original by Andrew Nikolabay)',
  author_email='nik.kataev00@gmail.com',
  url='https://github.com/barabum0/aiogram_calendar',
  keywords=['Aiogram', 'Telegram', 'Bots', 'Calendar'],
  install_requires=[
          'aiogram~=3.4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12'
  ],
)
