from django.db import models

# Create your models here.

class Newsletter(models.Model):
    january = 'JAN'
    february = 'FEB'
    march = 'MAR'
    april = 'APR'
    may = 'MAY'
    june = 'JUN'
    july = 'JUL'
    august = 'AUG'
    september = 'SEP'
    october = 'OCT'
    november = 'NOV'
    december = 'DEC'

    MONTH_CHOICES = (
        (january, 'January'),
        (february, 'February'),
        (march, 'March'),
        (april, 'April'),
        (may, 'May'),
        (june, 'June'),
        (july, 'July'),
        (august, 'August'),
        (september, 'September'),
        (october, 'October'),
        (november, 'November'),
        (december, 'December'),
    )

    Y2015 = '2015'
    Y2016 = '2016'
    Y2017 = '2017'
    Y2018 = '2018'
    Y2019 = '2019'
    Y2020 = '2020'
    Y2021 = '2021'
    Y2022 = '2022'
    Y2023 = '2023'

    YEAR_CHOICES = (
        (Y2015, '2015'),
        (Y2016, '2016'),
        (Y2017, '2017'),
        (Y2018, '2018'),
        (Y2019, '2019'),
        (Y2020, '2020'),
        (Y2021, '2021'),
        (Y2022, '2022'),
        (Y2023, '2023'),
    )

    month = models.CharField(max_length=20, choices=MONTH_CHOICES, default='')
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, default='')
    pdf_file = models.FileField(upload_to='media', blank=True)
    pdf_img = models.FileField(upload_to='media', blank=True)
    date = models.DateField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.month + ' ' + self.year

class Subscriber(models.Model):
    first_name = models.CharField(max_length=30, default="", blank=False)
    last_name = models.CharField(max_length=50, default="", blank=False)
    email = models.EmailField(max_length=100, default="", blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name