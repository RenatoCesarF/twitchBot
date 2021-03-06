import utils as utils
import twitchio
from twitchio.ext import commands
import sys

from commands.commandsList import commandsList
from commands.mudaATela import ChangeScreen
from commands.projects import projects
from commands.euInfo import euInfo
from commands.socialMediaModel import socialMediaModel
from commands.projectModel import projectModel
from commands.socialMediaList import socialMediaList

commandsPossibleRequests = ['commands', 'comandos', 'help', 'bot']
projectsPossibleRequests = ['projects','projetos']

def main():
    bot = Bot()
    print("\nIT'S ALIVE!!!!")
    sys.stdout.flush()
    bot.run()

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(irc_token=envVars.ACCESS_TOKEN, client_id=envVars.CLIENT_ID, nick='renatocesarf', prefix='!', initial_channels=["#renatocesarf"])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        message.content = message.content.lower()
        await self.handle_commands(message)
  
    @commands.command(name='mudaatela')
    async def _mudaatela(self,ctx):
        await ChangeScreen(self, ctx)
    

    # =============== SOCIAL MEDIA STUFFS =============
    @commands.command(aliases=["social","socialmedia","redesocial"])
    async def _postSocialMediaList(self,ctx):
        await socialMediaList(self,ctx)

    @commands.command(name='github')
    async def _github(self,ctx):
        await socialMediaModel(self, ctx, "O Link pro meu Github é: https://github.com/RenatoCesarF Todos os nossos projetos estão lá 🐙")

    @commands.command(name= 'instagram')
    async def _instagram(self,ctx):
        await socialMediaModel(self, ctx,"Meu Instagram é: https://www.instagram.com/eu_renato_/ Segue lá 😎")
    
    @commands.command(aliases=['twitter','tt'])
    async def _twitter(self,ctx):
        await socialMediaModel(self, ctx,"Meu Twitter é: https://twitter.com/nerat0 Segue lá 🐦")
    
    @commands.command(name='youtube')
    async def _youtube(self,ctx):
        await socialMediaModel(self, ctx,"Meu canal é: https://www.youtube.com/channel/UCHPXJJhhkw1i7oAkq_Mcumw Se inscreve pra dar uma força 📼📽️ ")
        
   
    # =============== SHOW COMMANDS =============
    @commands.command(aliases=commandsPossibleRequests)
    async def _commands(self,ctx):
        await commandsList(self, ctx)

    # =============== SHOW PROJECTS =============
    @commands.command(aliases=projectsPossibleRequests)
    async def _project(self,ctx):
        await projects(self, ctx)

    # =============== EACH PROJECT =============
    @commands.command(name="whatshouldiplay")
    async def _whatShouldIPlay(self,ctx):
        await projectModel(self, ctx,"📱 whatShouldIPlay", "https://github.com/RenatoCesarF/what_should_i_play")

    @commands.command(name="tbot")
    async def _tbot(self,ctx):
        await projectModel(self, ctx,"🤖 ThisBot"," https://github.com/RenatoCesarF/twitchBot")
    
    @commands.command(name="soundboard")
    async def _soundBoard(self,ctx):
        await projectModel(self, ctx,"🔊 SoundBoard","https://github.com/RenatoCesarF/Soundboard")
    
    @commands.command(name="rings")
    async def _soundBoard(self,ctx):
        await projectModel(self, ctx,"🥏 Rings","https://github.com/RenatoCesarF/Rings")
    
    @commands.command(name="discordbot")
    async def _soundBoard(self,ctx):
        await projectModel(self, ctx,"🤖 DeltaBot","https://github.com/RenatoCesarF/Delta-Bot")
    
    @commands.command(aliases=["eu","renato","info"])
    async def _showAboutMeInformation(self,ctx):
        await euInfo(self,ctx)
   
    @commands.command(aliases=["picpay","pix"])
    async def _picpay(self,ctx):
        await ctx.send("Pra fazer Contribuições por Pix ou Picpay entre no meu site -> https://renatocesar.netlify.app/contributors")

    @commands.command(aliases=["doação","doacao","donate"])
    async def _doacao(self,ctx):
        await ctx.send("Você pode fazer uma colaboração atravez do link:  https://streamlabs.com/renatocesarf e entrar pra lista de colaboradores. Se prefirir pode usar o Pix -> !pix pra pegar o QRCode ou por -> !picpay ")

    @commands.command(name="discord")
    async def _discord(self, ctx):
        await ctx.send("Entre no nosso servidor Discord pra conversar, dar ideia e ficar por dentro 😉! https://discord.gg/q5THHP42w6")

    @commands.command(aliases=["linguagens","languages","programação","programacao"])
    async def _language(self, ctx):
        await ctx.send(" -> Python | -> Flutter | -> React-Js | -> C# |")


if __name__ == "__main__":
    envVars = utils.EnvVars()
    main()
