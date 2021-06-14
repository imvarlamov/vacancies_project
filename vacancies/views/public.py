from django.views.generic import View, ListView
from django.shortcuts import render
from django.db.models import Count, Q
from vacancies.models import Company, Specialty, Vacancy


# Главная
class MainView(View):
    def get(self, request):
        companies = Company.objects.annotate(count_vacancies=Count('vacancies'))
        specialties = Specialty.objects.annotate(count_vacancies=Count('vacancies'))
        return render(request, 'public/index.html', context={
            'companies': companies,
            'specialties': specialties,
        })


# Поиск
class SearchView(ListView):
    model = Vacancy
    template_name = "public/search.html"

    def get_queryset(self):
        request = self.request.GET.get('s')
        return Vacancy.objects.filter(
            Q(title__icontains=request) | Q(description__icontains=request) | Q(skills__icontains=request),
        )
