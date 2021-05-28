# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

class GPhLPipedream(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""
	
	# Properties
	command=StringProperty(max_length=500)
	jsonversion=StringProperty(max_length=500)
	runby=StringProperty(max_length=500)
	runfrom=StringProperty(max_length=500)
	jobid=StringProperty(unique_index=True, default=uuid4)
	output=StringProperty(max_length=500)
	version=StringProperty(max_length=500)

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
		'GPhL_pipedream_node_properties': {
		'command': self.command,
		'jsonversion': self.jsonversion,
		'runby': self.runby,
		'runfrom': self.runfrom,
		'jobid': self.jobid,
		'output': self.output,
		'version': self.version,
		},
		}