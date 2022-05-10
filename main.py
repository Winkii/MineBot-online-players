from discord_webhook import DiscordWebhook, DiscordEmbed
import configparser
from mcstatus import JavaServer
import requests
from time import sleep

def send_webhook(webhook,status,name,status_color,txt_description):
    reponse_name = requests.get(url_name.format(name))
    contenu_name = reponse_name.json()
    
    # create embed object for webhook
    embed = DiscordEmbed(title=name , description=txt_description , color=status_color)
    # set thumbnail
    embed.set_thumbnail(url=url_head.format(contenu_name['id']))
    # set footer
    embed.set_footer(text="Online players : "+str(status.players.online)+"/"+str(status.players.max))
    # set timestamp (default is now)
    embed.set_timestamp()
    # add embed object to webhook
    webhook.add_embed(embed)

    response = webhook.execute()

    webhook.remove_embeds()

#embed color
offline = 16711680
online = 62464

#url for skin head thumbnail
url_name = "https://api.mojang.com/users/profiles/minecraft/{}?"
url_head = "https://mc-heads.net/avatar/{}.png"

#init config file
config = configparser.ConfigParser()
config.read('params.conf')

#init discord webhook
webhook = DiscordWebhook(url=config['WEBHOOK']['url'],username="MineBot")
print("webhook initiated")

#init mc server
server = JavaServer.lookup(str(config['MINECRAFT']['server']+":"+config['MINECRAFT']['server_port']))
print("Connexion with Java server initiated")
#current_online = server.query().players.names
current_online = []
#print("current_online init" + str(current_online))

while True:

    status = server.status()
    query = server.query()
    players_name = query.players.names
    #print("players_name "+ str(players_name))
    


    for name in players_name:
        if name not in current_online :
            status_color = online
            description = "is online"
            send_webhook(webhook,status,name,status_color,description)
    disconnected = list(set(current_online) - set(players_name))    
    #print("disconnected "+str(disconnected))
    if len(disconnected) > 0:
        for offline_name in disconnected:
            status_color = offline
            description = "is offline"
            send_webhook(webhook,status,offline_name,status_color,description)
    #get skin head
    current_online = players_name    

    #print("current_online end of while" + str(current_online))
    sleep(int(config['WEBHOOK']['delay']))

