from django.urls import path , include



urlpatterns = [
    path('CRUD/' , include('Server.CRUD.server_crud_urls'))
]