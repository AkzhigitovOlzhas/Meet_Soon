from .models import Conference
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ConferenceForm(ModelForm):
    class Meta:
        model = Conference
        fields = ['title', 'organizer', 'description', 'place', 'date']

        widgets = {
            'title': TextInput(attrs={
                'id': "title",
                'name': "name",
                'type': "text",
                'placeholder': "Матемаркетинг"
            }),
            'description': Textarea(attrs={
                'name': "description",
                'rows': "5",
                'placeholder': "Одна из крупных онлайн-конференций, в рамках которой будут проведены доклады..."
            }),
            'organizer': TextInput(attrs={
                'id': "organizer",
                'type': "text",
                'name': "organizer",
                'placeholder': "Mail Group"
            }),
            'place': TextInput(attrs={
                'id': "place",
                'type': "text",
                'name': "place",
                'placeholder': "Москва ул.Тверская 13"
            }),
            'date': DateTimeInput(attrs={
                'id': "date",
                'type': "datetime-local",
                'name': "date",
            })
        }

