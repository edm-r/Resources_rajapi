from rest_framework import serializers
from .models import Resource

class ResourceSerializer(serializers.ModelSerializer):
    file_link = serializers.SerializerMethodField()
    published_date = serializers.DateField(required=False)  # Utilisez DateField ici
    
    class Meta:
        model = Resource
        fields = ['id', 'title', 'description', 'type', 'file', 'file_link', 'published_date', 'status']
    
    def get_file_link(self, obj):
        """Génère l'URL absolue du fichier uploadé"""
        if obj.file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return None