from django.db import models

# Create your models here.
class Evenement(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField()
    image_url = models.URLField(default='http://url_a_definir')

    def __str__(self):
        return self.nom


class Participant(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Participation(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.participant} participe à {self.evenement}"