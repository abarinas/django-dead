import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-dead',
    version='0.0.25',
    packages=find_packages(),
    include_package_data=True,
    license='GPLv3',
    description='DEAD is yet another Django Project and Applications Generator',
    long_description=README,
    url='https://github.com/000paradox000/django-dead',
    author='Ariel Calzada',
    author_email='ariel.calzada@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: The GNU General Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    scripts=[
        'bin/dead-admin.py'
    ],
    install_requires=[
        'django',
    ],
)