from django import forms

class addContent(forms.Form):
    title = forms.CharField(label="title")
    url = forms.CharField(label="url") 

    TYPE_CHOICES = (
    ('','Type'),
    ('Book','Book'),
    ('Article','Article'),
    ('Video','Video'),
    ('Podcast','Podcast'),
    ('Course','Course'),
    ('Blog','Blog'),
    )
    type = forms.ChoiceField(widget=forms.Select, choices=TYPE_CHOICES)

    TOPIC_CHOICES = (
        ('', 'Topic'),
        ('Religion', 'Religion'), 
        ('Technology', 'Technology'), 
        ('Science', 'Science'),
        ('History', 'History'),
        ('Business', 'Business'), 
        ('Art', 'Art'), 
        ('Languages', 'Languages'), 
        ('Economics', 'Economics'), 
        ('Philosophy', 'Philosophy')
    )
    topic = forms.ChoiceField(widget=forms.Select, choices=TOPIC_CHOICES)
    
    author = forms.CharField(label="author")

    title.widget.attrs['class'] = 'form-control'
    title.widget.attrs['placeholder'] = 'Title'

    url.widget.attrs['class'] = 'form-control'
    url.widget.attrs['placeholder'] = 'URL'
    
    type.widget.attrs['class'] = 'form-select'
    
    topic.widget.attrs['class'] = 'form-select'
    
    author.widget.attrs['class'] = 'form-control'
    author.widget.attrs['placeholder'] = 'Author'

