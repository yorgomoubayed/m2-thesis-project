from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class ComputingHost(StructuredNode):
	ch_softwares=StringProperty()
	ch_softwares_number=IntegerProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'ch_softwares': self.ch_softwares,
				'ch_softwares_number': self.ch_softwares_number,
			},
		}