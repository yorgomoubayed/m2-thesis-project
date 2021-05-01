# Python imports
from uuid import uuid4

# Third-party imports
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo

# Models imports
from api.models.ligandsfitting_model import LigandsFitting
from api.models.refinement_model import Refinement
from api.models.postrefinement_model import PostRefinement
from api.models.reductionscaling_model import ReductionScaling
from api.models.autoPROC_model import autoPROC
from api.models.rhofit_model import Rhofit
from api.models.buster_model import Buster
from api.models.report_model import Report
from api.models.coordinates_model import Coordinates
from api.models.structurefactors_model import StructureFactors
from api.models.pdbfile_model import PDBFile
from api.models.mmciffile_model import mmCIFFile
from api.models.construct_model import Construct
from api.models.reference_model import Reference
from api.models.pipedream_model import Pipedream
from api.models.pipedream_cmd_options_model import PipedreamCmdOptions
from api.models.autoproc_cmd_options_model import AutoprocCmdOptions
from api.models.buster_cmd_options_model import BusterCmdOptions
from api.models.rhofit_cmd_options_model import RhofitCmdOptions
from api.models.running_model import Running
from api.models.pending_model import Pending
from api.models.completed_model import Completed
from api.models.failed_model import Failed
from api.models.importation_model import Importation

class DPStep(StructuredNode):
	
	"""
	Defines node properties and relationships
	Provides data serializer
	"""

	# Properties
	uuid=StringProperty(unique_index=True, default=uuid4)
	name=StringProperty()
	
	# Relationships
	is_fitting=RelationshipTo(LigandsFitting, 'IS')
	is_refinement=RelationshipTo(Refinement, 'IS')
	is_postrefinement=RelationshipTo(PostRefinement, 'IS')
	is_reductionscaling=RelationshipTo(ReductionScaling, 'IS')
	is_importation=RelationshipTo(Importation, 'IS')
	
	with_autoproc=RelationshipTo(autoPROC, 'WITH')
	with_rhofit=RelationshipTo(Rhofit, 'WITH')
	with_buster=RelationshipTo(Buster, 'WITH')
	with_pipedream=RelationshipTo(Pipedream, 'WITH')
	
	genereates_report=RelationshipTo(Report, 'GENERATES')
	generates_coordinates=RelationshipTo(Coordinates, 'GENERATES')
	generates_structurefactors=RelationshipTo(StructureFactors, 'GENERATES')
	
	failed=RelationshipTo(Failed, 'IS')
	completed=RelationshipTo(Completed, 'IS')
	pending=RelationshipTo(Pending, 'IS')
	running=RelationshipTo(Running, 'IS')

	pipedream_cmd_options=RelationshipTo(PipedreamCmdOptions, 'HAS')
	autoproc_cmd_options=RelationshipTo(AutoprocCmdOptions, 'HAS')
	buster_cmd_options=RelationshipTo(BusterCmdOptions, 'HAS')
	rhofit_cmd_options=RelationshipTo(RhofitCmdOptions, 'HAS')

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
		return {
		'dpstep_node_properties': {
		'uuid': self.uuid,
		'name': self.name,
		},
		}