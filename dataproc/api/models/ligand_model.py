from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

from api.models.dataset_model import Dataset

class Ligand(StructuredNode):

	uuid=StringProperty()
	name=StringProperty()

	# Relationships
	associated=RelationshipTo(Dataset, 'ASSOCIATED')

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'uuid': self.uuid,
				'name': self.name,
			},
		}