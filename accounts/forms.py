from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="", 
        widget=forms.TextInput(attrs=
            {'class':'form-control', 'placeholder':'E-mail'}))
    first_name = forms.CharField(label="", max_length=100, 
        widget=forms.TextInput(attrs=
            {'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, 
        widget=forms.TextInput(attrs=
            {'class':'form-control', 'placeholder':'Last Name'}))
    
    class Meta: 
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-xl text-[#101418] focus:outline-0 focus:ring-0 border border-[#d4dbe2] bg-gray-50 focus:border-[#d4dbe2] h-14 placeholder:text-[#5c718a] p-[15px] text-base font-normal leading-normal'
        self.fields['username'].widget.attrs['placeholder'] = 'Choose a username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '''
        <span class="form-text text-muted">
            <small>Obrigatório. 150 caracteres ou menos. Letras, dígitos e alguns caracteres.</small>
        </span>
        
        '''
        self.fields['first_name'].widget.attrs['class'] = 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-xl text-[#101418] focus:outline-0 focus:ring-0 border border-[#d4dbe2] bg-gray-50 focus:border-[#d4dbe2] h-14 placeholder:text-[#5c718a] p-[15px] text-base font-normal leading-normal'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'

        self.fields['last_name'].widget.attrs['class'] = 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-xl text-[#101418] focus:outline-0 focus:ring-0 border border-[#d4dbe2] bg-gray-50 focus:border-[#d4dbe2] h-14 placeholder:text-[#5c718a] p-[15px] text-base font-normal leading-normal'
        
        self.fields['email'].widget.attrs['class'] = 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-xl text-[#101418] focus:outline-0 focus:ring-0 border border-[#d4dbe2] bg-gray-50 focus:border-[#d4dbe2] h-14 placeholder:text-[#5c718a] p-[15px] text-base font-normal leading-normal'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'

        self.fields['password1'].widget.attrs['class'] = 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-xl text-[#101418] focus:outline-0 focus:ring-0 border border-[#d4dbe2] bg-gray-50 focus:border-[#d4dbe2] h-14 placeholder:text-[#5c718a] p-[15px] text-base font-normal leading-normal'
        self.fields['password1'].widget.attrs['placeholder'] = 'Create a password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '''
        <ul class="form-text text-muted small">
            <li>Sua senha deve ser única.</li>
            <li>Sua senha deve conter pelo menos 8 caracteres.</li>
            <li>Sua senha não pode ser totalmente numérica.</li>
        </ul>
        
        '''
        
        self.fields['password2'].widget.attrs['class'] = 'form-input flex w-full min-w-0 flex-1 resize-none overflow-hidden rounded-xl text-[#101418] focus:outline-0 focus:ring-0 border border-[#d4dbe2] bg-gray-50 focus:border-[#d4dbe2] h-14 placeholder:text-[#5c718a] p-[15px] text-base font-normal leading-normal'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '''
        <span class="form-text text-muted">
            <small>Digite a mesma senha de antes, para verificação.</small>
        </span>
        '''