from django.db import models  #models data. what it means to be a particular type of thing
from django.utils import timezone

# Create your models here.
class IceCream(models.Model):#what it means to be a django model. Its pretty much a row

    VANILLA = 'VANILLA'
    CHOCOLATE = 'CHOCOLATE'

    BASE_CHOICES = [
        (VANILLA, 'Vanilla'),
        (CHOCOLATE, 'Chocolate'),
    ]

    DAILY = 'DAILY'
    WEEKLY = 'WEEKLY'
    SEASONAL = 'SEASONAL'

    FEATURED = [
    (DAILY, 'daily'), (WEEKLY, 'weekly'), (SEASONAL, 'seasonal')
    ]

    AVAILABLE_CHOICES = [
    #left vaulve is stored in database and the right value is the visual
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (SEASONAL, 'Seasonal'),
    ]

    flavor = models.CharField(max_length=100)
    base = models.CharField(max_length=100, choices=BASE_CHOICES, default=VANILLA)
    available = models.CharField(max_length=100, choices=AVAILABLE_CHOICES, default=WEEKLY)
    featured = models.BooleanField(default=False)
    date_churned = models.DateTimeField('date churned', default=timezone.now)
    votes = models.IntegerField(default=0)

    def __str__(self): #built in mehtod returning a string of flavor
        return self.flavor
#get absoluteurl
    def get_absoulute_url(self):
        return reverse('ice_cream:index')







# flavor: CharField
# base: CharField with choices (chocolate, vanilla)
# available = CharField with choices (daily, weekly, seasonal)
# featured = BoolField
# date_churned = DateField
