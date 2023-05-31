from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='azuredevopsX',  # Required
    version='0.0.16',  # Required
    author="xxxxxx",
    author_email="xxxxx",
    description="A lib to access data from Microsoft Azure DevOps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/integration_seon/libs/application/tfs",
    packages=find_packages(),
    
    install_requires=[
        'azure-devops',
        'requestx',
        'factory-boy'
    ],

    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    setup_requires=['wheel'],
    
)


