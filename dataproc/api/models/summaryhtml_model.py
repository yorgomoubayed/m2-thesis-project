from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class SummaryHtml(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)
	report_name=StringProperty()