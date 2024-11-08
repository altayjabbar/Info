from django.db import models

class CarInfo(models.Model):
    FOOD_CHOICES = [
        (1, 'Qida'),
        (2, 'Qeyri-qida')
    ]

    TERMINAL_CHOICES = [
        (1, 'Sederek G/P'),
        (2, 'Ipek G/P')
    ]
    barcode = models.CharField(max_length=255,unique=True, null=False, verbose_name='NV-in barkodu') #barcode can be same ?/
    car_nummber = models.CharField(max_length=255, null=False, verbose_name='Masin nomresi')
    name = models.CharField(max_length=255, null=False ,verbose_name='Adi')
    weight_at_border = models.FloatField(null=False,verbose_name='Serhedeki Cekisi')
    weight_at_silkway = models.FloatField(null=False,verbose_name='Ipek yolundaki cekisi')
    note = models.TextField(null=True,verbose_name='Elave qeyd')
    
    
    # Relations
    country = models.ForeignKey('Country', on_delete=models.CASCADE, null=False,verbose_name='Olke')
    

    is_food = models.IntegerField(
        choices=FOOD_CHOICES,
        default=1,verbose_name='Qida/qeyri-qida')
    terminal = models.IntegerField(
        choices=TERMINAL_CHOICES,
        default=1)
    

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Masinlar'
        



class Country(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'olkeler'