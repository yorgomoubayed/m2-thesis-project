from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class ComputationHost(StructuredNode):
	ip=StringProperty()
	uuid=StringProperty(unique_index=True, default=uuid4)
	hostname=StringProperty()
	friendlyName=StringProperty()
	workingdirectory=StringProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'ip': self.ip,
				'uuid': self.uuid,
				'hostName': self.hostName,
				'friendlyName': self.friendlyName,
				'workingDirectory': self.workingDirectory,
			},
		}