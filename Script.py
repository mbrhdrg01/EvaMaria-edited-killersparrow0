class script(object):
    START_TXT = """𝑯𝒐𝒍𝒂 👋 {},
𝑴𝒚 𝒏𝒂𝒎𝒆 𝒊𝒔 <a href=https://t.me/{}>{}</a>, 𝑰 𝒄𝒂𝒏 𝒑𝒓𝒐𝒗𝒊𝒅𝒆 𝒎𝒐𝒗𝒊𝒆𝒔, 𝑱𝒖𝒔𝒕 𝒋𝒐𝒊𝒏 @movie_ott 𝒂𝒏𝒅 𝒄𝒉𝒊𝒍𝒍 😎🍿."""
    HELP_TXT = """𝑯𝒐𝒍𝒂 {}
𝑯𝒆𝒓𝒆 𝒊𝒔 𝒕𝒉𝒆  𝐇𝐞𝐥𝐩  𝒇𝒐𝒓 𝒎𝒚 𝒄𝒐𝒎𝒎𝒂𝒏𝒅."""
    ABOUT_TXT = """✯ 𝑴𝒚 𝑵𝒂𝒎𝒆: {}
✯ 𝑪𝒓𝒆𝒂𝒕𝒐𝒓: <a href=https://t.me/TeamEvamaria> 𝑻𝒆𝒂𝒎 𝑬𝒗𝒂 𝑴𝒂𝒓𝒊𝒂 </a>
✯ 𝑬𝒅𝒊𝒕𝒐𝒓 : <a href=https://t.me/elonmuskme> @ </a>
✯ 𝑳𝒊𝒃𝒓𝒂𝒓𝒚: <a href=https://docs.pyrogram.org/> 𝑷𝒚𝒓𝒐𝒈𝒓𝒂𝒎 </a>
✯ 𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆: <a href=https://www.python.org/> 𝑷𝒚𝒕𝒉𝒐𝒏 3</a>
✯ 𝑫𝒂𝒕𝒂 𝑩𝒂𝒔𝒆: <a href=http://mongodb.com> 𝑴𝒐𝒏𝒈𝒐 𝑫𝑩</a>
✯ 𝑩𝒐𝒕 𝑺𝒆𝒓𝒗𝒆𝒓: <a href=http://heroku.com> 𝑯𝒆𝒓𝒐𝒌𝒖 </a>
✯ 𝑩𝒖𝒊𝒍𝒅 𝑺𝒕𝒂𝒕𝒖𝒔: 𝒗1.0.1 [<a href=https://t.me/elonmuskme> 𝑪𝒖𝒔𝒕𝒐𝒎 𝒃𝒖𝒊𝒍𝒅 𝒐𝒇 @𝒆𝒍𝒐𝒏𝒎𝒖𝒔𝒌𝒎𝒆 </a> ]"""
    SOURCE_TXT = """<b>𝐍𝐎𝐓𝐄:</b>
- 𝑬𝒗𝒂 𝑴𝒂𝒓𝒊𝒂 𝒊𝒔 𝒂 𝒐𝒑𝒆𝒏 𝒔𝒐𝒖𝒓𝒄𝒆 𝒑𝒓𝒐𝒋𝒆𝒄𝒕. 
- 𝑺𝒐𝒖𝒓𝒄𝒆 - https://github.com/EvamariaTG/EvaMaria  
<b>𝐃𝐄𝐕𝐒:</b>
- <a href=https://t.me/TeamEvamaria>𝑻𝒆𝒂𝒎 𝑬𝒗𝒂 𝑴𝒂𝒓𝒊𝒂</a>
-𝑬𝒅𝒊𝒕𝒐𝒓: <a href=https://t.me/elonmuskme>𝒆𝒍𝒐𝒏𝒎𝒖𝒔𝒌𝒎𝒆</a>"""
    MANUELFILTER_TXT = """𝐇𝐞𝐥𝐩: <b>𝐅𝐢𝐥𝐭𝐞𝐫𝐬</b>
- 𝐅𝐢𝐥𝐭𝐞𝐫 𝐢𝐬 𝐭𝐡𝐞 𝐟𝐞𝐚𝐭𝐮𝐫𝐞 𝐰𝐞𝐫𝐞 𝐮𝐬𝐞𝐫𝐬 𝐜𝐚𝐧 𝐬𝐞𝐭 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐞𝐝 𝐫𝐞𝐩𝐥𝐢𝐞𝐬 𝐟𝐨𝐫 𝐚 𝐩𝐚𝐫𝐭𝐢𝐜𝐮𝐥𝐚𝐫 𝐤𝐞𝐲𝐰𝐨𝐫𝐝 𝐚𝐧𝐝 𝐄𝐯𝐚𝐌𝐚𝐫𝐢𝐚 𝐰𝐢𝐥𝐥 𝐫𝐞𝐬𝐩𝐨𝐧𝐝 𝐰𝐡𝐞𝐧𝐞𝐯𝐞𝐫 𝐚 𝐤𝐞𝐲𝐰𝐨𝐫𝐝 𝐢𝐬 𝐟𝐨𝐮𝐧𝐝 𝐭𝐡𝐞 𝐦𝐞𝐬𝐬𝐚𝐠𝐞
<b>𝐍𝐎𝐓𝐄:</b>
1. 𝐞𝐯𝐚 𝐦𝐚𝐫𝐢𝐚 𝐬𝐡𝐨𝐮𝐥𝐝 𝐡𝐚𝐯𝐞 𝐚𝐝𝐦𝐢𝐧 𝐩𝐫𝐢𝐯𝐢𝐥𝐥𝐚𝐠𝐞.
2. 𝐨𝐧𝐥𝐲 𝐚𝐝𝐦𝐢𝐧𝐬 𝐜𝐚𝐧 𝐚𝐝𝐝 𝐟𝐢𝐥𝐭𝐞𝐫𝐬 𝐢𝐧 𝐚 𝐜𝐡𝐚𝐭.
3. 𝐚𝐥𝐞𝐫𝐭 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝐡𝐚𝐯𝐞 𝐚 𝐥𝐢𝐦𝐢𝐭 𝐨𝐟 64 𝐜𝐡𝐚𝐫𝐚𝐜𝐭𝐞𝐫𝐬.
<b>𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:</b>

• /plus - <code>𝐚𝐝𝐝 𝐚 𝐟𝐢𝐥𝐭𝐞𝐫 𝐢𝐧 𝐜𝐡𝐚𝐭</code>
• /filter - <code>𝐚𝐝𝐝 𝐚 𝐟𝐢𝐥𝐭𝐞𝐫 𝐢𝐧 𝐜𝐡𝐚𝐭</code>
• /filters - <code>𝐥𝐢𝐬𝐭 𝐚𝐥𝐥 𝐭𝐡𝐞 𝐟𝐢𝐥𝐭𝐞𝐫𝐬 𝐨𝐟 𝐚 𝐜𝐡𝐚𝐭</code>
• /rem - <code>𝐝𝐞𝐥𝐞𝐭𝐞 𝐚 𝐬𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐟𝐢𝐥𝐭𝐞𝐫 𝐢𝐧 𝐜𝐡𝐚𝐭</code>
• /delall - <code>𝐝𝐞𝐥𝐞𝐭𝐞 𝐭𝐡𝐞 𝐰𝐡𝐨𝐥𝐞 𝐟𝐢𝐥𝐭𝐞𝐫𝐬 𝐢𝐧 𝐚 𝐜𝐡𝐚𝐭 (𝐜𝐡𝐚𝐭 𝐨𝐰𝐧𝐞𝐫 𝐨𝐧𝐥𝐲)</code>"""
    BUTTON_TXT = """𝐇𝐞𝐥𝐩: <b>𝐁𝐮𝐭𝐭𝐨𝐧𝐬</b>
- 𝑵𝒂𝒕𝒂𝒍𝒊𝒂 𝑫𝒚𝒆𝒓 🌸 𝑺𝒖𝒑𝒑𝒐𝒓𝒕𝒔 𝒃𝒐𝒕𝒉 𝒖𝒓𝒍 𝒂𝒏𝒅 𝒂𝒍𝒆𝒓𝒕 𝒊𝒏𝒍𝒊𝒏𝒆 𝒃𝒖𝒕𝒕𝒐𝒏𝒔.
<b>𝐍𝐎𝐓𝐄:</b>
1. 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝒘𝒊𝒍𝒍 𝒏𝒐𝒕 𝒂𝒍𝒍𝒐𝒘𝒔 𝒚𝒐𝒖 𝒕𝒐 𝒔𝒆𝒏𝒅 𝒃𝒖𝒕𝒕𝒐𝒏𝒔 𝒘𝒊𝒕𝒉𝒐𝒖𝒕 𝒂𝒏𝒚 𝒄𝒐𝒏𝒕𝒆𝒏𝒕, 𝒔𝒐 𝒄𝒐𝒏𝒕𝒆𝒏𝒕 𝒊𝒔 𝒎𝒂𝒏𝒅𝒂𝒕𝒐𝒓𝒚.
2. 𝑬𝒗𝒂 𝑴𝒂𝒓𝒊𝒂 𝒔𝒖𝒑𝒑𝒐𝒓𝒕𝒔 𝒃𝒖𝒕𝒕𝒐𝒏𝒔 𝒘𝒊𝒕𝒉 𝒂𝒏𝒚 𝒕𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝒎𝒆𝒅𝒊𝒂 𝒕𝒚𝒑𝒆.
3. 𝑩𝒖𝒕𝒕𝒐𝒏𝒔 𝒔𝒉𝒐𝒖𝒍𝒅 𝒃𝒆 𝒑𝒓𝒐𝒑𝒆𝒓𝒍𝒚 𝒑𝒂𝒓𝒔𝒆𝒅 𝒂𝒔 𝒎𝒂𝒓𝒌𝒅𝒐𝒘𝒏 𝒇𝒐𝒓𝒎𝒂𝒕.
<b>𝐔𝐑𝐋 𝐛𝐮𝐭𝐭𝐨𝐧𝐬:</b>
<code>[Button Text](url:https://t.me/elonmuskme)</code>
<b>Alert buttons:</b>
<code>[Button Text](alert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """𝐇𝐞𝐥𝐩: <b>𝐀𝐮𝐭𝐨 𝐅𝐢𝐥𝐭𝐞𝐫</b>
<b>𝐍𝐎𝐓𝐄:</b>
1. 𝑴𝒂𝒌𝒆 𝒎𝒆 𝒕𝒉𝒆 𝒂𝒅𝒎𝒊𝒏 𝒐𝒇 𝒚𝒐𝒖𝒓 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒊𝒇 𝒊𝒕'𝒔 𝒑𝒓𝒊𝒗𝒂𝒕𝒆.
2. 𝒎𝒂𝒌𝒆 𝒔𝒖𝒓𝒆 𝒕𝒉𝒂𝒕 𝒚𝒐𝒖𝒓 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒅𝒐𝒆𝒔 𝒏𝒐𝒕 𝒄𝒐𝒏𝒕𝒂𝒊𝒏𝒔 𝒄𝒂𝒎𝒓𝒊𝒑𝒔, 𝒑𝒐𝒓𝒏 𝒂𝒏𝒅 𝒇𝒂𝒌𝒆 𝒇𝒊𝒍𝒆𝒔.
3. 𝑭𝒐𝒓𝒘𝒂𝒓𝒅 𝒕𝒉𝒆 𝒍𝒂𝒔𝒕 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒕𝒐 𝒎𝒆 𝒘𝒊𝒕𝒉 𝒒𝒖𝒐𝒕𝒆𝒔.
 𝑰'𝒍𝒍 𝒂𝒅𝒅 𝒂𝒍𝒍 𝒕𝒉𝒆 𝒇𝒊𝒍𝒆𝒔 𝒊𝒏 𝒕𝒉𝒂𝒕 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒕𝒐 𝒎𝒚 𝒅𝒃."""
    CONNECTION_TXT = """𝐇𝐞𝐥𝐩: <b>𝐂𝐨𝐧𝐧𝐞𝐜𝐭𝐢𝐨𝐧𝐬</b>
- 𝑼𝒔𝒆𝒅 𝒕𝒐 𝒄𝒐𝒏𝒏𝒆𝒄𝒕 𝒃𝒐𝒕 𝒕𝒐 𝑷𝑴 𝒇𝒐𝒓 𝒎𝒂𝒏𝒂𝒈𝒊𝒏𝒈 𝒇𝒊𝒍𝒕𝒆𝒓𝒔 
- 𝒊𝒕 𝒉𝒆𝒍𝒑𝒔 𝒕𝒐 𝒂𝒗𝒐𝒊𝒅 𝒔𝒑𝒂𝒎𝒎𝒊𝒏𝒈 𝒊𝒏 𝒈𝒓𝒐𝒖𝒑𝒔.
<b>𝐍𝐎𝐓𝐄:</b>
1.𝑶𝒏𝒍𝒚 𝒂𝒅𝒎𝒊𝒏𝒔 𝒄𝒂𝒏 𝒂𝒅𝒅 𝒂 𝒄𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒐𝒏.
2. 𝑺𝒆𝒏𝒅 <code>/connect</code> 𝒇𝒐𝒓 𝒄𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝒎𝒆 𝒕𝒐 𝒖𝒓 𝑷𝑴
<b>𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:</b>
• /connect  - <code>𝒄𝒐𝒏𝒏𝒆𝒄𝒕 𝒂 𝒑𝒂𝒓𝒕𝒊𝒄𝒖𝒍𝒂𝒓 𝒄𝒉𝒂𝒕 𝒕𝒐 𝒚𝒐𝒖𝒓 𝑷𝑴</code>
• /disconnect  - <code>𝒅𝒊𝒔𝒄𝒐𝒏𝒏𝒆𝒄𝒕 𝒇𝒓𝒐𝒎 𝒂 𝒄𝒉𝒂𝒕</code>
• /connections - <code>𝒍𝒊𝒔𝒕 𝒂𝒍𝒍 𝒚𝒐𝒖𝒓 𝒄𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒐𝒏𝒔</code>"""
    EXTRAMOD_TXT = """𝐇𝐞𝐥𝐩: <b>𝐄𝐱𝐭𝐫𝐚 𝐌𝐨𝐝𝐮𝐥𝐞𝐬</b>
<b>𝐍𝐎𝐓𝐄:</b>
𝒕𝒉𝒆𝒔𝒆 𝒂𝒓𝒆 𝒕𝒉𝒆 𝒆𝒙𝒕𝒓𝒂 𝒇𝒆𝒂𝒕𝒖𝒓𝒆𝒔 𝒐𝒇 𝑵𝒂𝒕𝒂𝒍𝒊𝒂 𝑫𝒚𝒆𝒓 🌸
<b>𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:</b>
• /id - <code>𝒈𝒆𝒕 𝒊𝒅 𝒐𝒇 𝒂 𝒔𝒑𝒆𝒄𝒊𝒇𝒆𝒅 𝒖𝒔𝒆𝒓.</code>
• /info  - <code>𝒈𝒆𝒕 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 𝒂𝒃𝒐𝒖𝒕 𝒂 𝒖𝒔𝒆𝒓.</code>
• /imdb  - <code>𝒈𝒆𝒕 𝒕𝒉𝒆 𝒇𝒊𝒍𝒎 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 𝒇𝒓𝒐𝒎 𝑰𝑴𝑫𝒃 𝒔𝒐𝒖𝒓𝒄𝒆.</code>
• /search  - <code>𝒈𝒆𝒕 𝒕𝒉𝒆 𝒇𝒊𝒍𝒎 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 𝒇𝒓𝒐𝒎 𝒗𝒂𝒓𝒊𝒐𝒖𝒔 𝒔𝒐𝒖𝒓𝒄𝒆𝒔.</code>"""
    SONG_TXT ="""<b>𝐒𝐎𝐍𝐆 𝐌𝐎𝐃𝐔𝐋𝐄</b>

𝐒𝐨𝐧𝐠 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐦𝐨𝐝𝐮𝐥𝐞
🎈 𝐂𝐨𝐦𝐦𝐚𝐧𝐝

- /𝐬 [𝐒𝐨𝐧𝐠 𝐍𝐚𝐦𝐞] - 𝑻𝒐 𝒅𝒐𝒘𝒏𝒍𝒐𝒂𝒅 𝒔𝒐𝒏𝒈
- Eg:- /s lovely

𝐔𝐬𝐚𝐠𝐞
- 𝐰𝐨𝐫𝐤𝐢𝐧𝐠 𝐩𝐦 𝐚𝐧𝐝 𝐠𝐫𝐨𝐮𝐩𝐬"""
    ADMIN_TXT = """𝐇𝐞𝐥𝐩: <b>𝐀𝐝𝐦𝐢𝐧 𝐦𝐨𝐝𝐬</b>
            
<b>𝐍𝐎𝐓𝐄:</b>
𝑻𝒉𝒊𝒔 𝒎𝒐𝒅𝒖𝒍𝒆 𝒐𝒏𝒍𝒚 𝒘𝒐𝒓𝒌𝒔 𝒇𝒐𝒓 𝒎𝒚 𝒂𝒅𝒎𝒊𝒏𝒔, 𝒔𝒐 𝒅𝒐𝒏’𝒕 𝒘𝒂𝒔𝒕𝒆 𝒚𝒐𝒖𝒓 𝒕𝒊𝒎𝒆 😏
<b>𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:</b>
• /logs - <code>𝒕𝒐 𝒈𝒆𝒕 𝒕𝒉𝒆 𝒓𝒆𝒔𝒄𝒆𝒏𝒕 𝒆𝒓𝒓𝒐𝒓𝒔</code>
• /stats - <code>𝒕𝒐 𝒈𝒆𝒕 𝒔𝒕𝒂𝒕𝒖𝒔 𝒐𝒇 𝒇𝒊𝒍𝒆𝒔 𝒊𝒏 𝒅𝒃.</code>
• /users - <code>𝒕𝒐 𝒈𝒆𝒕 𝒍𝒊𝒔𝒕 𝒐𝒇 𝒎𝒚 𝒖𝒔𝒆𝒓𝒔 𝒂𝒏𝒅 𝒊𝒅𝒔.</code>
• /chats - <code>𝒕𝒐 𝒈𝒆𝒕 𝒍𝒊𝒔𝒕 𝒐𝒇 𝒕𝒉𝒆 𝒎𝒚 𝒄𝒉𝒂𝒕𝒔 𝒂𝒏𝒅 𝒊𝒅𝒔.</code>
• /leave  - <code>𝒕𝒐 𝒍𝒆𝒂𝒗𝒆 𝒇𝒓𝒐𝒎 𝒂 𝒄𝒉𝒂𝒕.</code>
• /disable  -  <code>𝒅𝒐 𝒅𝒊𝒔𝒂𝒃𝒍𝒆 𝒂 𝒄𝒉𝒂𝒕.</code>
• /ban  - <code>𝒕𝒐 𝒃𝒂𝒏 𝒂 𝒖𝒔𝒆𝒓.</code>
• /unban  - <code>𝒕𝒐 𝒖𝒏𝒃𝒂𝒏 𝒂 𝒖𝒔𝒆𝒓.</code>
• /channel - <code>𝒕𝒐 𝒈𝒆𝒕 𝒍𝒊𝒔𝒕 𝒐𝒇 𝒕𝒐𝒕𝒂𝒍 𝒄𝒐𝒏𝒏𝒆𝒄𝒕𝒆𝒅 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔</code>
• /broadcast - <code>𝒕𝒐 𝒃𝒓𝒐𝒂𝒅𝒄𝒂𝒔𝒕 𝒂 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒕𝒐 𝒂𝒍𝒍 𝒖𝒔𝒆𝒓𝒔</code>"""
    STATUS_TXT = """★ 📁𝑻𝒐𝒕𝒂𝒍 𝒇𝒊𝒍𝒆: <code>{}</code>
★ 👥𝑻𝒐𝒕𝒂𝒍 𝒖𝒔𝒆𝒓𝒔: <code>{}</code>
★ 💬𝑻𝒐𝒕𝒂𝒍 𝒄𝒉𝒂𝒕𝒔: <code>{}</code>
★ 📀𝑼𝒔𝒆𝒅 𝒔𝒕𝒐𝒓𝒂𝒈𝒆: <code>{}</code> 𝑴𝒊𝑩
★ 🆓𝑭𝒓𝒆𝒆 𝒔𝒕𝒐𝒓𝒂𝒈𝒆: <code>{}</code> 𝑴𝒊𝑩"""
    LOG_TEXT_G = """#𝑵𝒆𝒘𝑮𝒓𝒐𝒖𝒑
🏘 𝑮𝒓𝒐𝒖𝒑 = {}(<code>{}</code>)
👬🏻 𝑻𝒐𝒕𝒂𝒍 𝑴𝒆𝒎𝒃𝒆𝒓𝒔 = <code>{}</code>
👩🏻‍💼 𝑨𝒅𝒅𝒆𝒅 𝑩𝒚 - {}
"""
    LOG_TEXT_P = """#𝑵𝒆𝒘𝑼𝒔𝒆𝒓
🆔 𝑰𝑫 - <code>{}</code>
💁🏻‍♂️ 𝑼𝒔𝒆𝒓𝒏𝒂𝒎𝒆 - {}
"""
