from django.shortcuts import render

cars = ['Honda', 'Toyota', 'GM', 'Nissan']

# Create your views here.
def base(request):
    print('Ace of the base')
    return render(request, 't_i_app/base.html',)
