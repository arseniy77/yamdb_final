from rest_framework import mixins, status, viewsets
from rest_framework.response import Response


class DestroyModelMixin:

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            DestroyModelMixin, viewsets.GenericViewSet):
    pass
