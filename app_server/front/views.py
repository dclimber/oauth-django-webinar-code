from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET


def index(request):
    context = {
    }
    return render(request, 'front/index.html', context)


@require_GET
def callback(request):
    return redirect('index')
