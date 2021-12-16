from django import forms
from jobs.models import Jobs


class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['name', 'url', 'description', 'customer']

    def __init__(self, pk, *args, **kwargs):
        super(JobsForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        name_value = cleaned_data.get('name')
        customer_value = cleaned_data.get('customer')

        if self.pk:
            if Jobs.objects.filter(name__icontains=name_value, customer=customer_value, active=1).exclude(id=self.pk).exists():
                self._errors['name'] = self.error_class(['Job-ul deja exista.'])
        else:
            if Jobs.objects.filter(name__icontains=name_value, customer=customer_value, active=1).exists():
                self._errors['name'] = self.error_class(['Job-ul deja exista.'])

        return cleaned_data
