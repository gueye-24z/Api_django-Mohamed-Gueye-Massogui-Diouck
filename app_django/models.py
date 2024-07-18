from django.db import models
from django.contrib.auth.models import User

# Modèle pour les groupes d'oeufs
class EggGroup(models.Model):
    identifier = models.CharField(max_length=79)

    class Meta:
        db_table = 'egg_groups'

# Modèle pour les items
class Item(models.Model):
    identifier = models.CharField(max_length=79)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField(blank=True, null=True)
    fling_effect_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'items'

# Modèle pour les mouvements
class Move(models.Model):
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.SmallIntegerField(blank=True, null=True)
    pp = models.SmallIntegerField(blank=True, null=True)
    accuracy = models.SmallIntegerField(blank=True, null=True)
    priority = models.SmallIntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField(blank=True, null=True)
    contest_type_id = models.IntegerField(blank=True, null=True)
    contest_effect_id = models.IntegerField(blank=True, null=True)
    super_contest_effect_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'moves'

# Modèle pour les Pokémons
class Pokemon(models.Model):
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField(blank=True, null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.IntegerField()

    class Meta:
        db_table = 'pokemon'

# Modèle pour les groupes d'oeufs des Pokémons
class PokemonEggGroup(models.Model):
    species_id = models.IntegerField()
    egg_group_id = models.IntegerField()

    class Meta:
        db_table = 'pokemon_egg_groups'

# Modèle pour les générations des formes des Pokémons
class PokemonFormGeneration(models.Model):
    pokemon_form_id = models.IntegerField()
    generation_id = models.IntegerField()
    game_index = models.IntegerField()

    class Meta:
        db_table = 'pokemon_form_generations'

# Modèle pour les mouvements des Pokémons
class PokemonMove(models.Model):
    pokemon_id = models.IntegerField()
    version_group_id = models.IntegerField()
    move_id = models.IntegerField()
    pokemon_move_method_id = models.IntegerField()
    level = models.IntegerField()
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'pokemon_moves'

# Modèle pour les statistiques des Pokémons
class PokemonStat(models.Model):
    pokemon_id = models.IntegerField()
    stat_id = models.IntegerField()
    base_stat = models.IntegerField()
    effort = models.IntegerField()

    class Meta:
        db_table = 'pokemon_stats'

# Modèle pour les types des Pokémons
class PokemonType(models.Model):
    pokemon_id = models.IntegerField()
    type_id = models.IntegerField()
    slot = models.IntegerField()

    class Meta:
        db_table = 'pokemon_types'

# Modèle pour les statistiques
class Stat(models.Model):
    identifier = models.CharField(max_length=79)
    damage_class_id = models.IntegerField(blank=True, null=True)
    is_battle_only = models.IntegerField()
    game_index = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'stats'

# Modèle pour les types
class Type(models.Model):
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'types'

# Modèle pour les Pokémons possédés par les utilisateurs
class UserPokemon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_pokemons'
        unique_together = ('user', 'pokemon')
