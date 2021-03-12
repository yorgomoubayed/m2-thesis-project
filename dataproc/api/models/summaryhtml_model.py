from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class SummaryHtml(StructuredNode):
	uid=UniqueIdProperty()
	report_name=StringProperty()