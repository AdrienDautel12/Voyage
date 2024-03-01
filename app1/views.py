from django.shortcuts import render
from .models import Reservation


def index(request):
    return render(request, 'signin.html')

def reservation(request):
    return render (request,'reservation.html')

def hebergement(request):
    return render (request,'hebergement.html')

def details_h(request):
    if request.method == 'POST':
        num_persons = request.POST.get('num_persons')
        num_nights = request.POST.get('num_nights')
        prix_nuit = request.POST.get('prix_nuit')
        outdoor = request.POST.get('outdoor')
        animals = request.POST.get('animals')

        return render(request, 'details_h.html', {
            'num_persons': num_persons,
            'num_nights': num_nights,
            'prix_nuit': prix_nuit,
            'outdoor': outdoor,
            'animals': animals
        })
    else:
        return render('hebergement')
    

def details(request):
    if request.method == 'POST':
        departure = request.POST.get('departure')
        destination = request.POST.get('destination')
        transport_type = request.POST.get('transport_type')
        price = request.POST.get('price')
        num_persons = request.POST.get('num_persons')
        date = request.POST.get('date')
        time = request.POST.get('time')

        return render(request, 'details.html', {
            'departure': departure,
            'destination': destination,
            'transport_type': transport_type,
            'price': price,
            'num_persons': num_persons,
            'date': date,
            'time': time
        })
    else:
        return render('reservation')
    
def historique_reservations(request):
    reservations = Reservation.objects.filter(utilisateur=request.user)
    return render(request, 'historique_reservations.html', {'reservations': reservations})

