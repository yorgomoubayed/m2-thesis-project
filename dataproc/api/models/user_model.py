from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class User(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)
	name=StringProperty()
	surname=StringProperty()

	# @property
	# def serialize(self):
	#     return {
	#         'node_properties': {
	#             'uuid': self.uuid,
	#             'username': self.username,
	#         },
	#     }


