from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from djoser.serializers import TokenSerializer
from rest_framework import serializers

from api.functions import get_user_id_from_request
from api.models import *



# UserModel = get_user_model()
#
#
#
#
#

#
# class MailCommandListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MailCommand
#         fields = "__all__"
#
#
# class CommandListSerializer(serializers.ModelSerializer):
#     commandcall = CommandCallListSerializer(many=True, read_only=True)
#     mail_command = MailCommandListSerializer(many=True, read_only=True)
#     class Meta:
#         model = Command
#         fields = '__all__'
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['commandcall'] = CommandCallListSerializer(instance.call.all(), many=True).data
#         # data['mail_command'] = MailCommandListSerializer(instance.mail_command.all(), many=True).data
#
#         return data
#
#
# class CommandSerializer(serializers.ModelSerializer):
#     command_calls = CommandCallListSerializer(many=True, read_only=True, source='CommandCall')
#
#     class Meta:
#         model = Command
#         fields = '__all__'


class CommandCallListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandCall
        fields = "__all__"

class CommandCallDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandCall
        fields = ('id', 'name','command_id')

    def validate(self, data):
        """
        Проверяем, что все обязательные поля заполнены
        """
        if not data.get('command_id'):
            raise serializers.ValidationError("Поле commmand_id обязательно для заполнения")

        if not data.get('name'):
            raise serializers.ValidationError("Поле name обязательно для заполнения")
        return data


class BotDetailSerializer(serializers.ModelSerializer):

    # commands = CommandListSerializer(many=True, read_only=True)

    class Meta:
        model = Bot
        fields = '__all__'

    def validate(self, data):
        """
        Проверяем, что все обязательные поля заполнены
        """
        if not data.get('unique_name'):
            raise serializers.ValidationError("Поле unique_name обязательно для заполнения")

        if not data.get('name'):
            raise serializers.ValidationError("Поле name обязательно для заполнения")

        if not data.get('token'):
            raise serializers.ValidationError("Поле token обязательно для заполнения")

        if not data.get('url'):
            raise serializers.ValidationError("Поле url обязательно для заполнения")



        return data

class TypeCommandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCommand
        fields = ('id', 'name')

    def validate(self, data):
        """
        Проверяем, что все обязательные поля заполнены
        """
        if not data.get('name'):
            raise serializers.ValidationError("Поле name обязательно для заполнения")
        return data


class CommandsListSerializer(serializers.ModelSerializer):




    class Meta:
        model = Command
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        type_ids = representation.pop('type_id', [])
        types = TypeCommand.objects.filter(id__in=type_ids)
        type_names = TypeCommandDetailSerializer(types, many=True).data
        representation['type'] = type_names

        command_calls = instance.calls.all()
        call_data = CommandCallDetailSerializer(command_calls, many=True).data
        representation['calls'] = call_data

        return representation





class BotsListSerializer(serializers.ModelSerializer):
    commands = serializers.SerializerMethodField()
    class Meta:
        model = Bot
        fields = "__all__"

    def get_commands(self, bot):
        commands = Command.objects.filter(bot_id=bot.id)
        print("bot id",bot.id)
        return CommandsListSerializer(commands, many=True).data


    def __init__(self, *args, **kwargs):
        request = kwargs['context']['request']
        userid = get_user_id_from_request(request)
        user = User.objects.get(id=userid)
        super().__init__(*args, **kwargs)
        print(user.id)
        self.Meta.queryset = Bot.objects.filter(login_id=user.id)



class TypeCommandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCommand
        fields = ('id', 'name')


class CommandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ('id', 'name', 'link_status', 'bot_id', 'type_id')

#
#
# # class CommandLinkDetailSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Link_command
# #         fields = '__all__'
# #
# #
# # class CommandLinksListView(serializers.ModelSerializer):
# #     class Meta:
# #         model = Link_command
# #         fields = "__all__"
# #
# #

# #
# #
# # class CommandTypesListView(serializers.ModelSerializer):
# #     class Meta:
# #         model = Type_command
# #         fields = "__all__"
# #
# #
# # User = get_user_model()
# #
# #
# # class CustomUserCreateSerializer(UserCreateSerializer):
# #     def validate_email(self, value):
# #         if User.objects.filter(email=value).exists():
# #             raise serializers.ValidationError('Email already exists')
# #         return value
# #
# #     class Meta:
# #         model = User
# #         fields = ('id', 'email', 'password','username')
# #
# # class CustomTokenSerializer(TokenSerializer):
# #     user_id = serializers.IntegerField(source='user.id')
# #
# #     class Meta(TokenSerializer.Meta):
# #         fields = TokenSerializer.Meta.fields + ('user_id',)
# #
# #
