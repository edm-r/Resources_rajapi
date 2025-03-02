from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def default_published_date():
    """Retourne la date actuelle sans l'heure."""
    return timezone.now().date()

class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50)
    file = models.FileField(upload_to='resources/')
    published_date = models.DateField(default=default_published_date)  # Utilisez la fonction ici
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('draft', 'Brouillon'), ('published', 'Publié')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def file_link(self):
        """Retourne l'URL du fichier uploadé"""
        if self.file:
            return self.file.url
        return None