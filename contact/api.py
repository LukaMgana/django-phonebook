# contact/api.py
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contact


# serializer class for contacts
class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
