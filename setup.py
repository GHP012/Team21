from setuptools import setup, find_packages

setup(
    name='analyzePredict', #the name package managers will use for your project, like numpy or pandas
    version='0.11', #the current version number of your project
    packages=find_packages(exclude=['tests*']),
    license='MIT', #name of the license you chose
    description='EDSA example python package', #one-sentence description of your package
    long_description=open('README.md').read(),
    #install_requires=[numpy, pandas], #list of all other packages this package depends on; package managers will install these automatically as needed
    url='https://github.com/OmphileL/Team21',
    author='Omphile Louw, Gavin Pillay, Suvarna Chetty, Nombulelo Msibi, Tuduetso Mmokwa',
    author_email=''
)
