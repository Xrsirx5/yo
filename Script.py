class script(object):
    START_TXT = """đ·đŽđ»đŸ {},
đŒđą đđđđ , <a href='https://t.me/Don_movie_robot'>Don</a>, đžđ'đ đđđđą đđđđą đđđđ đđđ đđ đđ đąđđđ đđđđđ đđđ đđđđ đđ đđđđđ, đđđđđ đđđ đž'đđ đđđđđđđ đđđđđđ đđđđđ đ€
"""
    HELP_TXT = """đ·đŽđ {}
đđŠđłđŠ đđŽ đđ©đŠ đđŠđ­đ± đđ°đł đđș đđ°đźđźđąđŻđ„đŽ."""
    ABOUT_TXT = """
<b>đ§đđđŠ Don đđđąđšđ§ đ đŠđ</b>
â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
ââââââ° êȘá„êȘźêȘđœ êȘđŽá§ â±âââ±âÛȘÛȘ
ââ­ââââââââââââââââŁ 
ââŁâȘŒ đđ đđŒđđ - <a href="https://t.me/@Don_movie_robot"> Don </a>
ââŁâȘŒ đđČđ«đ»đȘđ»đ»đ - đżđđđŸđ¶đđ°đŒ
ââŁâȘŒ đđȘđ·đ°đŸđȘđ°đź - đżđđđ·đŸđœ đč
ââŁâȘŒ đđȘđœđȘ đđȘđŒđź - đŒđŸđœđ¶đŸ đłđ±
ââŁâȘŒ đđžđœ đŒđźđ»đżđźđ» -  đ·đŽđđŸđșđ
ââŁâȘŒ đđŸđČđ”đ­ đąđœđȘđœđŸđŒ - v1.0.1 [ đ±đŽđđ° ]
ââ°ââââââââââââââââŁ âââââââââââââââââââââ±âÛȘÛȘ"""
    SOURCE_TXT = """<b>NOTE:</b>
- đ° đđ  đ close đđđđđđ đđđđđđđ. 
- ŐOááááŽ áOáȘáŽ - <a href="https://t.me/+L2DhAQdRb9BmZWU1"> đđđđđ đđđ„đ </a>

đ đđŠđ§đđ„:
<a href="https://t.me/A6rzuxpt69drdr6t9d5"> đ»đŹđšđŽ đšđ”đ”đš </a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details

âą/whois :-give a user full details"""
    SONG_TXT ="""<b>SONG MODULE</b>
Song Download
Song Download Module, For Those Who Love Music

đ Command

- /song [Song Name] - To Download Music

Usage
- working pm and groups"""
    JSON_TXT ="""<b>JSON MODULE</b>
JSON:
Bot returns json for all replied messages with /json

Features:
Message Editting JSON
Pm Support
Group Support

Note:
Everyone can use this command , if spaming happens bot will automatically ban you from the group"""
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>đ Commands & Usage:</b>

â /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

â /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>đČ NOTHING MUCH JUST SOME FUN THINGS</b>
tđđ đđđđ đźđđ: 
đŁ. /dice - Roll The Dice 
đ€. /Throw đđ /Dart - đłđ đŹđșđđŸ Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and tessa will respond whenever a keyword is found the message

<b>NOTE:</b>
1. đšđđđ đđđ đđđđđđ đđđđ đđđđđ đđđđđđđđđđ.
2. đ¶đđđ đđđđđđ đđđ đđđ đđđđđđđ đđ đ đđđđ.
3. đšđđđđ đđđđđđđ đđđđ đ đđđđđ đđ 64 đđđđđđđđđđ.

<b>Commands and Usage:</b>
âą /filter - <code>add a filter in chat</code>
âą /filters - <code>list all the filters of a chat</code>
âą /del - <code>delete a specific filter in chat</code>
âą /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Anna ben Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ANNA BEN supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https//t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains cam rip, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âą /connect  - <code>connect a particular chat to your PM</code>
âą /disconnect  - <code>disconnect from a chat</code>
âą /connections - <code>list all your connections</code>"""
    IMBD_TXT ="""<b>NOTE:</b>

âą /imdb  - <code>get the film information from IMDb source.</code>
âą /search  - <code>get the film information from various sources.</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of anna ben

<b>Commands and Usage:</b>
âą /id - <code>get id of a specifed user.</code>
âą /info  - <code>get information about a user.</code>
"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âą /logs - <code>to get the rescent errors</code>
âą /stats - <code>to get status of files in db.</code>
âą /users - <code>to get list of my users and ids.</code>
âą /chats - <code>to get list of the my chats and ids </code>
âą /leave  - <code>to leave from a chat.</code>
âą /disable  -  <code>do disable a chat.</code>
âą /ban  - <code>to ban a user.</code>
âą /unban  - <code>to unban a user.</code>
âą /channel - <code>to get list of total connected channels</code>
âą /broadcast - <code>to broadcast a message to all users</code>"""
    FILTER_TXT = """đđđđđđ đ đđđđđđ đđđđ đđđđđ
â đđđđ đ°đąđ­đĄ @A6rzuxpt69drdr6t9d5"""
    STATUS_TXT = """âȘ đ»đđđđ đđđđđ: <code>{}</code>
âȘ đ»đđđđ đŒđđđđ: <code>{}</code>
âȘ đ»đđđđ đȘđđđđ: <code>{}</code>
âȘ đŒđđđ đșđđđđđđ: <code>{}</code> đŒđđ±
âȘ đ­đđđ đșđđđđđđ: <code>{}</code> đŒđđ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
