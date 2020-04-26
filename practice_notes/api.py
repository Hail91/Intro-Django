from rest_framework import serializers, viewsets
from .models import PersonalNote

class PersonalNoteSerializer(serializers.Serializer):

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')
    
class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    # Django will default to this Queryset
    queryset = PersonalNote.objects.none()
    # Unless we define an override function like the one below...
    def get_queryset(self):
        # import pdb; pdb.set_trace() <-- Useful debugger
        logged_in_user = self.request.user
        if logged_in_user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=logged_in_user)