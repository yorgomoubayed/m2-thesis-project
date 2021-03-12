from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

from api.models.dataset_model import Datatset

class DataCollection (StructuredNode):
 	collection_type=StringProperty()
 	collection_size=StringProperty()

 	# Relationships
 	genereates_dataset=RelationshipTo(Datatset, 'GENERATES')