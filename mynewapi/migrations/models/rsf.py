from django.db import models, report, DPStep, MTZfile, ScalepackFile, Reference, Construct
from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo, DateTimeProperty, BooleanProperty

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