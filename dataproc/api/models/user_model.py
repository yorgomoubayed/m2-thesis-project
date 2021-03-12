from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class User(StructuredNode):
	uid=UniqueIdProperty()
	name=StringProperty()
	surname=StringProperty()
