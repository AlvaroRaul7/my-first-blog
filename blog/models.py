from django.db import models
from django.utils import timezone

class Post(models.Model): #Objeto Post(models.Model) asi Django sabe que es un modelo
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #Vinculo con otro modelo
    title = models.CharField(max_length=200) #Caracteres con un max de 200
    text = models.TextField() #Texto largo sin limite
    created_date = models.DateTimeField(default=timezone.now) #Fecha y Hora
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #Metodo para publicar
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title