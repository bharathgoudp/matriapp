
from django import forms
from matriapp.models import Matrimonydata
from django.forms.widgets import Media,MediaDefiningClass,Widget,TextInput,NumberInput,EmailInput,URLInput,PasswordInput,HiddenInput,MultipleHiddenInput,FileInput,ClearableFileInput,Textarea,DateInput,DateTimeInput,TimeInput,CheckboxInput,Select,NullBooleanSelect,SelectMultiple,RadioSelect,CheckboxSelectMultiple,MultiWidget,SplitDateTimeWidget,SplitHiddenDateTimeWidget,SelectDateWidget
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column, Button,Field, Fieldset

dosham=(
    ('yes',"YES"),
    ('no','NO'),
    ("don't","Don't know")
)
maritalstatus=(
    ('Never Married ','Never Married '),
    ('Widowed ','Widowed '),
    ('Divorced','Divorced'),
    ('Awaiting divorce','Awaiting divorce')
)
Noofchildren=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4')
)
familystatus=(
    ('Middle class','Middle class'),
    ('Upper middle class ','Upper middle class '),
    ('Rich','Rich'),
    ('Affluent','Affluent')
)
familytype=(
    ('Joint','joint'),
    ('Nuclear','Nuclear')
)
familyvalues=(
    ('Orthodox','Orthodox'),
    ('Traditional','Traditional'),
    ('Moderate','Moderate'),
    ('Liberal','Liberal')
)
anydisability=(
    ('Normal','Normal'),
    ('Physically challenged','Physically challenged')
)
employedin=(
    ('Government','Government'),
    ('Private','Private'),
    ('Business','Business'),
    ('Defence','Defence'),
    ('Self Employed','Self Employed'),
    ('Not working','Not working')
)
# step2 radiobuttons
Bodytype=(
    ('Slim','Slim'),
    ('Average','Average'),
    ('Athletic','Athletic'),
    ('Heavy','Heavy')
)

Eatinghabbit=(
    ('Vegetarian','Vegetarian'),
    ('Non-Vegetarian','Non-Vegetarian'),
    ('Eggetarian','Eggetarian')
)

Drinkinghabit=(
    ('No','No'),
    ('Drinks Socially','Drinks Socially'),
    ('Yes','Yes')
)

smokinghabit=(
    ('No','No'),
    ('Occasionally','Occasionally'),
    ('Yes','Yes')
)
FamilyLocation=(
    ('Same as my Location','Same as my Location'),
    ('Different Location','Different Location')
)
#step4 checkbox inputs
have_children = (
    ('yes & living together', 'Yes & living together'),
    ('yes & not living together', 'Yes & not living together'),
    ('no', 'No')
)



hobbies=(
    ('Cooking','Cooking'),
    (' Nature',' Nature'),
    (' Dancing',' Dancing'),
    ('Photography','Photography'),
    ('Dancing','Dancing'),
    ('Painting','Painting'),
    ('pets',' Pets'),
    ('Playing Musical Instruments','Playing Musical Instruments'),
    (' Puzzles',' Puzzles'),
    ('Gardening /Landscaping','Gardening /Landscaping'),
    ('Art / Handicraft','Art / Handicraft'),
    ('Listening to Music','Listening to Music'),
    (' Movies',' Movies'),
    ('Internet Surfing','Internet Surfing'),
    ('Traveling','Traveling')
)


favouriteMusic=(
    ('Film songs','Film songs'),
    ('Indian /Classical Music','Indian /Classical Music'),
    (' Western Music',' Western Music')
)
sportesFItness=(
    ('Cricket','Cricket'),
    ('Carrom','Carrom'),
    ('Chess','Chess'),
    (' Jogging',' Jogging'),
    ('Badminton','Badminton'),
    ('Swimming','Swimming'),
    ('Tennis','Tennis'),
    ('Football','Football')
    
)

spokenlangauge=(
    ('English','English'),
    ('Hindi','Hindi'),
    ('Tamil','Tamil'),
    ('Telugu','Telugu'),
    ('Malayalam','Malayalam'),
    ('Kannada','Kannada'),
    ('Gujarati','Gujarati'),
    ('Marathi','Marathi'),
    ('Urdu','Urdu')
)





