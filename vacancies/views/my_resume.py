from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from vacancies.models import Resume
from vacancies.forms import ResumeForm


# myresume/letsstart #################################################################################################
class MyResumeLetsStartView(LoginRequiredMixin, View):
    def get(self, request):
        if Resume.objects.filter(owner_id=request.user.id):
            return redirect('my_resume')
        return render(request, 'resume/resume_create.html')


# myresume/create #####################################################################################################
class MyResumeCreateView(LoginRequiredMixin, View):
    def get(self, request):
        if Resume.objects.filter(owner_id=request.user.id):
            return redirect('my_resume')
        form = ResumeForm()
        return render(request, 'resume/resume_edit.html', context={
            'form': form,
        })

    def post(self, request):
        if Resume.objects.filter(owner_id=request.user.id):
            return redirect('my_resume')
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.owner = get_object_or_404(User, id=request.user.id)
            resume.save()
            messages.add_message(request, messages.SUCCESS, 'Готово!')
            return redirect('my_resume')
        messages.add_message(request, messages.ERROR, 'Что-то пошло не так!')
        return render(request, 'resume/resume_edit.html', context={
            'form': form,
        })


# myresume/ ##########################################################################################################
class MyResumeView(LoginRequiredMixin, View):
    def get(self, request):
        if Resume.objects.filter(owner_id=request.user.id):
            resume = Resume.objects.filter(owner_id=request.user.id).first()
            form = ResumeForm(instance=resume)
            return render(request, 'resume/resume_edit.html', context={
                'form': form,
            })
        return redirect('resume_lets_start')

    def post(self, request):
        resume = Resume.objects.filter(owner_id=request.user.id).first()
        if resume:
            form = ResumeForm(request.POST, instance=resume)
            if form.is_valid():
                resume = form.save(commit=False)
                resume.owner = get_object_or_404(User, id=request.user.id)
                resume.save()
                messages.add_message(request, messages.SUCCESS, 'Готово!')
                return redirect('my_resume')
            messages.add_message(request, messages.ERROR, 'Что-то пошло не так!')
            return render(request, 'resume/resume_create.html', context={
                'form': form,
            })
        return redirect('resume_lets_start')
