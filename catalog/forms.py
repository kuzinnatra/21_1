from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("__all__")

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        censored_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for i in censored_list:
            if i in cleaned_data:
                raise forms.ValidationError('Поле содержит запрещенные слова')
        return cleaned_data


    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        censored_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for i in censored_list:
            if i in cleaned_data:
                raise forms.ValidationError('Поле содержит запрещенные слова')
        return cleaned_data