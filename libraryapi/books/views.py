from django.shortcuts import render
from books.models import Book
from books.serializer import bookserializer,userserializer
from django.contrib.auth.models import User
from rest_framework import mixins,generics,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# @api_view(['GET','POST'])
# def booklist(request):
#     if (request.method == 'GET'):
#         book=Book.objects.all()
#         b=bookserializer(book,many=True)
#         return Response(b.data)
#     elif(request.method == 'POST'):
#         b=bookserializer(data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data,status=status.HTTP_201_CREATED)
#         return Response(b.error,status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET','PUT','DELETE'])
# def bookdetails(request,pk):#primarykey based
#     try:
#         book=Book.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if(request.method=='GET'):
#         b = bookserializer(book)
#         return Response(b.data)
#     elif(request.method=='PUT'):#updation
#         b= bookserializer(book,data=request.data)
#         if b.is_valid():
#             b.save()
#             return Response(b.data, status=status.HTTP_201_CREATED)
#         return Response(b.error, status=status.HTTP_400_BAD_REQUEST)
#     elif(request.method == 'DELETE'):
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------mixins--------------------

# class booklist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Book.objects.all()
#     serializer_class=bookserializer
#     def get(self,request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
# class bookdetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = bookserializer
#
#     def get(self, request):
#         return self.retrieve(request)
#
#     def put(self, request):
#         return self.update(request)
#
#     def get(self, request):
#         return self.destroy(request)

#---------------------------generics----------------------

# class booklist(generics.ListCreateAPIView):#non primay
#     queryset=Book.objects.all()
#     serializer_class=bookserializer
# class bookdetails(generics.RetrieveUpdateDestroyAPIView):#primay key based
#     queryset = Book.objects.all()
#     serializer_class = bookserializer

#----------------------------------viewset----------------------------

class bookviewset(viewsets.ModelViewSet):#primary and non primary key based
    permission_classes=[IsAuthenticated,]
    queryset = Book.objects.all()
    serializer_class = bookserializer

#----------------------------------------registration form--------------------------------------------------------------


class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer



