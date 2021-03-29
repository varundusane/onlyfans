from django.urls import path
from .views import home_view, jobDetails

app_name='scraped'
urlpatterns = [
    path('',home_view, name= 'home_View'),
    path('job/<id>/', jobDetails, name="job_details"),

]