from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class ScalepackFile(StructuredNode):
	uid=UniqueIdProperty()
	rsf_filetype=StringProperty(unique_index=True, required=True)
