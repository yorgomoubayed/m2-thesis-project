# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

class MTZfile(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	rsf_filetype = StringProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
		'mtz_node_properties': {
		'uuid': self.uuid,
		'rsf_filetype': self.rsf_filetype,
		},
		}