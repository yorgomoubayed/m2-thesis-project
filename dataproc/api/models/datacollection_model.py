from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

from api.models.dataset_model import Dataset

class DataCollection(StructuredNode):
	name=StringProperty()
	uuid=StringProperty(unique_index=True, default=uuid4)
	collection_type=StringProperty()
	collection_size=StringProperty()

	# Relationships
	generates=RelationshipTo(Dataset, 'GENERATES')

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'name': self.name,
				'uuid': self.uuid,
				'collection_type': self.collection_type,
				'collection_size': self.collection_size,
			},
		}