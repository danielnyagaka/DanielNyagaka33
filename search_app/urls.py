from django.urls import path,re_path
from . import views

app_name = 'search_app'

urlpatterns = [
		re_path(r'^.*/', views.searchResult, name='searchResult'), 
    ]