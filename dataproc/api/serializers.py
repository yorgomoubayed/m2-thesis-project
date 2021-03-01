from rest_framework import serializers
from dataproc.models import Contruct


class ContructSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contruct
		fields = ['title', 'created_at', 'updated_at',]