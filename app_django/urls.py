from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, MoveViewSet, PokemonViewSet, ConnexionView, RegisterView, MesPokemonsView, RoleView, AdminUsersView

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'moves', MoveViewSet, basename='move')
router.register(r'pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = [
    path('', include(router.urls)),
    path('connexion/', ConnexionView.as_view(), name='connexion'),
    path('register/', RegisterView.as_view(), name='register'),
    path('mesPokemons/', MesPokemonsView.as_view(), name='mes_pokemons'),
    path('role/', RoleView.as_view(), name='role'),
    path('admin/users/', AdminUsersView.as_view(), name='admin_users'),
]


