import asyncio
import random

import discord #import du module
from discord.ext import commands

intents = discord.Intents.all() # on donne tous les intents à notre bot notamment pour qu'il puisse lister tout les users
intents.message_content = True

client = discord.Client(intents=intents) # on crée un objet client en lui donnant les intents

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}') # on affiche un message dans la console pour dire que le bot est connecté

@client.event
async def on_message(message): # on crée une fonction qui sera appelée à chaque fois qu'un message est envoyé
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send('Pong ! :ping_pong:')

    elif message.content.startswith('!members'):
        members_list = await get_members(message.guild)
        await message.channel.send(f"Liste des membres du serveur :\n{', '.join(members_list)}") # on affiche la liste des membres du serveur

    elif message.content.startswith('bonjour'): # si le message commence par "bonjour"
        await message.channel.send(':wave:')

    elif message.content.startswith('!joke'): # si le message commence par "!joke"
        joke = get_random_joke()
        await message.channel.send(joke)

    elif message.content.startswith('!welcome'): # si le message commence par "!welcome"
        user = message.author
        await message.channel.send(f"Bienvenue {user.mention} ! :tada:") # on mentionne l'utilisateur pour lui dire bienvenue

    elif message.content.startswith('sardoche'):
        await message.channel.send(f"{message.author.mention}, tu as été time-out pour avoir mentionné 'sardoche' !") # on mentionne l'utilisateur pour lui dire qu'il a été time-out
        await timeout_user(message.author, message.guild)

async def get_members(guild):
    members_list = [member.name for member in guild.members] # on crée une liste avec le nom de chaque membre du serveur
    return members_list

async def timeout_user(user, guild):
    role = discord.utils.get(guild.roles, name="Time Out")  # Rôle "Time Out"
    if not role:
        role = await guild.create_role(name="Time Out", reason="Création du rôle Time Out") # On crée le rôle "Time Out" s'il n'existe pas

    await user.add_roles(role)

    await asyncio.sleep(300)  # Durée du time out en secondes (300s = 5 minutes)

    await user.remove_roles(role)

def get_random_joke(): # on crée une fonction qui renvoie une blague aléatoire
    jokes = [
        "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
        "Qu'est-ce qui est vert, qui monte et qui descend ? Un petit pois dans un ascenseur.",
        "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
        "Quel est le comble pour un électricien ? De péter les plombs en courant."
    ]
    return random.choice(jokes)

client.run('MTIzNDc2MTk2MzEyMTE1MjAyMQ.GBlY2I.YlGUKLydbLOgSBLRPuiqIQs4yv1ifIuDppbqD0') # on lance le bot avec le token