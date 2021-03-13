from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # API
    path('api/', include('poems.urls')),
    path('', TemplateView.as_view(template_name='index.html'))
]
