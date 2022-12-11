from email.policy import default
from pickletools import long4
import time
from datetime import datetime
import discord
from decouple import config
import sys
import image_gen
import odds_math
import player_data
import currence_calc
import messaging_info
from datetime import datetime

def main():
    print('Process start')

    print('CLOSING NOW')

if __name__ == "__main__":
    main()
    
client = discord.Client()
bot = config('bot_token', default='')
restart_role = int(config('restart_notification_role_id', default=''))

@client.event
async def on_ready():
    try:
        print('Triggered the bot functions')
        restart_channel = client.get_channel(999562042212110338)
        server_commands.server_warning_ten_min()
        await restart_channel.send(f'<@&{restart_role}>\n```fix\n+ SERVER RESTART IN 10 MINUTES! +\n```')
        print('10 minute warning produced successfully')
        time.sleep(300)

        print('Triggered the bot functions')
        server_commands.server_warning_five_min()
        await restart_channel.send('```fix\n+ SERVER RESTART IN 5 MINUTES! +\n```')
        print('5 minute warning produced successfully')
        time.sleep(60)

        server_commands.server_warning_four_min()
        await restart_channel.send('```fix\n+ SERVER RESTART IN 4 MINUTES! +\n```')
        print('4 minute warning produced successfully')
        time.sleep(60)
        
        server_commands.start_storm()
        server_commands.server_warning_three_min()
        await restart_channel.send('```fix\n+ SERVER RESTART IN 3 MINUTES! +\n```')
        print('3 minute warning produced successfully')
        time.sleep(60)

        server_commands.server_warning_two_min()
        await restart_channel.send('```fix\n+ SERVER RESTART IN 2 MINUTES! +\n```')
        print('2 minute warning produced successfully')
        time.sleep(60)

        server_commands.trigger_lightning()
        server_commands.server_warning_one_min()
        await restart_channel.send(f'<@&{restart_role}>\n```fix\n+ SERVER RESTART IN 1 MINUTE. EXIT NOW! +\n```')
        print('1 minute warning produced successfully')
        time.sleep(50)

        server_commands.server_warning_ten_sec()
        await restart_channel.send('```fix\n+ SERVER RESTART IN 10 SECONDS! +\n```')
        print('10 second warning produced successfully')
        time.sleep(5)

        server_commands.stop_weather()
        server_commands.server_warning_five_sec()
        await restart_channel.send('```fix\n+ SERVER RESTART IN 5 SECONDS! +\n```')
        print('5 second warning produced successfully')
        time.sleep(5)

        await restart_channel.send(f'<@&{restart_role}>\n```diff\n- SERVER IS RESTARTING! SERVER WILL BE FULLY ONLINE IN 5 TO 10 MINUTES. -\n```')
        await restart_channel.send(f'```diff\n+ {datetime.now()} +\n```\n\n')
        await client.close()
        
    except ConnectionRefusedError:
        await restart_channel.send(f'```ml\n"ATTEMPTED TO RESTART WHILE SERVER IS RESTARTING, HANG TIGHT!"\n```')
        await restart_channel.send(f'```diff\n+ {datetime.now()} +\n```\n\n')
        print('Server was already restarting, closing the program')
        sys.exit()

    except Exception:
        await restart_channel.send(f'<@&{292697215326093323}>\n```ml\n"I am having some issues, need you to check on my programming."\n```')
        await restart_channel.send(f'```diff\n+ {datetime.now()} +\n```\n\n')
        print('ERROR: Ran into an issue running the program, please check under the hood.')
        sys.exit()

def start_bot():
    client.run(bot)
    time.sleep(5)