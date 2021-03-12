from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class SummaryOut(StructuredNode):
	uid=UniqueIdProperty()
	report_name=StringProperty()