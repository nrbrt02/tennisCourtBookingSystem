from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, validate_image_file_extension
# from .utils import validate_times 
# Create your models here.

COURT_TYPES = (
    ('clay', 'Clay'),
    ('grass', 'Grass'),
    ('hardcourt', 'Hardcourt'),
)
COURT_LOCATION = (
    ('indoors', 'Indoors'),
    ('outside', 'Out-side'),
)
BOOK_TYPE = (
    ('single', '1 Person'),
    ('child', 'Child Under 18'),
    ('double', 'Double (4 persons)'),
    ('couple', 'Couple'),
    ('family', 'Family'),
)

STATUS=(
    ('pendig', 'Pendig'),
    ('done', 'Done'),
    ('paid', 'Paid'),
    ('cancled', 'Cancled'),
)

class Court(models.Model):
    name = models.CharField(max_length=50, unique=True)
    court_type = models.CharField(max_length=20, choices=COURT_TYPES)
    court_location = models.CharField(max_length=20, choices=COURT_LOCATION)
    has_lighting = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    pre_image = models.ImageField(upload_to='img/upload', null=False)
    description = models.TextField(null=True);
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
class Image(models.Model):
    name = models.ImageField(upload_to='img/upload', validators=[validate_image_file_extension])
    court_id = models.ForeignKey(Court, on_delete=models.CASCADE)
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.name.delete()
        super().delete(*args, **kwargs)

class Sessions(models.Model):
    name = models.CharField(max_length=50, unique=True)
    startTime = models.TimeField()
    endTime = models.TimeField()
    price = models.PositiveIntegerField()
    isTainer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    # def clean(self):
    #     if self.startTime >= self.endTime:
    #         raise ValidationError("Start time must be before end time.")
    #     super().clean()

PHONE_REGEX = r'^07\d{8}$' 

class Booking(models.Model):
    date = models.DateField()
    session_id = models.ForeignKey(Sessions, on_delete=models.CASCADE)
    court_id = models.ForeignKey(Court, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=BOOK_TYPE)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, validators=[RegexValidator(PHONE_REGEX, 'Phone number must start with 07 and have 8 digits')])
    status = models.CharField(max_length=10, choices=STATUS, default='pendig')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.name} - {self.date} - {self.court_id} - {self.status}"
    
    def preSave(self, *args, **kwargs):
        existing_booking = Booking.objects.filter(
        date=self.date,
        session_id=self.session_id,
        court_id=self.court_id,
        ).first()
        if existing_booking == None:
            # print("the duoble chaeck is triggerd")
            # self.error_message = 'This court Already Booked at This session, find another one'
            # super(Booking, self).save(*args, **kwargs)
            return True
        else:
            return False