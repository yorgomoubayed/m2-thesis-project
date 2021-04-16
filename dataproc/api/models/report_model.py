from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

from api.models.statisticalreport_model import StatisticalReport
from api.models.summaryout_model import SummaryOut
from api.models.summaryhtml_model import SummaryHtml

class Report(StructuredNode):
	report_path=StringProperty()
	report_source=StringProperty()
	report_size=StringProperty()

	 # Relationships
	is_statisticalreport=RelationshipTo(StatisticalReport, 'IS')
	is_summaryout=RelationshipTo(SummaryOut, 'IS')
	is_summaryhtml=RelationshipTo(SummaryHtml, 'IS')

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'report_path': self.report_path,
				'report_source': self.report_source,
				'report_size': self.report_size,
			},
		}