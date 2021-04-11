from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class Buster(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)


	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
	    return {
	        'node_properties': {
	            'uuid': self.uuid,
	        },
	    }