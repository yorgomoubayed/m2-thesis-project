from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

from api.models.datatset_model import Datatset

class Ligand(StructuredNode):
	 
	# Relationships
 	associated=RelationshipTo(Datatset, 'ASSOCIATED')

 	@property
 	def serialize(self):

 		"""
 		Serializer for node properties
 		"""
 		
 	    return {
 	        'node_properties': {
 	            # 'uuid': self.uuid,
 	            # 'tool_name': self.name,
 	        },
 	    }