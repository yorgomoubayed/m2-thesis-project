from django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, DateTimeProperty, BooleanProperty

# class City(StructuredNode):
#     code = StringProperty(unique_index=True, required=True)
#     name = StringProperty(index=True, default="city")

#####################################
# Nodes and properties of the model #
#####################################

class LigandsFitting(StructuredNode):
	uid=UniqueIdProperty()
	dp_step_name = StringProperty()
	created_at=DateTimeProperty()
	updated_at=DateTimeProperty()
	pipedream_id=IntegerProperty()
	score=IntegerProperty()
	fitting_success=BooleanProperty()

class Refinement(StructuredNode):
	uid=UniqueIdProperty()
	dp_step_name=StringProperty()
	created_at=DateTimeProperty()
	updated_at=DateTimeProperty()

class PostRefinement(StructuredNode):
	uid=UniqueIdProperty()
	dp_step_name=StringProperty()
	pipedream_id=IntegerProperty()
	created_at=DateTimeProperty()
	updated_at=DateTimeProperty()

class ReductionScaling(StructuredNode):
	uid=UniqueIdProperty()
	dp_step_name=StringProperty()
	created_at=DateTimeProperty()
	updated_at=DateTimeProperty()

class autoPROC(StructuredNode):
	uid=UniqueIdProperty()
	tool_name=StringProperty()

class Buster(StructuredNode):
	uid=UniqueIdProperty()
	tool_name=StringProperty()

class Rhofit(StructuredNode):
	uid=UniqueIdProperty()
	tool_name=StringProperty()

class StatisticalReport(StructuredNode):
	uid=UniqueIdProperty()
	report_name=StringProperty()

class ComputingHost(StructuredNode):
	ch_softwares=StringProperty()
	ch_softwares_number=IntegerProperty()

class StorageHost(StructuredNode):
	sh_files=StringProperty()
	sh_files_number=IntegerProperty()

##########################################################################

class Report(StructuredNode):
 	report_path=StringProperty()
 	report_source=StringProperty()
 	report_size=StringProperty()

 	# Relationships
 	is_statisticalreport=RelationshipTo(StatisticalReport, 'IS')

class RefelctionStructureFactors(StructuredNode):
 	rsf_source=StringProperty()
 	rsf_filesize=StringProperty()
 	rsf_filepath=StringProperty()

 	# Relationships
 	input_as_ref=RelationshipTo(DPStep, 'INPUT_AS_REFERENCE')
 	input_of=RelationshipTo(DPStep, 'INPUT')
 	generates_mtz=RelationshipTo(MTZfile, 'GENERATES')
 	generates_scalepack=RelationshipTo(ScalepackFile, 'GENERATES')
 	labelled=RelationshipTo(Reference, 'LABELLED')
 	belongs=RelationshipTo(Construct, 'BELONGS')

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
 	# generates_coordinates=RelationshipTo(Coordinates, 'GENERATES')
 	generates_rsf=RelationshipTo(RefelctionStructureFactors, 'GENERATES')

class Coordinates(StructuredNode):
 	coordinates_source=StringProperty(unique_index=True, required=True)
 	coordinates_filesize=StringProperty(unique_index=True, required=True)
 	coordinates_filepath=StringProperty(unique_index=True, required=True)

 	# Relationships
 	input_as_ref=RelationshipTo(DPStep, 'INPUT_AS_REFERENCE')
 	input_of=RelationshipTo(DPStep, 'INPUT')
 	has_pdb=RelationshipTo(PDBFile, 'HAS')
 	has_mmcif=RelationshipTo(mmCIFFile, 'HAS')
 	belongs=RelationshipTo(Construct, 'BELONGS')
 	labelled=RelationshipTo(Reference, 'LABELLED')


class DataCollection (StructuredNode):
 	collection_type=StringProperty()
 	collection_size=StringProperty()

 	# Relationships
 	genereates_dataset=RelationshipTo(Datatset, 'GENERATES')

class Datatset(StructuredNode):
 	dataset_file_no=IntegerProperty()
 	dataset_size=StringProperty()

 	# Relationships
 	input_of=RelationshipTo(DPStep, 'INPUT')
 	stored=RelationshipTo(StorageHost, 'STORED')
 	belongs=RelationshipTo(Construct, 'BELONGS')

class mmCIFFile(StructuredNode):
	uid=UniqueIdProperty()
	coordinates_filetype=StringProperty(unique_index=True, required=True)

class PDBFile(StructuredNode):
	uid=UniqueIdProperty()
	coordinates_filetype=StringProperty(unique_index=True, required=True)

class MTZfile(StructuredNode):
	uid=UniqueIdProperty()
	rsf_filetype = StringProperty(unique_index=True, required=True)

class ScalepackFile(StructuredNode):
	uid=UniqueIdProperty()
	rsf_filetype = StringProperty(unique_index=True, required=True)

class Reference(StructuredNode):
	uid=UniqueIdProperty()

class OCF(StructuredNode):
	
	# Relationships
	has_rsf=RelationshipTo(RefelctionStructureFactors, 'HAS')
	has_coordinates=RelationshipTo(Coordinates, 'HAS')

class Construct(StructuredNode):
	
	# Relationships
	has_ocf=RelationshipTo(OCF, 'HAS')
	has_storage_host=RelationshipTo(StorageHost, 'HAS')
	has_computing_host=RelationshipTo(ComputingHost, 'HAS')


class Ligand(StructuredNode):
	 
	# Relationships
 	associated=RelationshipTo(Datatset, 'ASSOCIATED')

