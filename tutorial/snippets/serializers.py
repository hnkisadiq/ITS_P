from rest_framework import serializers
from snippets.models import Farms
from snippets.models import Houses,Well
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
        fields = ('id','H_id', 'h_point','Area','Income')

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
        instance.h_point = validated_data.get('h_point', instance.h_point)
        instance.Area = validated_data.get('Area', instance.Area)
        instance.Income = validated_data.get('Income', instance.Income)
        instance.save()
        return instance
class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = ('id','w_id', 'w_point','depth')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Well.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.w_id = validated_data.get('w_id', instance.w_id)
        instance.w_point = validated_data.get('w_point', instance.w_point)
        instance.depth = validated_data.get('depth', instance.depth)
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
        instance.poly = validated_data.get('poly', instance.poly)
        instance.Area = validated_data.get('Area', instance.Area)
        instance.crops = validated_data.get('crops', instance.crops)
        instance.save()
        return instance
