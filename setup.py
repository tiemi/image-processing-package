from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="imagem_processing",
    version='0.0.1',
    author="Ytalo",
    description="image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Hanieri21/imagem-processing-package",
    packages=find_packages(),
    python_requires='>=3.5',
)