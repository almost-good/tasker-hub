from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError 
from django.forms import modelformset_factory, inlineformset_factory
from allauth.account.forms import SignupForm
from .models import Task, Subtask



SubtaskFormSet = inlineformset_factory(
    Task, 
    Subtask, 
    fields=[
        'title', 
        'note', 
        'is_completed'
        ], extra=1
)


class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = [
            'title', 
            'note', 
            'is_completed'
            ]


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        
        fields = [
            'name',
            'task_image',
            'is_completed'
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        author = cleaned_data.get('author')

        if Task.objects.filter(name=name, author=author).exists():
            raise ValidationError("Task name taken, try another.")
        
        return cleaned_data


class CustomSignupForm(SignupForm):
    '''
    Custom signup form used to override the default signup form.
    
    **Fields:**
    
    ``username``
        The username of the user.
    ``email``
        The email of the user.
    ``password1``
        The password of the user.
    ``password2``
        The password confirmation of the user.
        
    **Methods:**
    ``__init__``
        Overrides the default fields.
    ``clean_email``
        Checks if the email is unique in the database.
    '''
    
    # Overriding the default fields.
    username = forms.CharField(
        max_length=20,
        help_text="Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.",
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    email = forms.EmailField(
        max_length=50,
        required=True,
        help_text='Required. 50 characters or fewer.',
    )
    
    def __init__(self, *args, **kwargs):
        '''
        Overrides the default fields.
        '''
        
        super().__init__(*args, **kwargs)
        
        self.fields['email'].label = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password2'].widget.attrs['placeholder'] = ''
        self.fields['password2'].label = 'Confirm Password'
        
    def clean_email(self):
        '''
        Checks if the email is unique in the database.
        
        **Returns:**
        
        ``email``
            The email of the user.
            
        **Raises:**
        
        ``ValidationError``
            If the email is already taken.
        '''
        
        email = self.cleaned_data.get('email')

        # Automatically checks if the email is unique in the database.
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already taken.")
        
        return email

