from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, DateTimeProperty
from uuid import uuid4

class PostRefinement(StructuredNode):
 	uuid=StringProperty(unique_index=True, default=uuid4)
 	dp_step_name=StringProperty()
 	pipedream_id=IntegerProperty()
 	created_at=DateTimeProperty()
 	updated_at=DateTimeProperty()