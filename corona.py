from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=".corona", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 14)

    

    animation_chars = [

            "`Calling china for a serious meeting...`",
            "`Getting a kid`",    
            "`Driving to airport`",
            "`Starting Plane..`",
            "`Sending Chinese Kid to you...0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Sending Chinese Kid to you...20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Sending Chinese Kid to you...52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Sending Chinese Kid to you...84%\n█████████████████████▒▒▒▒ `",
            "`Sending Chinese Kid to you...100%\n████████████████████ `",
            "`Plane over the Target`",
            "`Dropping Kid`",
            "`Kid is falling...`",    
            "`Kid landed on your Head`",
            "`You have Corona Virus now` \n\n`Pay $6969 To `ɦεαrt hαckєr💞💖` To get healed`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 14])
