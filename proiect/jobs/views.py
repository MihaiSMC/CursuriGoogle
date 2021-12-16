from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView

from jobs.forms import JobsForm
from jobs.models import Jobs


class CreateJobView(LoginRequiredMixin, CreateView):
    model = Jobs
    form_class = JobsForm
    template_name = 'jobs/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:listare')

    def get_form_kwargs(self):
        data = super(CreateJobView, self).get_form_kwargs()
        data.update({'pk': None})
        return data


class UpdateJobView(LoginRequiredMixin, UpdateView):
    model = Jobs
    form_class = JobsForm
    template_name = 'jobs/jobs_form.html'

    def get_form_kwargs(self):
        data = super(UpdateJobView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('jobs:listare')


class ListJobView(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = 'jobs/jobs_index.html'

    def get_queryset(self):
        return Jobs.objects.filter(active=1)


@login_required
def delete_location(request, pk):
    if request.user.is_authenticated:
        Jobs.objects.filter(id=pk).update(active=0)
    return redirect('jobs:listare')
