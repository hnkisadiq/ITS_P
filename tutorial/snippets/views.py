from rest_framework import status
from snippets.serializers import FarmSerializer
from snippets.models import Farms
from snippets.serializers import HouseSerializer
from snippets.models import Houses
from snippets.serializers import Property2Serializer
from snippets.serializers import Property1Serializer
from snippets.serializers import IdentitySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet,Identity,Property_1,Property_2
from snippets.serializers import SnippetSerializer
@api_view(['GET', 'POST'])
def snippet_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def Identity_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Identity.objects.all()
        serializer = IdentitySerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IdentitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def identity_detail(request, pk,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Identity.objects.get(pk=pk)
    except Identity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IdentitySerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IdentitySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def property1_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Property_1.objects.all()
        serializer = Property1Serializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Property1Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def property1_detail(request, pk,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Property_1.objects.get(pk=pk)
    except Property_1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Property1Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Property1Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def property2_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Property_2.objects.all()
        serializer = Property2Serializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Property2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def property2_detail(request, pk,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Property_2.objects.get(pk=pk)
    except Poperty_2.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Property2Serializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Property2Serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def house_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Houses.objects.all()
        serializer = HouseSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def house_detail(request, pk,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Houses.objects.get(pk=pk)
    except Houses.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HouseSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HouseSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def farm_list(request,format=None):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Farms.objects.all()
        serializer = FarmSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FarmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def farm_detail(request, pk,format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = Farms.objects.get(pk=pk)
    except Farms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FarmSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FarmSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
