import requests

from django.conf import settings
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST

from core.utils import get_full_url


@require_GET
def index(request):
    # create callback url
    callback_url = get_full_url(request, 'callback')
    # get access token from session
    token = request.session.get('webinar_access_token')

    context = {
        'registered': bool(token is not None),
        'auth_url': (
            f'{settings.OAUTH_SERVER_URL}/o/authorize?response_type=code'
            f'&client_id={settings.CLIENT_ID}&redirect_uri={callback_url}'
        ),
    }
    return render(request, 'front/index.html', context)


@require_GET
def callback(request):
    # clear stored auth code
    request.session.pop('webinar_auth_code', None)
    # get auth code sent from Authorization server
    code = request.GET.get('code')
    if code is not None:
        # save it in the session
        request.session['webinar_auth_code'] = code
        resp = requests.post(
            get_full_url(request, 'get-token'),
            data={
                'code': code,
            }
        )
        resp_data = resp.json()
        if 'access_token' in resp_data:
            # delete auth code, as it is no longer needed
            request.session.pop('webinar_auth_code', None)
            request.session['webinar_access_token'] = resp_data['access_token']
    return redirect('index')


@require_POST
def workhorse(request):
    pass
