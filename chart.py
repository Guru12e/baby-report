from PIL import Image, ImageDraw, ImageFont
import math
import random

signs = [
        ("Aries", 0, 30),
        ("Taurus", 30, 60),
        ("Gemini", 60, 90),
        ("Cancer", 90, 120),
        ("Leo", 120, 150),
        ("Virgo", 150, 180),
        ("Libra", 180, 210),
        ("Scorpio", 210, 240),
        ("Sagittarius", 240, 270),
        ("Capricorn", 270, 300),
        ("Aquarius", 300, 330),
        ("Pisces", 330, 360),
]

sign_degree = {
    "Aries": 30,
    "Taurus":60,
    "Gemini":90,
    "Cancer":120,
    "Leo":150,
    "Virgo":180,
    "Libra":210,
    "Scorpio": 240,
    "Sagittarius":270,
    "Capricorn":300,
    "Aquarius":330,
    "Pisces":360,
}

def find_planets(planets):
    navamsa_sign= {
        "Aries":["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"],
        "Taurus":["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo"],
        "Gemini":["Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini"],
        "Cancer":["Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
        "Leo":["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"],
        "Virgo":["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo"],
        "Libra":["Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini"],
        "Scorpio":["Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
        "Sagittarius":[	"Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"],
        "Capricorn":["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo"],
        "Aquarius":["Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini"],
        "Pisces":["Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"],
    }
    
    navamsa_planets = []
                        
    for planet in planets:
        for label,start,stop in signs:
            if start < planet["full_degree"] <= stop:
                norm = abs(planet["full_degree"] - start)
                second = norm * 60
                navamsa = round(second / 200) - 1
                if navamsa < 0:
                    navamsa = 0
                degree = sign_degree[navamsa_sign[label][navamsa]] - 5
                navamsa_planets.append({"Name":planet["Name"], "full_degree": degree})

            
    return planets,navamsa_planets



def draw_birth_chart(positions, filename, path, name="", dob="", location=""):
    try:
        background_image = Image.open(f'{path}/static/image.png')
        canvas_size = background_image.size 
    except IOError: 
        canvas_size = (800, 800)
        background_image = Image.new('RGB', canvas_size, 'white')
        
    try:
        om_image = Image.open(f'{path}/static/om.png')
        om_image = om_image.resize((50, 50))
    except IOError: 
        print("failed")

    image = Image.new('RGB', canvas_size)
    image.paste(background_image, (0, 0))

    draw = ImageDraw.Draw(image)

    blue = (3, 4, 94)
    black = (0, 0, 0)

    large_square_size = canvas_size[0]
    small_square_size = large_square_size / 4

    large_square_offset = (canvas_size[0] - large_square_size) / 2

    try:
        font_path = f"{path}/static/Linotte-SemiBold.otf"
        font = ImageFont.truetype(font_path, 30)
    except IOError:
        font = ImageFont.load_default()

    center_x = canvas_size[0] // 2
    center_y = canvas_size[1] // 2
    
    if om_image:
        om_position = (center_x - 25,center_y - 120)  
        image.paste(om_image, om_position, om_image)

    name_font = ImageFont.truetype(font_path, 38) if font_path else ImageFont.load_default()
    draw.text((center_x, center_y - 40), name, fill=black, font=name_font, anchor="mm")

    dob_font = ImageFont.truetype(font_path, 32) if font_path else ImageFont.load_default()
    draw.text((center_x, center_y), f"{dob}", fill=black, font=dob_font, anchor="mm")
    draw.text((center_x, center_y + 40), f"{location}", fill=black, font=dob_font, anchor="mm")

    small_squares = [
        {'x': large_square_offset, 'y': large_square_offset},
        {'x': large_square_offset + small_square_size, 'y': large_square_offset},
        {'x': large_square_offset + 2 * small_square_size, 'y': large_square_offset},
        {'x': large_square_offset + 3 * small_square_size, 'y': large_square_offset},
        {'x': large_square_offset + 3 * small_square_size, 'y': large_square_offset + small_square_size},
        {'x': large_square_offset + 3 * small_square_size, 'y': large_square_offset + 2 * small_square_size},
        {'x': large_square_offset + 3 * small_square_size, 'y': large_square_offset + 3 * small_square_size},
        {'x': large_square_offset + 2 * small_square_size, 'y': large_square_offset + 3 * small_square_size},
        {'x': large_square_offset + small_square_size, 'y': large_square_offset + 3 * small_square_size},
        {'x': large_square_offset, 'y': large_square_offset + 3 * small_square_size},
        {'x': large_square_offset, 'y': large_square_offset + 2 * small_square_size},
        {'x': large_square_offset, 'y': large_square_offset + small_square_size},
    ]

    rashi_labels = [
        "Pisces", "Aries", "Taurus", "Gemini", 
        "Cancer", "Leo", "Virgo", "Libra", 
        "Scorpio", "Sagittarius", "Capricorn", "Aquarius"
    ]

    zodiac_boundaries = {
        "Pisces": (330, 360),
        "Aries": (0, 30),
        "Taurus": (30, 60),
        "Gemini": (60, 90),
        "Cancer": (90, 120),
        "Leo": (120, 150),
        "Virgo": (150, 180),
        "Libra": (180, 210),
        "Scorpio": (210, 240),
        "Sagittarius": (240, 270),
        "Capricorn": (270, 300),
        "Aquarius": (300, 330)
    }

    if positions:
        planets_in_cells = {i: [] for i in range(len(small_squares))}

        for planet in positions:
            planet_name = planet["Name"]
            planet_degree = planet["full_degree"]

            for label, (start_deg, end_deg) in zodiac_boundaries.items():
                if start_deg <= planet_degree < end_deg:
                    cell_index = rashi_labels.index(label)
                    if planet_name == "Ascendant":
                        planets_in_cells[cell_index].append(("Asc", planet_degree))
                    else:
                        planets_in_cells[cell_index].append((planet_name, planet_degree))
                    break

        for index, planets in planets_in_cells.items():
            cell_pos = small_squares[index]
            cell_center_x = cell_pos['x'] + small_square_size / 2
            cell_center_y = cell_pos['y'] + small_square_size / 2

            num_planets = len(planets)
            if num_planets > 1:
                radius = small_square_size * 0.3
                angle_step = 2 * math.pi / num_planets
                for i, (planet_name, _) in enumerate(planets):
                    angle = i * angle_step
                    x_offset = radius * math.cos(angle)
                    y_offset = radius * math.sin(angle)
                    draw.text(
                        (cell_center_x + x_offset, cell_center_y + y_offset + 20), 
                        planet_name, 
                        fill=blue, 
                        font=font, 
                        anchor="mm"
                    )
            else:
                if planets:
                    planet_name = planets[0][0]
                    draw.text(
                        (cell_center_x, cell_center_y + 20), 
                        planet_name, 
                        fill=blue, 
                        font=font, 
                        anchor="mm"
                    )
                    

    image.save(filename)

def generate_birth_navamsa_chart(planets, path, dob, location, name= ""):
    positions, navamsa = find_planets(planets)
    number = random.randrange(1, 100000000)
    number2 = random.randrange(1, 10000000)

    draw_birth_chart(positions, f'{path}/{number2}.png', path, name, dob, location)
    draw_birth_chart(navamsa, f'{path}/{number}.png', path, name, dob, location)

    return {"birth_chart": f"{number2}.png", "navamsa_chart": f"{number}.png"}