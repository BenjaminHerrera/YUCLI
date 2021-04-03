from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3'
]

setup(
    name='YUCLI',
    version='1.0.0',
    description='A customizable command line environment for Python projects',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/BenjaminHerrera/YUCLI',
    author='Benjamin Herrera',
    author_email='BenHerrera1044@outlook.com',
    license='GNU General Public License v3 (GPLv3)',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requires=['kivy>=2.0.0']
)