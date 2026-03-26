from django.db import models

class Report(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PROCESSING", "Processing"),
        ("COMPLETED", "Completed"),
    ]
    name = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS_CHOICES, default="PENDING")
    pdf_genrated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
