from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class StorageHost(StructuredNode):
	name=StringProperty()
	uuid=StringProperty(unique_index=True, default=uuid4)
	sh_files=StringProperty()
	sh_files_number=IntegerProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'name': self.name,
				'uuid': self.uuid,
				'sh_files': self.sh_files,
				'sh_files_number': self.sh_files_number,
			},
		}