from discord.ext import commands
from discord.ui import Button, ButtonStyle

class AutoTicketPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_ticket(self, user):
        # Create a ticket by sending a direct message to the user
        channel = await user.create_dm()
        await channel.send("Open ticket")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # Ignore messages from other bots

        if isinstance(message.channel, discord.DMChannel):
            # This is a direct message to the bot, create a ticket
            await self.create_ticket(message.author)

    @commands.Cog.listener()
    async def on_button_click(self, button, interaction):
        if button.custom_id == 'open_ticket':
            # Send a direct message to the bot with the message "Open ticket"
            channel = await self.bot.fetch_user(interaction.user.id).create_dm()
            await channel.send("Open ticket")

    @commands.command()
    async def createbutton(self, ctx, target_channel: discord.TextChannel):
        button = Button(style=ButtonStyle.green, label="Open Ticket", custom_id='open_ticket')
        view = discord.ui.View()
        view.add_item(button)

        await target_channel.send("Click the button to open a ticket:", view=view)

def setup(bot):
    bot.add_cog(AutoTicketPlugin(bot))
