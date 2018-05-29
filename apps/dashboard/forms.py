from django import forms

from apps.userinfo.models import Userinfo


class UserinfoForm(forms.ModelForm):
    agent_type = forms.MultipleChoiceField(choices=Userinfo.AGENT_TYPE, widget=forms.CheckboxSelectMultiple)

    def clean_agent_type(self):
        return self.cleaned_data['agent_type']

    class Meta:
        model = Userinfo

        fields = [
            'first_name',
            'last_name',
            'ine',
            'street',
            'street_number',
            'street_between',
            'street_and_between',
            'suburb',
            'locality',
            'city',
            'state',
            'user_type',
            'agent_type',
        ]

        labels = {
            'first_name': 'Primer Nombre',
            'last_name': 'Apellido',
            'ine': 'INE',
            'street': 'Dirección',
            'street_number': 'Número',
            'street_between': 'Entre',
            'street_and_between': 'Y Entre',
            'suburb': 'Colonia',
            'locality': 'Localidad',
            'city': 'Municipio',
            'state': 'Estado',
            'user_type': 'Tipo de Usuario',
            'agent_type': 'Tipo de Agente',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ine': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'street_number': forms.TextInput(attrs={'class': 'form-control'}),
            'street_between': forms.TextInput(attrs={'class': 'form-control'}),
            'street_and_between': forms.TextInput(attrs={'class': 'form-control'}),
            'suburb': forms.Select(attrs={'class': 'form-control'}),
            'locality': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'user_type': forms.RadioSelect
        }
