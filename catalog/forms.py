from django import forms
from django.forms import BooleanField, ModelForm

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"

class ProductForm(StyleFormMixin, forms.ModelForm):
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

class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'