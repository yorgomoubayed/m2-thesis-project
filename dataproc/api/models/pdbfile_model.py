from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class PDBFile(StructuredNode):
	uid=UniqueIdProperty()
	coordinates_filetype=StringProperty(unique_index=True, required=True)