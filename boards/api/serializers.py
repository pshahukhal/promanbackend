from rest_framework import serializers
from boards.models import Boards,Lists,Cards

#serializers required to serialize model to json 

class BoardSerializer (serializers.ModelSerializer):
    class Meta:
        model = Boards
        fields = ('__all__')

class ListSerializer (serializers.ModelSerializer):
    class Meta:
        model = Lists
        fields = ('id','title')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields= ('id','title','content')

#serialize that will include the detail of board as well as the lists inside it 
class BoardDetailSerializer (serializers.ModelSerializer):
    lists = ListSerializer(
        source='boardlists',
        many=True
    )
    class Meta:
        model = Boards
        fields = ('title','lists')

#serialize that will include the detail of list as well as the cards inside it 
class ListDetailSerializer(serializers.ModelSerializer):
    cards = CardSerializer(
        source='listcards',
        many=True
    )
    class Meta:
        model = Lists
        fields = ('title','cards')

