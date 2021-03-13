import requests

from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.utils import get_full_url

CLIENT_ID = settings.CLIENT_ID
CLIENT_SECRET = settings.CLIENT_SECRET
OAUTH_SERVER_URL = settings.OAUTH_SERVER_URL


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    """
    Gets token with auth code. Input should be in the format:
    {"code": "code"}
    """
    redir_url = get_full_url(request, 'callback')
    resp = requests.post(
        f'{OAUTH_SERVER_URL}/o/token/',
        data={
            'grant_type': 'authorization_code',
            'redirect_uri': redir_url,
            'code': request.data['code'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(resp.json())


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
