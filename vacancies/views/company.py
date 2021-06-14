from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from vacancies.models import Company


# Страница компании
class CompanyView(View):
    def get(self, request, company_id):
        company = get_object_or_404(Company, id=company_id)
        return render(request, 'company/company.html', context={
            'company': company,
        })
