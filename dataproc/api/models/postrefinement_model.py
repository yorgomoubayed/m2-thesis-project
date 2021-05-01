# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, DateTimeProperty

class PostRefinement(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	dp_step_name=StringProperty()
	pipedream_id=IntegerProperty()
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
		'pipedream_id': self.pipedream_id,
		'created_at': self.created_at,
		'updated_at': self.updated_at,
		},
		}