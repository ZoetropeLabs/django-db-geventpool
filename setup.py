# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='django-db-geventpool',
    version='2',
    install_requires=[
        'django>=1.5',
        'psycopg2-binary>=2.5.1;platform_python_implementation != "PyPy"',
        'psycopg2cffi>=2.7;platform_python_implementation == "PyPy"',
        'psycogreen>=1.0'],
    url='https://github.com/jneight/django-db-geventpool',
    description='Add a DB connection pool using gevent to django',
    long_description=open("README.rst").read(),
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    author='Javier Cordero Martinez',
    author_email='jcorderomartinez@gmail.com'
)
