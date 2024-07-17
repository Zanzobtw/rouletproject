# Turns python object into JSON

from rest_framework import serializers
from . models import check_list

class Check_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Check_list
        fields = {"id", "task", "description", "status"}
