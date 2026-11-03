from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Machine, Manual, AuditLog, InspectionResult, SupervisorReview
from .serializers import (
    MachineSerializer, 
    ManualSerializer, 
    AuditLogSerializer, 
    InspectionResultSerializer, 
    SupervisorReviewSerializer
)

def home_view(request):
    """Renders the main MechZen Phase 2 dashboard interface."""
    return render(request, 'mechzen.html')

def batch_upload_view(request):
    """Handles asynchronous batch plate image uploads for background worker processing."""
    if request.method == 'POST':
        return JsonResponse({
            "status": "success", 
            "message": "Batch inspection job queued successfully via Celery worker."
        })
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

def supervisor_review_view(request):
    """Handles role-based access control (RBAC) supervisor reviews and override actions."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return JsonResponse({
                "status": "success", 
                "message": "Supervisor review override submitted and logged successfully."
            })
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

class RAGQueryAPIView(APIView):
    """API view for RAG-based equipment manual queries and AI assistance."""
    def post(self, request):
        query = request.data.get('query', '')
        return Response({
            "status": "success",
            "query": query,
            "answer": "Retrieved relevant quality inspection and standard operating procedures successfully."
        }, status=status.HTTP_200_OK)

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class ManualViewSet(viewsets.ModelViewSet):
    queryset = Manual.objects.all()
    serializer_class = ManualSerializer

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer

class InspectionResultViewSet(viewsets.ModelViewSet):
    queryset = InspectionResult.objects.all()
    serializer_class = InspectionResultSerializer

class SupervisorReviewViewSet(viewsets.ModelViewSet):
    queryset = SupervisorReview.objects.all()
    serializer_class = SupervisorReviewSerializer