from django import forms
from .models import Pizza, TipoPizza, TamanhoPizza, ValorPizza


class PizzaForm(forms.ModelForm):
    tipo = forms.ModelChoiceField(queryset=TipoPizza.objects.all())
    tamanho = forms.ModelChoiceField(queryset=TamanhoPizza.objects.all())
    preco = forms.DecimalField(
        max_digits=7, decimal_places=2, disabled=True, required=False
    )

    class Meta:
        model = Pizza
        fields = ["nome", "descricao", "tipo", "tamanho", "preco"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Preço só será setado se já existir um tipo e tamanho definidos
        tipo = self.initial.get("tipo") or self.data.get("tipo")
        tamanho = self.initial.get("tamanho") or self.data.get("tamanho")
        if tipo and tamanho:
            try:
                valor = ValorPizza.objects.get(id_tipo=tipo, id_tamanho=tamanho)
                self.fields["preco"].initial = valor.preco
            except ValorPizza.DoesNotExist:
                self.fields["preco"].initial = None
