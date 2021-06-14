from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from accounts.views import RegisterView, MyLoginView

from vacancies.views.public import MainView, SearchView
from vacancies.views.company import CompanyView
from vacancies.views.vacancies import SendView, VacanciesView, VacanciesSpecialtyView, VacancyView
from vacancies.views.my_company import MyCompanyLetsStartView, MyCompanyView, MyCompanyCreateView
from vacancies.views.my_vacancies import MyVacanciesView, MyVacancyView, MyVacanciesCreateView
from vacancies.views.my_resume import MyResumeLetsStartView, MyResumeView, MyResumeCreateView
from vacancies.views.custom_handlers import custom_handler404, custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    # public
    path('', MainView.as_view(), name='main'),
    path('search', SearchView.as_view(), name='search'),
    # vacancies
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:specialty_code>/', VacanciesSpecialtyView.as_view(), name='vacancies_specialty'),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view(), name='vacancy'),
    path('vacancies/companies/<int:company_id>/', CompanyView.as_view(), name='company'),
    # my_company
    path('mycompany/letsstart/', MyCompanyLetsStartView.as_view(), name='lets_start'),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),
    path('mycompany/create/', MyCompanyCreateView.as_view(), name='my_company_create'),
    # my_vacancies
    path('vacancies/<int:vacancy_id>/send/', SendView.as_view(), name='send'),
    path('mycompany/vacancies/', MyVacanciesView.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/<int:vacancy_id>/', MyVacancyView.as_view(), name='my_vacancy'),
    path('mycompany/vacancies/create/', MyVacanciesCreateView.as_view(), name='my_vacancies_create'),
    # my_resume
    path('myresume/letsstart', MyResumeLetsStartView.as_view(), name='resume_lets_start'),
    path('myresume/create', MyResumeCreateView.as_view(), name='my_resume_create'),
    path('myresume/', MyResumeView.as_view(), name='my_resume'),
    # authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

handler404 = custom_handler404
handler500 = custom_handler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
