from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=255)
    
    def __str__(self):
        return self.filename
    
    def get_file_content(self):
        """Read and return the content of the uploaded file"""
        try:
            with self.file.open('r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"
