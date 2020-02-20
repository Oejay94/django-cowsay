from django.db import models
from simple_history.models import HistoricalRecords
from django.utils import timezone


class Cowsay(models.Model):
    default = 'cow'
    skeleton = 'skeleton'
    stegosaurus = 'stegosaurus'
    tux = 'tux'
    ghostbusters = 'ghostbusters'
    bong = 'bong'
    flaming_sheep = 'flaming-sheep'
    dragon_and_cow = 'dragon-and-cow'

    COW_CHOICES = [
        (default, 'Cow'),
        (skeleton, 'Skeleton'),
        (stegosaurus, 'Stegosaurus'),
        (tux, 'Tux'),
        (ghostbusters, 'Ghostbusters'),
        (bong, 'Bong'),
        (flaming_sheep, 'Flaming-Sheep'),
        (dragon_and_cow, 'Dragon-and-Cow')
    ]

    text = models.CharField(max_length=50)
    time = models.TimeField(default=timezone.now)
    change_cow = models.CharField(max_length=15, choices=COW_CHOICES, default=default, null=True)
