from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

from api.models.dpstep_model import DPStep
from api.models.storagehost_model import StorageHost
from api.models.construct_model import Construct


class Dataset(StructuredNode):
 	name=StringProperty()
 	dataset_file_no=IntegerProperty()
 	dataset_size=StringProperty()

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
 		'name': self.name,
 		'dataset_file_no': self.dataset_file_no,
 		'dataset_size': self.dataset_size,
 		},
 		}

