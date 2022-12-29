from django.db import models

# Create your models here.

class Tutorial(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  
  #! CursorPagination için;
  # created = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title
    