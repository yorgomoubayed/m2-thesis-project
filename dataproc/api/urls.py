from django.urls import path
from dataproc.api.views import(
	api_detail_construct_view,
	api_update_construct_view,
	api_delete_construct_view,
	api_create_construct_view,
)

app_name = 'dataproc'

urlpatterns = [
	path('<slug>/', api_detail_construct_view, name="detail"),
	path('<slug>/update', api_update_construct_view, name="update"),
	path('<slug>/delete', api_delete_construct_view, name="delete"),
	path('create', api_create_construct_view, name="create"),
]