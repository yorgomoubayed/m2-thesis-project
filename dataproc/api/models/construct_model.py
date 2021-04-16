from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

from api.models.ocf_model import OCF
from api.models.storagehost_model import StorageHost
from api.models.computinghost_model import ComputingHost
from api.models.user_model import User

class Construct(StructuredNode):
	
	uuid=StringProperty(unique_index=True, default=uuid4)
	name=StringProperty()
	
	# Relationships
	has_ocf=RelationshipTo(OCF, 'HAS')
	has_storage_host=RelationshipTo(StorageHost, 'HAS')
	has_computing_host=RelationshipTo(ComputingHost, 'HAS')
	has_user=RelationshipTo(User, 'HAS')

	@property
	def serialize(self):
	    return {
	        'node_properties': {
	            'uuid': self.uuid,
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
	#             'nodes_type': 'ComputingHost',
	#             'nodes_related': self.serialize_relationships(self.computinghost.all()),
	#         },
	#         {
	#             'nodes_type': 'User',
	#             'nodes_related': self.serialize_relationships(self.user.all()),
	#         },
	#     ]
