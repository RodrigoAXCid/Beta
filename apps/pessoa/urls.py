from django.urls import path
from .views import (contacts, PessoaCreateView, 
                    PessoaListView, PessoaDetailView, 
                    PessoaUpdateView, PessoaDeleteView)

app_name = 'pessoa'

urlpatterns = [
    path('', contacts, name='contacts'),
    path('novo/', PessoaCreateView.as_view(), name='novo'),
    path('lista/', PessoaListView.as_view(), name='lista'),
    path('detalhe/<int:pk>/', PessoaDetailView.as_view(), name='detalhe'),
    path('atualizar/<int:pk>/', PessoaUpdateView.as_view(), name='atualizar'),
    path('confirmar/eliminar/<int:pk>/', PessoaDeleteView.as_view(), name='eliminar')
]
