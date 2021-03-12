from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class StatisticalReport(StructuredNode):
	uid=UniqueIdProperty()
	report_name=StringProperty()