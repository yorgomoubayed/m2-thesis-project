# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json

# from api.models import *


# @csrf_exempt
# def connectConstructUser(request):
#     if request.method == 'PUT':
#         json_data = json.loads(request.body)
#         uid = json_data['uid']
#             construct = Construct.nodes.get(uid=uid)
#             user = User.nodes.get(code=code)
#             res = construct.user.connect(user)
#             response = {"result": res}
#             return JsonResponse(response, safe=False)
#         except:
#             response = {"error": "Error occurred"}
#             return JsonResponse(response, safe=False)

# @csrf_exempt
# def connectPaP(request):
#     if request.method == 'PUT':
#         json_data = json.loads(request.body)
#         uid1 = json_data['uid1']
#         uid2 = json_data['uid2']
#         try:
#             person1 = Person.nodes.get(uid=uid1)
#             person2 = Person.nodes.get(uid=uid2)
#             res = person1.friends.connect(person2)
#             response = {"result": res}
#             return JsonResponse(response, safe=False)
#         except:
#             response = {"error": "Error occurred"}
#             return JsonResponse(response, safe=False)