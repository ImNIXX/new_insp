from django.db import models

# Create your models here.


class User(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=100, blank=True)
    dob = models.CharField(max_length=100, blank=True)
    role_id = models.IntegerField()
    status = models.IntegerField()
    register_date = models.DateTimeField(auto_now_add=True)
    user_directory = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "insp_user"

    def __str__(self):
        return self.username


class Inspections(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    facility = models.CharField(max_length=100)
    stakeholders = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    operating_area = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100, blank=True)
    datetime = models.DateField(max_length=50, blank=True)
    draft_directory = models.CharField(max_length=100, blank=True)
    draft_name = models.CharField(max_length=100, blank=True)
    draft_slug = models.CharField(max_length=100, blank=True)
    status = models.IntegerField(null=True)
    approve = models.CharField(max_length=100, blank=True)
    user_id = models.IntegerField()

    class Meta:
        db_table = "insp_inspection"

    def __str__(self):
        return self.title


class Facility(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    facility = models.CharField(max_length=100)

    class Meta:
        db_table = "insp_facility"

    def __str__(self):
        return self.facility


class Type(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    type_slug = models.CharField(max_length=200, blank=True)
    draft_html = models.TextField()

    class Meta:
        db_table = "insp_type"

    def __str__(self):
        return self.type