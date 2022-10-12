from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from apps.pessoa.models import Pessoa

# Create your views here.
def contacts(request):
    return render(request, 'pessoa/contacts.html')

class PessoaCreateView(CreateView):
    model = Pessoa
    fields = '__all__'
    success_url = reverse_lazy('pessoa:lista')

class PessoaListView(ListView):
    model = Pessoa

class PessoaDetailView(DetailView):
    model = Pessoa

class PessoaUpdateView(UpdateView):
    model = Pessoa
    fields = ['nome', 'idade', 'email', 'cc']
    template_name = 'pessoa/pessoa_update.html'
    success_url = reverse_lazy('pessoa:lista')

class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = reverse_lazy('pessoa:lista')
