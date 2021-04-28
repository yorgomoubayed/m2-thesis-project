# Import libraries
from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

# Import models
from api.models.ocf_model import OCF
from api.models.storagehost_model import StorageHost
from api.models.computationhost_model import ComputationHost
from api.models.user_model import User

class Construct(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	userUuid=StringProperty(unique_index=True, default=uuid4)
	name=StringProperty()
	
	# Relationships
	has_ocf=RelationshipTo(OCF, 'HAS')
	has_storage_host=RelationshipTo(StorageHost, 'HAS')
	has_computation_host=RelationshipTo(ComputationHost, 'HAS')
	has_user=RelationshipTo(User, 'HAS')

	@property
	def serialize(self):
	    return {
	        'node_properties': {
	            'uuid': self.uuid,
	            'userUuid': self.userUuid,
	            'name': self.name,
	        },
	    }

	# @property
	# def serialize_connections(self):
	#     return [
	#         {
	#             'nodes_type': 'OCF',
	#             'nodes_related': self.serialize_relationships(self.ocf.all()),
	#         },
	#         {
	#             'nodes_type': 'StorageHost',
	#             'nodes_related': self.serialize_relationships(self.storagehost.all()),
	#         },
	#         {
	#             'nodes_type': 'ComputationHost',
	#             'nodes_related': self.serialize_relationships(self.computationhost.all()),
	#         },
	#         {
	#             'nodes_type': 'User',
	#             'nodes_related': self.serialize_relationships(self.user.all()),
	#         },
	#     ]
