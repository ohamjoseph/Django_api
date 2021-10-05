from rest_framework import serializers
from .models import Departements, Provinces, Region

class DepartementsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departements
        fields = ['nom']

class ProviencesSerializer(serializers.ModelSerializer):
    departement = serializers.StringRelatedField(many=True)
    class Meta:
        model = Provinces
        fields = ['nom','chef_lieu','departement']
    chef_lieu=serializers.CharField(source='chef_lieu.nom')

class RegionSerializer(serializers.ModelSerializer):
    province = ProviencesSerializer(many=True)
    chef_lieu=serializers.CharField(source='chef_lieu.nom')

    class Meta:
        model = Region
        fields=['nom','chef_lieu','province']
