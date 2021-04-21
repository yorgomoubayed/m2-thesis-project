from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

from api.models.dataset_model import Dataset

class DataCollection(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)
	imagesnumber=IntegerProperty()
	flux=IntegerProperty()
	resolution=StringProperty()
	wavelength=IntegerProperty()
	transmission=IntegerProperty()
	exposuretime=IntegerProperty()
	detectordistance=IntegerProperty()
	beamlinename=StringProperty()

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
				"imagesNumber": self.imagesnumber,
				"flux": self.flux,
				"resolution": self.resolution,
				"wavelength": self.wavelength,
				"transmission": self.transmission,
				"exposureTime": self.exposuretime,
				"detectorDistance": self.detectordistance ,
				"beamlineName": self.beamlinename,
			},
		}