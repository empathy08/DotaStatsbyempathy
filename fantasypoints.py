from PIL import Image, ImageDraw, ImageFont


def fantasy(d: dict):
    headlines = ["KILLS", "DEATHS", "LASTHITS", "DENIES", "GPM", "TOWERS", "ROSHAN", "УЧАСТИЙ",
                 "ОБСОВ", "СТАКОВ", "RUNES", " ФБ", "STUNNED"]

    values = [
        d["kills"], d["deaths"], d["last_hits"], d["denies"], d["gold_per_min"], d["towers_killed"],
        d["roshans_killed"], round(d["teamfight_participation"], 2), d["obs_placed"], d["camps_stacked"],
        d["rune_pickups"], d["firstblood_claimed"], round(d["stuns"], 2)
    ]

    points = [
        round(d["kills"] * 0.3, 2), round(3 - (d["deaths"] * 0.3), 2), round(d["last_hits"] * 0.003, 2),
        round(d["denies"] * 0.003, 2), round(d["gold_per_min"] * 0.002, 2), round(d["towers_killed"], 2),
        round(d["roshans_killed"], 2), round(d["teamfight_participation"] * 3, 2), round(d["obs_placed"] * 0.5, 2),
        round(d["camps_stacked"] * 0.5, 2), round(d["rune_pickups"] * 0.25, 2), round(d["firstblood_claimed"] * 4, 2),
        round(d["stuns"] * 0.05, 2)
    ]

    image = Image.open("images/blue2560x1440.jpg")
    font = ImageFont.truetype("arial.ttf", 30)
    drawer = ImageDraw.Draw(image)

    x = 30

    for i in range(13):
        drawer.text((x, 500), f"{headlines[i]}", font=font, fill='black')
        drawer.text((x, 800), f"{values[i]}", font=font, fill='black')
        drawer.text((x, 1100), f"{points[i]}", font=font, fill='black')

        x += 185

    return image.save("images/Fantasypointsimg.jpg")
