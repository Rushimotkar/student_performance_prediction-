from webbrowser import get
from typing  import List
from setuptools import find_packages, setup



def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]



setup(    name="django-redis-cache",
    version="3.0.0",
    
    packages=find_packages(),
    install_requires=get.requires("requirements.txt")
     )


