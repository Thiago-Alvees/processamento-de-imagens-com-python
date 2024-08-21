from setuptools import setup, find_packages

setup(
    name='image_processing',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  
        'numpy',
    ],
    description='A simple package for image processing.',
    author='Seu Nome',
    author_email='seuemail@example.com',
    url='https://github.com/seunome/image_processing',  
)
