from django.urls import reverse


def get_full_url(request, url_name):
    server_host = request.get_host()
    url = reverse(url_name)
    return f'{request.scheme}://{server_host}{url}/'
