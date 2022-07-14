from django.db import models

class Category(models.Model):
    name = models.TextField()
    ordering = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    
class Offer(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.TextField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



    


