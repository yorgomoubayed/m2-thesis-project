# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, DateTimeProperty

class Refinement(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	WilsonB=StringProperty()
	Rfree=IntegerProperty()
	MeanB=StringProperty()
	type=StringProperty()
	step=StringProperty()
	RMSbonds=IntegerProperty()
	RMSangles=IntegerProperty()
	R=IntegerProperty()
	WatersPresent=StringProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		return {
		'postrefinement_node_properties': {
		'uuid': self.uuid,
		'WilsonB': self.WilsonB,
		'Rfree': self.Rfree,
		'MeanB': self.MeanB,
		'type': self.type,
		'step': self.step,
		'RMSbonds': self.RMSbonds,
		'RMSangles': self.RMSangles,
		'R': self.R,
		'WatersPresent': self.WatersPresent,
		},
		}

