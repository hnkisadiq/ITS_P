from rest_framework import serializers
from snippets.models import Farms
from snippets.models import Houses
from snippets.models import Snippet,Identity,Property_1,Property_2, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identity
        fields = ('id', 'Adhaar_id', 'Name')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Identity.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.Adhaar_id = validated_data.get('Adhaar_id', instance.Adhaar_id)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.save()
        return instance

class Property1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Property_1
        fields = ( 'A_id', 'house_id')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Property_1.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.A_id = validated_data.get('A_id', instance.A_id)
        instance.house_id = validated_data.get('house_id', instance.house_id)
        instance.save()
        return instance

class Property2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Property_2
        fields = ( 'A_id', 'farm_id')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Property_2.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.A_id = validated_data.get('A_id', instance.A_id)
        instance.farm_id = validated_data.get('farm_id', instance.farm_id)
        instance.save()
        return instance

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = ('id','H_id', 'lat', 'lon','Area','Income')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Houses.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.H_id = validated_data.get('H_id', instance.H_id)
        instance.lat = validated_data.get('lat', instance.lat)
        instance.long = validated_data.get('long', instance.long)
        instance.Area = validated_data.get('Area', instance.Area)
        instance.Income = validated_data.get('Income', instance.Income)
        instance.save()
        return instance

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farms
        fields = ('id','F_id', 'poly','Area','crops')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Farms.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.F_id = validated_data.get('F_id', instance.F_id)
        '''instance.lat1 = validated_data.get('lat1', instance.lat1)
        instance.long1 = validated_data.get('long1', instance.long1)
        instance.lat2 = validated_data.get('lat2', instance.lat2)
        instance.long2 = validated_data.get('long2', instance.long2)
        instance.lat3 = validated_data.get('lat3', instance.lat3)
        instance.long3 = validated_data.get('long3', instance.long3)
        instance.lat4 = validated_data.get('lat4', instance.lat4)
        instance.long4 = validated_data.get('long4', instance.long4)'''
        instance.poly = validated_data.get('poly', instance.poly)
        instance.Area = validated_data.get('Area', instance.Area)
        instance.crops = validated_data.get('crops', instance.crops)
        instance.save()
        return instance
