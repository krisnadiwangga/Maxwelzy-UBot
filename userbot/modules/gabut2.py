from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.Kyy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Kyy`")
    sleep(3)
    await typew.edit("`19 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Batam, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU π`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": "πΎπ€π’π’ππ£π: `kyy`\
    \nβ³ : perkenalan Kyy\
    \n\nπΎπ€π’π’ππ£π: `.sayang`\
    \nβ³ : Gombalan maut`\
    \n\nπΎπ€π’π’ππ£π: `.semangat`\
    \nβ³ : Jan Lupa Semangat."
})
