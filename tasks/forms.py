from django import forms
import datetime


class TaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description',max_length=500)
    owner = forms.CharField(label='Owner', max_length=100)
    status = forms.ChoiceField(label='Status', choices=[('untouched', 'untouched'), ('in progress', 'in progress'),
                                                        ('on hold', 'on hold'), ('completed', 'completed')])
    due_date = forms.DateField(label='Due Date', localize=True, initial=datetime.date.today,
                               widget=forms.SelectDateWidget())
    member = forms.CharField(label='Member', max_length=100, required=False)


class SearchForm(forms.Form):
    search_value = forms.CharField(label='Search title, description, owner or status', max_length=100)