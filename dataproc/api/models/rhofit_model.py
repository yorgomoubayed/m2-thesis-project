from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class Rhofit(StructuredNode):
	uid=UniqueIdProperty()
	tool_name=StringProperty()