from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


from api.models import *

UserModel = get_user_model()


class BotDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = '__all__' # явно указываем все поля модели
class BotsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('app_name', 'token', 'url', 'name', 'launch_status', 'login_id')


class CommandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = '__all__'


class CommandsListView(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = ('bot_id', 'command_name', 'type_id', 'link_status', 'media_status')


class CommandLinkDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link_command
        fields = '__all__'


class CommandsLinkListView(serializers.ModelSerializer):
    class Meta:
        model = Link_command
        fields = ('current_command', 'following_command')