from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_list: List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!="-e .":
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print("requirement.txt file is not found")

    return requirement_list

print(get_requirements())

setup(
    name="Network-security",
    version="0.0.1",
    Nmae="Animesh Hazarika",
    author_email="animeshhazarika58@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)



