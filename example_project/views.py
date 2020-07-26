from django.urls import reverse_lazy
from django.views import generic

from example_project.models import ExampleModel


class ExampleCreateView(generic.CreateView):
    model = ExampleModel
    fields = '__all__'
    success_url = reverse_lazy('list')


class ExampleUpdateView(generic.UpdateView):
    model = ExampleModel
    fields = '__all__'
    success_url = reverse_lazy('list')


class ExampleListView(generic.ListView):
    model = ExampleModel
