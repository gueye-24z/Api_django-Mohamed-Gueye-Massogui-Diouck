from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import Item, Move, Pokemon, PokemonType
from .serializers import ItemSerializer, MoveSerializer, PokemonSerializer, PokemonTypeSerializer, UserSerializer

class ItemViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

class MoveViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        move = Move.objects.get(pk=pk)
        serializer = MoveSerializer(move)
        return Response(serializer.data)

class PokemonViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        pokemon = Pokemon.objects.get(pk=pk)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='name/(?P<name>[^/.]+)')
    def get_by_name(self, request, name=None):
        pokemon = Pokemon.objects.get(identifier=name)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='types/(?P<identifier>[^/.]+)')
    def get_by_type(self, request, identifier=None):
        pokemon_types = PokemonType.objects.filter(pokemon__identifier=identifier)
        serializer = PokemonTypeSerializer(pokemon_types, many=True)
        return Response(serializer.data)

class ConnexionView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class MesPokemonsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Logique pour récupérer les Pokémons de l'utilisateur
        return Response({'message': 'Liste des Pokémons de l\'utilisateur'})

class RoleView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({'message': 'Vous êtes un admin'})

class AdminUsersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user_id = request.data.get('user_id')
        User.objects.filter(id=user_id).delete()
        return Response({'message': 'Utilisateur supprimé'}, status=status.HTTP_204_NO_CONTENT)
