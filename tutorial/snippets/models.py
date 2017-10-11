from django.db import models
from django.contrib.gis.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

class Identity(models.Model):
    Adhaar_id=models.IntegerField()
    Name= models.CharField(max_length=100, blank=True, default='Koushik')


class Property_1(models.Model):
    A_id=models.ForeignKey(Identity,on_delete=models.CASCADE)
    house_id=models.AutoField(primary_key=True)

class Property_2(models.Model):
    A_id=models.ForeignKey(Identity,on_delete=models.CASCADE)
    farm_id=models.AutoField(primary_key=True)

class Houses(models.Model):
    H_id=models.ForeignKey(Property_1,on_delete=models.CASCADE)
    lat=models.DecimalField(decimal_places=2,max_digits=5)
    lon=models.DecimalField(decimal_places=2,max_digits=5)
    Area=models.IntegerField()
    Income=models.IntegerField()

class Farms(models.Model):
    F_id=models.ForeignKey(Property_2,on_delete=models.CASCADE)
    Area=models.IntegerField()
    poly = models.PolygonField(default='')
    crops= models.CharField(max_length=100, blank=True, default='Rice')
    


