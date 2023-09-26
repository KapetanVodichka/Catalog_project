from django import forms

from catalog.models import Product, ProductVersion


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    active_version = forms.ModelChoiceField(
        queryset=ProductVersion.objects.all(),
        required=False,
        label='Выберите какая версия должна быть активной'
    )

    class Meta:
        model = Product
        # fields = '__all__'
        # fields = ('name', 'description', 'image', 'category', 'price',)
        exclude = ('creation_date', 'last_date_changing',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        words_to_ban = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for words in words_to_ban:
            if words in cleaned_data:
                raise forms.ValidationError(f'{words} - недопустимое слово для использования')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        words_to_ban = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words_to_ban:
            if word in cleaned_data:
                raise forms.ValidationError(f'{word} - недопустимое слово для использования')

        return cleaned_data


class ProductVersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = ProductVersion
        exclude = ('product', 'active_version',)
