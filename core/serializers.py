from rest_framework import serializers
from .models import Machine, Manual, AuditLog, InspectionResult, SupervisorReview

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'

class InspectionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionResult
        fields = '__all__'

class SupervisorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorReview
        fields = '__all__'