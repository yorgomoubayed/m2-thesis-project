from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class PDBFile(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)
	coordinates_filetype=StringProperty()