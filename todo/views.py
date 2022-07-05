from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, status, views, generics
from rest_framework.permissions import AllowAny
from .models import Todos
from .serializers import CreateUserSerializer, TodosSerializer


class Signup(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateUserSerializer


class Logout(views.APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class Signin(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'username': user.username
        })


class TodosPagination(PageNumberPagination):
    page_size = 5


class TodosViewSet(viewsets.ModelViewSet):
    serializer_class = TodosSerializer
    pagination_class = TodosPagination

    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)
