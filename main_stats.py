from PIL import Image, ImageDraw, ImageFont


def hero_name(num: int) -> str:
    hero_dict = {
        1: "Antimage", 2: "Axe", 3: "Bane", 4: "Bloodseeker", 5: "Crystalmaiden", 6: "Drowranger", 7: "Earthshaker",
        8: "Juggernaut", 9: "Mirana", 10: "Morphling", 11: "Shadowfiend", 12: "Phantomlancer", 13: "Puck",
        14: "Pudge", 15: "Razor", 16: "Sandking", 17: "Stormspirit", 18: "Sven", 19: "Tiny", 20: "Vengefulspirit",
        21: "Windranger", 22: "Zeus", 23: "Kunkka", 25: "Lina", 31: "Lich", 26: "Lion", 27: "Shadowshaman",
        28: "Slardar", 29: "Tidehunter", 30: "Witchdoctor", 32: "Riki", 33: "Enigma", 34: "Tinker", 35: "Sniper",
        36: "Necrophos", 37: "Warlock", 38: "Beastmaster", 39: "Queenofpain", 40: "Venomancer", 41: "Facelessvoid",
        42: "Wraithking", 43: "Deathprophet", 44: "Phantomassassin", 45: "Pugna", 46: "Templarassassin",
        47: "Viper", 48: "Luna", 49: "Dragonknight", 50: "Dazzle", 51: "Clockwerk", 52: "Leshrac",
        53: "Natureprophet", 54: "Lifestealer", 55: "Darkseer", 56: "Clinkz", 57: "Omniknight", 58: "Enchantress",
        59: "Huskar", 60: "Nightstalker", 61: "Broodmother", 62: "Bountyhunter", 63: "Weaver", 64: "Jakiro",
        65: "Batrider", 66: "Chen", 67: "Spectre", 68: "Ancientapparition", 69: "Doom", 70: "Ursa",
        71: "Spiritbreaker",
        72: "Gyrocopter", 73: "Alchemist", 74: "Invoker", 75: "Silencer", 76: "Outworlddestroyer", 77: "Lycan",
        78: "Brewmaster", 79: "Shadowdemon", 80: "Lonedruid", 81: "Chaosknight", 82: "Meepo", 83: "Treantprotector",
        84: "Ogremagi", 85: "Undying", 86: "Rubick", 87: "Disruptor", 88: "Nyxassassin", 89: "Nagasiren",
        90: "Keeperofthelight", 91: "Io", 92: "Visage", 93: "Slark", 94: "Medusa", 95: "Trollwarlord",
        96: "Centaurwarrunner", 97: "Magnus", 98: "Timbersaw", 99: "Bristleback", 100: "Tusk", 101: "Skywrathmage",
        102: "Abaddon", 103: "Eldertitan", 104: "Legioncommander", 106: "Emberspirit", 107: "Earthspirit",
        109: "Terrorblade", 110: "Pheonix", 111: "Oracle", 105: "Techies", 112: "Winterwyvern", 113: "Arcwarden",
        138: "Muerta", 135: "Dawnbreaker", 123: "Hoodwink", 129: "Mars", 136: "Marci", 119: "Darkwillow",
        121: "Grimstroke", 114: "Monkeyking", 120: "Pangolier", 137: "Primalbeast", 128: "Snapfire", 108: "Underlord",
    }
    name = hero_dict[num]
    return name


def overview(arr: dict):

    win = arr['win']
    level = arr['level']
    kills = arr['kills']
    deaths = arr['deaths']
    assists = arr['assists']
    last_hits = arr['last_hits']
    denies = arr['denies']
    networth = arr['net_worth']
    gpm = arr['gold_per_min']
    xpm = arr['xp_per_min']
    hero_damage = arr['hero_damage']
    tower_damage = arr['tower_damage']
    healing = arr['hero_healing']
    if win == 1:
        image = Image.open("images/w-bg.jpg")
        drawer = ImageDraw.Draw(image)
    else:
        image = Image.open("images/l-bg.jpg")
        drawer = ImageDraw.Draw(image)

    drawer.text((320, 120), f"Уровень: {level}", font=("helvetica_bold.otf", 50), fill='black')
    drawer.text((320, 190), f"К/Д/А:{kills}/{deaths}/{assists}", font=("helvetica_bold.otf", 50), fill='black')
    drawer.text((100, 260), f"Крипов(Добито/Не отдано): {last_hits} / {denies}", font=("helvetica_bold.otf", 50), fill='black')
    drawer.text((320, 330), f"Нетворс: {networth}", font=("helvetica_bold.otf", 50), fill='black')
    drawer.text((250, 390), f"GPM/XPM: {gpm} / {xpm}", font=("helvetica_bold.otf", 50), fill='black')
    drawer.text((250, 460), f"Урона героям: {hero_damage}", font=("helvetica_bold.otf", 50), fill='black')
    drawer.text((240, 530), f"Урона строениям: {tower_damage}", font=("helvetica_bold.otf", 50), fill='black')
    drawer.text((340, 600), f"Лечения: {healing}", font=("helvetica_bold.otf", 50), fill='black')

    return image.save("images/mainstatsimg.jpg", format="JPEG")




