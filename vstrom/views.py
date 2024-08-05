from .models import Evenement,Participant
from .forms import SearchContactForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

class IndexView(FormView):
    template_name = 'vstrom/index.html'
    form_class = SearchContactForm
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data['evenements'])
        print(form.cleaned_data['participants'])
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['evenements'] = Evenement.objects.all()
        return context

class LoadParticipantsView(ListView):
    template_name = 'vstrom/participants_options.html'
    context_object_name = 'participants'

    def get_queryset(self):
        # on récupère l'évènement depuis l'id de la dropdown list
        evenement_id = self.request.GET.get('evenements')
        evenement = get_object_or_404(Evenement, pk=evenement_id)

        # Utilisation de prefetch_related pour optimiser les requêtes
        return Participant.objects.filter(participation__evenement=evenement).prefetch_related('participation_set')
