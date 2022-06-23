import discord 
import random
import os


computer = ['R', 'P', 'S']
p = 'Paper'
r = 'Rock'
s = 'Scissors'

client=discord.Client()


@client.event
async def on_ready():
    print('you have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    user_message = str(message.content).upper()
    global username
    username = str(message.author).split('#')[0]
    if user_message == '!R' or user_message == '!S' or user_message == '!P':
        change(user_message)
        # print(gameplay.game(change(user_message)))
        await message.channel.send(start(change(user_message)))

def displayText():
    print( "Geeks 4 Geeks !")



def start(player_pick):
    computer_pick = random.choice(computer)
    # computer_pick = "R"
    pick_status = False
    p_pick = check_computer(player_pick)
    c_pick = check_player(computer_pick)
    while pick_status == False:
    
        if check_computer(player_pick) == check_player(computer_pick):
            pick_status = True
            return f'No winner this is a draw {username}:({p_pick}) : BOT ({c_pick})'

        elif check_computer(player_pick) == p and check_player(computer_pick) == r:
            pick_status = True
            return f"{username} won this round, {username}: ({p_pick}) : BOT ({c_pick})"

        elif check_computer(player_pick) == p and check_player(computer_pick) == s:
            pick_status = True
            return f"{username} lost this round, {username}: ({p_pick}) : BOT ({c_pick})"
            # return "%s lost this round", "%s: (%s) : BOT (%s)" % (username,username,check_computer(player_pick), check_player(computer_pick))

        elif check_computer(player_pick) == r and check_player(computer_pick) == p:
            pick_status = True
            return f"{username} lost this round, {username}: ({p_pick}) : BOT ({c_pick})"
            # return "%s lost this round", "%s: (%s) : BOT (%s)" % (username,username,check_computer(player_pick), check_player(computer_pick))

        elif check_computer(player_pick) == r and check_player(computer_pick) == s:
            pick_status = True
            return f"{username} won this round, {username}: ({p_pick}) : BOT ({c_pick})"
            # return "%s won this round", "%s: (%s) : BOT (%s)" % (username,username,check_computer(player_pick), check_player(computer_pick))

        elif check_computer(player_pick) == s and check_player(computer_pick) == r:
            pick_status = True
            return f"{username} lost this round, {username}: ({p_pick}) : BOT ({c_pick})"
            # return "%s lost this round", "%s: (%s) : BOT (%s)" % (username,username,check_computer(player_pick), check_player(computer_pick))

        elif check_computer(player_pick) == s and check_player(computer_pick) == p:
            pick_status = True
            return f"{username} won this round, {username}: ({p_pick}) : BOT ({c_pick})"
            # return "%s won this round", "%s: (%s) : BOT (%s)" % (username,username,check_computer(player_pick), check_player(computer_pick))    


def check_player(player):
    if player == 'R':
        return r
    if player == 'P':
        return p
    if player == 'S':
        return s

def check_computer(computer):
    if computer == 'R':
        return r
    if computer == 'P':
        return p
    if computer == 'S':
        return s

def change(alpha):
    if alpha == '!R':
        return 'R'
    if alpha == '!P':
        return 'P'
    if alpha == '!S':
        return 'S'
client.run(os.getenv('TOKEN'))

# print (game("P"))