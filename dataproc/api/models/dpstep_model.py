from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

from api.models.ligandsfitting_model import LigandsFitting
from api.models.refinement_model import Refinement
from api.models.postrefinement_model import PostRefinement
from api.models.reductionscaling_model import ReductionScaling
from api.models.autoPROC_model import autoPROC
from api.models.rhofit_model import Rhofit
from api.models.buster_model import Buster
from api.models.report_model import Report
from api.models.coordinates_model import Coordinates
from api.models.reflectionstructurefactors_model import RefelctionStructureFactors
from api.models.pdbfile_model import PDBFile
from api.models.mmciffile_model import mmCIFFile
from api.models.construct_model import Construct
from api.models.reference_model import Reference

class DPStep(StructuredNode):
 	
 	# Relationships
 	is_fitting=RelationshipTo(LigandsFitting, 'IS')
 	is_refinement=RelationshipTo(Refinement, 'IS')
 	is_postrefinement=RelationshipTo(PostRefinement, 'IS')
 	is_reductionscaling=RelationshipTo(ReductionScaling, 'IS')
 	with_tool_1=RelationshipTo(autoPROC, 'WITH')
 	with_tool_2=RelationshipTo(Rhofit, 'WITH')
 	with_tool_3=RelationshipTo(Buster, 'WITH')
 	genereates_report=RelationshipTo(Report, 'GENERATES')
 	generates_coordinates=RelationshipTo(Coordinates, 'GENERATES')
 	generates_rsf=RelationshipTo(RefelctionStructureFactors, 'GENERATES')

 	@property
 	def serialize(self):

 		"""
 		Serializer for node properties
 		"""
 		
 	    return {
 	        'node_properties': {
 	            # 'uuid': self.uuid,
 	            # 'tool_name': self.name,
 	        },
 	    }
# class Coordinates(StructuredNode):
#  	coordinates_source=StringProperty(unique_index=True, required=True)
#  	coordinates_filesize=StringProperty(unique_index=True, required=True)
#  	coordinates_filepath=StringProperty(unique_index=True, required=True)

#  	# Relationships
#  	input_as_ref=RelationshipTo(DPStep, 'INPUT_AS_REFERENCE')
#  	input_of=RelationshipTo(DPStep, 'INPUT')
#  	has_pdb=RelationshipTo(PDBFile, 'HAS')
#  	has_mmcif=RelationshipTo(mmCIFFile, 'HAS')
#  	belongs=RelationshipTo(Construct, 'BELONGS')
#  	labelled=RelationshipTo(Reference, 'LABELLED')
