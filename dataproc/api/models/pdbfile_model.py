# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

class PDBFile(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
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