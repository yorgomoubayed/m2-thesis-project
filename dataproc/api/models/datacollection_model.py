# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

# Models imports
from api.models.dataset_model import Dataset

class DataCollection(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	imagesNumber=IntegerProperty()
	flux=StringProperty()
	resolution=StringProperty()
	wavelength=IntegerProperty()
	transmission=IntegerProperty()
	exposureTime=IntegerProperty()
	detectorDistance=IntegerProperty()
	beamlineName=StringProperty()

	# Relationships
	generates=RelationshipTo(Dataset, 'GENERATES')

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'datacollection_node_properties': {
				"uuid": self.uuid,
				"imagesNumber": self.imagesNumber,
				"flux": self.flux,
				"resolution": self.resolution,
				"wavelength": self.wavelength,
				"transmission": self.transmission,
				"exposureTime": self.exposureTime,
				"detectorDistance": self.detectorDistance ,
				"beamlineName": self.beamlineName,
			},
		}