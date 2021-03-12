import requests

from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.decorators.http import require_GET, require_POST

from core.utils import get_full_url

from .forms import ResourceForm


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
        'form': ResourceForm()
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


@require_GET
def logout(request):
    token = request.session.get('webinar_access_token')
    if token is not None:
        requests.post(
            get_full_url(request, 'revoke-token'),
            data={
                'token': token,
            }
        )
        request.session.pop('webinar_access_token', None)
    return redirect('index')


@require_POST
def workhorse(request):
    form = ResourceForm(request.POST)
    api_url = f'{settings.OAUTH_SERVER_URL}/api/v1/'
    if form.is_valid():
        data = form.cleaned_data.get('data')
        # create url
        resource_type = form.cleaned_data['resource_type']
        url = f'{api_url}{resource_type}/'
        # create headers
        token = request.session.get('webinar_access_token')
        headers = {'Authorization': f'Bearer {token}'}
        # make appropriate request
        request_method = form.cleaned_data['method']
        if request_method == 'GET':
            resp = requests.get(
                url,
                headers=headers
            )
        else:
            resp = requests.post(
                url,
                data=data,
                headers=headers
            )
        if resp.status_code == 401:
            del request.session['webinar_access_token']
            return redirect('index')
        return JsonResponse(
            {
                'status': 'success' if resp.status_code == 200 else 'fail',
                'data': resp.json()
            },
            status=resp.status_code
        )
    # output form errors
    form_error_tpl = render_to_string('front/_form_fields.html', {'form': form})
    return JsonResponse(
        {
            'status': 'fail',
            'data': {
                'message': 'Form invalid',
                'form': form_error_tpl
            },
        }, status=400
    )
