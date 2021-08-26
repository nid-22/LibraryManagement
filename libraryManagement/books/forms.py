from django import forms
from books.models import Books,Author

class addBookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Author'].empty_label = 'Select Author'

class addAuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields = '__all__'

    