from rest_framework.serializers import ModelSerializer

from .models import Textbook, Note, Word


class TextbookSerializer(ModelSerializer):
    class Meta:
        model = Textbook
        fields = ('id', 'name', 'grade', 'user_id', 'regdate')
        depth = 1


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'textbook', 'lesson', 'regdate')
        depth = 1


# class WordclassSerializer(ModelSerializer):
#     class Meta:
#         model = Wordclass
#         fields = ('id', 'name', 'memo')


class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'spelling', 'meaning', 'note', 'memo')
        depth = 1

