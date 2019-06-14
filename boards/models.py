from django.db import models
import datetime


# Create your models here.
class Boards(models.Model):   #for trello boards 
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class Lists(models.Model):  # for trello lists 
    boardid = models.ForeignKey(Boards,on_delete=models.CASCADE,related_name="boardlists")
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)

    def __str__ (self):
        return self.title      

class Cards(models.Model) : # for trello cards 
    listid = models.ForeignKey(Lists, on_delete=models.CASCADE,related_name="listcards")
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    content= models.CharField(max_length=256,blank=True) 
    duedate = models.DateField(("Date"), default=datetime.date.today,blank=True)
    
    def __str__ (self):
        return self.title    