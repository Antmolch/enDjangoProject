
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from api.views import *

urlpatterns = [
     path('bot/create', BotCreateView.as_view()),
     path('bot/all', BotsListView.as_view()),

     path('commandType/create', TypeCommandCreateView.as_view()),
     path('commandType/all', TypeCommandListView.as_view()),

     path('command/create', CommandCreateView.as_view()),
     path('command/all', CommandsListView.as_view()),

     path('command/call/all', CallsListView.as_view()),
     path('command/call/create', CallsCreateView.as_view()),

     path('media/create',MediaCreateView.as_view()),
     path('media/all',MediaListView.as_view()),

     path('messageCommand/create', MessageCommandCreateView.as_view()),
     path('messageCommand/all', MessageCommandListView.as_view()),

     path('mailCommand/create', MailCommandCreateView.as_view()),
     path('mailCommand/all', MailCommandListView.as_view()),

     path('botChat/create', BotChatCreateView.as_view()),
     path('botChat/all', BotChatListView.as_view()),

     path('link/create', LinkCreateView.as_view()),
     path('link/all', LinkListView.as_view()),

#     path('bot/<int:pk>', BotDetailView.as_view()),
#     #
#     # path('command/create', CommandCreateView.as_view()),
#     # path('command/all', CommandsListView.as_view()),
#     # path('command/<int:pk>', CommandDetailView.as_view()),
#     #
#     # path('command/link/create', CommandLinkCreateView.as_view()),
#     # path('command/link/all', CommandLinksListView.as_view()),
#     # path('command/link/<int:pk>', CommandLinkDetailView.as_view()),
#     #

#     # path('command/type/all', CommandTypesListView.as_view()),
#     # path('command/type/<int:pk>', CommandTypeDetailView.as_view()),
#     #
#     #
#
#
]
