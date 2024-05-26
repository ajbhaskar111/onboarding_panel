from django.db import models
# Create your models here.




class CountryModel(models.Model):
    Name = models.CharField(max_length=120)

    class Meta:
        db_table = 'country'

    def __str__(self) -> str:
        return self.Name    


class UserModel(models.Model):
    country_name = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    User_name = models.CharField(max_length= 120)
    Email = models.EmailField(unique = True)
    Password = models.CharField(max_length= 55)

    class Meta:
        db_table = 'user'

    def __str__(self) -> str:
        return self.User_name

choise_boolean = (
    ('yes','Yes'),
    ('no','No')
)
class DocumentSetModel(models.Model):
    Name_of_document = models.CharField(max_length= 500)
    Country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    Has_backside = models.CharField(choices= choise_boolean, max_length= 5)
    OcrLables = models.JSONField(default=dict, null= True, blank= True)

    class Meta:
        db_table = 'documentset'

    def __str__(self) -> str:
        return self.Name_of_document 

surname_choice = (
    ('mr','Mr'),
    ('miss','Miss'),
    ('mrs','Mrs')
)
gender_choice = (
    ('male','Male'),
    ('female','Female'),
    ('other','Other')
)
class CustomerMode(models.Model):
    Surname = models.TextField(choices=surname_choice)
    Firstname = models.CharField(max_length= 200)
    Nationality = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    Gender = models.TextField(choices=gender_choice) 
    Card_number = models.CharField(max_length= 120) 
    CreateBy = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'customer'

    def __str__(self) -> str:
        return self.Firstname


class CustomerDocumentModel(models.Model):
    Customer = models.ForeignKey(CustomerMode,on_delete=models.CASCADE)
    atteched_file = models.FileField(upload_to='upload/data/')
    Extracted_json = models.JSONField(default=dict)
    Created_at = models.TimeField()

    class Meta:
        db_table = 'customerdocument'

    def __str__(self) -> str:
        return self.atteched_file
