from rest_framework import serializers
from .models import Movie

# Serializer defines conversion logic of python object to json format
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year']