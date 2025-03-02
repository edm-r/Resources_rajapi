from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Resource
from .serializers import ResourceSerializer
from .authentication import MicroserviceTokenAuthentication

class ResourceCreateView(APIView):
    authentication_classes = [MicroserviceTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResourceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResourceDetailView(APIView):
    """
    Vue combinée pour la mise à jour et la suppression d'une ressource
    """
    authentication_classes = [MicroserviceTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_resource(self, resource_id, user):
        """
        Récupère une ressource spécifique appartenant à l'utilisateur authentifié
        """
        try:
            return Resource.objects.get(id=resource_id, author=user)
        except Resource.DoesNotExist:
            return None

    def get(self, request, resource_id):
        """
        Récupère les détails d'une ressource spécifique
        """
        resource = self.get_resource(resource_id, request.user)
        if not resource:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ResourceSerializer(resource, context={'request': request})
        return Response(serializer.data)

    def put(self, request, resource_id):
        """
        Met à jour une ressource existante
        """
        resource = self.get_resource(resource_id, request.user)
        if not resource:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ResourceSerializer(resource, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, resource_id):
        """
        Met à jour partiellement une ressource existante
        """
        resource = self.get_resource(resource_id, request.user)
        if not resource:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ResourceSerializer(resource, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, resource_id):
        """
        Supprime une ressource existante
        """
        resource = self.get_resource(resource_id, request.user)
        if not resource:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)