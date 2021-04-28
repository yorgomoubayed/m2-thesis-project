# Import libraries
from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

# Improt models
from api.models.reflectionstructurefactors_model import RefelctionStructureFactors
from api.models.coordinates_model import Coordinates

class OCF(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	name=StringProperty()
	userUuid=StringProperty(unique_index=True, default=uuid4)
	pipedreamCommand=StringProperty()
	priority=IntegerProperty()

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
				'userUuid': self.userUuid,
				'name': self.name,
				'pipedreamCommand': self.pipedreamCommand,
				'priority': self.priority,
			},
		}