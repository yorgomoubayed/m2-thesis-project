"""
api application controllers to create relationships between the nodes
"""

# Import python and django libraries
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Import models
from api.models import *

# Define CRUD methods
@csrf_exempt
def connectConstructUser(request):

	"""
	Create a relationship between a construct and a user
	"""

	if request.method=="PUT":
		json_data=json.loads(request.body)
		uuid=json_data["uuid"]
		name=json_data["name"]

		try:
			construct=Construct.nodes.get(name=name)
			user=User.nodes.get(uuid=uuid)
			return JsonResponse({"Status": construct.has_user.connect(user)}, safe=False)

		except:
			return JsonResponse({"Error": "error occurred"}, safe=False)