from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, DateTimeProperty, BooleanProperty
from uuid import uuid4

class LigandsFitting(StructuredNode):
 	uuid=StringProperty(unique_index=True, default=uuid4)
 	dp_step_name = StringProperty()
 	created_at=DateTimeProperty()
 	updated_at=DateTimeProperty()
 	pipedream_id=IntegerProperty()
 	score=IntegerProperty()
 	fitting_success=BooleanProperty()