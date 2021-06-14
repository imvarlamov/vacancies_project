from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View


from vacancies.models import Company
from vacancies.forms import CompanyForm


# Моя компания (предложение создать) /mycompany/letsstart/
class MyCompanyLetsStartView(LoginRequiredMixin, View):
    def get(self, request):
        if Company.objects.filter(owner_id=request.user.id).first():
            return redirect('my_company')
        return render(request, 'company/lets_start.html')


# Моя компания (заполненная форма) /mycompany/ НЕ ОТОБРАЖАЕТСЯ ЛОГОТИП
class MyCompanyView(LoginRequiredMixin, View):
    def get(self, request):
        company = Company.objects.filter(owner_id=request.user.id).first()
        if company:
            form = CompanyForm(instance=company)
            return render(request, 'company/company_edit.html', context={
                'form': form,
            })
        return redirect('lets_start')


# Моя компания (пустая форма) /mycompany/create/
class MyCompanyCreateView(LoginRequiredMixin, View):
    def get(self, request):
        if Company.objects.filter(owner_id=request.user.id).first():
            return redirect('my_company')
        form = CompanyForm()
        return render(request, 'company/company_edit.html', context={
            'form': form,
        })

    def post(self, request):
        if Company.objects.filter(owner_id=request.user.id).first():
            return redirect('my_company')
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = get_object_or_404(User, id=request.user.id)
            company.save()
            messages.add_message(request, messages.SUCCESS, 'Компания успешно добавлена на сайт!')
            return redirect('my_company')
        messages.add_message(request, messages.ERROR, 'Что-то пошло не так.')
        return render(request, 'company/company_edit.html', context={
            'form': form,
        })


# Моя компания (форма редактирования)
class MyCompanyEditView(LoginRequiredMixin, View):
    def get(self, request):
        company = Company.objects.filter(owner_id=request.user.id).first()
        if company:
            form = CompanyForm(instance=company)
            return render(request, 'company/company_edit.html', context={
                'form': form,
            })
        return redirect('lets_start')

    def post(self, request):
        company = Company.objects.filter(owner_id=request.user.id).first()
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = get_object_or_404(User, id=request.user.id)
            company.save()
            messages.add_message(request, messages.SUCCESS, 'Вакансия успешно обновлена!')
            return redirect('my_company')
        messages.add_message(request, messages.SUCCESS, 'Что-то пошло не так.')
        return render(request, 'company/company_edit.html', context={
            'form': form,
        })
