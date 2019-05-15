
from django.shortcuts import render
from rest_framework import viewsets         
from .serializers import ContactSerializer, AlumniSerializer, EventSerializer     
from .models import Contact, Event, Alumni                     

class ContactView(viewsets.ModelViewSet):       
    serializer_class = ContactSerializer        
    queryset = Contact.objects.all()            

class EventView(viewsets.ModelViewSet):       
    serializer_class = EventSerializer        
    queryset = Event.objects.all()  

class AlumniView(viewsets.ModelViewSet):       
    serializer_class = AlumniSerializer        
    queryset = Alumni.objects.all() 