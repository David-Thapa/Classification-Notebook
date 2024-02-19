from setuptools import find_packages,setup
from typing import List

HYPE_E_DOT = "-e ."

## Function
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n", "") for req in requirements]
        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)
        
    return requirements
        
## Description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

##Initialization
__version__ = "0.0.0"

REPO_NAME = "CLASSIFICATION-NOTEBOOK"
AUTHOR_USER_NAME = "David-Thapa"
SRC_REPO = "classifications"
AUTHOR_EMAIL = "daybeat06@gmail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for classification",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where = "src"),
    install_requires = get_requirements('requirements.txt')
)