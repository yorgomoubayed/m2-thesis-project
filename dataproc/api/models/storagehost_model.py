from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class StorageHost(StructuredNode):
	uuid=StringProperty()
	name=StringProperty()
	sh_files=StringProperty()
	sh_files_number=IntegerProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'sh_files': self.sh_files,
				'sh_files_number': self.sh_files_number,
			},
		}