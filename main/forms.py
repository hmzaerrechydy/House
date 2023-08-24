from django import forms

class addContent(forms.Form):
    title = forms.CharField(label="title")
    url = forms.CharField(label="url") 
    CHOICES = (
    ('Book','Book'),
    ('Article','Article'),
    ('Video','Video'),
    ('Podcast Episode','Podcast Episode'),
    ('Course','Course'),
    )
    type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    topic = forms.CharField(label="topic") 
    author = forms.CharField(label="author")

    title.widget.attrs['class'] = 'form-control'
    title.widget.attrs['placeholder'] = 'Title'

    url.widget.attrs['class'] = 'form-control'
    url.widget.attrs['placeholder'] = 'URL'
    
    type.widget.attrs['class'] = 'form-select'
    
    topic.widget.attrs['class'] = 'form-control'
    topic.widget.attrs['placeholder'] = 'Topic'

    author.widget.attrs['class'] = 'form-control'
    author.widget.attrs['placeholder'] = 'Author'

