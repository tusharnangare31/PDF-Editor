from django.db import models
from django.contrib.auth.models import User
import os

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    storage_limit = models.IntegerField(default=100 * 1024 * 1024)  # Default 100MB
    created_at = models.DateTimeField(auto_now_add=True)
    is_email_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class ProcessedDocument(models.Model):
    DOCUMENT_TYPES = [
        ('original', 'Original'),
        ('merged', 'Merged PDF'),
        ('split', 'Split PDF'),
        ('compressed', 'Compressed PDF'),
        ('converted', 'Converted Document'),
        ('edited', 'Edited PDF'),
        ('secured', 'Secured PDF'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='user_documents/%Y/%m/%d/')
    file_size = models.IntegerField(default=0)  # Size in bytes
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def filename(self):
        return os.path.basename(self.file.name)
    
    def delete(self, *args, **kwargs):
        # Delete the file when the model instance is deleted
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)

class DocumentHistory(models.Model):
    OPERATIONS = [
        ('merge', 'Merge PDFs'),
        ('split', 'Split PDF'),
        ('compress', 'Compress PDF'),
        ('convert_to', 'Convert To PDF'),
        ('convert_from', 'Convert From PDF'),
        ('rotate', 'Rotate PDF'),
        ('add_page_numbers', 'Add Page Numbers'),
        ('add_watermark', 'Add Watermark'),
        ('remove_pages', 'Remove Pages'),
        ('protect', 'Protect PDF'),
        ('unlock', 'Unlock PDF'),
        ('sign', 'Sign PDF'),
        ('ocr', 'OCR PDF'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history')
    operation = models.CharField(max_length=20, choices=OPERATIONS)
    input_document = models.ForeignKey(ProcessedDocument, on_delete=models.SET_NULL, 
                                       null=True, blank=True, related_name='operations_as_input')
    output_document = models.ForeignKey(ProcessedDocument, on_delete=models.SET_NULL, 
                                        null=True, blank=True, related_name='operations_as_output')
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)  # Store operation details as JSON
    
    def __str__(self):
        return f"{self.user.username} - {self.operation} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Document Histories"
