from rest_framework.serializers import ModelSerializer
from .models import Tutorial

class TutorialSerializer(ModelSerializer):
  
  class Meta:
    model = Tutorial
    fields = "__all__"
    # fields = ("id",
    #           "title",
    #           "description")