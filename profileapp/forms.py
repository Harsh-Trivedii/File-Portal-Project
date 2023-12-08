from django import forms

class UserProfileSearchForm(forms.Form):
    search_query=forms.CharField(max_length=30,required=False,label='Search by typing username')
