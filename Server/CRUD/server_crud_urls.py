from django.urls import path 
from . import views


urlpatterns = [
    path('with_noid' , views.With_NOID , name="WITH_NOID"),
    path('with_id/<int:pk>' , views.With_ID , name="WITH_ID"),
]