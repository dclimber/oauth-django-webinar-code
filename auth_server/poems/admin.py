from django.contrib import admin

from .models import Poem, Poet

admin.site.register(Poet)
admin.site.register(Poem)
