from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ This view returns the shopping bag page """
    return render(request, 'bag/bag.html')
