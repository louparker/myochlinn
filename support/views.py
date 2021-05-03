from django.shortcuts import render


def support(request):
    """ A view to return the support page """
    return render(request, 'support/support.html')
