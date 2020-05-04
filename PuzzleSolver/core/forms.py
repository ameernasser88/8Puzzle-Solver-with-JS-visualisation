from django import forms

CHOICES = (
    ("1", "BFS"),
    ("2", "DFS"),
    ("3", "A* - Manhattan Distance"),
    ("4", "A* - Euclidean Distance"),
)


class HomeForm(forms.Form):
    initial_state = forms.CharField(label='Enter Initial State separated by , : ', max_length=18)
    search_algorithm = forms.ChoiceField(label="Search Algorithm : ",choices=CHOICES,required=True)