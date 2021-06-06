from django.db import models


class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)

    timestamp = models.DateField(auto_now_add=True, auto_now=False)


class Vehicle_Details(models.Model):

    #General details
    is_actice = models.BooleanField(default=False)
    wheeler = models.IntegerField()
    transporter = models.CharField(max_length=100)
    rc_no=models.CharField(max_length=70)
    chasis_no = models.CharField(max_length=70)
    vehicle_no=models.CharField(max_length=50)
    rfid_tag = models.IntegerField()
    vehicle_temp_no= models.CharField(max_length=50,null=True,blank=True)
    permit_type=models.CharField(max_length=50,null=True,blank=True)
    
    #Statutory details
    road_tax = models.CharField(max_length=50)
    fitness = models.CharField(max_length=50)
    insurance = models.CharField(max_length=50)
    pollution = models.CharField(max_length=50)
    permit = models.CharField(max_length=50)
    road_taxt_expriry=models.DateField(auto_now=False, auto_now_add=False)
    fitnes_expiry = models.DateField(auto_now=False, auto_now_add=False)
    insurance_expiry = models.DateField(auto_now=False, auto_now_add=False)
    pollution_expiry = models.DateField(auto_now=False, auto_now_add=False)
    permit_expiry = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)

    #Other details
    status = models.CharField(max_length=50,null=True,blank=True)
    vehicle_owner = models.CharField(max_length=50)
    owner_address = models.CharField(max_length=50)
    status_change_date = models.DateField(auto_now=False, auto_now_add=False)
    owner_contact = models.IntegerField()
    own_vehivle = models.BooleanField(default=False)