from django import forms


class QuoteRequestForm(forms.Form):
    full_name = forms.CharField(
        label='Full name',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Jane Doe',
            'autocomplete': 'name',
        }),
    )
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'you@example.com',
            'autocomplete': 'email',
        }),
    )
    phone_number = forms.CharField(
        label='Phone number',
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '09 123 456 789',
            'autocomplete': 'tel',
        }),
    )
    message = forms.CharField(
        label='Message',
        max_length=1000,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Tell us what kind of quote you need.',
            'rows': 4,
        }),
    )
