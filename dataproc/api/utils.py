# from api.models.user_model import User
# from api.models.construct_model import Construct

# MODEL_ENTITIES = {
# 'Construct': Construct,
# 'User': User
# }

# def fetch_nodes(fetch_info):
#     node_type       = fetch_info['node_type']
#     search_word     = fetch_info['name']
#     country         = fetch_info['country']
#     limit           = fetch_info['limit']
#     start           = ((fetch_info['page'] - 1) * limit)
#     end             = start + limit
#     jurisdiction    = fetch_info['jurisdiction']
#     node_set        = filter_nodes(MODEL_ENTITIES[node_type], search_word, country, jurisdiction)
#     fetched_nodes   = node_set[start:end]

#     return [node.serialize for node in fetched_nodes]

"""
Convert JSON to Python object
"""
  
import json
  
# JSON string
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'
  
# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)
  
print(employee_dict['name'])