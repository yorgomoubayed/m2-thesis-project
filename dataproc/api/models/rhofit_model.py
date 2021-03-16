from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class Rhofit(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)
	tool_name=StringProperty()