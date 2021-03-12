from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

from api.models.dpstep_model import DPStep
from api.models.storagehost_model import StorageHost
from api.models.construct_model import Construct


class Datatset(StructuredNode):
 	dataset_file_no=IntegerProperty()
 	dataset_size=StringProperty()

 	# Relationships
 	input_of=RelationshipTo(DPStep, 'INPUT')
 	stored=RelationshipTo(StorageHost, 'STORED')
 	belongs=RelationshipTo(Construct, 'BELONGS')