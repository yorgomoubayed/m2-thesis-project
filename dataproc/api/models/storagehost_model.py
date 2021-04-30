# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

class StorageHost(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	ip=StringProperty()
	uuid=StringProperty(unique_index=True, default=uuid4)
	hostName=StringProperty()
	friendlyName=StringProperty()
	workingDirectory=StringProperty()

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'storagehost_node_properties': {
				'ip': self.ip,
				'uuid': self.uuid,
				'hostName': self.hostName,
				'friendlyName': self.friendlyName,
				'workingDirectory': self.workingDirectory,
			},
		}