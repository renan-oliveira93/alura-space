from django import forms
from apps.galery.models import Picture

class PictureForms(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ['published',]
        labels = {
            'name': 'Título da Imagem',
            'credits': 'Créditos da imagem',
            'category': 'Categoria',
            'description': 'Descrição',
            'picture': 'Imagem',
            'picture_date': 'Data de criação',
            'user': 'Usuário'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-controls'}),
            'credits': forms.TextInput(attrs={'class':'form-controls'}),
            'category': forms.Select(attrs={'class':'form-controls'}),
            'description': forms.Textarea(attrs={'class':'form-controls'}),
            'picture': forms.FileInput(attrs={'class':'form-controls'}),
            'picture_date': forms.DateInput(
                format = '%d/%m/%y',
                attrs = {
                    'type': 'date',
                    'class':'form-control'
                }
            ),
            'user': forms.Select(attrs={'class':'form-controls'}),
        }