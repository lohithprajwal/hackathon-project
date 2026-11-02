from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=50, default='Operational')
    description = models.TextField()
    image = models.ImageField(upload_to='machines/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Manual(models.Model):
    machine = models.ForeignKey(Machine, related_name='manuals', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='manuals/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_indexed = models.BooleanField(default=False)

class ManualChunk(models.Model):
    manual = models.ForeignKey(Manual, related_name='chunks', on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, related_name='chunks', on_delete=models.CASCADE)
    page_number = models.IntegerField()
    content = models.TextField()
    embedding = models.JSONField(blank=True, null=True)

class AuditLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    query = models.TextField()
    citation = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Verified')
