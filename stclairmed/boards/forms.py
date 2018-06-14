from django import forms

class SearchForm(forms.Form):
    term = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Keywords'}),
        min_length=1,
        max_length=35,
        )

    choices = (('practices', 'Practices',),('doctors', 'Doctors',),('all', 'All',))
    my_choice_field = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=choices
        )

    class Meta:
        fields = ['term', 'field']

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=35,
    )

    email = forms.EmailField()

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':5, 'placeholder':"Type your comment/question here."}
        ),
        max_length=4000,
        help_text="You may not type a message longer than 4000 characters."
    )

    class Meta:
        fields = ['name', 'email', 'message']


class SuperSearch(forms.Form):
    keyword = forms.CharField(
        max_length = 45,
        min_length = 1
    )

    class Meta:
        fields = ['keyword']
