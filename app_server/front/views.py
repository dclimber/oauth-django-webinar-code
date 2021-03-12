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
    return redirect('index')


@require_POST
def workhorse(request):
    pass