class Step1_Form(forms.ModelForm):
    Dosham=forms.ChoiceField(choices=dosham, widget=forms.RadioSelect(attrs={'class': 'special'}))
    MaritalStatus=forms.ChoiceField(choices=maritalstatus,widget=forms.RadioSelect(attrs={'class':'special'}))
    NoofChildren=forms.ChoiceField(choices=Noofchildren, widget=forms.RadioSelect(attrs={'class':'special'}))
    FamilyStatus=forms.ChoiceField(choices=familystatus, widget=forms.RadioSelect(attrs={'class':'special'}))
    FamilyType=forms.ChoiceField(choices=familytype, widget=forms.RadioSelect(attrs={'class':'special'}))
    FamilyValues=forms.ChoiceField(choices=familyvalues, widget=forms.RadioSelect(attrs={'class':'special'}))
    AnyDisability=forms.ChoiceField(choices=anydisability, widget=forms.RadioSelect(attrs={'class':'special'}))
    EmployedIn=forms.ChoiceField(choices=employedin, widget=forms.RadioSelect(attrs={'class':'special'}))
    class Meta:
        model=Matrimonydata
        fields = ('Name','CreateProfile','Gender','MotherTongue','Mobile','Email','Caste','Subcaste','Dosham','MaritalStatus','NoofChildren',
                       'Height','FamilyStatus','FamilyType','FamilyValues','AnyDisability','HighestEducation','EmployedIn','Occupation')   

class Step2_Form(forms.ModelForm):
    Bodytype=forms.ChoiceField(choices=Bodytype,widget=forms.RadioSelect(attrs={'class':'special'}))
    Eatinghabit=forms.ChoiceField(choices=Eatinghabbit,widget=forms.RadioSelect(attrs={'class':'special'}))
    Drinkinghabit=forms.ChoiceField(choices=Drinkinghabit,widget=forms.RadioSelect(attrs={'class':'special'}))
    Smokinghabit=forms.ChoiceField(choices=smokinghabit,widget=forms.RadioSelect(attrs={'class':'special'}))
    Familylocation=forms.ChoiceField(choices=FamilyLocation,widget=forms.RadioSelect(attrs={'class':'special'}))
    class Meta:
        model=Matrimonydata
        fields=('Bodytype','Weight','Educationdetail','Occupationdetail','Eatinghabit','Drinkinghabit','Smokinghabit','Star','Raasi','Birthtime',
                  'Country','State','City','Fatherstatus','Motherstatus','NoofBrothers','Brothersmarried','NoofSisters','Sistersmarried',
                  'Familylocation','Contactno','Ancestralorigin')

class Step3_Form(forms.ModelForm):
    Hobbies=forms.MultipleChoiceField(choices=hobbies,widget=forms.CheckboxSelectMultiple)
    FavouriteMusic=forms.MultipleChoiceField(choices=favouriteMusic,widget=forms.CheckboxSelectMultiple)
    Sportsfi=forms.MultipleChoiceField(choices=sportesFItness,widget=forms.CheckboxSelectMultiple)
    spokenLang=forms.MultipleChoiceField(choices=spokenlangauge,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Matrimonydata
        fields=('Hobbies','Hobothers','FavouriteMusic','favOthers','Sportsfi','sportOthers','spokenLang','Language_others')

class Step4_Form(forms.ModelForm):
    Marital_status= forms.ChoiceField(choices=maritalstatus,widget=forms.RadioSelect(attrs={'class': 'special'}))
    Have_childeren = forms.ChoiceField(choices=have_children,widget=forms.RadioSelect(attrs={'class': 'special'}))
    Physical_status = forms.ChoiceField(choices=anydisability, widget=forms.RadioSelect(attrs={'class': 'special'}))
    Eating_habits=forms.ChoiceField(choices=Eatinghabbit,widget=forms.RadioSelect(attrs={'class':'special'}))
    Drinking_habits=forms.ChoiceField(choices=Drinkinghabit,widget=forms.RadioSelect(attrs={'class':'special'}))
    Smoking_habit=forms.ChoiceField(choices=smokinghabit,widget=forms.RadioSelect(attrs={'class':'special'}))
    kujaDosham = forms.ChoiceField(choices=dosham, widget=forms.RadioSelect(attrs={'class': 'special'}))

    class Meta:
        model=Matrimonydata
        fields=('Agefrom','Ageto','Marital_status','Have_childeren','prefredheigth','Physical_status','Eating_habits','Drinking_habits',
                  'Smoking_habit','Religion','kujaDosham')                

