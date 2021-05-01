# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, DateTimeProperty

class ReductionScaling(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
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