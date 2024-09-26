from setuptools import find_packages, setup
from typing import List

def get_requirements(path:str) -> List[str]:
    HYPHEN_E_DOT = '-e .'
    """
    THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS
    """
    reuirements = []
    with open(path) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace('/n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements

setup(
    name='mlproject',
    version='0.0.0.1',
    author= 'Himanshu',
    author_email='xyz@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)