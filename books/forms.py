from django import forms
from django.utils.text import slugify
from .models import Book
import datetime
now = datetime.datetime.now()


class BookForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    author = forms.CharField(label='Author', max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}))
    author_slug = forms.SlugField(required=False, label='Slug', max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Author'}))
    genre = forms.CharField(label='Genre', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre'}))
    pub_year = forms.IntegerField(label='Year of Publication',
                                  widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Year of Publication'}))
    summary = forms.CharField(label='Summary', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                 'placeholder':
                                                                                 'What is this book about?...'}))
    characters = forms.CharField(label='Characters', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                'placeholder':
                                                                                'Who are the main characters of this '
                                                                                'book?...'}))

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'pub_year', 'summary', 'characters']

    def save(self):
        instance = super(BookForm, self).save(commit=False)
        instance.title_slug = slugify(instance.title)
        instance.author_slug = slugify(instance.author)
        instance.save()

        return instance

    def clean_pub_year(self):
        data = self.cleaned_data['pub_year']
        if data > now.year:
            raise forms.ValidationError("Year of Publication is not valid!")
        return data
