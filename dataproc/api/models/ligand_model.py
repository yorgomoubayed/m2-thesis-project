# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

# Models imports
from api.models.dataset_model import Dataset

class Ligand(StructuredNode):

	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
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