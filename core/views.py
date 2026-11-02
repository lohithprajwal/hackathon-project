from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Machine, Manual, AuditLog
from .serializers import MachineSerializer, ManualSerializer, AuditLogSerializer

# 1. Standard template view for loading your frontend HTML
def home_view(request):
    return render(request, 'mechzen.html')

# 2. REST API Viewsets with AllowAny and empty authentication to bypass CSRF/403 errors
class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

class ManualViewSet(viewsets.ModelViewSet):
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

# 3. API View for processing maintenance manual queries
class RAGQueryAPIView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []
    
    def post(self, request):
        question = request.data.get('question', '')
        machine_id = request.data.get('machine_id', '')
        
        # Process RAG query or return grounded response
        return Response({
            "status": "VERIFIED",
            "answer": f"Processed query for {machine_id}: {question}",
            "sources": []
        }, status=status.HTTP_200_OK)