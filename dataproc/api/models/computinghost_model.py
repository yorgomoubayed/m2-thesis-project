from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class ComputingHost(StructuredNode):
	name=StringProperty()
	uuid=StringProperty(unique_index=True, default=uuid4)
	ch_softwares=StringProperty()
	ch_softwares_number=IntegerProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'name': self.name,
				'uuid': self.uuid,
				'ch_softwares': self.ch_softwares,
				'ch_softwares_number': self.ch_softwares_number,
			},
		}