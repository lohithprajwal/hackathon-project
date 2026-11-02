from django.contrib import admin
from .models import Machine, Manual, AuditLog

# Register models directly without field mismatches
admin.site.register(Machine)
admin.site.register(Manual)
admin.site.register(AuditLog)