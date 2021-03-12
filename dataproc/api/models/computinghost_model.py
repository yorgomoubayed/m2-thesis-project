from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

class ComputingHost(StructuredNode):
	ch_softwares=StringProperty()
	ch_softwares_number=IntegerProperty()
