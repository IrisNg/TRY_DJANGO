from django.db import models

# Movie class inherit from models.Model base class
class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()

    # Override this method to create verbose name for an object of Movie
    def __str__(self):
        return f'{self.title} from {self.year}' 