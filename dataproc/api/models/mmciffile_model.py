from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class mmCIFFile(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)
	coordinates_filetype=StringProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
	    return {
	        'node_properties': {
	            'uuid': self.uuid,
	            'coordinates_filetype': self.coordinates_filetype,
	        },
	    }