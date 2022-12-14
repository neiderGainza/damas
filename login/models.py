from django.db import models

# Create your models here.

class User(models.Model):
    name     = models.CharField(primary_key = True, max_length = 20)
    email    = models.EmailField()
    password = models.CharField(max_length = 20) 
    
    followers = models.ManyToManyField("self", blank = True, default = [], symmetrical=False) 

    date = models.DateField(auto_now=False, auto_now_add=True) # fecha de incripcion
    description = models.CharField(max_length = 1000, blank = True, default = "Me gusta jugar damas!!!")

    partidas_jugadas = models.IntegerField(blank = True, default = 0) 
    elo     = models.IntegerField(blank = True, default = 1500) 
    
    online  = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.name
        