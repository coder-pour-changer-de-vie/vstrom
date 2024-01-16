from django.http import JsonResponse
from django.shortcuts import render
from .models import Evenement, Participant
from .forms import SearchContactForm

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = SearchContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['evenements'])
            print(form.cleaned_data['participants'])
        else:
            print(form.errors)
    else :
        form = SearchContactForm()

    evenements = Evenement.objects.all()
    context = {
        'form': form,
        'evenements': evenements
    }
    return render(request, 'vstrom/index.html', context)

def load_participants(request):

    # on récupère l'évènement depuis l'id de la dropdown list
    evenement = Evenement.objects.get(pk=request.GET.get('evenements'))

    # on récupère les participants via la table d'association
    participations = evenement.participation_set.all()
    participants = []

    for participation in participations:
        participants.append(participation.participant)

    return render(request, 'vstrom/participants_options.html', {'participants': participants} )
