from rest_framework import serializers

from .models import User_data, Period

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_data
        fields = '__all__'

class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'          

class ListSerializer(serializers.Serializer):

    class Meta:
        model = [User_data, Period]
        fields = '__all__'