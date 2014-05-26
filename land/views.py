from django.shortcuts import render


def index(request):
    """
    Returns index page
    """
    return render(request, 'index.html')


def about(request):
    """
    returns about page 
    """
    return render(request, 'about.html')


def demos(request):
    """
    returns demo page
    """
    return render(request, 'demos.html')
