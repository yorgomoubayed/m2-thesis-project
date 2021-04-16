from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

# from api.models.pdbfile_model import PDBFile
# from api.models.mmciffile_model import mmCIFFile
# from api.models.construct_model import Construct
# from api.models.reference_model import Reference

class Coordinates(StructuredNode):
	coordinates_source=StringProperty(unique_index=True, required=True)
	coordinates_filesize=StringProperty()
	coordinates_filepath=StringProperty()

	# Relationships
	input_as_ref=RelationshipTo('api.models.dpstep_model.DPStep', 'INPUT_AS_REFERENCE')
	input_of=RelationshipTo('api.models.dpstep_model.DPStep', 'INPUT')
	has_pdb=RelationshipTo('api.models.pdbfile_model.PDBFile', 'HAS')
	has_mmcif=RelationshipTo('api.models.mmciffile_model.mmCIFFile', 'HAS')
	belongs=RelationshipTo('api.models.construct_model.Construct', 'BELONGS')
	labelled=RelationshipTo('api.models.reference_model.Reference', 'LABELLED')


	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
			'node_properties': {
				'coordinates_source': self.coordinates_source,
				'coordinates_filesize': self.coordinates_filesize,
				'coordinates_filepath': self.coordinates_filepath,
			},
		}