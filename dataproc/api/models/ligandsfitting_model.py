# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, DateTimeProperty, BooleanProperty

class LigandsFitting(StructuredNode):

	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	type=StringProperty()

	@property
	def serialize(self):

 		"""
 		Serializer for node properties
 		"""

 		return {
 		'ligands_fitting_node_properties': {
 		'uuid': self.uuid,
 		'type': self.type,
 		},
 		}
