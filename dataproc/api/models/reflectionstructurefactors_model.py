from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

# from api.models.dpstep_model import DPStep
# from api.models.mtzfile_model import MTZfile
# from api.models.scalepackfile_model import ScalepackFile
# from api.models.reference_model import Reference
# from api.models.construct_model import Construct


class RefelctionStructureFactors(StructuredNode):
	rsf_source=StringProperty()
	rsf_filesize=StringProperty()
	rsf_filepath=StringProperty()

	# Relationships
	input_as_ref=RelationshipTo('DPStep', 'INPUT_AS_REFERENCE')
	input_of=RelationshipTo('DPStep', 'INPUT')
	generates_mtz=RelationshipTo('MTZfile', 'GENERATES')
	generates_scalepack=RelationshipTo('ScalepackFile', 'GENERATES')
	labelled=RelationshipTo('Reference', 'LABELLED')
	belongs=RelationshipTo('Construct', 'BELONGS')

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'rsf_source': self.rsf_source,
				'rsf_filesize': self.rsf_filesize,
				'rsf_filepath': self.rsf_filepath,
			},
		}