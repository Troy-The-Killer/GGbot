#!/usr/bin/env python 3.6

import discord
import Token
import Prefix

client = discord.Client()
token = Token.Secreto()
prefix = Prefix.Prefixo()

@client.event
async def on_ready():
    print('--------------- Online ---------------')
    print(f'Nome: {client.user.name}')
    print(f'  ID: {client.user.id}')
    print('--------------------------------------')

    user = str(len(set(client.get_all_members())))

    await client.change_presence(game=discord.Game(name=f'💞 {user} Membros'))

@client.event
async def on_message(message):
    if message.content.lower().startswith(f'{prefix}help') or message.content.lower().startswith(f'{prefix}ajuda'):
        ajudaEmbed = discord.Embed(
            title='📜 Informação',
            color=0x00ffc7,
            description='Não tenho comandos públicos. Minha função é enviar mensagens no privado.'
        )
        return await client.send_message(message.channel, embed=ajudaEmbed)

    if message.content.lower().startswith(f'{prefix}aviso'):
        if not message.author.server_permissions.administrator:
            Invalido = discord.Embed(
                title='📤 Não é possível enviar!',
                color=0xff0000,
                description='Você não tem permissão. 😢'
            )
            return await client.send_message(message.channel, embed=Invalido)

        Mensagem = message.content.strip(f'{prefix}aviso')

        Enviando = discord.Embed(
            title='📥 Enviando Mensagem!',
            color=0x00ff04,
            description='\n'
        )
        Enviando.add_field(name='📜 Mensagem', value=Mensagem)

        await client.send_message(message.channel, embed=Enviando)

        membros = list(message.server.members)
        valor = 0

        for member in membros:
            final = discord.Embed(
                title='💯 Importante!',
                color=0x1ce14d,
                description=(Mensagem)
            )
            final.set_image(url="https://i.imgur.com/E8jZvwo.png")

            try:
                await client.send_message(member, embed=final)
                print(member.name)
                valor += 1

            except:
                pass

        print(f'\n--- FIM ---')

        sucesso = discord.Embed(
            color=0x1ce14d,
            description='✅ Mensagem enviada com Sucesso!'
        )

        await client.send_message(message.channel, embed=sucesso)

client.run(token)
