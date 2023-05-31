from azuredevopsX import factories
from pprint import pprint 

organization_url = "URL"
personal_access_token =  "code"

service = factories.ProjectFactory(personal_access_token=personal_access_token,organization_url=organization_url)
results = service.get_all(today=False)

pprint (len(results))

for item in results:
    pprint (item.__dict__)
    
    
    
