import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
    
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
    
setup(
    name='django-bukber',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    lisence='BSD Lisence',
    description='A simple Django app to conduct Web-based bukber',
    long_description=README,
    url='https://rezajuliandri.id',
    author='Reza Juliandri',
    author_email='rezajuliandri20@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
