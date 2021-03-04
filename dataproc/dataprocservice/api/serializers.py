from rest_framework import serializers
from dataprocservice.models import Construct


class ConstructSerializer(serializers.ModelSerializer):
	class Meta:
		model = Construct
		fields = ['title', 'created_at', 'updated_at',]