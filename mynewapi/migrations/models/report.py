from django.db import models, StatisticalReport
from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, DateTimeProperty, BooleanProperty

class Report(StructuredNode):
 	report_path=StringProperty()
 	report_source=StringProperty()
 	report_size=StringProperty()
 	
 	# Relationships
 	is_statisticalreport=RelationshipTo(StatisticalReport, 'IS')