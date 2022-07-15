from setuptools import setup,find_packages
from typing import List



# declaring variables for setup function
Project_Name="housing-predictor"
Version="0.0.1"
Author="himanshu"
Description = "this is my firts full stack machine leaning project"

Requirement_File_Name = "requirements.txt"

def get_requirements_list()->List[str]:
    """"
    description: this function is going to return the list of requirements
    mentioned in requirements.txt
    return
    """
    with open(Requirement_File_Name) as requirement_file:
        return requirement_file.readlines().remove ("-e .")


setup(
    name=Project_Name,
    version=Version,
    author=Author,
    description=Description,
    packages=find_packages(),
    install_requires=get_requirements_list()

)
# by running python setup.py install
# we can directly install all the  libraries in requirements.txt
