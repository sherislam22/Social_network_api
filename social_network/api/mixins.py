from rest_framework.decorators import action
from rest_framework.response import Response
from . import services
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated


class LikedMixin:
    @action(methods=['POST'],detail=True)
    def like(self, request, pk=None):
        """Лайкает `obj`.
        """
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()
    @action(methods=['POST'],detail=True)
    def unlike(self, request, pk=None):
        """Удаляет лайк с `obj`.
        """
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()
    @action(methods=['GET'], detail=True)
    def fans(self, request, pk=None):
        """Получает всех пользователей, которые лайкнули `obj`.
        """
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = UserSerializer(fans, many=True)
        return Response(serializer.data)