# Import libraries
from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

# Import models
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
			'node_properties': {
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