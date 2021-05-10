import utils as utils
from twitchio.ext import commands
import twitchio

from commands.commandsList import commandsList
from commands.mudaATela import ChangeScreen
from commands.projects import projects
from commands.eu import euInfo
from commands.socialMediaModel import socialMediaModel
from commands.projectModel import projectModel
from commands.socialMediaList import socialMediaList

envVars = utils.EnvVars()

commandsPossibleRequests = ['commands', 'comandos', 'help', 'bot']
projectsPossibleRequests = ['projects','projetos']



def main():
    bot = Bot()
    print("\nIT'S ALIVE!!!!\n")
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
    async def mudaatela(self,ctx):
        await ChangeScreen(self, ctx)
    
    # =============== SOCIAL MEDIA STUFFS =============
    @commands.command(aliases=["social","socialmedia","redesocial"])
    async def postSocialMediaList(self,ctx):
        await socialMediaList(self,ctx)

    @commands.command(name='github')
    async def github(self,ctx):
        await socialMediaModel(self, ctx, "O Link pro meu Github é: https://github.com/RenatoCesarF Todos os nossos projetos estão lá 🐙")

    @commands.command(name= 'instagram')
    async def insta(self,ctx):
        await socialMediaModel(self, ctx,"Meu Instagram é: https://www.instagram.com/eu_renato_/ Segue lá 😎")
    
    @commands.command(aliases=['twitter','tt'])
    async def ctwitter(self,ctx):
        await socialMediaModel(self, ctx,"Meu Twitter é: https://twitter.com/nerat0 Segue lá 🐦")
    
    @commands.command(name='youtube')
    async def youtube(self,ctx):
        await socialMediaModel(self, ctx,"Meu canal é: https://www.youtube.com/channel/UCHPXJJhhkw1i7oAkq_Mcumw Se inscreve pra dar uma força 📼📽️ ")
        
    # =============== SHOW COMMANDS =============
    @commands.command(aliases=commandsPossibleRequests)
    async def Fcommands(self,ctx):
        await commandsList(self, ctx)

    # =============== SHOW PROJECTS =============
    @commands.command(aliases=projectsPossibleRequests)
    async def project(self,ctx):
        await projects(self, ctx)

    # =============== EACH PROJECT =============
    @commands.command(name="whatshouldiplay")
    async def whatShouldIPlay(self,ctx):
        await projectModel(self, ctx,"📱 whatShouldIPlay", "https://github.com/RenatoCesarF/what_should_i_play")

    @commands.command(name="tbot")
    async def thisbot(self,ctx):
        await projectModel(self, ctx,"🤖 ThisBot"," https://github.com/RenatoCesarF/twitchBot")
    
    @commands.command(name="soundboard")
    async def soundBoard(self,ctx):
        await projectModel(self, ctx,"🔊 SoundBoard","https://github.com/RenatoCesarF/Soundboard")
    
    @commands.command(name="overlay")
    async def soundBoard(self,ctx):
        await projectModel(self, ctx,"🖥️ StreamOverlay","https://github.com/RenatoCesarF/StreamOverlay")
    
    @commands.command(aliases=["eu","renato","info"])
    async def showAboutMeInformation(self,ctx):
        await euInfo(self,ctx)
   
    @commands.command(name="picpay")
    async def picpay(self,ctx):
        await ctx.send("Ainda estamos trabalhando nisso...")

    @commands.command(aliases=["doação","doacao","donate"])
    async def Cdoacao(self,ctx):
        await ctx.send("Você pode fazer uma colaboração atravez do link: https://streamelements.com/renatocesarf/tip e entrar pra lista de colaboradores. Se prefirir pode usar o Pix -> !pix pra pegar o QRCode ou por -> !picpay ")
      
    @commands.command(name="pix")
    async def pix(self,ctx):
        await ctx.send("Ainda estamos trabalhando nisso...")#TODO: página no meu site onde vai ter a lista de apoiadores, o QR Code do pix e o QR Code do picpay

if __name__ == "__main__":
    main()
