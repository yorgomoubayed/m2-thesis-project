from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class Buster(StructuredNode):
	uid=UniqueIdProperty()
	tool_name=StringProperty()