from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

from api.models.reflectionstructurefactors_model import RefelctionStructureFactors
from api.models.coordinates_model import Coordinates

class OCF(StructuredNode):
	
	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	name=StringProperty()
	pipedreamcommand=StringProperty()
	priority=StringProperty()
	useruuid=StringProperty()

	# Relationships
	has_rsf=RelationshipTo(RefelctionStructureFactors, 'HAS')
	has_coordinates=RelationshipTo(Coordinates, 'HAS')

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'uuid': self.uuid,
				'name': self.name,
				'pipedreamCommand': self.pipedreamcommand,
				'priority': self.priority,
				'useruuid': self.useruuid,
			},
		}