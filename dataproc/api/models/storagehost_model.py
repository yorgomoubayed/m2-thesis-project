from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class StorageHost(StructuredNode):
	ip=StringProperty()
	uuid=StringProperty(unique_index=True, default=uuid4)
	hostname=StringProperty()
	friendlyname=StringProperty()
	workingdirectory=StringProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'ip': self.name,
				'uuid': self.uuid,
				'hostname': self.sh_files,
				'friendlyname': self.sh_files_number,
				'workingdirectory': self.workingdirectory,
			},
		}