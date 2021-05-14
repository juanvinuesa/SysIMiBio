# https://pypi.org/project/pyinaturalist/
# https://pyinaturalist.readthedocs.io/en/stable/
# https://api.inaturalist.org/v1/docs/#!/Projects/get_projects
# https://github.com/niconoe/pyinaturalist
# https://www.inaturalist.org/pages/api+reference
pip install pyinaturalist


from pyinaturalist.node_api import get_all_observations
obs = get_all_observations(user_id='institutomisionerodebiodiversidad')


from pyinaturalist.rest_api import get_observations
obs = get_observations(user_id='niconoe', response_format='dwc')

from pyinaturalist.node_api import get_taxa_autocomplete

while True:
    query = input("> ")
    response = get_taxa_autocomplete(q=query, minify=True)
    print("\n".join(response["results"]))


from pyinaturalist.node_api import get_projects #https://api.inaturalist.org/v1/docs/#!/Projects/get_projects
bdm = get_projects(q="biodiversidad-de-misiones")
bdm.keys()
bdm["total_results"]
bdm["page"]
bdm["per_page"]
type(bdm["results"])
bdm["results"][0]
bdm["results"][0].keys()
from pyinaturalist.node_api import get_projects_by_id