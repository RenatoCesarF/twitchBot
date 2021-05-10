import utils as utils
from twitchio.ext import commands
import twitchio

from commands.commandsList import commandsList
from commands.mudaATela import ChangeScreen
from commands.projects import projects

from commands.socialMedia.github import postGithub
from commands.socialMedia.instagram import postInstagram
from commands.socialMedia.twitter import postTwitter
from commands.socialMedia.youtube import postYoutube

from commands.projectModel import projectModel

envVars = utils.EnvVars()

commandsPossibleRequests = ['commands', 'comandos', 'help', 'bot']
projectsPossibleRequests = ['projects','projetos']

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=envVars.ACCESS_TOKEN, client_id=envVars.CLIENT_ID, nick='renatocesarf', prefix='!', initial_channels=["#renatocesarf"])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        # print(message.content)
        await self.handle_commands(message)


    @commands.command(name='mudaatela')
    async def mudaatela(self,ctx):
        await ChangeScreen(self, ctx)
    
    # =============== SOCIAL MEDIA STUFFS =============
    @commands.command(name='github')
    async def github(self,ctx):
        await postGithub(self, ctx)

    @commands.command(name='instagram')
    async def instagram(self,ctx):
        await postInstagram(self, ctx)
    
    @commands.command(name='twitter')
    async def twitter(self,ctx):
        await postTwitter(self, ctx)
    
    @commands.command(name='youtube')
    async def youtube(self,ctx):
        await postYoutube(self, ctx)
        
    # =============== SHOW COMMANDS =============
    @commands.command(name=commandsPossibleRequests[0])
    async def Fcommands(self,ctx):
        await commandsList(self, ctx)
    
    @commands.command(name=commandsPossibleRequests[1])
    async def comandos(self,ctx):
        await commandsList(self, ctx)

    @commands.command(name=commandsPossibleRequests[2])
    async def helpCommands(self,ctx):
        await commandsList(self, ctx)
    
    @commands.command(name=commandsPossibleRequests[3])
    async def bot(self,ctx):
        await commandsList(self, ctx)

    # =============== SHOW PROJECTS =============
    @commands.command(name=projectsPossibleRequests[0])
    async def project(self,ctx):
        await projects(self, ctx)

    @commands.command(name=projectsPossibleRequests[1])
    async def projetos(self,ctx):
        await projects(self, ctx)

    # =============== EACH PROJECT =============
    @commands.command(name="whatShouldIPlay")
    async def whatShouldIPlay(self,ctx):
        await projectModel(self, ctx,"📱 whatShouldIPlay", "https://github.com/RenatoCesarF/what_should_i_play")

    @commands.command(name="thisbot")
    async def thisbot(self,ctx):
        await projectModel(self, ctx,"🤖 ThisBot"," https://github.com/RenatoCesarF/twitchBot")
    
    @commands.command(name="soundBoard")
    async def soundBoard(self,ctx):
        await projectModel(self, ctx,"🔊 SoundBoard","https://github.com/RenatoCesarF/Soundboard")
    
    @commands.command(name="overlay")
    async def soundBoard(self,ctx):
        await projectModel(self, ctx,"🖥️ StreamOverlay","https://github.com/RenatoCesarF/StreamOverlay")
  


bot = Bot()
print("\nIT'S ALIVE!!!!\n")
bot.run()