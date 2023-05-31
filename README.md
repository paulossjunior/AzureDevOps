# Application Software Artifact That access Microsft Azure DevOPS
## Goal
A example of Application Software Artifact That access Microsft Azure DevOPS to retrieve data.

## Documentation

The Documentation can be found in this [link](./docs/README.md)

## Generate documentation

To create the code documentation:
```bash
pdoc --html --force azuredevopsX/ --output docs

```
### Acess code documentation	

To accesss the documentation, go to folder docs/azuredevopsX and open index.html 
	

## Usage

```python

from azuredevopsX import factories
from pprint import pprint 
organization_url = "<DEVOPS URL>"
personal_access_token =  "<personal code access>"

project_service = factories.ProjectFactory(personal_access_token=personal_access_token,
                                            organization_url=organization_url)
projects = project_service.get_projects()

for project in projects:
    pprint(project.__dict__)

```
