from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

from api.models.datatset_model import Datatset

class Ligand(StructuredNode):
	 
	# Relationships
 	associated=RelationshipTo(Datatset, 'ASSOCIATED')
