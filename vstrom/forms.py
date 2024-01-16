from django import forms

from .models import Evenement, Participant

class SearchContactForm(forms.Form):
    evenements = forms.ModelChoiceField(queryset=Evenement.objects.all(), widget=forms.Select(attrs={'hx-get': 'load_participants/', 'hx-target': '#id_participants'}))
    participants = forms.ModelChoiceField(queryset=Participant.objects.none())

    def __init__(self, *args, **kwargs):
        super(SearchContactForm, self).__init__(*args, **kwargs)

        '''
        Pour mécanisme HTMX lors la soumission de formualaire via un POST
        
        A partir de l'évenement, on redéfinit le queryset pour les participants
        afin que les données soient alignées avec l'évènement sélectionné.
        
        Dans le cas contraire, on est confronté à une erreur de formulaire 
        indiquant que le choix n'est pas valide.
        '''
        if "evenements" in self.data:
            evenement_id = int(self.data.get("evenements"))
            evenement = Evenement.objects.get(pk=evenement_id)

            participations = evenement.participation_set.all()
            participants = []

            for participation in participations:
                participants.append(participation.participant)

            self.fields["participants"].queryset = Participant.objects.filter(id__in=[participant.id for participant in participants])

        '''
        On définit les attributs de style des champs du formulaire ici pour une implémentation rapide,
        évolution possible : utilisation de Crispy Forms
        '''
        self.fields["evenements"].widget.attrs.update({"class": "form-control"})
        self.fields["participants"].widget.attrs.update({"class": "form-control"})