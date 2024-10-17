import logging
from cakes.models import Cake
from rest_framework import mixins
from rest_framework import generics
from api.serializer import CakeSerializer
from rest_framework.response import Response

logger = logging.getLogger(__name__)


def validate_data(data, action='create'):
    name = data.get('name')
    comment = data.get('comment')
    yumFactor = data.get('yumFactor')

    if name is None or (name and len(name) > 100):
        return True, "Name of cake should not exceeds 100 characters"

    if action == 'create' and Cake.objects.filter(name=name).exists():
        return True, "Cake with this name already exists. Please enter a unique name"

    if comment is None or (comment and (len(comment) < 5 or len(comment) > 200)):
        return True, "Comment length should be between 5-200 characters"

    if yumFactor is not None:
        if type(yumFactor) is str:
            yumFactor = int(yumFactor)

        if yumFactor < 1 or yumFactor > 5:
            return True, "yumFactor should be between 1-5"

    return False, ""


class CakeList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer

    def get(self, request, *args, **kwargs):
        try:
            return self.list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return Response(data="Unexpected Error", status=500)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data

            error, errorMessage = validate_data(data)
            if error:
                return Response({'error': errorMessage}, status=400)

            return self.create(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return Response(data="Unexpected Error", status=500)


class CakeDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return Response(data="Unexpected Error", status=500)

    def put(self, request, *args, **kwargs):
        try:
            data = request.data

            error, errorMessage = validate_data(data, 'update')
            if error:
                return Response({'error': errorMessage}, status=400)

            return self.update(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return Response(data="Unexpected Error", status=500)

    def delete(self, request, *args, **kwargs):
        try:
            return self.destroy(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return Response(data="Unexpected Error", status=500)
