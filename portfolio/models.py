from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects_list/')
    url = models.URLField()

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # Menandai pesan sudah dibaca atau belum

    def __str__(self):
        return f"{self.name} - {self.email}"
