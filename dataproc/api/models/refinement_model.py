from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, DateTimeProperty
from uuid import uuid4

class Refinement(StructuredNode):
 	uuid=StringProperty(unique_index=True, default=uuid4)
 	dp_step_name=StringProperty()
 	created_at=DateTimeProperty()
 	updated_at=DateTimeProperty()

 	@property
 	def serialize(self):

 		"""
 		Serializer for node properties
 		"""
 		
 	    return {
 	        'node_properties': {
 	            'uuid': self.uuid,
 	            'dp_step_name': self.dp_step_name,
 	            'created_at': self.created_at,
 	            'updated_at': self.updated_at,
 	        },
 	    }