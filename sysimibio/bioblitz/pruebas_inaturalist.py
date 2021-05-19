# https://pypi.org/project/pyinaturalist/
# https://pyinaturalist.readthedocs.io/en/stable/
# https://api.inaturalist.org/v1/docs/#!/Projects/get_projects
# https://github.com/niconoe/pyinaturalist
# https://www.inaturalist.org/pages/api+reference
pip install pyinaturalist


from pyinaturalist.node_api import get_all_observations
obs = get_all_observations(user_id='institutomisionerodebiodiversidad')

from pyinaturalist.node_api import get_observation
get_observation(observation_id=79307481)
from pyinaturalist.node_api import get_observations
# obs = get_observations(user_id='niconoe', response_format='dwc')
obs = get_observations(project_id=69644)
obs.keys()
obs.get("results")[0].keys()
# observation
obs.get("results")[3]['id']
obs.get("results")[0]['quality_grade']
obs.get("results")[3]['created_at']
obs.get("results")[3]['uri']
# specie
# obs.get("results")[3]['taxon'].keys()
obs.get("results")[0]['taxon']['name']
obs.get("results")[3]['taxon']['rank']
obs.get("results")[3]['taxon']['iconic_taxon_name']
obs.get("results")[3]['taxon']['endemic']
obs.get("results")[3]['taxon']['threatened']
obs.get("results")[3]['taxon']['introduced']
obs.get("results")[3]['taxon']['native']

# todo los que siguen
# geo
obs.get("results")[3]['geojson']
# User info
obs.get("results")[3]['user']["id"]
obs.get("results")[3]['user']["login"]
obs.get("results")[3]['user']["name"]

# con reseaarch
obs.get("results")[3]



from pyinaturalist.rest_api import get_observations as rg
obsRest = rg(q='annonaceae', response_format='dwc')
obsRest.keys()
obsRest['total_results']
obs.get("results")[0]['taxon']
obs.get("results")[0]['geojson']
from pyinaturalist.node_api import get_observation_species_counts
get_observation_species_counts(project_id=69644)

from pyinaturalist.node_api import get_observation_histogram
get_observation_histogram(project_id=69644)

from pyinaturalist.node_api import get_taxa_autocomplete

while True:
    query = input("> ")
    response = get_taxa_autocomplete(q=query, minify=True)
    print("\n".join(response["results"]))


from pyinaturalist.node_api import get_projects #https://api.inaturalist.org/v1/docs/#!/Projects/get_projects
bdm = get_projects(q="BioBlitz-Misiones", member_id=1626810)
bdm.keys()
bdm["total_results"]
bdm["page"]
bdm["per_page"]
type(bdm["results"])
bdm["results"][0]
bdm["results"][0].keys()
from pyinaturalist.node_api import get_projects_by_id

from pyinaturalist.node_api import get_projects_by_id
get_projects_by_id(project_id=105820)