from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

# from api.models.ocf_model import OCF
# from api.models.storagehost_model import StorageHost
# from api.models.computinghost_model import ComputingHost
# from api.models.user_model import User

class Construct(StructuredNode):
	
	uid=UniqueIdProperty(default=uuid4)
	name=StringProperty()
	
	# Relationships
	has_ocf=RelationshipTo('api.models.ocf_model.OCF', 'HAS')
	has_storage_host=RelationshipTo('api.models.storagehost_model.StorageHost', 'HAS')
	has_computing_host=RelationshipTo('api.models.computinghost_model.ComputingHost', 'HAS')
	has_user=RelationshipTo('api.models.user_model.User', 'HAS')