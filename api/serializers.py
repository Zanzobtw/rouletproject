# Turns python object into JSON

from rest_framework import serializers
from . models import Check_List

class Check_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Check_List
        fields = {"id", "task", "description", "status"}
