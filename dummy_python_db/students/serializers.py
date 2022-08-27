from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from students.models import student_details

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student_details
        # fields = ['name','age','mail']
        fields = '__all__'