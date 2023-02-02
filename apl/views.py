from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from apl.form import ApplicationForm
from apl.models import Application, Files


class ApplicationListView(ListView):
    model = Application
    form_class = ApplicationForm
    template_name = 'apl/users_list.html'
    context_object_name = 'apl'


class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'apl/create.html'
    context_object_name = 'apl'
    success_url = reverse_lazy('apl_create')

    def form_valid(self, form):
        messages.success(self.request, 'Application successfully created.')
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('files')
        if form.is_valid():
            id = form.save().pk
            application = Application.objects.get(pk=id)
            if files:
                for f in files:
                    fl = Files(application=application, file=f)
                    fl.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)