from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class autoPROC(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)
	tool_name=StringProperty()

	# @property
	# def serialize(self):

	# 	"""
	# 	Serializer for node properties
	# 	"""
		
	# 	return {
	# 		'node_properties': {
	# 			'uuid': self.uuid,
	# 			'tool_name': self.name,
	# 		},
	# 	}