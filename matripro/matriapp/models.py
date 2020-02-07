from django.db import models
import uuid
from django.utils.text import slugify 
from django.contrib.auth.models import User
import string
import random

# Create your models here.
class MotherTonguee(models.Model):
    locallang = models.CharField(max_length=30)
    def __str__(self):
     return "{}".format(self.locallang)
class Castee(models.Model):
    cst = models.CharField(max_length=10)
    def __str__(self):
     return "{}".format(self.cst)
class Subcastee(models.Model):
    subcst = models.CharField(max_length=20)
    def __str__(self):
     return "{}".format(self.subcst)
class Heightt(models.Model):
    hgt = models.CharField(max_length=10)
    def __str__(self):
        return "{}".format(self.hgt)

class Preheightt(models.Model):
    phgt = models.CharField(max_length=10)
    def __str__(self):
        return "{}".format(self.phgt)
     
class Weightt(models.Model):
    wght = models.CharField(max_length=10)
    def __str__(self):
        return "{}".format(self.wght)
     
class Starr(models.Model):
    chukka = models.CharField(max_length=30)
    def __str__(self):
     return "{}".format(self.chukka)
class Raasii(models.Model):
    rasi = models.CharField(max_length=30)
    def __str__(self):
     return "{}".format(self.rasi)
class Countryy(models.Model):
    cuntry = models.CharField(max_length=25)
    def __str__(self):
     return "{}".format(self.cuntry)
class Statee(models.Model):
    stat = models.CharField(max_length=25)
    def __str__(self):
     return "{}".format(self.stat)
class Cityy(models.Model):
    cty = models.CharField(max_length=25)
    def __str__(self):
     return "{}".format(self.cty)
class Agee(models.Model):
    ag = models.CharField(max_length=20)
    def __str__ (self):
        return "{}".format(self.ag)

class Ageto(models.Model):
    agto = models.CharField(max_length=20)
    def __str__ (self):
        return "{}".format(self.agto)       
class Religionn(models.Model):
    relig = models.CharField(max_length=25)
    def __str__(self):
        return "{}".format(self.relig)


class Matrimonydata(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    #Step1
    Name = models.CharField(max_length=25)
    CreateProfile = models.CharField(max_length=20)
    Gender = models.CharField(max_length=15)
    MotherTongue = models.ForeignKey(MotherTonguee,on_delete=models.CASCADE, default=None, blank=True, null=True)
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Caste = models.ForeignKey(Castee,on_delete=models.CASCADE)
    Subcaste = models.ForeignKey(Subcastee,on_delete=models.CASCADE, default=None, blank=True, null=True)
    Dosham = models.CharField(max_length=20)
    MaritalStatus = models.CharField(max_length=25)
    NoofChildren = models.CharField(max_length=20)
    Height = models.ForeignKey(Heightt,on_delete=models.CASCADE, default=None, blank=True, null=True)
    FamilyStatus = models.CharField(max_length=20)
    FamilyType = models.CharField(max_length=20)
    FamilyValues = models.CharField(max_length=25)
    AnyDisability = models.CharField(max_length=25)
    
    HighestEducation = models.CharField(max_length=30)
    EmployedIn = models.CharField(max_length=25)
    Occupation = models.CharField(max_length=25)
     #Step2   
    Bodytype = models.CharField(max_length=25)
    Weight = models.ForeignKey(Weightt,on_delete=models.CASCADE, default=None, blank=True, null=True)
    Educationdetail = models.CharField(max_length=35)
    Occupationdetail = models.CharField(max_length=35)
    Eatinghabit = models.CharField(max_length=35)
    Drinkinghabit = models.CharField(max_length=35)
    Smokinghabit = models.CharField(max_length=35)
    Star = models.ForeignKey(Starr,on_delete=models.CASCADE, default=None, blank=True, null=True)
    Raasi = models.ForeignKey(Raasii,on_delete=models.CASCADE, default=None, blank=True, null=True)
    Birthtime = models.CharField(max_length=50)
    #Place_of_Birth
    Country = models.ForeignKey(Countryy,on_delete=models.CASCADE, default=None, blank=True, null=True)
    State = models.ForeignKey(Statee,on_delete=models.CASCADE, default=None, blank=True, null=True)
    City = models.ForeignKey(Cityy,on_delete=models.CASCADE, default=None, blank=True, null=True)
    Fatherstatus = models.CharField(max_length=30)
    Motherstatus = models.CharField(max_length=30)
    NoofBrothers = models.CharField(max_length=20)
    Brothersmarried = models.CharField(max_length=25)
    NoofSisters = models.CharField(max_length=25)
    Sistersmarried = models.CharField(max_length=30)
    Familylocation = models.CharField(max_length=30)
    Contactno = models.IntegerField(null=True)
    Ancestralorigin = models.CharField(max_length=30)
   #Step3
    Hobbies=models.CharField(max_length=500)
    Hobothers=models.CharField( max_length=50)
    FavouriteMusic=models.CharField(max_length=50)
    favOthers=models.CharField(max_length=50)
    Sportsfi=models.CharField(max_length=50)
    sportOthers=models.CharField(max_length=50)
    spokenLang=models.CharField(max_length=50)
    Language_others=models.CharField(max_length=50)
    
    
   #step4
    Agefrom=models.ForeignKey(Agee,on_delete=models.CASCADE, default=None, blank=True, null=True)
    Ageto=models.ForeignKey(Ageto,on_delete=models.CASCADE, default=None, blank=True, null=True)
    Marital_status=models.CharField(max_length=50)
    Have_childeren=models.CharField(max_length=50)
    prefredheigth=models.ForeignKey(Preheightt,on_delete=models.CASCADE, default=None, blank=True, null=True)
    Physical_status=models.CharField(max_length=50)
    Eating_habits=models.CharField(max_length=50)
    Drinking_habits=models.CharField(max_length=50)
    Smoking_habit=models.CharField(max_length=50)
    Religion=models.ForeignKey(Religionn,on_delete=models.CASCADE, default=None, blank=True, null=True)
    kujaDosham=models.CharField(max_length=50)
    def __str__(self):
        return self.Name
      
    



def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 
  
def unique_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.title) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
      
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 4)) 
              
        return unique_slug_generator(instance, new_slug = new_slug) 
    return slug 
