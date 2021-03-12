from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, DateTimeProperty

class ReductionScaling(StructuredNode):
 	uid=UniqueIdProperty()
 	dp_step_name=StringProperty()
 	created_at=DateTimeProperty()
 	updated_at=DateTimeProperty()