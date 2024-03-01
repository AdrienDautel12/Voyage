from django.urls import path
from .views import reservation,details,historique_reservations,hebergement,details_h


from .import views

urlpatterns =[
    path("",views.index, name ="index"),
    path('reservation/', reservation, name='reservation'),
    path('details/', details, name='details'),
    path('historique/', historique_reservations, name='historique_reservations'),
    path('hebergement/', hebergement, name='hebergement'),
    path('details_h/', details_h, name='details_h'),


    

]