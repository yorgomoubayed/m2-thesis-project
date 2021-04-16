from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, DateTimeProperty
from uuid import uuid4

class PostRefinement(StructuredNode):
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