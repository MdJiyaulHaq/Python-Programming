from setuptools import setup, find_packages
setup(
    name='pdf-editor',
    version='1.1.4',
    author='Md Jiyaul Haq',
    long_description=open('README.md').read(),
    packages=find_packages(exclude=['tests*', 'data*']),
    install_requires=[
        'put_whatever_dependencies_you_need_here',
        'PyPDF2',
        'etc.',
    ],
) # This is a sample setup.py file for a Python package named 'pdf-editor'.