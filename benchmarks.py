from PIL import Image, ImageDraw, ImageFont


def benchmarks(d: dict):
    bench = [d["gold_per_min"], d["xp_per_min"], d["kills_per_min"], d["last_hits_per_min"], d["hero_damage_per_min"],
             d["hero_healing_per_min"], d["tower_damage"], d["stuns_per_min"], d["lhten"]]

    names = ["GPM", "XPM", "Kills per min", "Lasthits per min", "Hero damage per min", "Hero healing per min",
             "Tower damage", "Stuns per min", "Lasthits per\nfirst 10 mins"]

    image = Image.open("images/black1920x1080.jpg")
    font = ImageFont.truetype("arial.ttf", 35)
    drawer = ImageDraw.Draw(image)
    drawer.text((400, 50), f"Ваш результат: ", font=font, fill="white")
    drawer.text((1100, 30), "Лучше, чем %\nот недавних показателей игроков\nна этом герое", font=font, fill="white")

    x = 150

    for i in range(9):
        drawer.text((100, x), f"{names[i]}", font=font, fill="white")
        drawer.text((500, x), f"{round((bench[i])['raw'], 2)}", font=font, fill="white")
        drawer.text((1100, x), f"{round((bench[i])['pct'] * 100, 2)}%", font=font, fill="white")
        x += 100

    return image.save("images/Benchmarksimg.jpg")
