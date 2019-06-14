from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView

from boards.models import Boards,Lists, Cards
from .serializers import BoardSerializer,BoardDetailSerializer,ListSerializer,ListDetailSerializer,CardSerializer

class BoardListView(ListAPIView):
    queryset= Boards.objects.all()
    serializer_class = BoardSerializer

class BoardDetailView(RetrieveAPIView):
    queryset= Boards.objects.all()
    serializer_class = BoardDetailSerializer

class BoardCreateView(CreateAPIView):
    queryset= Boards.objects.all()
    serializer_class = BoardSerializer

class BoardUpdateView(UpdateAPIView):
    queryset= Boards.objects.all()
    serializer_class = BoardSerializer

class BoardDeleteView(DestroyAPIView):
    queryset= Boards.objects.all()
    serializer_class = BoardSerializer    

class ListListView(ListAPIView):
    queryset= Lists.objects.all()
    serializer_class = ListSerializer

class ListDetailView(RetrieveAPIView):
    queryset= Lists.objects.all()
    serializer_class = ListDetailSerializer

class ListCreateView(CreateAPIView):
    queryset= Lists.objects.all()
    serializer_class = ListSerializer

class ListUpdateView(UpdateAPIView):
    queryset= Lists.objects.all()
    serializer_class = ListSerializer

class ListDeleteView(DestroyAPIView):
    queryset= Lists.objects.all()
    serializer_class = ListSerializer

class CardListView(ListAPIView):
    queryset= Cards.objects.all()
    serializer_class = CardSerializer

class CardDetailView(RetrieveAPIView):
    queryset= Cards.objects.all()
    serializer_class = CardSerializer

class CardCreateView(CreateAPIView):
    queryset= Cards.objects.all()
    serializer_class = CardSerializer

class CardUpdateView(UpdateAPIView):
    queryset= Cards.objects.all()
    serializer_class = CardSerializer

class CardDeleteView(DestroyAPIView):
    queryset= Cards.objects.all()
    serializer_class = CardSerializer    