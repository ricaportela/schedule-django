from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    
    def __str__(self):
        return self.name
    
class PhoneNumberContact(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,)
    phonenumber = models.CharField(max_length=20)
    phonetype = models.CharField(max_length=20)  # home, office, cellphone
    
    def __str__(self):
        return self.phonetype 


# class PhoneTypes(models.Model):
#     phonetype = models.ForeignKey(PhoneNumberContacts, on_delete=models.CASCADE)
#     description = models.CharField(max_length=20)
    