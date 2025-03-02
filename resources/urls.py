from django.urls import path
from .views import ResourceCreateView, ResourceDetailView

urlpatterns = [
    path('resources/', ResourceCreateView.as_view(), name='resource-create'),
    path('resources/<int:resource_id>/', ResourceDetailView.as_view(), name='resource-detail'),
]