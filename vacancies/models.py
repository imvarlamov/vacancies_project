from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=30)
    logo = models.ImageField(
        upload_to='MEDIA_COMPANY_IMAGE_DIR',
        height_field='height_field',
        width_field='width_field',
        default='100x60.gif',
    )
    height_field = models.PositiveIntegerField(default=60)
    width_field = models.PositiveIntegerField(default=100)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', null=True)

    def __str__(self):
        return f'{ self.pk } { self.name } { self.location } { self.description }'


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=120)
    picture = models.ImageField(
        upload_to='MEDIA_SPECIALITY_IMAGE_DIR',
        height_field='height_field',
        width_field='width_field',
        default='100x60.gif',
    )
    height_field = models.PositiveIntegerField(default=60)
    width_field = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f'{ self.code } { self.title }'


class Vacancy(models.Model):
    title = models.CharField(max_length=120)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=300)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_ad = models.DateField(auto_now=True)

    def __str__(self):
        return f'{ self.pk } { self.title }'


class Application(models.Model):
    written_username = models.CharField(max_length=120)
    written_phone = models.CharField(max_length=15)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', null=True)

    def __str__(self):
        return f'{ self.pk } { self.written_username } {self.vacancy}'


class Resume(models.Model):
    class Status(models.TextChoices):
        NOT_IN_SEARCH = 'NIS', _('Не ищу работу')
        CONSIDERATION = 'CON', _('Рассматриваю предложения')
        IN_SEARCH = 'INS', _('Ищу работу')

    class Grade(models.TextChoices):
        INTERN = 'INT', _('Intern')
        JUNIOR = 'JR', _('Junior')
        MIDDLE = 'MID', _('Middle')
        SENIOR = 'SNR', _('Senior')
        LEAD = 'LD', _('Lead')

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    status = models.CharField(max_length=3, choices=Status.choices)
    salary = models.IntegerField()
    grade = models.CharField(max_length=3, choices=Grade.choices)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='resume_spec')
    education = models.CharField(max_length=400)
    experience = models.CharField(max_length=400)
    portfolio = models.CharField(max_length=200)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume_owner', null=True)

    def __str__(self):
        return f'{ self.pk } { self.name } {self.status}'
