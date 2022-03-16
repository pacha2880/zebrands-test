from django.http import HttpResponse
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
from rest_framework import status
from django.http import Http404
from .permissions import AuthenticatedOrReadOnly, AuthenticatedOnly


class ProductList(APIView):
    """
    List all products, or create a new product.
    """

    permission_classes = [AuthenticatedOrReadOnly]

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    """
    Retrieve, update or delete a product instance.
    """

    permission_classes = [AuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Product.objects.get(sku=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        product.queried()
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NotificationList(generics.ListAPIView):
    """
    List all notifications.
    """

    permission_classes = [AuthenticatedOnly]
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
