from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class HomeView(TemplateView):
    template_name = 'index.html'


class AdvisorCreate(generics.GenericAPIView):
    serializer_class = AdvisorSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if(serializer.is_valid()):

            serializer.save()
            return Response(
                {
                    'Message': 'Advisor Created Successfully',
                }, status=status.HTTP_200_OK)
        else:
            return Response({"Error": 'Advisor not Created'}, status=status.HTTP_400_BAD_REQUEST)


class Advisor(generics.ListAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class AdvisorBooking(generics.CreateAPIView):
    model = AdvisorBook
    serializer_class = AdvisorBookSerializer
    permission_classes = [IsAuthenticated]


class advisorBookingList(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        usr_id = self.request.session.get('id')
        user = User.objects.filter(id=usr_id)
        print(user, '-------------234------------------------------09876')
        queryset = AdvisorBook.objects.all()
        serializer = AdvisorBookSerializer(queryset, many=True)
        return Response(serializer.data)
