import discord
from discord.ext import commands
from commands.stundas import get_schedule  # Importing the function from the sheet handling file
from commands.open_ai_handler import generate_gpt_response, set_openai_api_key
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

openai_api_key = 'OPENAI_API_KEY' #Open_api_key here
set_openai_api_key(openai_api_key)

@bot.event
async def on_ready():
    print("Bot has connected to Discord!")

class TimeTable(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Pirmdiena", description="Dot stundu sarakstu pirmdienai."),
            discord.SelectOption(label="Otrdiena", description="Dot stundu sarakstu otrdienai."),
            discord.SelectOption(label="Trešdiena", description="Dot stundu sarakstu trešdienai."),
            discord.SelectOption(label="Ceturtdiena", description="Dot stundu sarakstu ceturtdienai."),
            discord.SelectOption(label="Piektdiena", description="Dot stundu sarakstu piektdienai."),
        ]

        super().__init__(placeholder="Izvēlies dienu.", options=options, min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):
        day_chosen = self.values[0]
        day, lessons = get_schedule(day_chosen)
        
        if day and lessons:
            response = f" - Stundu saraksts {day[0]}:\n - "
            response += "\n - ".join(lessons)
        else:
            response = "Stundu saraksts izvēlētai dienai nav pieejams."

        await interaction.response.send_message(response, ephemeral=True)

class TimeTableView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(TimeTable())

@bot.command()
async def table(ctx: commands.Context):
    await ctx.send("Izvēlies dienu kurai vēlies redzēt stundu sarakstu.", view=TimeTableView())

@bot.command()
async def gpt(ctx, *, prompt: commands.clean_content):
    try:
        async with ctx.typing():
            user_id = ctx.author.id
            user_name = ctx.author.name
            reply = generate_gpt_response(user_id, user_name, prompt)
            await ctx.send(reply)
    except Exception as e:
        await ctx.send("Kaut kas nogāja greizi.")
        print("Error:", e)



bot.run("DISCORD_BOT_TOKEN") #Discord token here.