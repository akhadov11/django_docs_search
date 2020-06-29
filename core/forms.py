from django import forms


class SearchForm(forms.Form):
    ser_num = forms.CharField(label="Series and number", max_length=9)
