from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class User(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)
	name=StringProperty()
	surname=StringProperty()
