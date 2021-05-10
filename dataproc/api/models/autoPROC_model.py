# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

class autoPROC(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""
	
	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	refinedCell_beta=StringProperty()
	refinedCell_b=StringProperty()
	wavelength=StringProperty()
	refinedCell_a=StringProperty()
	refinedCell_alpha=StringProperty()
	spaceGroup=StringProperty()
	refinedCell_c=StringProperty()
	refinedCell_gamma=StringProperty()
	
	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
		'autoPROC_node_properties': {
		'uuid': self.uuid,
		'refinedCell_beta': self.refinedCell_beta,
		'refinedCell_b': self.refinedCell_b,
		'wavelength': self.wavelength,
		'refinedCell_a': self.refinedCell_a,
		'refinedCell_alpha': self.refinedCell_alpha,
		'spaceGroup': self.spaceGroup,
		'refinedCell_c': self.refinedCell_c,
		'refinedCell_gamma': self.refinedCell_gamma,
		},
		}