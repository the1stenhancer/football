from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=20)
    cc = models.CharField(primary_key=True, max_length=10, help_text='uniquely identifies countries')
    # league_set used to get all league instances associated with a particular country

    class Meta:
        ordering = ('name',)
        db_table = 'countries'

    def __str__(self):
        return f'%(name)s' % {'name': self.name}


class League(models.Model):
    id = models.AutoField(primary_key=True, help_text='uniquely identifies leagues within a country')
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        ordering = ('country',)
        db_table = 'leagues'

    def __str__(self):
        return f'%(league)s' % {'league': self.name}


class Prediction(models.Model):
    id = models.AutoField(primary_key=True)
    fh = models.SmallIntegerField()
    sh = models.SmallIntegerField()
    ft = models.SmallIntegerField()
    o1 = models.SmallIntegerField()
    o2 = models.SmallIntegerField()
    ot = models.SmallIntegerField()

    class Meta:
        ordering = ('id',)
        db_table = 'predictions'

    def __str__(self):
        return f'Prediction: (%s %s %s %s %s %s)' % (self.fh, self.sh, self.ft, self.o1, self.o2, self.ot)


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    fh = models.SmallIntegerField(default=-1)
    sh = models.SmallIntegerField(default=-1)
    ft = models.SmallIntegerField(default=-1)
    o1 = models.SmallIntegerField(default=-1)
    o2 = models.SmallIntegerField(default=-1)
    ot = models.SmallIntegerField(default=-1)

    class Meta:
        ordering = ('id',)
        db_table = 'results'

    def __str__(self):
        return f'Result: (%s %s %s %s %s %s)' % (self.fh, self.sh, self.ft, self.o1, self.o2, self.ot)


class Match(models.Model):
    objects = models.Manager()
    id = models.BigAutoField(primary_key=True)
    hot_pick = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    fixture = models.IntegerField()
    postponed = models.BooleanField(default=False)
    home = models.CharField(max_length=60)
    away = models.CharField(max_length=60)
    date = models.DateField()
    time = models.TimeField()
    predictions = models.ForeignKey(Prediction, on_delete=models.CASCADE)
    results = models.ForeignKey(Result, on_delete=models.CASCADE, blank=True)
