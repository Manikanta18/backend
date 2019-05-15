from rest_framework import serializers
from .models import Contact, Alumni, Event

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'note')

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumni
        fields = ('id', 'name', 'image', 'company', 'country')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'testname', 'date', 'description')