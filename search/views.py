# search/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer, ClothesSerializer, MobileSerializer
from book.models import Book
from clothes.models import Clothes
from mobile.models import Mobile


@api_view(['GET'])
def search(request):
    query = request.query_params.get('q', None)
    if query is not None:
        book_queryset = Book.objects.filter(title__icontains=query)
        clothes_queryset = Clothes.objects.filter(name__icontains=query)
        mobile_queryset = Mobile.objects.filter(name__icontains=query)

        results = list(book_queryset) + list(clothes_queryset) + list(mobile_queryset)

        if 'books' in request.query_params.get('type'):
            serializer = BookSerializer(book_queryset, many=True)
        elif 'clothes' in request.query_params.get('type'):
            serializer = ClothesSerializer(clothes_queryset, many=True)
        elif 'mobiles' in request.query_params.get('type'):
            serializer = MobileSerializer(mobile_queryset, many=True)
        else:
            return Response({'message': 'Invalid search path'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)
    else:
        return Response({'message': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)
