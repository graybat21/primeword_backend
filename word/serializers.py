from rest_framework.serializers import ModelSerializer
from .models import Textbook, Note, Word


class TextbookSerializer(ModelSerializer):
    class Meta:
        model = Textbook
        fields = ('textbook_id', 'name', 'grade', 'user_id')

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('note_id', 'textbook', 'lesson')

class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = ('word_id', 'word', 'meaning', 'note')