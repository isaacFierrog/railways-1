from rest_framework.viewsets import ModelViewSet
from .serializers import PersonaSerializer
from .models import Persona


class PersonaViewSet(ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()