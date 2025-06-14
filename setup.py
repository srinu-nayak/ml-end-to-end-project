from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(filepath:str) -> List[str]:
    requirements = []
    with open(filepath, 'r') as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='ml-end-to-end-project',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    author='Srinu',
    author_email='<srinunayakk7@gmail.com>',
    install_requires=get_requirements('requirements.txt')
)