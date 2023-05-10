from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import permissions, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token

def get_user_id_from_token(token):
    try:
        token_obj = Token.objects.get(key=token)
        user_id = token_obj.user_id
        return user_id
    except Token.DoesNotExist:
        return None

class BotCreateView(generics.CreateAPIView):
    serializer_class = BotDetailSerializer

    def perform_create(self, serializer):
        # получаем пользователя из запроса

        auth_header = self.request.META.get('HTTP_AUTHORIZATION')
        token = auth_header.split()[1] if auth_header else None
        userid = get_user_id_from_token(token)

        user = self.request.user
        print(userid)
        # добавляем пользователя в словарь данных для сохранения объекта
        serializer.validated_data['login_id'] = User.objects.get(id=userid)
        # сохраняем объект
        serializer.save()
    #    permission_classes = [permissions.IsAuthenticated]
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     # Получаем токен из заголовка Authorization
    #     auth_header = request.META.get('HTTP_AUTHORIZATION')
    #     token = auth_header.split()[1] if auth_header else None
    #
    #     # Выводим токен в консоль
    #     print(f"Authorization token: {token}")
    #     userid = get_user_id_from_token(token)
    #     print(f"User login: {userid}")
    #
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class BotsListView(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = BotsListSerializer
#     queryset = Bot.objects.all()
#


class BotsListView(generics.ListAPIView):
 #   permission_classes = [permissions.IsAuthenticated]
    serializer_class = BotsListSerializer


    another_model = CommandsListSerializer()


    class Meta:
        model = Bot
        fields = ("id", 'app_name', 'token', 'url', 'name', 'launch_status', 'login_id', 'another_model')

    def get_queryset(self):

        return Bot.objects.filter(login_id=self.request.user)



class BotDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BotDetailSerializer
    queryset = Bot.objects.all()



class CommandCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommandDetailSerializer


class CommandsListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommandsListSerializer
    queryset = Command.objects.all()



class CommandDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommandDetailSerializer
    queryset = Command.objects.all()



class CommandLinkCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommandLinkDetailSerializer


class CommandLinksListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommandLinksListView
    queryset = Link_command.objects.all()



class CommandLinkDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommandLinkDetailSerializer
    queryset = Link_command.objects.all()

class CommandTypeCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommandTypeDetailSerializer

class CommandTypesListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommandTypesListView
    queryset = Type_сommand.objects.all()


class CommandTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommandLinkDetailSerializer
    queryset = Type_сommand.objects.all()


