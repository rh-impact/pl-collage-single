from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'collage_single',
    version          = '0.1',
    description      = 'An app to create single collage image',
    long_description = readme,
    author           = 'Adithya Krishna',
    author_email     = 'adikrish@redhat.com',
    url              = 'http://wiki',
    packages         = ['collage_single'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'collage_single = collage_single.__main__:main'
            ]
        }
)
