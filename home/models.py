from django.db import models

class Post(models.Model):
    
    comentarios = models.TextField( null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentarios
