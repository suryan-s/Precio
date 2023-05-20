from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Precio',
    version='0.0.2',
    packages=['backend'],
    url='',
    license='MIT',
    author='Suryan',
    author_email='suryannasa@gmail.com',
    description='''Precio is an open-source software tool for monitoring,
    automating and visualizing farming data. It provides
    real-time data analysis and insights of farming,
    enabling informed decision-making and improving farming efficiency.''',
    install_requires=requirements
)
