from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, DateTimeProperty, BooleanProperty

class LigandsFitting(StructuredNode):
 	uid=UniqueIdProperty()
 	dp_step_name = StringProperty()
 	created_at=DateTimeProperty()
 	updated_at=DateTimeProperty()
 	pipedream_id=IntegerProperty()
 	score=IntegerProperty()
 	fitting_success=BooleanProperty()