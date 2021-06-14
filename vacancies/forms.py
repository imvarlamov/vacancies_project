from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Application, Company, Resume, Vacancy


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('written_username', 'written_phone', 'written_cover_letter')
        labels = {
            'written_username': 'Ваше имя',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо',
        }
        widgets = {
            'written_username': forms.TextInput(),
            'written_phone': forms.TextInput(),
            'written_cover_letter': forms.Textarea(attrs={'rows': '4'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Записаться на пробный урок'))


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'description', 'employee_count', 'owner')
        labels = {
            'name': 'Название компании',
            'location': 'География',
            'logo': 'Логотип',
            'description': 'Информация о компании',
            'employee_count': 'Количество сотрудников',
            'owner': 'Владелец компании',
        }
        widgets = {
            'name': forms.TextInput(),
            'location': forms.TextInput(),
            'logo': forms.FileInput(attrs={'class': 'custom-file-input', 'multiple data-min-file-count': '0'}),
            'description': forms.Textarea(attrs={'rows': '4'}),
            'employee_count': forms.TextInput(),
            'owner': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group pb-2 col-md-6 mb-0'),
                Column('logo', css_class='form-group pb-2 col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('employee_count', css_class='form-group pb-2 col-md-6 mb-0'),
                Column('location', css_class='form-group pb-2 col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('description', css_class='form-group'),
            ),
        )
        self.helper.add_input(Submit('submit', 'Сохранить'))


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'company', 'skills', 'description', 'salary_min', 'salary_max')
        labels = {
            'title': 'Название вакансии',
            'specialty': 'Специальность',
            'company': 'Компания',
            'skills': 'Требуемые навыки',
            'description': 'Описание вакансии',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
        }
        widgets = {
            'title': forms.TextInput(),
            'specialty': forms.Select,
            'company': forms.Select(),
            'skills': forms.Textarea(attrs={'rows': '2'}),
            'description': forms.Textarea(attrs={'rows': '12'}),
            'salary_min': forms.TextInput(),
            'salary_max': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group pb-2 col-md-6 mb-0'),
                Column('specialty', css_class='form-group pb-2 col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('salary_min', css_class='form-group pb-2 col-md-6 mb-0'),
                Column('salary_max', css_class='form-group pb-2 col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('skills', css_class='form-group pb-2'),
            ),
            Row(
                Column('description', css_class='form-group'),
            ),
        )
        self.helper.add_input(Submit('submit', 'Сохранить'))


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'surname', 'status', 'salary', 'specialty', 'grade',
                  'education', 'experience', 'portfolio')
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'status': 'Готовность к работе',
            'salary': 'Ожидаемое вознаграждение',
            'specialty': 'Специализация',
            'grade': 'Квалификация',
            'education': 'Образование',
            'experience': 'Опыт работы',
            'portfolio': 'Ссылка на портфолио',
        }
        widgets = {
            'name': forms.TextInput(),
            'surname': forms.TextInput(),
            'status': forms.Select(attrs={'class': 'custom-select mr-sm-2'}),
            'salary': forms.TextInput(),
            'specialty': forms.Select(attrs={'class': 'custom-select mr-sm-2'}),
            'grade': forms.Select(attrs={'class': 'custom-select mr-sm-2'}),
            'education': forms.Textarea(attrs={'rows': '3'}),
            'experience': forms.Textarea(attrs={'rows': '3'}),
            'portfolio': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group pb-2 col-md-6 mb-0'),
                Column('surname', css_class='form-group pb-2 col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('status', css_class='form-group pb-2 col-md-6 mb-0'),
                Column('salary', css_class='form-group pb-2 col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('specialty', css_class='form-group pb-2 col-md-6 mb-0'),
                Column('grade', css_class='form-group pb-2 col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('education', css_class='form-group pb-2'),
            ),
            Row(
                Column('experience', css_class='form-group pb-2'),
            ),
            Row(
                Column('portfolio', css_class='form-group pb-2'),
            ),
        )
        self.helper.add_input(Submit('submit', 'Сохранить'))
