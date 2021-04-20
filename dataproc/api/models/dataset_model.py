from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, DateTimeProperty
from uuid import uuid4

from api.models.dpstep_model import DPStep
from api.models.storagehost_model import StorageHost
from api.models.construct_model import Construct


class Dataset(StructuredNode):
 	
 	# Properties
 	uuid=StringProperty(unique_index=True, default=uuid4)
 	name=StringProperty()
 	# dataset_file_no=IntegerProperty()
 	# dataset_size=StringProperty()
 	filetemplatename=StringProperty()
 	useruuid=StringProperty()
 	crystaluuid=StringProperty()
 	currentpath=StringProperty()
 	generationpath=StringProperty()
 	blstartingdate=DateTimeProperty()
 	beamlinename=StringProperty()
 	facilityname=StringProperty()

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
 		'node_properties': {
 		'uuid': self.uuid,
 		'name': self.name,
 		'filetemplatename': self.filetemplatename,
 		'useruuid': self.useruuid,
 		'crystaluuid': self.crystaluuid,
 		'currentpath': self.currentpath,
 		'generationpath': self.generationpath,
 		'blstartingdate': self.blstartingdate,
 		'beamlinename': self.beamlinename,
 		'facilityname': self.facilityname,
 		# 'dataset_file_no': self.dataset_file_no,
 		# 'dataset_size': self.dataset_size,
 		},
 		}

