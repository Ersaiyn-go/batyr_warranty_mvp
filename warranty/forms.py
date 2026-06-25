from django import forms


class WarrantyCheckForm(forms.Form):
    serial_number = forms.CharField(
        label='Серийный номер',
        max_length=64,
        widget=forms.TextInput(attrs={
            'placeholder': 'Например: BW-SUN-2026-000125',
            'autocomplete': 'off',
            'class': 'serial-input',
        })
    )

    def clean_serial_number(self):
        return self.cleaned_data['serial_number'].strip().upper()
