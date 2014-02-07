from django.conf import settings

DSC = getattr(settings, "DOC_STORE_CONFIG", None)
db_name=DSC['db']
collection_name=DSC['collection']
