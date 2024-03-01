from django.contrib import admin
from .models import Personne,Reservation,Activite,Hebergement,Voyage

admin.site.register(Personne)
admin.site.register(Reservation)
admin.site.register(Activite)
admin.site.register(Hebergement)
admin.site.register(Voyage)
