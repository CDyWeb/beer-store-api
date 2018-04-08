from django.shortcuts import render


def index(request):
    """
    Returns index page
    """
    return render(request, 'index.html')

