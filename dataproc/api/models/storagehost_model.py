from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class StorageHost(StructuredNode):
	sh_files=StringProperty()
	sh_files_number=IntegerProperty()