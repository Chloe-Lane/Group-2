from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='Email Address',
        max_length=100,
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    first_name = forms.CharField(
        label='First Name',
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=50,
        required=False,  # Optional field
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    date_of_birth = forms.DateField(
        label='Date of Birth',
        widget=forms.SelectDateWidget(years=range(1900, 2025))
    )
    gender = forms.ChoiceField(
        label='Gender',
        choices=[('male', 'Male'), ('female', 'Female')],
        widget=forms.RadioSelect
    )
    country = forms.ChoiceField(
        label='Country',
        choices=[('us', 'United States'), ('denmark', 'Denmark'), ('other', 'Other')],
        widget=forms.Select(attrs={'class': 'country'})
    )
    captcha = forms.CharField(
        label='Verify registration',
        widget=forms.TextInput(attrs={'placeholder': 'Enter the characters from above.'})
    )
