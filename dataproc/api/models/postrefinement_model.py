from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, DateTimeProperty

class PostRefinement(StructuredNode):
 	uid=UniqueIdProperty()
 	dp_step_name=StringProperty()
 	pipedream_id=IntegerProperty()
 	created_at=DateTimeProperty()
 	updated_at=DateTimeProperty()