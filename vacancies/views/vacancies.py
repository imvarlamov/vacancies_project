from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.generic import View

from vacancies.models import Specialty, Vacancy, Application
from vacancies.forms import ApplicationForm


# Все вакансии
class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        title = 'Все вакансии'
        return render(request, 'vacancies/vacancies.html', context={
            'vacancies': vacancies,
            'title': title,
        })


# Вакансии по специальности
class VacanciesSpecialtyView(View):
    def get(self, request, specialty_code):
        try:
            vacancies = Vacancy.objects.filter(specialty__code=specialty_code)
        except Vacancy.DoesNotExist:
            raise Http404
        title = Specialty.objects.values('title').get(code=specialty_code)
        return render(request, 'vacancies/vacancies.html', context={
            'vacancies': vacancies,
            'title': title['title'],
        })


# Вакансия
class VacancyView(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        return render(request, 'vacancies/vacancy.html', context={
            'vacancy': vacancy,
            'form': ApplicationForm,
        })

    def post(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        form = ApplicationForm(request.POST)
        if form.is_valid():
            written_username = form.cleaned_data.get('written_username')
            written_phone = form.cleaned_data.get('written_phone')
            written_cover_letter = form.cleaned_data.get('written_cover_letter')
            if request.user.id:
                Application.objects.create(
                    written_username=written_username,
                    written_phone=written_phone,
                    written_cover_letter=written_cover_letter,
                    user=User.objects.get(id=request.user.id),
                    vacancy=Vacancy.objects.get(id=vacancy_id),
                )
            else:
                return redirect('login')
            return redirect('send', vacancy_id)
        return render(request, 'vacancies/vacancy.html', context={
            'vacancy': vacancy,
            'form': form,
        })


# Отправка заявки /vacancies/<vacancy_id>/send/
class SendView(View):
    def get(self, request, vacancy_id):
        return render(request, 'vacancies/send.html', context={
            'vacancy_id': vacancy_id,
        })
