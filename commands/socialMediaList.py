async def socialMediaList(self, ctx):
    allComands = ''
    ComandList = [
        "!github",
        "!youtube",
        "!insta",
        "!twitter",
        "!linkedin",
      
    ]

    for command in ComandList:
        allComands += " -> {} | ".format(command) 
        
    await ctx.send(allComands)
