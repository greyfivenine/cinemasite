from django import forms
from django.core.exceptions import ValidationError

from .models import Comment, Place, Schedule, Movie


class AdminScheduleForm(forms.ModelForm):
    movie_name = forms.ModelChoiceField(queryset = Movie.objects.filter(soon=False))
    class Meta:
        model = Schedule
        fields = '__all__'



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_author', 'author_email', 'comment_text']

        widgets = {
            'comment_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'comment_text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите комментарий'}),
            'author_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите e-mail'}),
        }

class BuyTicketForm(forms.Form):

    PAYMENT_METHODS = {
        ('VISA', 'VISA'),
        ('MIR', 'Мир'),
        ('MASTERCARD', 'MASTERCARD'),
        ('Phone', 'Телефон')
    }

    def clean_is_bought(self):
        flag = self.cleaned_data['is_bought']

        if flag:
            raise ValidationError('Это место уже куплено!')
        return flag

    is_bought = forms.BooleanField(required=False)
    payment_method = forms.ChoiceField(label = 'Метод оплаты', choices=PAYMENT_METHODS, widget=forms.Select(attrs={'class': 'form-control mb-2'}))
    card_owner = forms.CharField(label = 'Владелец карты', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Введите владельца карты'}))
    card_number = forms.CharField(label = 'Номер карты', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Введите номер карты'}))
    card_cvc = forms.CharField(label = 'CVC-код', max_length=3, widget=forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Введите CVC-код'}))
