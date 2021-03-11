import logging

import requests

from decouple import config
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import CreateUserSerializer

CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
OAUTH_SERVER_URL = config('OAUTH_SERVER_URL')

logger = logging.getLogger('django.server')


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    """
    # Put the data from the request into the serializer
    serializer = CreateUserSerializer(data=request.data)

    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save()
        logger.info('user created')
        # Then we get a token for the created user.
        # This could be done differently
        req = requests.post(
            f'{OAUTH_SERVER_URL}/o/token/',
            data={
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        return Response(req.json())
    logger.info('Serializer is not valid')
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    """
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    """
    req = requests.post(
        f'{OAUTH_SERVER_URL}/o/token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(req.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    """
    req = requests.post(
        f'{OAUTH_SERVER_URL}/o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(req.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    """
    Method to revoke tokens.
    {"token": "<token>"}
    """
    req = requests.post(
        f'{OAUTH_SERVER_URL}/o/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise)
    if req.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, req.status_code)

    # Return the error if it goes badly
    return Response(req.json(), req.status_code)
