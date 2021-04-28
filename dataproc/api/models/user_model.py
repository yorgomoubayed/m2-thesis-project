from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class User(StructuredNode):
	
	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)

	@property
	def serialize(self):
	    return {
	        'node_properties': {
	            'uuid': self.uuid
	        },
	    }


