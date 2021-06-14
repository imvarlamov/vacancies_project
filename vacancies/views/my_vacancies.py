from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View


from vacancies.models import Application, Vacancy
from vacancies.forms import VacancyForm


# Мои вакансии (список) /mycompany/vacancies/ ########################################################################
class MyVacanciesView(LoginRequiredMixin, View):
    def get(self, request):
        vacancies = Vacancy.objects.filter(
            company__owner_id=request.user.id)\
            .annotate(application_count=Count('applications'))
        if vacancies:
            return render(request, 'vacancies/vacancy_list.html', context={
                'vacancies': vacancies,
            })
        return render(request, 'vacancies/vacancy_list.html', context={})


# Мои вакансии (новая пустая форма) /mycompany/vacancies/create/ #####################################################
class MyVacanciesCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = VacancyForm()
        return render(request, 'vacancies/vacancy_edit.html', context={
            'form': form,
        })

    def post(self, request):
        form = VacancyForm(request.Post)
        if form.isvalid():
            vacancy = form.save(commit=False)
            vacancy.company.owner = get_object_or_404(User, id=request.user.id)
            vacancy.save()
            messages.add_message(request, messages.SUCCESS, 'Готово!')
            return redirect('my_vacancies')
        messages.add_message(request, messages.ERROR, 'Что-то пошло не так.')
        return render(request, 'vacancies/vacancy_edit.html', context={
            'form': form,
        })


# Одна моя вакансия (заполненная форма) /mycompany/vacancies/<vacancy_id> ############################################
class MyVacancyView(LoginRequiredMixin, View):
    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.filter(id=vacancy_id, company__owner_id=request.user.id)\
            .annotate(application_count=Count('applications')).first()
        if vacancy:
            applications = Application.objects.filter(vacancy_id=vacancy_id)
            form = VacancyForm(instance=vacancy)
            return render(request, 'vacancies/vacancy_edit.html', context={
                'applications': applications,
                'vacancy': vacancy,
                'form': form,
            })
        return redirect('my_vacancies')

    def post(self, request, vacancy_id):
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company.owner = get_object_or_404(User, id=request.user.id)
            vacancy.save()
            messages.add_message(request, messages.SUCCESS, 'Готово!')
            return redirect('my_vacancy')
        messages.add_message(request, messages.ERROR, 'Что-то пошло не так.')
        return render(request, 'vacancies/vacancy_edit.html', context={
            'form': form,
        })
