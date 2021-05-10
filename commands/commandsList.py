async def commandsList(self, ctx):
    allComands = ''
    ComandList = [
        "!mudaatela: pra quando eu esquecer de mudar a tela",
        "!projects: mostrar lista de projetos desenvolvidos na Stream",
        "!<nomeDoProjeto>: posta o repositório do projeto",
        "!bot !help !comandos: mostrar lista de comandos disponíveis",
        "!<nomeDaRedeSocial>: link pra rede social",
    ]

    for command in ComandList:
        allComands += " => 🔹 {} | ".format(command)

    await ctx.send(allComands)


"""
"!github: link pro meu Github",
"!instagram: link pro meu Instagram",
"!twitter: link pro meu Twitter",
"!youtube: link pro meu Youtube",
"""