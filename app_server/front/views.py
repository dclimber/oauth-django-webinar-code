from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def index(request):
    # create callback url
    server_host = request.get_host()
    callback_url = reverse('callback')
    full_callback_url = f'{request.scheme}://{server_host}{callback_url}/'
    # get access token from session
    token = request.session.get('webinar_access_token')

    context = {
        'registered': bool(token is not None),
        'auth_url': (
            f'{settings.OAUTH_SERVER_URL}/o/authorize?response_type=code'
            f'&client_id={settings.CLIENT_ID}&redirect_uri={full_callback_url}'
        ),
    }
    return render(request, 'front/index.html', context)


@require_GET
def callback(request):
    return redirect('index')


@require_POST
def workhorse(request):
    pass
