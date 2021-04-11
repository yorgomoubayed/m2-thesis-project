from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

from api.models.dataset_model import Datatset

class DataCollection (StructuredNode):
 	collection_type=StringProperty()
 	collection_size=StringProperty()

 	# Relationships
 	genereates_dataset=RelationshipTo(Datatset, 'GENERATES')

 	@property
 	def serialize(self):

 		"""
 		Serializer for node properties
 		"""
 		
 	    return {
 	        'node_properties': {
 	            'collection_type': self.collection_type,
 	            'collection_size': self.collection_size,
 	        },
 	    }