from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dataproc.models import Construct
from dataproc.api.serializers import ConstructSerializer

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'

@api_view(['GET', ])
def api_detail_construct_view(request, slug):

	try:
		construct = Construct.objects.get(slug=slug)
	except Construct.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ConstructSerializer(blog_post)
		return Response(serializer.data)


@api_view(['PUT',])
def api_update_construct_view(request, slug):

	try:
		construct = Construct.objects.get(slug=slug)
	except Construct.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = ConstructSerializer(construct, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['SUCCESS'] = UPDATE_SUCCESS
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
def api_delete_blog_view(request, slug):

	try:
		construct = Construct.objects.get(slug=slug)
	except Construct.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'DELETE':
		operation = construct.delete()
		data = {}
		if operation:
			data['SUCCESS'] = DELETE_SUCCESS
		return Response(data=data)


@api_view(['POST'])
def api_create_construct_view(request):

	construct = Construct()

	if request.method == 'POST':
		serializer = ConstructSerializer(construct, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)