from django.forms.models import BaseInlineFormSet, ModelForm
from django.forms.models import inlineformset_factory

class VariacaoObrigatoria(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super(VariacaoObrigatoria, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form