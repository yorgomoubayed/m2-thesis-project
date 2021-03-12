from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class autoPROC(StructuredNode):
	uid=UniqueIdProperty()
	tool_name=StringProperty()