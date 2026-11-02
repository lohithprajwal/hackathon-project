from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    home_view, 
    MachineViewSet, 
    ManualViewSet, 
    AuditLogViewSet, 
    RAGQueryAPIView
)

# Set up REST Framework router for ViewSets
router = DefaultRouter()
router.register(r'machines', MachineViewSet)
router.register(r'manuals', ManualViewSet)
router.register(r'auditlogs', AuditLogViewSet)

urlpatterns = [
    # Frontend home page route
    path('', home_view, name='home'),
    
    # API endpoints (e.g., /api/machines/, /api/manuals/)
    path('api/', include(router.urls)),
    
    # Custom RAG query endpoint
    path('api/rag-query/', RAGQueryAPIView.as_view(), name='rag-query'),
]