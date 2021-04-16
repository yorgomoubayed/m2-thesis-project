from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class SummaryOut(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)
	report_name=StringProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'uuid': self.uuid,
				'report_name': self.report_name,
			},
		}