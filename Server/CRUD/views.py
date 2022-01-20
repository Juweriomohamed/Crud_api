from rest_framework.decorators import api_view
from rest_framework.response import Response
from CRUD import models
from . import serializer
from django.core.exceptions import ObjectDoesNotExist

# GET , POST , DELETE , PUT


@api_view(['GET', 'POST'])
def With_NOID(request):

    if request.method == 'GET':
        accounts = models.Accounts.objects.all()
        serializeData = serializer.AccountSerializer(accounts, many=True)

        response = Response()

        data = {
            'isError': False,
            'Message': serializeData.data
        }

        response.data = data

    elif request.method == 'POST':

        # Check email address
        try:
            user = models.Accounts.objects.get(Email=request.POST.get('Email'))

            response = Response()

            data = {
                'isError': True,
                'Message': "Email is already in use"
            }

            response.data = data

        except ObjectDoesNotExist:
            try:
                user = models.Accounts.objects.get(
                    Username=request.POST.get('Username'))

                response = Response()

                data = {
                    'isError': True,
                    'Message': "Username is already in use"
                }

                response.data = data
            except ObjectDoesNotExist:
                serializeData = serializer.AccountSerializer(data=request.data)

                if serializeData.is_valid():
                    serializeData.save()

                    response = Response()

                    data = {
                        'isError': False,
                        'Message': "New Account Has Been Created"
                    }

                    response.data = data

    return response


@api_view(['GET', 'PUT', 'DELETE'])
def With_ID(request, pk):

    if request.method == 'GET':
        try:
            account = models.Accounts.objects.get(id=pk)
            serializeData = serializer.AccountSerializer(account)

            response = Response()

            data = {
                'isError': False,
                'Message': serializeData.data
            }

            response.data = data
        except ObjectDoesNotExist:
            response = Response()

            data = {
                'isError': True,
                'Message': "Account Was Not Created"
            }

            response.data = data

    elif request.method == 'DELETE':
        try:
            account = models.Accounts.objects.get(id=pk)
            account.delete()

            response = Response()

            data = {
                'isError': False,
                'Message': "Account Has been Deleted"
            }

            response.data = data

        except ObjectDoesNotExist:
            response = Response()

            data = {
                'isError': True,
                'Message': "Account Was Not Created"
            }

            response.data = data

    elif request.method == 'PUT':
        try:
            account = models.Accounts.objects.get(id=pk)

            serializeData = serializer.AccountSerializer(account, request.data)

            if serializeData.is_valid():
                serializeData.save()

                response = Response()

                data = {
                    'isError': False,
                    'Message': "New Account Has Been Updated"
                }

                response.data = data

        except ObjectDoesNotExist:
            response = Response()

            data = {
                'isError': True,
                'Message': "Account Was Not Created"
            }

            response.data = data

    return response
