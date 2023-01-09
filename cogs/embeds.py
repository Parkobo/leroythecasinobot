from emoji import emojize as e
from nextcord import Colour, Embed

async def main_embed(pfp):
    embed = Embed(color=Colour.random(), title="Welcome to the Lottery", type='rich', url=None, description="Enjoy the stay!")
    embed.set_image(url="https://art.ngfiles.com/images/2722000/2722505_pixelheadache_animated-wallpaper.gif?f1662611959")
    embed.set_thumbnail(url=f"{pfp}")
    return embed

async def shop_embed(pfp, p_name):
    embed = Embed(color=Colour.random(), title=e(":package: ITEMS"), type='rich', url=None, description=e(":ticket: Ticket = $500\n:secret: Powerup = $500\n:wavy_dash:"))
    embed.set_author(name=f"How can I be of assistance {p_name}?", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
    embed.set_image(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/12cbe8a4-f55c-4b40-85bb-d8e1405e7b84/d98qb8z-56df9d2f-1a24-41d4-ad7d-e4244cc189be.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzEyY2JlOGE0LWY1NWMtNGI0MC04NWJiLWQ4ZTE0MDVlN2I4NFwvZDk4cWI4ei01NmRmOWQyZi0xYTI0LTQxZDQtYWQ3ZC1lNDI0NGNjMTg5YmUuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Nd7Pghx-n6PtcGxt3q1iXKcSmh0AlSH0jkMzXViaWqE")
    embed.set_thumbnail(url=f"{pfp}")
    embed.add_field(
        name=e(":1234: ODDS:"),
        value=e(
            f""":secret: 1 in 8\n
            :white_flower::secret: 1 in 20\n
            :white_flower::white_flower::secret: 1 in 200\n
            :white_flower::white_flower::white_flower: 1 in 500\n
            :white_flower::white_flower::white_flower::secret: 1 in 4,000\n
            :white_flower::white_flower::white_flower::white_flower: 1 in 10,000\n
            :white_flower::white_flower::white_flower::white_flower::secret: 1 in 80,000"""),
        inline=False)
    return embed

async def stats_embed(pfp, player):
    embed = Embed(color=Colour.random())
    embed.set_author(name="If you have any questions, use the /help command!", icon_url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3ce212da-22a2-4830-85cc-f5e5affc5cd6/dcxehfe-dd22d80d-4cff-49bf-be56-bb51f5ea0a78.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzNjZTIxMmRhLTIyYTItNDgzMC04NWNjLWY1ZTVhZmZjNWNkNlwvZGN4ZWhmZS1kZDIyZDgwZC00Y2ZmLTQ5YmYtYmU1Ni1iYjUxZjVlYTBhNzguZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.FPZzigXwn6ZWFixDogw4z5uQbIfnJSzyq8TDI9K_3o8')
    embed.set_image(url="https://www.icegif.com/wp-content/uploads/2022/03/icegif-83.gif")
    embed.set_thumbnail(url=f"{pfp}")
    embed.add_field(name=e(":bust_in_silhouette: NAME:"), value=player.get("Player Name"))
    embed.add_field(name=e(":moneybag: FUNDS:"), value=player.get("Funds"))
    embed.add_field(
        name=e(":green_book: MONETARY DATA:"),
        value=e(
            f""":accept::chart_with_upwards_trend: Lifetime Winnings -> ${player.get('Total Winnings')}
            :accept::chart_with_downwards_trend: Lifetime Losses -> ${player.get('Total Losses')}
            :accept::file_folder: Lifetime Revenue -> ${int(player.get("Total Winnings")) - int(player.get("Total Losses"))}
            :accept::dollar: Total Spent On Tickets -> ${int(player.get("Tickets Bought")*500)}
            :accept::pound: Total Spent On Powerups -> ${int(player.get("Powerups Bought")*500)}
            :wavy_dash:"""),
        inline=False)
    embed.add_field(
        name=e(":closed_book: TICKET DATA:"),
        value=e(
            f""":ticket::one: Tickets Bought -> {player.get('Tickets Bought')}
            :ticket::two: Tickets Used -> {player.get('Tickets Used')}
            :ticket::three: Tickets Gifted -> {player.get('Tickets Gifted')}
            :ticket::four: Tickets Received -> {player.get('Tickets Received')}
            :ticket::five: Current Tickets Count -> {player.get('Current Tickets Count')}
            :wavy_dash:"""),
        inline=False)
    embed.add_field(
        name=e(":orange_book: POWERUP DATA:"),
        value=e(
            f""":secret::one: Powerups Bought -> {player.get('Powerups Bought')}
            :secret::two: Powerups Used -> {player.get('Powerups Used')}
            :secret::five: Current Powerups Count -> {player.get('Current Powerups Count')}
            :wavy_dash:"""),
        inline=False)
    embed.add_field(
        name=e(":blue_book: LOTTERY DATA:"),
        value=e(
            f""":slot_machine::one: Win Count -> {player.get('Lottery Win Count')}
            :slot_machine::two: Lotteries Attempted -> {player.get('Attempts')}:wavy_dash:"""),
        inline=False)
    embed.set_footer(text=e(f"Joined on {player.get('Joined')}"))
    return embed

async def settings_embed(pfp, p_name):
    embed = Embed(color=Colour.random(), title="SETTINGS", type='rich', url=None, description="Player Settings")
    embed.set_author(name=f"You could win {p_name}!", icon_url='https://cdn-icons-png.flaticon.com/512/217/217853.png')
    embed.set_image(url="https://64.media.tumblr.com/0be6dd3b9a8624c8b0ed47deec5f39fd/tumblr_o9w9bfjRiY1vyuxeno1_1280.gif")
    embed.set_thumbnail(url=f"{pfp}")
    return embed

async def inventory_embed(pfp, player):
    total_worth = (player.get("Funds")) + ((int(player.get("Current Tickets Count")) + int(player.get("Current Powerups Count")))*500)
    embed = Embed(color=Colour.random())
    embed.set_author(name=f"""Your Assets Total Worth : ${total_worth}""", icon_url='https://media.tenor.com/k-PfH9O4EpcAAAAj/money-cash.gif')
    embed.set_image(url="https://www.icegif.com/wp-content/uploads/2022/03/icegif-83.gif")
    embed.set_thumbnail(url=f"{pfp}")
    embed.add_field(
        name=e("🏦 CASH OUT INFORMATION:"),
        value=e(
            f"""+ You can cash out 50% -> 100% of your wallet per request\n
            + Cash outs are completed in city in bulk, check for related announcements\n
            + Funds are delivered via wire transfer in city\n
            + Funds are returned to your account NOT INCLUDING fees paid if funds are not collected in city within a week of the first request\n
            + You have unlimited cash out requests, however, a fee applies after the first cash out within 24 hours:\n
            + Fees only apply to the amount requested for that specific withdrawl, and not the total requested of all combined cash outs\n
            :arrow_right:1st Time -> Free
            :arrow_right:2nd Time -> 15% Fee On Amount
            :arrow_right:3rd Time -> 35% Fee On Amount
            :arrow_right:4th Time -> 55% Fee On Amount
            :arrow_right:5+ Times -> 70% Fee On Amount
            :wavy_dash:"""),
        inline=False)
    embed.add_field(
        name=e("💝 DONATION INFORMATION:"),
        value=e(
            f"""+ You can donate 5,000 items a day to other users\n
            + Donations of items come at a small fee of 20% of the item's total value\n
            + Donation fees are non-refundable\n
            + Donation milestones in the form of discord roles are available\n
            :arrow_right:100 Donations -> Gifter
            :arrow_right:500 Donations -> Charitable
            :arrow_right:1,000 Donations -> Benevolent
            :arrow_right:4,000 Donations -> Donation Jockey
            :arrow_right:10,000 -> Donation Chief
            :arrow_right:75,000 -> Golden Caretaker
            :arrow_right:150,000 -> Philanthropist
            :arrow_right:250,000+ -> Miracle Worker"""),
        inline=False)
    embed.set_footer(text=e(
        f"""Total donated items: {player.get('Tickets Gifted')}\n
        Total cash withdrawn successfully: ${player.get('Total Cashed Out')}\n
        Total fees paid: ${player.get('Total Fees Paid')}"""
        ))
    return embed

async def alert_embed(pfp):
    embed = Embed(color=Colour.random(), title="ALERT", type='rich', url=None, description="You do not have enough funds to purchase any items from the shop at this time.")
    embed.set_image(url="https://64.media.tumblr.com/8d0620c4919bc5b9fa8b36dd9106a0ab/tumblr_n0zrp2SNo61rpfk7eo1_500.gif")
    embed.set_thumbnail(url=f"{pfp}")
    return embed

async def alert_cash_out_embed(pfp):
    embed = Embed(color=Colour.random(), title="ALERT", type='rich', url=None, description="You have no funds to withdraw at this time!")
    embed.set_image(url="https://64.media.tumblr.com/8d0620c4919bc5b9fa8b36dd9106a0ab/tumblr_n0zrp2SNo61rpfk7eo1_500.gif")
    embed.set_thumbnail(url=f"{pfp}")
    return embed