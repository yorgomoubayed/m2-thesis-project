# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

class BeamlineParams(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""
	
	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	
	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
		'BeamlineParams_node_properties': {
		'uuid': self.uuid,
		},
		}