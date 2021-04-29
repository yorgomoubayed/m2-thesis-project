from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, DateTimeProperty
from uuid import uuid4

from api.models.dpstep_model import DPStep
from api.models.storagehost_model import StorageHost
from api.models.construct_model import Construct

class Dataset(StructuredNode):
 	
 	# Properties
 	uuid=StringProperty(unique_index=True, default=uuid4)
 	fileTemplateName=StringProperty()
 	userUuid=StringProperty()
 	crystalUuid=StringProperty()
 	currentPath=StringProperty(max_length=500)
 	generationPath=StringProperty(max_length=500)
 	blStartingDate=StringProperty()
 	beamlineName=StringProperty()
 	facilityName=StringProperty()

 	# Relationships
 	input_of=RelationshipTo(DPStep, 'INPUT')
 	stored=RelationshipTo(StorageHost, 'STORED')
 	belongs=RelationshipTo(Construct, 'BELONGS')

 	@property
 	def serialize(self):

 		"""
 		Serializer for node properties
 		"""
 		
 		return {
 		'dataset_node_properties': {
	 		'uuid': self.uuid,
	 		'fileTemplateName': self.fileTemplateName,
	 		'userUuid': self.userUuid,
	 		'crystalUuid': self.crystalUuid,
	 		'currentPath': self.currentPath,
	 		'generationPath': self.generationPath,
	 		'blStartingDate': self.blStartingDate,
	 		'beamlineName': self.beamlineName,
	 		'facilityName': self.facilityName,
 		},
 		}

