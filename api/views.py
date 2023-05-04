from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class BotCreateView(generics.CreateAPIView):
    serializer_class = BotDetailSerializer

class BotsListView(generics.ListAPIView):
    serializer_class = BotsListSerializer
    queryset = Bot.objects.all()



class BotDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BotDetailSerializer
    queryset = Bot.objects.all()



class CommandCreateView(generics.CreateAPIView):
    serializer_class = CommandDetailSerializer


class CommandsListView(generics.ListAPIView):
    serializer_class = CommandsListView
    queryset = Command.objects.all()



class CommandDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommandDetailSerializer
    queryset = Command.objects.all()



class CommandLinkCreateView(generics.CreateAPIView):
    serializer_class = CommandLinkDetailSerializer


class CommandLinksListView(generics.ListAPIView):
    serializer_class = CommandLinksListView
    queryset = Link_command.objects.all()



class CommandLinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommandLinkDetailSerializer
    queryset = Link_command.objects.all()

class CommandTypeCreateView(generics.CreateAPIView):
    serializer_class = CommandTypeDetailSerializer

class CommandTypesListView(generics.ListAPIView):
    serializer_class = CommandTypesListView
    queryset = Type_command.objects.all()


class CommandTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommandLinkDetailSerializer
    queryset = Type_command.objects.all()


