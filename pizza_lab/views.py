from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy
from .models import Pizza
from django.http import HttpResponseBadRequest


# Criação das Views ou CRUDs


# View Home
class HomeView(TemplateView):
    template_name = "pizza_lab/home.html"


# View para visualizar e editar menu
class MenuListView(ListView):
    model = Pizza
    template_name = "pizza_lab/pizza_list.html"
    context_object_name = "menu"


# View para atualizar pizza
class MenuUpdateView(UpdateView):
    model = Pizza
    fields = ["nome", "descricao", "tamanho", "preco"]
    success_url = reverse_lazy("menu")


# View para deletar pizza
class MenuDeleteView(DeleteView):
    model = Pizza
    success_url = reverse_lazy("menu")


# View para criar pizza
class MenuCreateView(CreateView):
    model = Pizza
    fields = ["nome", "descricao", "id_tipo"]
    success_url = reverse_lazy("menu")

    # Resposta com status 400 (Bad Request)


def form_invalid(self, form):
    return super().form_invalid(form)
