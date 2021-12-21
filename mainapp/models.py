from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    desc = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='страна')
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    desc = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f'{self.name} | {self.country.name}'


class Accommodation(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='страна')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='регион')
    name = models.CharField(verbose_name='наименование', max_length=128)
    image = models.ImageField(verbose_name='изображение', upload_to='accommodation_img', blank=True)
    short_desc = models.TextField(verbose_name='краткое описание', blank=True)
    full_desc = models.TextField(verbose_name='полное описание', blank=True)
    availability = models.PositiveIntegerField(verbose_name='количество свободных номеров')
    price = models.DecimalField(verbose_name='стоимость', max_digits=8, decimal_places=2)
    room_desc = models.TextField(verbose_name='описание комнаты', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f'{self.name} | {self.country.name}'

    @staticmethod
    def get_items():
        return Accommodation.objects.filter(is_active=True).order_by('country', 'region', 'name')
