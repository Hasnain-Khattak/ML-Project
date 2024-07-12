from setuptools import setup, find_packages
from typing import List

HYPHEN_e_DOT = "-e ."
def get_pack(file_path:str) -> List[str]:
    """This Function will return this List of packages which are required.
    

    Args:
        File_path: Where are the packages have been written.

    Returns:
        List[str]: List of packages required for your Project.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', "") for req in requirements]
        
        if HYPHEN_e_DOT in requirements:
            requirements.remove(HYPHEN_e_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Hasnain',
    author_email='msaqibkhan987987@gmail.com',
    packages=find_packages(),
    install_requires=get_pack('requirements.txt')
)