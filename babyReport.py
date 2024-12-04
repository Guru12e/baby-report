import math
import random
import datetime
from math import atan2, cos, radians, sin
from fpdf import FPDF,YPos,XPos
from index import find_planets
from panchang import calculate_panchang
from chart import generate_birth_navamsa_chart
from datetime import datetime
from index import get_lat_lon
from babyContent import context,chakras,characteristics,dasa_status_table,table,karagan,exaltation,athmakaraka,ista_devata_desc,ista_devatas,saturn_pos,constitutionRatio,Constitution,elements_data,elements_content,gemstone_content,Gemstone_about,Planet_Gemstone_Desc,wealth_rudra,sign_mukhi,planet_quality,KaranaLord,thithiLord,yogamLord,nakshatraColor,nakshatraNumber,atma_names,thithiContent,karanamContent
from dasa import calculate_dasa
from dasaPrompt import dasaPrompt
from panchangPrompt import panchangPrompt
from chapter1 import physical
from health import healthPrompt
from chapter2 import chapterPrompt
from planetPrompt import PlanetPrompt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

nakshatras = [
    "Ashwini",
    "Bharani",
    "Krittika", 
    "Rohini", 
    "Mrigashira", 
    "Ardra",
    "Punarvasu", 
    "Pushya",
    "Ashlesha",
    "Magha", 
    "Purva Phalguni", 
    "Uttara Phalguni",
    "Hasta", 
    "Chitra", 
    "Swati", 
    "Vishakha", 
    "Anuradha", 
    "Jyeshtha", 
    "Mula",
    "Purva Ashadha", 
    "Uttara Ashadha",
    "Shravana",
    "Dhanishta",
    "Shatabhisha", 
    "Purva Bhadrapada", 
    "Uttara Bhadrapada",
    "Revati", 
]

number = {
    1: "First",
    2: "Second",
    3: "Third",
    4: "Fourth",
    5: "Fifth",
    6: "Sixth",
    7: "Seventh",
    8: "Eighth",
    9: "Ninth",
    10: "Tenth",
    11: "Eleventh",
    12: "Twelfth"
}

favourableDasa = ""

zodiac =  ["Aries","Taurus" ,"Gemini","Cancer","Leo","Virgo","Libra" ,"Scorpio" ,"Sagittarius" ,"Capricorn","Aquarius","Pisces"]

zodiac_lord = ["Mars","Venus","Mercury","Moon","Sun","Mercury","Venus","Mars","Jupiter","Saturn", "Saturn","Jupiter"]

def draw_gradient(pdf, x, y, w, h, start_color, end_color, steps=100):
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    for i in range(steps):
        r = r1 + (r2 - r1) * i / steps
        g = g1 + (g2 - g1) * i / steps
        b = b1 + (b2 - b1) * i / steps
        
        pdf.set_fill_color(int(r), int(g), int(b))
        
        pdf.rect(x, y + i * (h / steps), w, h / steps, 'F')

def draw_arrow(pdf, x_start, y_start, x_end, y_end, arrow_size=3):
    pdf.set_line_width(0.5)  
    pdf.line(x_start, y_start, x_end, y_end)  

    angle = radians(30)  
    line_angle = radians(90) if x_end == x_start else atan2(y_end - y_start, x_end - x_start)

    arrow_x1 = x_end - arrow_size * cos(line_angle - angle)
    arrow_y1 = y_end - arrow_size * sin(line_angle - angle)
    arrow_x2 = x_end - arrow_size * cos(line_angle + angle)
    arrow_y2 = y_end - arrow_size * sin(line_angle + angle)

    pdf.line(x_end, y_end, arrow_x1, arrow_y1)
    pdf.line(x_end, y_end, arrow_x2, arrow_y2)

def get_next_sade_sati(saturn_pos, moon_sign):
    for pos in saturn_pos:
        if pos["Sign"] == moon_sign:
            start_date = datetime.strptime(pos["Start Date"], "%B %d, %Y")
            return pos if start_date > datetime.now() else None
    return None

def get_current_saturn_sign(saturn_pos):
    current_date = datetime.now()
    for pos in saturn_pos:
        start_date = datetime.strptime(pos["Start Date"], "%B %d, %Y")
        end_date = datetime.strptime(pos["End Date"], "%B %d, %Y")
        if start_date <= current_date <= end_date:
            return pos
    return None 

def tithiImage(num):
    if num == 30:
        return "newMoon.jpg"
    elif num == 1:
        return "fullMoon.jpg"
    elif num <= 15:
        return "waningMoon.png"
    else:
        return "waxingMoon.png"

months_dict = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sept",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

def roundedBoxBorder(pdf,color,borderColor,x,y,planet,sign,path):
    pdf.set_fill_color(*hex_to_rgb(color))
    pdf.set_draw_color(*hex_to_rgb(borderColor))
    pdf.rect(x,y,50,50,round_corners=True,corner_radius=10,style='FD')
    pdf.set_xy(x,y)
    pdf.set_font('Karma-Semi', '', 18)
    pdf.set_text_color(0,0,0)
    pdf.cell(50, 10, f"{planet}", align='C')
    pdf.image(f"{path}/babyImages/{sign}.png",x + 12.5,pdf.get_y() + 12.5,25,25)
    pdf.set_xy(x,pdf.get_y() + 40)
    pdf.cell(50, 10, f"{sign}", align='C')

def setTitle(k):
    if "_" not in k:
        return k.capitalize()
    else:
        return f"{k.split('_')[0].capitalize()} {k.split('_')[1].capitalize()}"


def findStatus(planet,lord,sign):
    if sign in exaltation[planet]:
        return "Exalte" if exaltation[planet].index(sign) == 0 else "Debilite"
    return "Friend" if lord in table[planet][0] else "Enemy" if lord in table[planet][1] else "Neutral"

def roundedBox(pdf,color,x,y,w,h,corner=5,status=True):
    pdf.set_fill_color(*hex_to_rgb(color))
    pdf.rect(x,y,w,h,round_corners=status,corner_radius=corner,style='F')
    
class PDF(FPDF):
    def footer(self):
        self.set_y(-15)  
        self.set_font('Karma-Regular', '', 12) 
        self.set_text_color(128, 128, 128) 
        self.cell(0, 10, f'{self.page_no()}', align='C')
        
    def AddPage(self,path,title=None):
        self.add_page()
        self.image(f"{path}/babyImages/border.png",0,0,self.w,self.h) 
        if title: 
            self.set_text_color(hex_to_rgb("#966A2F"))
            self.set_font('Karma-Heavy', '', 26)
            self.set_xy(20,25)
            self.multi_cell(self.w - 40, 13, f"{title}", align='C') 
            
    def ContentDesign(self,color,title,content,path):
        self.set_text_color(0,0,0)
        self.set_y(self.get_y() + 5)
        self.set_font('Karma-Semi', '', 16)
        if title != "":
            self.set_xy(22.5,self.get_y() + 5)
            roundedBox(self, color, 20 , self.get_y()  - 2.5, self.w - 40, (self.no_of_lines(title,self.w - 45) * 7) + 10, 4)
            self.multi_cell(self.w - 45, 7,title, align='C')
        if isinstance(content, str):
            self.set_font('Karma-Regular', '', 14)
            self.set_xy(22.5,self.get_y() + 2.5)
            self.lineBreak(f"        {content}",path,color)
        elif isinstance(content,dict):
            for k,v in content.items():
                self.set_font('Karma-Semi', '', 16)
                if k == "name" or k == "field":
                    self.set_y(self.get_y() + 10)
                    self.cell(0,0,f"{k.capitalize()} : {v}",align='C')
                else:
                    self.set_xy(22.5,self.get_y() + 10)
                    roundedBox(self, color, 20 , self.get_y()  - 2.5, self.w - 40, (self.no_of_lines(k,self.w - 45) * 7) + 10, 4)
                    self.multi_cell(self.w - 45, 7,k.capitalize(), align='C')
                    self.set_font('Karma-Regular', '', 14)
                    self.set_xy(22.5,self.get_y() + 2.5)
                    self.lineBreak(f"        {v}",path,color)
        else:
            for v1 in content:
                if isinstance(v1,str):
                    self.set_font('Karma-Regular', '', 14)
                    if (self.get_y() + (self.get_string_width(v1) / (self.w - 45)) * 7) >= 270:
                        self.AddPage(path)
                        self.set_y(20)
                    if content.index(v1) != len(content) - 1:
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40, (self.no_of_lines(f"      {v1}",self.w - 45) * 7) + 18, 0,status=False)
                    else:
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40, (self.no_of_lines(f"      {v1}",self.w - 45) * 7) + 13, 4)
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40, 10, 0,status=False)
                    
                    self.set_xy(22.5,self.get_y() + 10)
                    self.multi_cell(self.w - 45, 7, f"      {v1}", align='L')
                else:
                    self.set_font('Karma-Regular', '', 14)
                    if (self.get_y() + (self.get_string_width(v1['content']) / (self.w - 45)) * 7 + 8) >= 260:
                        self.AddPage(path)
                        self.set_y(20)
                    self.set_font('Karma-Semi', '', 16)
                    titleWidth = (self.no_of_lines(f"{v1['title']}",self.w - 45)) * 8
                    self.set_font('Karma-Regular', '', 14)
                    contentWidth = (self.no_of_lines(f"      {v1['content']}",self.w - 45) * 7)
                    if content.index(v1) != len(content) - 1:
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40,titleWidth + contentWidth + 13, 0,status=False)
                    else:
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40,titleWidth + contentWidth + 5, 4)
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40, 10, 0,status=False)
                    self.set_xy(22.5,self.get_y() + 2.5)
                    self.set_font('Karma-Semi', '', 16)
                    self.multi_cell(self.w - 45, 8, f"{v1['title']}", align='L')
                    
                    self.set_font('Karma-Regular', '', 14)
                    self.set_xy(22.5,self.get_y() + 2.5)
                    self.multi_cell(self.w - 45, 7, f"      {v1['content']}", align='L')
        self.set_y(self.get_y() + 5)

    def table(self, planet, x, y,path,colors):
        self.set_xy(x, y)  
        self.set_fill_color(hex_to_rgb(colors))
        self.set_xy(x,y)
        self.rect(x - 2.5,self.get_y(),65,39,style='F',round_corners=True,corner_radius=2)
        self.cell(60, 8, f"Planet : {planet['Name']}", align='C')
        
        self.set_xy(x, y + 8)  
        self.cell(60, 8, f"Nakshatra: {planet['nakshatra']}", align='C')
        
        self.set_xy(x, y + 16)  
        self.cell(60, 8, f"Pada: {planet['pada']}", align='C')
        
        self.set_xy(x, y + 24)  
        self.cell(60, 8, f"Karagan: {karagan[planet['Name']]}", align='C')
        
        if planet['Name'] == 'Ascendant':
            self.set_xy(x, y + 32)  
            self.cell(60, 8, f"Status: Ubayam", align='C')
        else:
            self.set_xy(x, y + 32)  
            self.cell(60, 8, f"Status: {findStatus(planet['Name'], planet['zodiac_lord'], planet['sign'])}", align='C')
            
        if planet['Name'] != "Ascendant":
            self.image(f"{path}/babyImages/{planet['Name']}.png",x - 10,y - 10,20,20)
        else:
            self.image(f"{path}/babyImages/{planet['sign']}.png",x - 10,y - 10,20,20)
            
    def setDasa(self, dasa, bhukthi, x, y,start,end,path):
        self.set_draw_color(hex_to_rgb("#A6494F"))
        self.set_xy(x,y)
        self.rect(x - 2.5,self.get_y() + 10,55,119,style='D',round_corners=True,corner_radius=2)
        self.set_font('Karma-Heavy', '', 16)
        self.image(f"{path}/babyImages/{dasa}.png",x + 5,self.get_y() + 12.5, 15,15)
        self.set_xy(self.get_x() + 15, self.get_y() + 12.5)
        self.cell(35, 7, f"{dasa}", align='C')
        self.set_font('Karma-Regular', '', 12)
        self.set_xy(self.get_x() - 35, self.get_y() + 7)
        self.cell(35,7, f"({start}-{end})Age",align='C')
        self.set_draw_color(*hex_to_rgb("#BF4229"))
        self.set_fill_color(*hex_to_rgb("#BF4229"))
        self.rect(x + 10,self.get_y() + 15,30,0.5,style='DF')
        self.set_font('Karma-Semi', '', 14)
        self.set_xy(x, self.get_y() + 17)
        self.cell(50,7,f"{months_dict[bhukthi[0]['start_month'] + 1]} {bhukthi[0]['start_year']}",align='C')
        self.set_xy(x, self.get_y() + 7)
        self.cell(50,7,f"{months_dict[bhukthi[-1]['end_month'] + 1]} {bhukthi[-1]['end_year']}",align='C')
        self.rect(x + 10,self.get_y() + 8,30,0.5,style='DF')
        self.set_font('Karma-Regular', '', 12)
        
        self.set_y(self.get_y() + 5)

        for i, b in enumerate(bhukthi):
            self.set_xy(x,self.get_y() + 8)
            
            time = datetime.now().year
            
            if b['bhukthi'] in dasa_status_table[dasa][0]:
                self.set_fill_color(*hex_to_rgb("#DAFFDC"))
                global favourableDasa
                if favourableDasa == "" and b['start_year'] > time:
                    favourableDasa = f"{b['start_year']} to {b['end_year']}"
            elif b['bhukthi'] in dasa_status_table[dasa][1]:
                self.set_fill_color(*hex_to_rgb("#FFDADA"))
            else:
                self.set_fill_color(*hex_to_rgb("#DAE7FF"))
            if i == len(bhukthi) - 1:
                self.rect(x - 2,self.get_y(),54,8,style='F',round_corners=True,corner_radius=1)
            else:
                self.rect(x - 2,self.get_y(),54,8,style='F')
            self.cell(30,8, f"{b['bhukthi']}",align='L')
            self.cell(20,8,f"upto {months_dict[b['end_month']]} {b['end_year']}",align='R')
            
    def lineBreak(self, content, path,color):
        cell_width = self.w - 45 
        line_height = 7
        max_y = self.h - 30  
        current_y = self.get_y()
        if (current_y + (self.get_string_width(content) / cell_width) * line_height) < 250:
            roundedBox(self, color, 20 , self.get_y() , self.w - 40, self.no_of_lines(f"        {content}",self.w - 45) * 7 + 7.5, 4)
            self.set_xy(22.5,self.get_y() + 2.5)
            self.multi_cell(cell_width,line_height,f"       {content}",align='L')
        else:
            content_lines = []
            words = content.split(" ")
            current_line = ""
            
            for word in words:
                if self.get_string_width(current_line + word + " ") <= cell_width - 2.5:
                    current_line += word + " "
                else:
                    content_lines.append(current_line.strip())
                    current_line = word + " "
            content_lines.append(current_line.strip())  

            for line in content_lines:
                if current_y + line_height >= max_y: 
                    self.AddPage(path)  
                    current_y = 25
                    
                if content_lines.index(line) == len(content_lines) - 1:
                    roundedBox(self,color,20,current_y,self.w - 40, line_height,20)
                else:
                    roundedBox(self,color,20,current_y,self.w - 40, line_height + 5,status=False)
                    
                self.set_xy(22.5 , current_y)
                self.multi_cell(cell_width , line_height, line, align='L')
                current_y = self.get_y()
                        
    def draw_bar(self, x, y, width, height, color):
        self.set_fill_color(*color)
        self.rect(x, y - height, width, height, style="F")

    def draw_bar_chart(self, x_start, y_base, bar_width, bar_spacing, data, colors, max_height, path):
        max_value = max(data.values())  

        x = x_start
        for i, (label, value) in enumerate(data.items()):
            bar_height = (value / max_value) * max_height  
            color = colors[i % len(colors)]
            self.set_xy(x, y_base)
            self.set_font('Karma-Heavy', '', 12)
            self.cell(bar_width, 10, label, align='C')
            self.draw_bar(x, y_base, bar_width, bar_height, hex_to_rgb(color))
            self.draw_labels(x, y_base - bar_height - 20, label, path)
            x += bar_width + bar_spacing  

    def draw_labels(self, x, y, label,path): 
        if label == "Vadha" or label == "Kapha" or label == "Pitta":
            self.image(f"{path}/babyImages/{label}.png",x - 10 / 2 , y,0,10)
        else:
            self.set_fill_color(hex_to_rgb("#FFE6CC"))
            self.circle(x + 20 / 2, y + 10 / 2, 8, style='F')
            self.image(f"{path}/babyImages/{label}.png",x + 10 / 2 , y,0,10)
                
    def no_of_lines(self,text, cell_width):
        words = text.split()
        current_line = ''
        lines = 0

        for word in words:
            test_line = current_line + word + ' '
            if self.get_string_width(test_line) <= cell_width - 5:
                current_line = test_line
            else:
                lines += 1
                current_line = word + ' '

        if current_line:
            lines += 1

        return lines
            
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in range(0, 6, 2))
        
def generateBabyReport(formatted_date,formatted_time,location,lat,lon,planets,panchang,dasa,birthchart,gender,path,year,month,name = None):
    pdf = PDF('P', 'mm', 'A4')
    
    pdf.set_auto_page_break(True)
    
    pdf.add_font('Karma-Heavy', '', f'{path}/fonts/Merienda-Bold.ttf')
    pdf.add_font('Karma-Semi', '', f'{path}/fonts/Merienda-Regular.ttf') 
    pdf.add_font('Karma-Regular', '', f'{path}/fonts/Linotte-Regular.otf')
    
    pdf.add_page()
    pdf.set_font('Karma-Semi', '', 36)
    pdf.set_text_color(0,0,0)
    pdf.image(f"{path}/babyImages/main.png", 0 , 0 , pdf.w , pdf.h)
    pdf.set_xy(30,180)
    pdf.multi_cell(pdf.w - 60, 15, f"{name}'s Astrology Report", align='C')
    pdf.set_y(260)
    pdf.set_font_size(22)
    pdf.cell(0,0,f"{formatted_date} {formatted_time}",align='C')
    pdf.set_y(pdf.get_y() + 10)
    pdf.cell(0,0,f"{location}",align='C')
    
    pdf.AddPage(path)
    pdf.set_font('Karma-Heavy', '', 42) 
    pdf.set_text_color(0,0,0)
    pdf.set_font_size(32)
    pdf.set_y(30)
    pdf.cell(0,10,"Contents",align='C') 
    pdf.set_y(45)
    for c in context:
        if pdf.get_y() + (pdf.get_string_width(c) / (pdf.w - 30))  >= 260:
            pdf.AddPage(path)
            pdf.set_y(30)
            
        pdf.set_font('Karma-Semi', '', 16)
        pdf.set_xy(30,pdf.get_y() + 5)
        pdf.multi_cell(pdf.w - 60,10,f"{context.index(c) + 1}. {c}",align='L') 
    
    pdf.AddPage(path)
    pdf.set_xy(50,(pdf.h / 2) - 15)
    pdf.set_font('Karma-Heavy', '', 36) 
    pdf.multi_cell(pdf.w - 100,15,f"{name}'s Astrology Details",align='C')
    pdf.AddPage(path)
    pdf.set_y(40)
    pdf.set_font('Karma-Heavy', '', 42) 
    pdf.set_text_color(hex_to_rgb("#E85D2B"))
    pdf.cell(0,0,"Basic Details",align='C')
    pdf.set_text_color(0,0,0)
    
    pdf.set_font('Karma-Regular', '', 22) 
    
    pdf.set_xy(20,60)
    pdf.set_font_size(16)
    asc = list(filter(lambda x: x['Name'] == 'Ascendant', planets))[0]
    ninthHouseLord = zodiac_lord[((zodiac.index(asc['sign']) + 9) % 12) - 1]
    signLord = list(filter(lambda x: x['Name'] == ninthHouseLord,planets))[0]

    isthadevathaLord = list(filter(lambda x: x['Name'] == signLord['Name'],planets))[0]['nakshatra_lord']
    
    isthaDeva = ista_devatas[isthadevathaLord]
    
    atma = list(filter(lambda x: x['order'] == 1,planets))[0]
    if atma['Name'] == "Ascendant":
        atma = list(filter(lambda x: x['order'] == 2,planets))[0]
        
    moon = list(filter(lambda x : x['Name'] == "Moon",planets))[0]
        
    nakshatrasOrder = nakshatras[nakshatras.index(moon['nakshatra']):] + zodiac[:nakshatras.index(moon['nakshatra'])]
    favourableNakshatra = ""
    for index,nakshatra in enumerate(nakshatrasOrder):
        if index % 9 == 1:
            favourableNakshatra += f"{nakshatra}, "
            
    luckyNumber = nakshatraNumber[panchang['nakshatra']]
    
    left_column_text = [
        'Name :',
        'Date Of Birth :',
        'Time Of Birth :',
        'Place Of Birth :',
        'Birth Nakshatra, Lord :',
        'Birth Rasi, Lord :',
        'Birth Lagnam, Lord :',
        'Tithi :',
        'Nithya Yogam :',
        'Karanam :',
        'Birth Week Day :',
        'Atma Karagam, Lord : ',
        'Ishta Devata :',
        'Benefic Stars :',
        'Benefic Number :'
    ]

    right_column_text = [
        f"{name}",
        f"{formatted_date}",
        f"{formatted_time}",
        f"{location}",
        f"{panchang['nakshatra']}, {planets[2]['nakshatra_lord']}",
        f"{planets[2]['sign']}, {planets[2]['zodiac_lord']}",
        f"{planets[0]['sign']}, {planets[0]['zodiac_lord']}",
        f"{panchang['thithi']}",
        f"{panchang['yoga']}",
        f"{panchang['karanam']}",
        f"{panchang['week_day']}",
        f"{atma['Name']},{atma_names[atma['Name']]}",
        f"{isthaDeva[0]}",
        f"{favourableNakshatra}",
        f"{luckyNumber[0]},{luckyNumber[1]}"
    ]

    x_start = 30
    y_start = pdf.get_y() + 10
    pdf.set_xy(x_start, y_start)

    for index,row in enumerate(left_column_text):
        pdf.set_font('Karma-Semi', '', 14)
        pdf.cell(65, 10, row, new_x=XPos.RIGHT, new_y=YPos.TOP,align='R')
        y_start = pdf.get_y()
        pdf.set_font('Karma-Regular', '', 14)
        pdf.multi_cell(100, 10, right_column_text[index],align='L')
        y_start = pdf.get_y()
        pdf.set_xy(x_start, y_start)
    
    name = name.split(" ")[0]
    
    pdf.AddPage(path)
    pdf.set_font('Karma-Heavy', '', 26)  
    pdf.set_y(30)
    pdf.cell(0,0,'Birth Chart',align='C')
    # pdf.image(f"{path}/chart/{birthchart['birth_chart']}",(pdf.w / 2) - 45,pdf.get_y() + 10,90,90)
    pdf.image(f'{path}/chart/1.png',(pdf.w / 2) - 45,pdf.get_y() + 10,90,90)
    pdf.set_y(145)
    pdf.cell(0,0,'Navamsa Chart',align='C')
    # pdf.image(f"{path}/chart/{birthchart['navamsa_chart']}",(pdf.w / 2) - 45,pdf.get_y() + 10,90,90)
    pdf.image(f'{path}/chart/1.png',(pdf.w / 2) - 45,pdf.get_y() + 10,90,90)
    pdf.set_y(pdf.get_y() + 110)

    pdf.set_font('Karma-Regular', '', 18) 
    for b in dasa[planets[1]['nakshatra_lord']]:
        if (b['start_year'] <= year <= b['end_year']):
            if not (year == b['end_year'] and b['end_month'] >= month):
                pdf.cell(0,0,f"Dasa : {planets[2]['nakshatra_lord']} Bhukthi : {b['bhukthi']}",align='C')
                break
        
    pdf.AddPage(path)
    pdf.set_font('Karma-Heavy', '', 22)
    pdf.set_y(20)
    pdf.cell(0,0,f"{name}'s Life Journey",align='C') 
    
    i = 0
    
    for d,b in dasa.items():
        if i == 0:
            x = 20
            y = 20
        if i == 1:
            x = 80
            y = 20
        if i == 2:
            x = 140
            y = 20
            
        if i == 3:
            x = 20
            y = 145
            
        if i == 4:
            x = 80
            y = 145
            
        if i == 5:
            x = 140
            y = 145
            
        if i == 6:
            pdf.AddPage(path)
            x = 20
            y = 15
        
        if i == 7:
            x = 80
            y = 15
        
        if i == 8:
            x = 140
            y = 15
        
        if i == 0:
            start_age = 0
            end_age =  int(b[-1]['end_year']) - year
        else:
            start_age =  int(b[0]['end_year']) - year
            end_age =  int(b[-1]['end_year']) - year 
        i = i + 1
        pdf.setDasa(d,b,x,y,start_age,end_age,path)
        
    data = {
        "Favourable": "#DAFFDC",
        "Unfavourable": "#FFDADA",
        "Moderate": "#DAE7FF"
    }
        
    pdf.set_font('Karma-Heavy', '', 22)
    pdf.set_xy(22.5,pdf.get_y() + 20)
    pdf.cell(pdf.w - 45,0,f"Note:",align='L')
    for i,(label,value) in enumerate(data.items()):
        pdf.set_y(pdf.get_y() + 20)
        pdf.set_fill_color(*hex_to_rgb(value))
        pdf.rect(40,pdf.get_y() - 6,8,8,round_corners=True,corner_radius=5,style='F')
        pdf.set_font('Karma-Semi', '', 16)
        pdf.set_text_color(0,0,0)
        pdf.text(55,pdf.get_y(),f'{label}')
        
    pdf.AddPage(path,f"{name}'s Pancha Tava")
    roundedBox(pdf,"#FFF2D7",20,40,pdf.w - 40,27)
    pdf.set_xy(23.5,40)
    pdf.set_font('Karma-Regular', '', 16) 
    pdf.set_text_color(0,0,0)
    pdf.multi_cell(pdf.w - 45,8,f"       {name}'s birth chart reveals which of the five universal elements - fire, earth, air, water, and ether - shapes you the most. Knowing this can guide your life's purpose and selfunderstanding.",align='L')
    
    elements = {
        "Fire": 0,
        "Earth": 0,
        "Air": 0,
        "Water" : 0 
    }
    
    for pla in planets:
        for d,k in elements.items():
            if pla['Name'] == "Ascendant" or pla['Name'] == "Rahu" or pla['Name'] == "Ketu":
                continue
            if pla['sign'] in elements_data[d]:
                elements[d] = elements[d] + 1 
    for d,k in elements.items():
        elements[d] = (elements[d] / 7) * 100
        
    colors = [
        "#FF0000",
        "#43A458",
        "#B1DC36",
        "#4399FF"
    ]

    x_start = 20
    y_base = 150
    bar_width = 20
    bar_spacing = 10
    max_height = 50

    pdf.draw_bar_chart(x_start, y_base, bar_width, bar_spacing, elements, colors, max_height, path)
    
    y = 82.5
    for i,(label,value) in enumerate(elements.items()):
        pdf.set_font('Karma-Semi', '', 18)
        pdf.set_text_color(*hex_to_rgb(colors[i]))
        pdf.text(150,y,f'{label}: {value:.2f}%')
        y += 20
        
    el = elements
        
    max_key1 = max(elements, key=elements.get)

    del el[max_key1]

    max_key2 = max(el, key=elements.get)
    
    pdf.set_text_color(hex_to_rgb("#04650D"))
    pdf.set_fill_color(hex_to_rgb("#BAF596"))
    pdf.set_draw_color(hex_to_rgb("#06FF4C"))
    pdf.rect(22.5,160,pdf.w - 45,15,round_corners=True,corner_radius=5,style='DF')
    pdf.set_y(160)
    pdf.set_font_size(14)
    pdf.cell(0,15,f"{name}'s Dominant Element are {max_key1} and {max_key2}",align='C') 
    content = elements_content[max_key1][max_key2][0] 
    pdf.set_text_color(0,0,0)
    pdf.set_font('Karma-Regular', '', 14)
    roundedBox(pdf,"#FFE7E7",20,180,pdf.w - 40,(pdf.no_of_lines(content,pdf.w - 45) * 7) + 2.5)
    pdf.set_xy(22.5,182.5)
    pdf.multi_cell(pdf.w - 45,7,f"      {content}")
    
    pdf.AddPage(path,f"{name}'s  Ayurvedic Body Type")
    roundedBox(pdf,"#D7ECFF",20,pdf.get_y() + 9,pdf.w - 40,65)
    pdf.set_xy(22.5,pdf.get_y() + 10)
    pdf.set_font('Karma-Regular', '', 16) 
    pdf.set_text_color(0,0,0)
    pdf.multi_cell(pdf.w - 45,8,"       Acccording to ayurveda, On the basis of Vata,Pitta and Kapha, each child's body is of Vata Dominant and some of Pitta dominant. This is on the basis of the excess of dosha inside the body , its nature is determined.Here,We have tried to determine the ayurvedic nature on astrological basis. However this is no substitute for professional medical or ayurvedic advice. Please go only to an authorized doctor for any health-related treatment or Consultation.",align='L')
    
    lagna = list(filter(lambda x : x['Name'] == "Ascendant",planets))[0]

    data = {
    "Pitta": (int(constitutionRatio[moon['zodiac_lord']]['Pitta']) + int(constitutionRatio[lagna['zodiac_lord']]['Pitta'])) / 200 * 100,
    "Kapha": (int(constitutionRatio[moon['zodiac_lord']]['Kapha']) + int(constitutionRatio[lagna['zodiac_lord']]['Kapha'])) / 200 * 100,
    "Vadha": (int(constitutionRatio[moon['zodiac_lord']]['Vata']) + int(constitutionRatio[lagna['zodiac_lord']]['Vata'])) / 200 * 100,
    }
    
    colors = [
        "#E34B4B",   
        "#43C316",   
        "#4BDAE3"    
    ]

    x_start = 30
    y_base = 190
    bar_width = 20
    bar_spacing = 20
    max_height = 50

    pdf.draw_bar_chart(x_start, y_base, bar_width, bar_spacing, data, colors, max_height,path)
    pdf.set_y(140)
    for i,(label,value) in enumerate(data.items()):
        pdf.set_font('Karma-Semi', '', 18)
        pdf.set_text_color(*hex_to_rgb(colors[i]))
        pdf.text(150,pdf.get_y(),f'{label}: {value:.2f}%')
        pdf.set_y(pdf.get_y() + 20)
        
    pdf.set_xy(25,202.5)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Karma-Regular', '', 14) 
    pdf.multi_cell(pdf.w - 50,7,f"   {Constitution[max(data, key=data.get)]}")
    
    DesignColors = ["#BDE0FE", "#FEFAE0", "#FFC8DD", "#CAF0F8", "#FBE0CE", "#C2BCFF", "#9DE3DB", "#EDBBA3", "#EDF2F4", "#FFD6A5" , "#CBF3DB", "#94D8FD", "#DEE2FF", "#FEEAFA", "#D7AEFF", "#EEE4E1"]
    
    chakrasOrder = ["Root Chakra","Sacral Chakra","Solar Plexus Chakra","Heart Chakra","Throat Chakra","Third Eye Chakra","Crown Chakra"]
    
    pdf.AddPage(path,f"{name}'s Chakras")
    pdf.set_text_color(0,0,0)
    pdf.set_font_size(18)
    childChakras = chakras[planets[-1]['sign']]
    pdf.set_xy(20,pdf.get_y() + 10)
    pdf.multi_cell(pdf.w - 40,8,f"{name}'s Dominant Chakra{f's are {childChakras[0]} and {childChakras[1]}' if len(childChakras) > 1 else f' is {childChakras[0]}'}",align='C')
    pdf.set_font('Karma-Regular', '', 14)
    pdf.set_xy(20,pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 40,8,"       Chakras are energy centers in the body that influence a child’s personality, emotions, and growth. Each chakra connects to specific qualities like confidence, creativity, communication, and intuition. When balanced, these energy centers help children thrive, express themselves, and adapt to challenges. They guide emotional development, learning abilities, and the sense of connection to the world. Understanding chakras can provide insights into nurturing a child's holistic well-being and potential.",align='L')
    
    for chakra in childChakras:
        pdf.image(f"{path}/babyImages/chakra_{chakrasOrder.index(chakra) + 1}.png",pdf.w / 2 - 25,pdf.get_y() + 5,50,50)
        pdf.set_y(pdf.get_y() + 60)
        pdf.set_font('Karma-Heavy', '', 22)
        pdf.cell(0,0,f"{chakra}",align='C')
        pdf.set_xy(22.5,pdf.get_y() + 5)
        
    for index,chakra in enumerate(characteristics[planets[-1]['sign']]):
        if pdf.get_y() + 30 >= 260:
            pdf.AddPage(path)
            pdf.set_y(20)
        pdf.set_font('Karma-Regular', '', 14)
        pdf.set_xy(22.5,pdf.get_y() + 5)
        if index == 0:
            pdf.multi_cell(pdf.w - 45,8,f"       {name} {chakra}",align='L')
        else:
            pdf.multi_cell(pdf.w - 45,8,f"       {chakra}",align='L')
            

    pdf.AddPage(path,f"{name}'s True Self")
    pdf.set_xy(20,pdf.get_y() + 10)
    pdf.set_text_color(0,0,0)
    pdf.set_font_size(18)
    pdf.multi_cell(pdf.w - 40,8,f"Let's take a look at the three most influential and important sign for {name}!",align='C')
    pdf.set_font('Karma-Semi', '', 18)
    pdf.set_xy(30,pdf.get_y() + 10)
    pdf.cell(0,0,f"As per {name}'s kundli,")
    y = pdf.get_y() + 10
    roundedBoxBorder(pdf,"#FFE769","#C5A200",20,y,planets[1]['Name'],planets[1]['sign'],path)
    roundedBoxBorder(pdf,"#D1C4E9","#A394C6",80,y,planets[0]['Name'],planets[0]['sign'],path)
    roundedBoxBorder(pdf,"#B3E5FC","#82B3C9",140,y,planets[2]['Name'],planets[2]['sign'],path)
    pdf.set_y(pdf.get_y() + 10)
    
    # content = chapterPrompt(planets,6,name,gender)
    content = {'child_personality': 'Magizh, with Libra as the Lagnam sign, embodies a harmonious and charming outward persona. He exudes grace, fairness, and a desire for balance in all aspects of his life. Socially adept and diplomatic, Magizh naturally navigates relationships with ease, presenting himself as a peacemaker and mediator in conflicts. His physical attributes may reflect a sense of refinement and elegance, drawing others to his charismatic presence.', 'emotional_needs': "Magizh's Moon in Aries in the Seventh house indicates a child with fiery emotions, a strong sense of independence, and a competitive spirit. He craves excitement, challenges, and the freedom to express his emotions boldly. Magizh requires validation for his unique identity, seeking acknowledgment and admiration for his courage and individuality. He thrives on adventure and thrives in environments where he can assert himself and take bold initiatives.", 'core_identity': "Magizh's Sun in the Third house of Sagittarius shapes his core identity, portraying him as a curious and adventurous soul with a thirst for knowledge and exploration. His aspirations revolve around expanding his horizons through learning, travel, and intellectual pursuits. Motivated by a desire for freedom and growth, Magizh finds his sense of self through broadening his perspectives, sharing his wisdom with others, and embracing diversity. He embodies optimism, enthusiasm, and a love for discovery, forming the foundation of his inner self."}
    
    for index , (k, v) in enumerate(content.items()):
        if pdf.get_y() + 30 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(20)
            
        pdf.ContentDesign(random.choice(DesignColors),setTitle(k),v,path)
    
        
    pdf.AddPage(path,f"{name}'s Panchangam Growth Drivers")
    
    content = [
        "",
        "Magizh, born on a Saturday, possesses a charismatic and energetic personality that draws others towards him. With a natural flair for leadership and a confident demeanor, he is often the life of the party and the center of attention. Magizh's determination and drive allow him to excel in any endeavor he pursues, making him a force to be reckoned with in both his personal and professional life. His adventurous spirit and daring nature inspire those around him to push beyond their limits and strive for greatness.",
        "Magizh, born under the Bharani Nakshatra, is known for his intense and determined nature. He possesses a strong sense of purpose and tends to be ambitious in achieving his goals. Magizh is also known for his leadership qualities and assertiveness, often taking charge in difficult situations. His life path is marked by challenges that push him to grow and evolve, ultimately leading him towards success and fulfillment in his endeavors.",
        "Magizh, born under the Shiva Yogam, possesses a strong sense of determination and focus in achieving his goals. He is guided by a deep spiritual connection to Shiva, constantly seeking ways to improve and grow on a spiritual level. Magizh's Yogam characteristics empower him to overcome challenges and obstacles, leading to a profound impact on his overall well-being and personal development.",
        "Magizh, born under the Vishti Karanam, has a tendency to be impatient and quick-tempered, leading to a sense of urgency and drive in approaching tasks. Their work habits are characterized by a constant need to stay busy and productive, often taking on multiple projects at once. To achieve success, Magizh focuses on efficient time management and prioritizing tasks based on importance. Despite the challenges posed by their Karanam, Magizh has achieved notable success through their determination and ability to adapt to changing situations."
    ]
    
    colors = ["#E5FFB5","#94FFD2","#B2E4FF","#D6C8FF","#FFDECA"]    
    titles = [f"Tithi Represents {name}'s Emotions, Mental Well-being","Varam - Your Child's Career, Energy, and Key Life Decisions","Nakshatra - Your Child's Personality and Life Path","Yogam - Your Child's Path to Prosperity ","Karanam  - Your Child's Actions & Work "]
    
    titleImage = ['waningMoon.png' if panchang['thithi_number'] <= 15 else 'waxingMoon.png','week.png','nakshatra.png','yogam.png','karanam.png']
    
    pdf.set_text_color(0,0,0)
    pdf.set_y(pdf.get_y() + 5)
    for i in range(0,5):
        # con = panchangPrompt(panchang,i,name,gender)
        if pdf.get_y() + 50 >= 260:
            pdf.AddPage(path)
            pdf.set_y(30)
        con = content[i]
        pdf.image(f"{path}/babyImages/{titleImage[i]}",pdf.w / 2 - 10,pdf.get_y() + 5,20,20) 
        pdf.set_y(pdf.get_y() + 25)
        if i == 0:
            positive = thithiContent[panchang['thithi']][0]
            negative = thithiContent[panchang['thithi']][1]
            tips = thithiContent[panchang['thithi']][2]
    
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.set_font('Karma-Semi', '', 18)
            pdf.multi_cell(pdf.w - 45, 8,titles[i], align='C')
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.set_font('Karma-Regular', '', 14)
            pdf.multi_cell(pdf.w - 45,7,f"{name} was born on {panchang['paksha']} {panchang['thithi']},",align='C')
            y = pdf.get_y() + 5
            pdf.set_xy(20,y)
            pdf.set_fill_color(hex_to_rgb("#DAFFDC"))
            pdf.set_font('Karma-Semi', '', 16)
            pdf.cell((pdf.w - 40) / 2, 10, f"{name}'s Strength", align='C',new_x=XPos.LEFT,new_y=YPos.NEXT,fill=True)
            pdf.set_font("Karma-Regular", '', 14)
            for pos in positive:
                pdf.multi_cell((pdf.w - 40) / 2,10,f"       {pos}",align='C',new_x=XPos.LEFT,new_y=YPos.NEXT,fill=True) 
                
            pdf.set_fill_color(hex_to_rgb("#FFDADA"))
            pdf.set_xy(pdf.w / 2, y)
            pdf.set_font('Karma-Semi', '', 16)
            pdf.cell((pdf.w -40) / 2, 10, f"{name}'s Challenges", align='C',fill=True,new_x=XPos.LEFT,new_y=YPos.NEXT)
            pdf.set_font("Karma-Regular", '', 14)
            for neg in negative:
                pdf.multi_cell((pdf.w - 40) / 2,10,f"       {neg}",align='C',new_x=XPos.LEFT,new_y=YPos.NEXT,fill=True)
                
            pdf.set_xy(30,pdf.get_y() + 5)
            pdf.set_fill_color(hex_to_rgb(random.choice(DesignColors)))
            pdf.set_font("Times", '', 14)
            pdf.cell(pdf.w - 60,10,f"Thithi Lord: **{thithiLord[panchang['thithi']]}**",align='C',fill=True,new_y=YPos.NEXT,markdown=True)
                
            pdf.set_font("Times", '', 14)
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.multi_cell(pdf.w - 45,7,f"**Parenting Tips** : {tips['Name']} {tips['Description']} {tips['Execution']}",align='L',markdown=True)
            pdf.set_y(pdf.get_y() + 10)
            
        elif i == 4:
            positive = karanamContent[panchang['karanam']][0]
            negative = karanamContent[panchang['karanam']][1]
            tips = karanamContent[panchang['karanam']][2]
            
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.set_font('Karma-Semi', '', 18)
            pdf.multi_cell(pdf.w - 45, 8,titles[i], align='C')
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.set_font('Karma-Regular', '', 14)
            pdf.multi_cell(pdf.w - 45,7,f"{name} was born on {panchang['karanam']},",align='C')
            y = pdf.get_y() + 5
            pdf.set_xy(20,y)
            pdf.set_fill_color(hex_to_rgb("#DAFFDC"))
            pdf.set_font('Karma-Semi', '', 16)
            pdf.cell((pdf.w - 40) / 2, 10, f"{name}'s Strength", align='C',new_x=XPos.LEFT,new_y=YPos.NEXT,fill=True)
            pdf.set_font("Karma-Regular", '', 14)
            for pos in positive:
                pdf.multi_cell((pdf.w - 40) / 2,10,f"       {pos}",align='C',new_x=XPos.LEFT,new_y=YPos.NEXT,fill=True) 
                
            pdf.set_fill_color(hex_to_rgb("#FFDADA"))
            pdf.set_xy(pdf.w / 2, y)
            pdf.set_font('Karma-Semi', '', 16)
            pdf.cell((pdf.w -40) / 2, 10, f"{name}'s Challenges", align='C',fill=True,new_x=XPos.LEFT,new_y=YPos.NEXT)
            pdf.set_font("Karma-Regular", '', 14)
            for neg in negative:
                pdf.multi_cell((pdf.w - 40) / 2,10,f"       {neg}",align='C',new_x=XPos.LEFT,new_y=YPos.NEXT,fill=True)
                
            pdf.set_font("Times", '', 14)
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.multi_cell(pdf.w - 45,7,f"**Parenting Tips** : {tips['Tip']} {tips['Execution']}",align='L',markdown=True)
            pdf.set_y(pdf.get_y() + 10)
        else:
            pdf.ContentDesign(random.choice(DesignColors),titles[i],con,path)   

                
    # content1 = physical(planets,1,name,gender)
    # content2 = physical(planets,2,name,gender)
    # content3 = physical(planets,3,name,gender)
    # content4 = physical(planets,4,name,gender)
    
    content1 = "The child with Libra lagna and Venus placed in the first house in Vishakha Nakshatra may have a balanced and harmonious physical appearance. They are likely to have a slim and well-proportioned body built, with a graceful and charming demeanor. Their face may be symmetrical and pleasing to look at, with soft features and a gentle expression. Their eyes are likely to be charming and expressive, possibly with a twinkle in them, reflecting their sweet and affectionate nature. Their overall physical appearance exudes an aura of beauty and elegance, drawing others towards them effortlessly. This child may possess a magnetic presence that makes them stand out in a crowd, with a natural sense of style and grace that sets them apart from others."
    content2 = {'outer_personality': 'Magizh is a charismatic and charming individual with a magnetic aura. He exudes grace and elegance in his appearance and behavior, making a lasting impression on those around him. With Venus as his Nakshatra Lord in the 1st House of Libra, Magizh possesses a harmonious blend of beauty, creativity, and diplomacy.', 'character': [{'title': 'Creative and Artistic', 'content': "Magizh has a natural talent for creativity and artistry. His love for beauty and aesthetics is reflected in his passion for artistic pursuits like painting, music, or design. Venus's influence in the 1st House enhances his creative abilities and makes him attuned to harmonious expressions of beauty."}, {'title': 'Diplomatic and Charming', 'content': "Magizh's diplomatic nature and charm are his key strengths. With Venus in the 1st House, he has a way with words and a pleasant demeanor that enables him to navigate social interactions with ease. He can win people over with his affable personality and tactful communication style."}, {'title': 'Balanced and Fair-minded', 'content': 'Magizh possesses a sense of balance and fairness in his approach to life. The influence of Venus in the 1st House of Libra instills in him a desire for harmony and justice. He values fairness in his interactions and strives to maintain a sense of equilibrium in all aspects of his life.'}], 'behaviour': [{'title': 'Social and Sociable', 'content': 'Magizh is inherently social and enjoys connecting with others. His pleasant disposition and sociable nature make him a popular figure in his social circles. He thrives in group settings and finds fulfillment in building meaningful relationships with diverse individuals.'}, {'title': 'Adaptable and Flexible', 'content': 'Magizh demonstrates remarkable adaptability and flexibility in various situations. With Venus in the 1st House, he can easily adjust to different circumstances and environments. His ability to adapt quickly to change enhances his resilience and problem-solving skills.'}, {'title': 'Harmonious and Peaceful', 'content': "Magizh's quest for harmony and peace influences his behavior positively. He strives to create peaceful environments and promote understanding among people. His innate ability to diffuse conflicts and maintain harmony makes him a valuable peacemaker in challenging situations."}], 'negative_impact': [{'title': 'Tendency towards Indecisiveness', 'content': 'Magizh may struggle with indecisiveness at times due to the influence of Venus in the 1st House. His desire to maintain harmony and avoid conflicts can lead to hesitancy in making firm decisions. Developing assertiveness and clarity in decision-making can help him overcome this challenge.'}, {'title': 'Overly Concerned with External Appearance', 'content': "Magizh's emphasis on beauty and aesthetics may sometimes overshadow other important aspects of his life. He may place too much importance on external appearances and material possessions, leading to a superficial approach to his self-worth. Cultivating inner values and self-acceptance can help him find a balance between outer appearance and inner growth."}, {'title': 'Struggle with Confrontation', 'content': 'Due to his diplomatic nature, Magizh may find it challenging to confront difficult situations or address conflicts directly. He may avoid confrontation to maintain harmony, which can hinder his personal growth and lead to unresolved issues. Building assertiveness skills and communication techniques can empower him to navigate conflicts effectively.'}]}

    content3 = {'inner_worlds': "Magizh's emotional world is deeply influenced by his Janma Nakshatra (Bharani Nakshatra) and the placement of Venus in the 1st House of Libra in Vishakha Nakshatra. His emotional needs, thoughts, beliefs, feelings, reactions, and emotional stability are all affected by these astrological placements.", 'emotional_needs': [{'title': 'Desire for Harmony', 'content': "Magizh has a strong emotional need for harmony and balance in all aspects of his life. He craves peace and seeks to avoid conflicts and discord. This need for harmony is influenced by the placement of Venus in the 1st House of Libra, emphasizing the importance of relationships and cooperation in Magizh's emotional fulfillment."}, {'title': 'Need for Independence', 'content': "Despite his desire for harmony, Magizh also has a strong need for independence and freedom. He values his autonomy and seeks opportunities to assert his individuality. The placement of Mars in the 2nd House of Scorpio highlights Magizh's drive for self-expression and self-reliance, adding a layer of determination and intensity to his emotional needs."}, {'title': 'Seeking Emotional Depth', 'content': "Magizh has a deep emotional need for meaningful connections and experiences. He is drawn to profound emotions and seeks authenticity in his interactions. The influence of Jyeshtha Nakshatra on Mars in the 2nd House of Scorpio amplifies Magizh's desire for emotional depth and transformative experiences."}], 'impact': [{'title': 'Tendency towards Stubbornness', 'content': 'Magizh may struggle with stubbornness and rigidity in his emotional responses. This could lead to difficulties in adapting to changing circumstances and a resistance to considering alternative perspectives. To foster emotional growth, Magizh may need to work on cultivating flexibility and openness to new ideas.'}, {'title': 'Emotional Intensity', 'content': "Due to the placement of Mars in the 2nd House of Scorpio, Magizh may experience heightened emotional intensity and a tendency towards passionate reactions. This intensity can be both a strength and a challenge, impacting his relationships and emotional stability. Learning to channel this intensity constructively is key for Magizh's emotional well-being."}, {'title': 'Struggle with Trust Issues', 'content': 'Magizh may harbor deep-seated trust issues that stem from past experiences or subconscious fears. The combination of Venus in the 1st House of Libra and Mars in the 2nd House of Scorpio can create inner tensions related to trust and vulnerability. Cultivating self-awareness and exploring the roots of these trust issues can support Magizh in developing healthier and more fulfilling relationships.'}]}

    content4 = {'core_identity': "Magizh's core identity is characterized by a balanced blend of social charm, creativity, and spiritual depth. Magizh's Lagna in Libra indicates a strong sense of harmony, diplomacy, and a natural inclination towards relationships. With Venus placed in the 1st house of Libra in Vishakha Nakshatra, Magizh exudes a charming and charismatic aura, attracting others with ease. The Sun in the 3rd house of Sagittarius in Mula Nakshatra adds a touch of philosophical depth, curiosity, and a quest for knowledge to Magizh's identity. The Moon in the 7th house of Aries in Bharani Nakshatra suggests emotional intensity, independence, and a need for personal freedom.", 'recognitions': [{'title': 'Charm and Diplomacy', 'content': 'Magizh seeks recognition for their charm, diplomacy, and ability to create harmonious relationships. Others acknowledge Magizh for their social grace and ability to navigate diverse social circles with ease.'}, {'title': 'Intellectual Curiosity', 'content': 'Magizh desires acknowledgment for their intellectual curiosity, philosophical insights, and quest for knowledge. Others recognize Magizh for their ability to engage in meaningful conversations and explore new ideas.'}, {'title': 'Emotional Intensity', 'content': 'Magizh craves recognition for their emotional intensity, independence, and strong sense of self. Others admire Magizh for their courage to express their emotions authentically and stand up for their beliefs.'}], 'remedies': [{'title': 'Venus Remedies', 'content': "To enhance self-confidence and balance the ego, Magizh can wear a diamond or opal, chant the Venus mantra, 'Om Shukraya Namaha', and perform acts of kindness and generosity towards others to strengthen Venus's positive influence on their identity."}, {'title': 'Sun Remedies', 'content': "To strengthen the sense of self and overcome ego challenges, Magizh can wear a ruby or red coral, recite the Sun mantra, 'Om Suryaya Namaha', practice self-expression through creative pursuits, and engage in activities that boost self-esteem and leadership qualities."}, {'title': 'Moon Remedies', 'content': "To nurture emotional well-being and enhance self-awareness, Magizh can wear a pearl or moonstone, chant the Moon mantra, 'Om Somaya Namaha', practice mindfulness and meditation, and connect with their inner emotions through journaling or creative outlets."}]}
    
    content = [content1,content2,content3,content4]

    titles = ["Physical Attributes",{
        'outer_personality': "Outer Personality", 
        'character': "Character",
        'behaviour': "Behaviour", 
        'negative_impact' : "Impact of Negative Personality & Behavior on Child's Life", 
        'parenting_tips' : f"Parenting Tips to Nurturing {name}'s Personality & Behaviour Development" 
        }, {
            'inner_worlds' : "Inner Worlds", 
            'emotional_needs': "Emotional Needs", 
            'impact' : "Impact of Emotional Imbalance  on Child's Life", 
            'remedies': f"Understand & Nurture {name}'s Emotions & Feelings Turn them Smart and Resilient"
        },{
            'core_identity' : f"{name}'s Soul Desire",
            'recognitions' : f"{name}'s Desire for Acknowledgement",
            'remedies': f"Build {name}'s Confidence & Leadership Quality"
        }]
    
    pdf.AddPage(path,"Outer World - Physical Attributes, Personality, and Behavior")
    pdf.set_text_color(0,0,0)
        
    for index,c in enumerate(content):
        if index == 2:
            pdf.AddPage(path,"Inner World - Emotional Needs and Soul Desire ")
            
        if pdf.get_y() + 40 >= 260:
            pdf.AddPage(path)
            pdf.set_y(30)
        pdf.set_text_color(0, 0, 0)
        if isinstance(c, str):
            pdf.set_font('Karma-Semi', '', 18)
            pdf.set_xy(45,pdf.get_y() + 10)
            pdf.multi_cell(pdf.w - 90, 8, f"{titles[index]}", align='C')
            pdf.set_font('Karma-Regular', '', 14)
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.multi_cell(pdf.w - 45, 7, f"        {c}", align='L')
        else:
            for k, v in c.items():
                if pdf.get_y() + 40 >= 260:  
                    pdf.AddPage(path)
                    pdf.set_y(30)
                
                pdf.ContentDesign(random.choice(DesignColors),titles[index][k],v,path)
                    
    pdf.AddPage(path,"Potential Health Challenges and Holistic Wellness Solutions")
    # con = healthPrompt(planets,0,name,gender) 
    con = {'health_insights': 'Magizh is a unique individual with a balanced constitution of Vata, Pitta, and Kapha doshas. The composition of the five elements in his body is in harmony, ensuring overall well-being and vitality. His lagna sign Libra signifies a focus on balance and harmony in health matters, while the placement of Venus in the lagna enhances his beauty and vitality. Additionally, the influence of Mars in the 2nd house of Scorpio may indicate strong metabolic functions and a need for emotional balance in maintaining health. Overall, Magizh has the potential for good health with a tendency towards maintaining equilibrium and addressing any imbalances promptly.', 'challenges': [{'title': 'Digestive Issues', 'content': 'Magizh may experience digestive challenges due to the influence of Mars in Scorpio, indicating potential imbalances in metabolism and gut health. It is essential for him to focus on a balanced diet and lifestyle to alleviate these issues.'}, {'title': 'Emotional Wellness', 'content': 'The placement of Moon and Jupiter in the 7th house of Aries may suggest emotional sensitivity and fluctuation in mood. Magizh needs to practice mindfulness techniques and emotional regulation to support his mental well-being.'}, {'title': 'Skin Disorders', 'content': 'The presence of Rahu in the 6th house of Pisces can indicate skin-related issues such as allergies or sensitivities. Magizh should pay attention to his skincare routine and seek natural remedies to maintain healthy skin.'}, {'title': 'Respiratory Problems', 'content': 'With Ketu in the 12th house of Virgo and Mercury in the 3rd house of Sagittarius, Magizh may be prone to respiratory ailments. Practicing breathing exercises and maintaining a clean environment can help prevent such problems.'}, {'title': 'Bone Health', 'content': "Saturn's influence in the 5th and 11th houses of Aquarius and Capricorn may highlight the importance of bone health for Magizh. Incorporating calcium-rich foods and regular physical activity can support his skeletal system."}], 'natural_remedies': [{'title': 'Aloe Vera for Digestion', 'content': 'Drink a glass of fresh aloe vera juice in the morning to improve digestion and reduce inflammation in the gut.'}, {'title': 'Turmeric Paste for Skin', 'content': 'Create a turmeric paste using turmeric powder and honey, apply it to the affected skin area to reduce inflammation and promote healing.'}, {'title': 'Tulsi Tea for Respiration', 'content': 'Boil fresh tulsi leaves in water, strain the tea, and drink it warm to alleviate respiratory issues and boost immunity.'}, {'title': 'Ginger for Nausea', 'content': 'Chew on a small piece of fresh ginger or drink ginger tea to relieve nausea and improve digestion.'}, {'title': 'Fenugreek Seeds for Bone Health', 'content': 'Soak fenugreek seeds overnight, consume them in the morning to support bone strength and mineral absorption.'}], 'nutrition_tips': [{'title': 'Omega-3 Fatty Acids', 'content': "Include sources of omega-3 fatty acids such as flaxseeds, walnuts, and fatty fish in Magizh's diet to support brain health and reduce inflammation."}, {'title': 'Probiotic-rich Foods', 'content': 'Integrate probiotic-rich foods like yogurt, kefir, and sauerkraut to maintain a healthy gut microbiome and improve digestion.'}, {'title': 'Leafy Greens', 'content': 'Ensure a daily intake of leafy greens like spinach, kale, and arugula to boost nutrient intake and support overall well-being.'}, {'title': 'Vitamin D Supplements', 'content': 'Consider taking vitamin D supplements or spending time in sunlight to prevent deficiencies and strengthen bone health.'}, {'title': 'Hydration', 'content': 'Encourage Magizh to stay hydrated by drinking sufficient water throughout the day to support metabolism and organ function.'}], 'wellness_routines': [{'title': 'Morning Meditation', 'content': 'Start the day with a short meditation practice to center the mind, reduce stress, and enhance mental clarity.'}, {'title': 'Sound Therapy', 'content': 'Listen to calming sounds like nature sounds or chanting to promote relaxation and balance the mind-body connection.'}, {'title': 'Pranayama', 'content': 'Practice deep breathing exercises like alternate nostril breathing to improve respiratory function and calm the nervous system.'}, {'title': 'Yoga Asanas', 'content': "Incorporate yoga poses like child's pose, cat-cow stretch, and downward-facing dog to improve flexibility and relieve tension."}, {'title': 'Gratitude Journaling', 'content': 'Maintain a gratitude journal to cultivate a positive mindset, enhance self-awareness, and promote emotional well-being.'}], 'lifestyle_suggestions': [{'title': 'Stress Management', 'content': 'Teach Magizh stress management techniques like deep breathing, progressive muscle relaxation, and mindfulness to cope with daily stressors.'}, {'title': 'Time Management', 'content': 'Guide Magizh in setting realistic goals, prioritizing tasks, and creating a daily schedule to improve productivity and reduce anxiety.'}, {'title': 'Assertiveness Training', 'content': 'Empower Magizh to express his needs and boundaries effectively, practice assertive communication, and build self-confidence in interpersonal interactions.'}], 'preventive_tips': [{'title': 'Balanced Diet', 'content': 'Ensure Magizh follows a balanced diet rich in fruits, vegetables, whole grains, and lean proteins to support overall health and prevent nutritional deficiencies.'}, {'title': 'Regular Exercise', 'content': 'Encourage Magizh to engage in regular physical activity such as walking, yoga, or swimming to maintain fitness levels and support metabolic function.'}, {'title': 'Healthy Lifestyle Habits', 'content': "Promote healthy lifestyle habits like adequate sleep, hydration, and stress management techniques to enhance Magizh's well-being and prevent health challenges."}]}     

    pdf.set_text_color(0, 0, 0)
    for k, v in con.items():
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),setTitle(k),v,path)
                                
    pdf.AddPage(path,f"{name}'s Education and Intellect")
    pdf.set_font('Karma-Semi','', 16)
    pdf.set_y(pdf.get_y() + 10)
    pdf.cell(0,0,"Insights about your Child's education and intelligence",align='C')
    pdf.set_font('Karma-Regular', '', 14)
    
    educationTitle = {
        "insights" : "Education and Intellectual Insights",
        "suitable_educational" : "Suitable Educational Pursuits", 
        "cognitive_abilities" : "Unique Cognitive Abilities", 
        "recommendations" : "Personalized Learning Techniques & Recommendations"
    }
    # con = chapterPrompt(planets,3,name,gender)
    con = {'insights': 'Magizh has a diverse range of intellectual insights based on the placement of planets in his astrology chart. His educational journey is influenced by the positions of Venus, Mars, Sun, Mercury, Jupiter, Moon, Saturn, Rahu, and Ketu in various houses and nakshatras. These planetary placements indicate a blend of creativity, determination, logical thinking, and intuitive abilities in his learning potentials and intellectual pursuits.', 'suitable_educational': [{'title': 'Creative Arts', 'content': 'Magizh has a natural talent for creative expression and may excel in fields such as painting, music, or design.'}, {'title': 'Psychology', 'content': 'His cognitive abilities make him well-suited for understanding human behavior and emotions, making psychology a suitable field for him.'}, {'title': 'Engineering', 'content': 'With a strong influence of Mars and Saturn, engineering can be a rewarding path for Magizh to apply his analytical and problem-solving skills.'}, {'title': 'Communication Studies', 'content': 'The placement of Mercury and Sun suggests a proficiency in communication, making fields like journalism or media studies a good fit for him.'}, {'title': 'Astrology', 'content': 'Given the positioning of planets in his chart, Magizh may have a natural inclination towards astrology and esoteric studies.'}, {'title': 'Business Management', 'content': 'The presence of Venus and Jupiter hints at leadership qualities and strategic thinking, making business management a promising field for him.'}, {'title': 'Computer Science', 'content': 'The influence of Rahu in the sixth house indicates an interest in technology, making computer science an area where Magizh can thrive.'}], 'cognitive_abilities': [{'title': 'Critical Thinking', 'content': 'Magizh possesses strong critical thinking skills that allow him to analyze complex situations and come up with innovative solutions.'}, {'title': 'Emotional Intelligence', 'content': 'His understanding of emotions and interpersonal dynamics enables him to connect with others on a deeper level, enhancing his social skills.'}, {'title': 'Intuitive Decision Making', 'content': 'Magizh has a natural gift for intuitive decision-making, which can guide him in uncertain situations and lead to favorable outcomes.'}, {'title': 'Detail-Oriented', 'content': 'He pays close attention to detail, ensuring precision in his work and a thorough understanding of the subjects he engages with.'}, {'title': 'Adaptability', 'content': 'Magizh demonstrates adaptability in learning new concepts and approaches, making him versatile in different academic and professional environments.'}], 'recommendations': [{'title': 'Visual Learning Techniques', 'content': 'Encourage Magizh to utilize visual aids such as diagrams, charts, and videos to enhance his understanding of complex concepts.'}, {'title': 'Mind Mapping', 'content': 'Introduce him to mind mapping techniques to organize information and connect ideas effectively for better retention and recall.'}, {'title': 'Collaborative Learning', 'content': 'Promote group projects and discussions to foster his communication skills and collaborative abilities in academic settings.'}, {'title': 'Practice Meditation', 'content': 'Suggest regular meditation practices to help Magizh harness his intuitive abilities and maintain mental clarity for improved focus.'}, {'title': 'Utilize Technology', 'content': 'Incorporate educational apps and online platforms to supplement his learning experience and explore interactive ways to engage with course materials.'}]}
    
    pdf.set_text_color(0, 0, 0)
    
    for index,(k, v) in enumerate(con.items()):
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),educationTitle[k],v,path)
            
    pdf.AddPage(path,"Family and Relationships")
    # con = physical(planets,5,name,gender)
    con = {'family_relationship': "Magizh's family dynamics are influenced by strong connections with his parents and siblings. His relationship with his father (represented by the Sun) is nurturing and supportive, while his relationship with his mother (represented by the Moon) is emotionally fulfilling. In terms of social development, Magizh thrives in building friendships and engaging with peers, seeking harmony and balance in his interactions, influenced by Venus in the 1st House of Libra.", 'approaches': [{'title': 'Building Social Bonds', 'content': 'Magizh approaches social development by prioritizing harmonious relationships and seeking beauty and balance in interactions, influenced by Venus in the 1st House of Libra.'}, {'title': 'Nurturing Relationship with Father', 'content': "Magizh bonds with his father by seeking guidance and support, appreciating his father's warmth and leadership qualities, influenced by the Sun in the 3rd House of Sagittarius."}, {'title': 'Emotional Connection with Mother', 'content': 'Magizh forms a deep emotional bond with his mother, seeking comfort and security in her nurturing presence, influenced by the Moon in the 7th House of Aries.'}], 'challenges': [{'title': 'Overcoming Shyness', 'content': 'Magizh may struggle with shyness and hesitation in forming new friendships and social connections, impacting his social interactions and peer relationships.'}, {'title': 'Balancing Independence and Interdependence', 'content': 'Magizh faces the challenge of balancing his independent nature with the need for partnership and cooperation in relationships, especially with siblings and friends.'}, {'title': 'Navigating Family Expectations', 'content': 'Magizh may experience pressure from family expectations, especially in balancing personal aspirations with familial responsibilities, leading to internal conflicts.'}], 'parenting_support': [{'title': 'Encouraging Communication Skills', 'content': "Parents can support Magizh's social development by encouraging open communication, active listening, and expressive sharing of thoughts and emotions, fostering healthy relationships."}, {'title': 'Promoting Independence', 'content': "Parents can nurture Magizh's independence by allowing him space for self-expression, decision-making, and exploring personal interests, promoting self-confidence and autonomy."}, {'title': 'Cultivating Emotional Intelligence', 'content': 'Parents can help Magizh develop emotional intelligence by teaching him to identify and manage emotions, empathize with others, and navigate interpersonal relationships with empathy and understanding.'}]}
    
    familyTitle = {
        'family_relationship' : "",
        'approaches': f"{name}'s Approaches for Forming Relationships",
        'challenges' : "Challenges in the child's  relationship & social development",
        'parenting_support' : f"Parenting Support for Improve {name}'s Social Developments"
    }
    
    for k, v in con.items():
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),familyTitle[k],v,path)
                
    pdf.AddPage(path,f"{name}'s Career and Professions")
    pdf.set_font('Karma-Semi','', 16)
    pdf.set_xy(20,pdf.get_y() + 10)
    pdf.multi_cell(pdf.w - 40,8,"Wondering what the future holds for your child's career journey?",align='L')
    # con = chapterPrompt(planets,4,name,gender)
    
    con = {'career_path': "Based on Magizh's astrology details, it is evident that Magizh possesses a strong potential for a successful career path. With the placement of the 10th house lord Moon in the 7th house of Aries along with Jupiter, Magizh is likely to excel in professions that require creativity, intuition, and emotional intelligence. Additionally, the placement of planets in the 2nd house of Scorpio indicates a potential for financial success and determination in achieving goals. Magizh's career path is aligned with his natural talents and strengths, leading him towards a fulfilling and prosperous professional journey.", 'suitable_professions': [{'title': 'Creative Writer', 'content': 'As a Creative Writer, Magizh can leverage his emotional intelligence and creative abilities to excel in crafting compelling narratives and storytelling in various mediums such as books, articles, or screenplays.'}, {'title': 'Psychologist', 'content': 'With a deep understanding of human emotions and the ability to empathize with others, Magizh can thrive as a Psychologist, helping individuals navigate through their psychological challenges and achieve mental well-being.'}, {'title': 'Artist', 'content': "Magizh's artistic talents can shine in the field of Art, where he can express his creativity through various forms such as painting, sculpture, or graphic design, resonating with a wide audience."}, {'title': 'Entrepreneur', 'content': 'As an Entrepreneur, Magizh can channel his determination and leadership skills to establish his ventures, leveraging his innovative ideas to create successful business ventures in various industries.'}, {'title': 'Musician', 'content': 'With a knack for music and an intuitive understanding of rhythms and melodies, Magizh can pursue a career as a Musician, expressing his emotions and connecting with audiences through his musical talents.'}, {'title': 'Therapist', 'content': "Magizh's compassionate nature and ability to listen actively make him an ideal candidate for a Therapist, guiding individuals towards emotional healing and personal growth through therapeutic interventions."}, {'title': 'Photographer', 'content': 'Utilizing his creative eye and visual storytelling skills, Magizh can excel as a Photographer, capturing moments and emotions through his lens, creating impactful visual narratives in various genres.'}], 'business': [{'title': 'Art Gallery', 'content': 'Magizh can explore the business potential in owning an Art Gallery, showcasing his artistic creations or curating works of other artists, providing a platform for art enthusiasts to appreciate and purchase art pieces.'}, {'title': 'Psychological Counseling Center', 'content': 'Establishing a Psychological Counseling Center can be a fulfilling business venture for Magizh, offering counseling services to individuals seeking mental health support and guidance, creating a positive impact on the community.'}, {'title': 'Creative Writing Agency', 'content': 'By founding a Creative Writing Agency, Magizh can collaborate with talented writers and offer professional writing services for clients across diverse industries, showcasing his creative expertise and storytelling skills.'}, {'title': 'Music Production Studio', 'content': "Venturing into a Music Production Studio business can leverage Magizh's musical talents, offering a platform for aspiring musicians to record and produce their music, contributing to the music industry with innovative sounds."}, {'title': 'Online Art Store', 'content': 'Launching an Online Art Store can be a lucrative business opportunity for Magizh, curating and selling artistic creations online, reaching a global audience and expanding his reach in the art market.'}]}

    CarrerTitle = {
        "suitable_professions" : "Child’s Successful Career Path & Suitable Professions", 
        "business": "Business & Entrepreneurial Potentials"
    }
    
    for index,(k, v) in enumerate(con.items()):
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        if index == 0:    
            pdf.ContentDesign(random.choice(DesignColors),"",v,path)
        else:
            pdf.ContentDesign(random.choice(DesignColors),CarrerTitle[k],v,path)
                                    
    pdf.AddPage(path,"Subconscious Mind Analysis")
    # con = chapterPrompt(planets,5,name,gender)
    con = {'subconscious_mind': "Based on Magizh's astrology details, the subconscious mind may hold limiting beliefs related to self-worth, relationships, and transformation. There could be hidden fears regarding personal identity, financial stability, and deep-rooted anxiety about the unknown and spiritual growth.", 'personalized_affirmations': [{'title': 'I am worthy of love and success', 'content': "Repeat this affirmation 21 times every morning and evening: 'I am worthy of love and success, and I embrace my uniqueness.'"}, {'title': 'I attract positive relationships into my life', 'content': "Recite this affirmation 15 times before bedtime: 'I attract positive relationships into my life, and I surround myself with love and support.'"}, {'title': 'I trust in the process of transformation', 'content': "Say this affirmation 18 times during meditation: 'I trust in the process of transformation, and I release fear of the unknown.'"}, {'title': 'I am financially secure and abundant', 'content': "Repeat this affirmation 20 times while visualizing abundance: 'I am financially secure and abundant, and I welcome prosperity into my life.'"}, {'title': 'I embrace spiritual growth and enlightenment', 'content': "Recite this affirmation 17 times while connecting with nature: 'I embrace spiritual growth and enlightenment, and I am guided by inner wisdom.'"}], 'visualizations': [{'title': 'Golden Light of Self-Worth', 'content': 'Visualize a golden light surrounding you, affirming your self-worth and radiating love. Imagine this light expanding with each breath, filling you with confidence and positivity.'}, {'title': 'Fear Release Bonfire', 'content': 'Visualize writing down your fears on paper, then burning the paper in a bonfire. As the flames consume your fears, feel a sense of liberation and freedom washing over you.'}, {'title': 'Transformational Butterfly', 'content': 'Visualize yourself as a butterfly emerging from a cocoon, symbolizing transformation and growth. Feel the lightness and freedom of the butterfly as you soar towards new possibilities.'}, {'title': 'Abundance Fountain', 'content': 'Imagine a fountain overflowing with abundance and prosperity. Visualize yourself bathing in the waters of abundance, feeling financial security and wealth flowing into your life.'}, {'title': 'Mystical Forest of Enlightenment', 'content': 'Visualize walking through a mystical forest filled with wisdom and enlightenment. Connect with the energy of the forest, absorbing the knowledge and guidance it offers for your spiritual journey.'}], 'meditations': [{'title': 'Self-Worth Affirmation Meditation', 'content': "Sit in a comfortable position, close your eyes, and repeat the affirmation 'I am worthy of love and success' for 10 minutes. Focus on feeling the truth of the affirmation in your heart and soul."}, {'title': 'Fear Release Breathing Meditation', 'content': 'Take deep breaths in and out, visualizing inhaling calmness and exhaling fear. Spend 15 minutes releasing any fears or anxieties with each breath, opening yourself to peace and serenity.'}, {'title': 'Transformation Visualization Meditation', 'content': 'Visualize your body and mind undergoing a transformation process, shedding old beliefs and embracing new possibilities. Meditate on this transformation for 20 minutes, feeling the energy shift within you.'}, {'title': 'Abundance Manifestation Meditation', 'content': 'Imagine a stream of golden light entering the crown of your head, filling you with abundance and prosperity. Meditate on this flow of abundance for 25 minutes, allowing yourself to attract financial security and wealth.'}, {'title': 'Enlightenment Connection Meditation', 'content': 'Sit in silence and focus on connecting with your inner wisdom and higher self. Spend 30 minutes in meditation, deepening your spiritual connection and opening yourself to enlightenment and guidance.'}]}

    subTitle = {
        "subconscious_mind" : "",
        "personalized_affirmations" : "Personalized Affirmations", 
        "visualizations" : "Visualization Techniques", 
        "meditations": "Meditation Practices"
    }
    
    for index,(k, v) in enumerate(con.items()):
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
            
        if index == 1:
            pdf.set_y(pdf.get_y() + 10)
            pdf.set_font('Karma-Heavy', '', 22)
            pdf.cell(0,0,f"Train {name}'s Subconscious Mind",align='C')
            pdf.set_y(pdf.get_y() + 5)
        
        pdf.ContentDesign(random.choice(DesignColors),subTitle[k],v,path)
        
    pdf.AddPage(path,"Unique Talents and Natural Skills")
    
    uniqueTitle = {
        'insights': "", 
        'education' : "Unique Talents in Academics ", 
        'arts_creative' :"Unique Talents in Arts & creativity ",
        'physical_activity': "Unique Talents in Physical Activity"
    }
    # con = chapterPrompt(planets,0,name,gender)
    
    con = {'education': [{'title': 'Analytical Thinking', 'content': 'Magizh has a natural talent for analytical thinking and problem-solving, especially in educational pursuits. His Mercury in the 3rd house of Sagittarius enhances his ability to communicate ideas effectively and explore diverse subjects with depth and curiosity.'}, {'title': 'Philosophical Insight', 'content': 'With Mercury in Sagittarius in the 3rd house, Magizh possesses a deep interest in philosophical concepts and higher learning. He may excel in subjects that require abstract thinking and philosophical insights, making him a natural philosopher.'}, {'title': 'Adventurous Learning', 'content': 'Magizh is inclined towards adventurous learning experiences due to his Mercury in the 3rd house of Sagittarius. He thrives in environments that challenge his intellect and broaden his horizons, making him an enthusiastic learner.'}, {'title': 'Multilingual Skills', 'content': "Given Mercury's placement in Sagittarius, Magizh may have a flair for languages and possess multilingual skills. His ability to adapt to different linguistic structures and communicate effectively in various languages sets him apart in intellectual pursuits."}, {'title': 'Research Abilities', 'content': "Magizh's Mercury in Sagittarius in the 3rd house indicates strong research abilities. He has a natural inclination towards exploring new ideas, conducting in-depth investigations, and uncovering hidden knowledge, making him a skilled researcher."}], 'arts_creative': [{'title': 'Harmonious Artistic Expression', 'content': 'Magizh demonstrates a harmonious and balanced artistic expression with Venus in the 1st house of Libra. His creative endeavors are characterized by beauty, grace, and elegance, reflecting his Venusian influences in artistic pursuits.'}, {'title': 'Aesthetic Sensibility', 'content': 'With Venus in Libra in the 1st house, Magizh possesses a refined aesthetic sensibility. He has a keen eye for beauty, symmetry, and design, allowing him to create visually appealing artworks and appreciate artistic endeavors with discernment.'}, {'title': 'Diplomatic Communication', 'content': "Magizh's Venus placement in Libra enhances his diplomatic communication skills. He excels in expressing himself tactfully, fostering harmony in relationships, and using his artistic talents to convey messages effectively and persuasively."}, {'title': 'Creative Problem-Solving', 'content': "Magizh's Venus in Libra in the 1st house empowers him with creative problem-solving abilities. He approaches challenges with creativity, innovation, and a sense of balance, finding unique solutions through his artistic flair and ingenuity."}, {'title': 'Musical Talent', 'content': "Given Venus's influence, Magizh may possess musical talent and a deep appreciation for melodic vibrations. His artistic expressions through music are likely to be emotive, soulful, and resonant, showcasing his Venusian creativity."}], 'physical_activity': [{'title': 'Intense Physical Energy', 'content': "Magizh exhibits intense physical energy and drive with Mars in the 2nd house of Scorpio. His passion for physical activities is fueled by Mars's influence, making him determined, competitive, and resilient in pursuing his fitness goals."}, {'title': 'Strength and Endurance', 'content': 'With Mars in Scorpio in the 2nd house, Magizh possesses remarkable strength and endurance. He excels in activities that require stamina, power, and perseverance, showcasing his ability to overcome challenges and push his physical limits.'}, {'title': 'Strategic Sportsmanship', 'content': "Magizh's Mars placement in Scorpio enhances his strategic approach to sportsmanship and physical activities. He excels in competitive sports that demand strategic thinking, assertiveness, and calculated moves, showcasing his Mars-driven determination."}, {'title': 'Martial Arts Proficiency', 'content': "Given Mars's influence, Magizh may excel in martial arts and combat sports. His aggressive yet disciplined approach to training and combat situations highlights his Mars-related skills in self-defense, agility, and precision."}, {'title': 'Active Lifestyle Advocate', 'content': "Magizh's Mars in Scorpio in the 2nd house indicates his advocacy for an active lifestyle. He encourages others to embrace physical fitness, engage in vigorous activities, and prioritize their health and well-being, reflecting his Mars-driven passion for active living."}], 'insights': 'Magizh possesses a unique blend of intellectual curiosity, artistic sensibility, and physical vigor, as reflected in his Mercury, Venus, and Mars placements. His strong analytical thinking, philosophical insights, and adventurous learning spirit make him a versatile learner and a natural researcher. In the creative realm, his harmonious artistic expression, diplomatic communication, and musical talents set him apart in creative endeavors. Additionally, his intense physical energy, strategic sportsmanship, and advocacy for an active lifestyle showcase his leadership qualities and determination in physical pursuits. By nurturing these talents effectively and providing opportunities for growth and expression, Magizh can enhance his innate abilities and reach his full potential across intellectual, artistic, and physical domains.'}
    
    for index,(k, v) in enumerate(con.items()):
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),uniqueTitle[k],v,path)
        
        
    pdf.AddPage(path,"Karmic Life Lessons")        
    # con = chapterPrompt(planets,7,name,gender)
    
    con = {'child_responsibility_discipline': "Magizh, with Saturn placed in the Fifth house of Aquarius, your karmic life lesson revolves around responsibility and discipline. You are meant to learn the importance of taking on responsibilities seriously and maintaining discipline in all aspects of life. Avoid being careless or impulsive in decision-making, as Saturn's influence urges you to be accountable and focused to achieve your goals.", 'child_desire_ambition': "Magizh, with Rahu placed in the Sixth house of Pisces, your karmic life lesson is linked to desire and ambition. It is crucial for you to be aware of your desires and ambitions, as Rahu's placement suggests a strong drive for material success. However, be cautious of overindulgence and extreme ambitions that may lead you astray. Your purpose in life may involve overcoming illusions and achieving spiritual growth.", 'child_spiritual_wisdom': 'Magizh, with Ketu placed in the 12th house of Virgo, your karmic life lesson is centered around spiritual wisdom. You are encouraged to detach from material desires and seek spiritual truths. Avoid getting lost in worldly matters and focus on deepening your spiritual understanding. Your destiny may involve seeking enlightenment and spiritual liberation, transcending worldly attachments and illusions.'}

    
    karmicTitle = {
        "child_responsibility_discipline": "Saturn's Life Lesson",
        "child_desire_ambition": "Rahu's Life Lesson",
        "child_spiritual_wisdom": "Ketu's Life Lesson"
    }
    for index,(k, v) in enumerate(con.items()):
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),karmicTitle[k],v,path)
                            
    pdf.AddPage(path,"Sadhe Sati Analysis")
    roundedBox(pdf,"#D2CEFF",20,pdf.get_y() + 5,pdf.w-40,40,5)
    pdf.set_font('Karma-Regular', '', 14)
    pdf.set_xy(22.5,pdf.get_y() + 6.5)
    pdf.set_text_color(0,0,0)
    pdf.multi_cell(pdf.w - 45,7,"Sadhe Sati refers to the seven-and-a-half-year period in which Saturn moves through three signs, the moon sign, one before the moon and the one after it. Sadhe Sati starts when Saturn (Shani) enters the 12th sign from the birth Moon sign and ends when Saturn leaves the 2nd sign from the birth Moon sign.",align='L')
        
    current_saturn = get_current_saturn_sign(saturn_pos)

    current_zodiac_signs = zodiac[zodiac.index(current_saturn['Sign']):] + zodiac[:zodiac.index(current_saturn['Sign'])]

    moon_index = current_zodiac_signs.index(moon['sign'])
    
    previous_sign = current_zodiac_signs[moon_index - 1] 
    next_sign = current_zodiac_signs[(moon_index + 1) % len(current_zodiac_signs)] 
     
    start_time = ""
    end_time = ""
    
    if current_saturn['Sign'] == moon['sign']:
        sadhesati_status = "yes"
        start_time = current_saturn['Start Date']
        end_time = current_saturn['End Date']
    elif previous_sign == current_saturn['Sign']:
        sadhesati_status = "yes"
        prev = saturn_pos[saturn_pos.index(current_saturn) + 1]
        start_time = prev['Start Date']
        end_time = prev['End Date']
        end_date = datetime.strptime(end_time, "%B %d, %Y")
        if end_date < datetime.now():
            sadhesati_status = "not" 
            saturn_pos.remove(saturn_pos[saturn_pos.index(current_saturn) + 1])
            next_saturn = get_next_sade_sati(saturn_pos,moon['sign'])
            start_time = next_saturn['Start Date']
            end_time = next_saturn['End Date']
    elif next_sign == current_saturn['Sign']:
        sadhesati_status = "yes"
        next = saturn_pos[saturn_pos.index(current_saturn) - 1]
        start_time = next['Start Date']
        end_time = next['End Date']
        end_date = datetime.strptime(end_time, "%B %d, %Y")
        if end_date < datetime.now():
            sadhesati_status = "not" 
            saturn_pos.remove(saturn_pos[saturn_pos.index(current_saturn) - 1])
            next_saturn = get_next_sade_sati(saturn_pos,moon['sign'])
            start_time = next_saturn['Start Date']
            end_time = next_saturn['End Date']
    else:
        sadhesati_status = "not" 
        next_saturn = get_next_sade_sati(saturn_pos,moon['sign'])
        start_time = next_saturn['Start Date']
        end_time = next_saturn['End Date']
        
    pdf.set_y(pdf.get_y() + 12.5)
    pdf.set_font('Karma-Heavy', '', 24)
    pdf.cell(0, 0, f"Presence of Sadhesati in {name}", align='C')
    pdf.set_y(pdf.get_y() + 10)
    pdf.set_font('Karma-Regular', '', 14)

    pdf.set_fill_color(hex_to_rgb("#F5E7D2"))
    pdf.set_draw_color(hex_to_rgb("#B26F0B"))
    pdf.rect(20, pdf.get_y(), pdf.w - 40, 70, corner_radius=10.0, round_corners=True, style='DF')
    
    pdf.image(f"{path}/babyImages/{sadhesati_status}.png", 25, pdf.get_y() + 20, 30, 30)

    x_start = 60 
    y_start = pdf.get_y() + 15
    pdf.set_xy(x_start, y_start)
    
    statusDetails = {
        "not" : f"{name} is not undergoing",
        "yes" : f"{name} is currently undergoing",
    }

    table_data = [
        ("Sadhesati Status:", f"{statusDetails[sadhesati_status]}"),
        ("Current Sign:", f"{current_saturn['Sign']}"),
        ("Child Moon Sign:", f"{moon['sign']}"),
        ("Except Date:", f"{start_time} - {end_time}")
    ]

    for row in table_data:
        pdf.cell(40, 10, row[0],new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.multi_cell(75, 10, row[1], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        y_start += 10
        pdf.set_xy(x_start, y_start)
        
    roundedBox(pdf,"#FFCEE0",20,pdf.get_y() + 25,pdf.w-40,80)
    pdf.set_xy(22.5,pdf.get_y() + 27.5)
    pdf.set_font('Karma-Semi', '', 18) 
    pdf.multi_cell(pdf.w - 45,8,"Sadhesati Overview and Effects",align='L')
    pdf.set_xy(22.5,pdf.get_y() + 2.5)
    pdf.set_font('Karma-Regular', '', 12) 
    pdf.multi_cell(pdf.w - 45,8,"       Sade Sati is a significant astrological period lasting seven and a half years, during which Saturn transits over the Moon's position and the two adjacent houses in a birth chart. This phase often brings challenges, including emotional stress, financial instability, and personal setbacks. The impact of Sade Sati can vary based on Saturn's placement and other planetary influences in the birth chart. Remedies such as performing Saturn-related pujas, wearing specific gemstones, and engaging in charitable activities can help alleviate the negative effects and provide support during this period.",align='L')

    
    pdf.AddPage(path,f"Life Stones and Benefic/Lucky Stones")

    fiveHouseLord = zodiac_lord[((zodiac.index(asc['sign']) + 5) % 12) - 1]
    
    
    stones = [Planet_Gemstone_Desc[asc['zodiac_lord']],Planet_Gemstone_Desc[ninthHouseLord],Planet_Gemstone_Desc[fiveHouseLord]]
    stoneName = [f'Life Stone','Benefictical Stone', 'Lucky Stone']

    content = [
        {
            "Why Life Stone" : "The Ascendant, or LAGNA, represents the self and all aspects tied to it, such as health, vitality, status, identity, and life direction. It embodies the core essence of existence. The gemstone associated with the LAGNESH, the ruling planet of the Ascendant, is known as the LIFE STONE. Wearing this stone throughout one’s life ensures access to its profound benefits and transformative energies.",
            "Description" : stones[0]['Description']
        },
        {
            "Why Benefictical Stone" : "The Fifth House in the birth chart is a highly favorable domain. It governs intellect, advanced learning, children, unexpected fortunes, and more. This house also represents the STHANA of PURVA PUNYA KARMAS, signifying rewards from past virtuous actions. Thus, it is regarded as a house of blessings. The gemstone linked to the lord of the Fifth House is known as the BENEFIC STONE.",
            "Description" : stones[1]['Description']
        },
         {
            "Why Lucky Stone" : "The Ninth House in a birth chart, known as the BHAGYA STHAANA or the House of Luck, symbolizes destiny and fortune. It governs success, achievements, wisdom, and the blessings earned through good deeds in past lives. This house reveals the rewards one is destined to enjoy. The gemstone associated with the lord of the Ninth House is aptly called the LUCKY STONE.",
            "Description" : stones[2]['Description']    
        }
    ]
    pdf.set_y(pdf.get_y() + 5)
    for index,stone in enumerate(content):
        if index != 0:  
            pdf.AddPage(path)
            pdf.set_y(20)
            
        if stones[index]['Gemstone'] == "Ruby" or stones[index]['Gemstone'] == "Red Coral" or stones[index]['Gemstone'] == "Emerald":
            pdf.image(f"{path}/babyImages/stone_bg.png",pdf.w / 2 - 22.5, pdf.get_y() + 40,45,0)   
        else:
            pdf.image(f"{path}/babyImages/stone_bg.png",pdf.w / 2 - 22.5, pdf.get_y() + 30,45,0)           
        pdf.image(f"{path}/babyImages/{stones[index]['Gemstone']}.png",pdf.w / 2 - 22.5, pdf.get_y() + 5,45,0)
        if stones[index]['Gemstone'] == "Ruby" or stones[index]['Gemstone'] == "Red Coral" or stones[index]['Gemstone'] == "Emerald":
            pdf.set_y(pdf.get_y() + 10)
        pdf.set_font('Karma-Heavy', '', 26)
        pdf.set_text_color(0,0,0)
        pdf.set_y(pdf.get_y() + 55)
        pdf.cell(0,0,f"{stoneName[index]} : {stones[index]['Gemstone']}",align='C')
        for k,v in stone.items():
            pdf.ContentDesign(random.choice(DesignColors),k,v,path)
    
    pdf.image(f'{path}/babyImages/end.png',(pdf.w / 2) - 15,pdf.get_y() + 20,30,0)
    
    pdf.AddPage(path,"Rudraksha Recommendations")
    pdf.image(f"{path}/babyImages/rudra.png",pdf.w / 2 - 32.5, 40,65,0)
    roundedBox(pdf,"#FDF0D5",25,110,pdf.w-50,37.5)
    pdf.set_xy(30,112)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Karma-Regular', '', 13)
    pdf.multi_cell(pdf.w - 60,8,f"Learn about your child's Rudraksha to improve various aspects of your life. Rudraksha beads have unique properties that, when worn near the heart, can affect your child brain in different ways depending on their type. This can help change your child's mood and mindset.",align='L')
    pdf.set_xy(22.5,pdf.get_y() + 5)
    pdf.set_font('Karma-Regular', '', 13)
    roundedBox(pdf,"#CCEAFF",25,167.5,pdf.w - 50,(pdf.no_of_lines(f"      {wealth_rudra[asc['sign']]}", pdf.w - 55) * 8) + 40)
    pdf.image(f"{path}/babyImages/{sign_mukhi[asc['sign']][0]}.png",pdf.w / 2 - 22.5 - 10, 175,20,0)
    pdf.image(f"{path}/babyImages/rudraPlus.png",pdf.w / 2 - 22.5 + 15, 180,10,0)
    pdf.image(f"{path}/babyImages/{sign_mukhi[asc['sign']][1]}.png",pdf.w / 2 - 22.5 + 30, 175,20,0)
    pdf.set_xy(pdf.w / 2 - 22.5 - 10,200)
    pdf.cell(20,0,f"{sign_mukhi[asc['sign']][0]}",align='C')
    pdf.set_xy(pdf.w / 2 - 22.5 + 25,200)
    pdf.cell(20,0,f"{sign_mukhi[asc['sign']][1]}",align='C')
    pdf.set_xy(27.5,205)
    pdf.multi_cell(pdf.w - 55,8,f"      {wealth_rudra[asc['sign']]}")
    
    pdf.AddPage(path,"Atma Karga & Ishta Devata ")
    roundedBox(pdf,"#FFD7D7",20,pdf.get_y() + 4,pdf.w - 40,50)
    pdf.set_font('Karma-Semi', '', 20)
    pdf.set_text_color(0,0,0)
    pdf.set_y(pdf.get_y() + 10)
    pdf.cell(0,0,'AtmaKaraka',align='C')
    pdf.set_text_color(hex_to_rgb("#940000"))
    pdf.set_font_size(12)
    pdf.set_xy(22.5,pdf.get_y() + 4)
    pdf.multi_cell(pdf.w - 45,8,"Atmakaraka, a Sanskrit term for 'soul indicator' is the planet with the highest degree in your birth chart. It reveals your deepest desires and key strengths and weaknesses. Understanding your Atmakaraka can guide you toward your true purpose and inspire meaningful changes in your life.",align='L')
    
    pdf.image(f"{path}/babyImages/atma_{atma['Name']}.jpeg",pdf.w / 2 - 22.5, 95,45,0)
    roundedBox(pdf,"#FFE7E7",45,182,pdf.w - 90,12)
    pdf.set_y(182)
    pdf.set_font('Karma-Semi', '', 20)
    pdf.cell(0,12,f"{atma['Name']} is your Atmakaraka",align='C')
    pdf.set_xy(22.5,200)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Karma-Regular', '', 18) 
    pdf.multi_cell(pdf.w - 45,8,f"      {athmakaraka[atma['Name']]}",align='L')
    
    pdf.AddPage(path,f"{name}'s Favourable God")
    roundedBox(pdf,"#D7FFEA",20,pdf.get_y() + 5,pdf.w-40,40)
    pdf.set_font('Karma-Regular', '', 14) 
    pdf.set_text_color(hex_to_rgb("#365600"))
    pdf.set_xy(22.5,pdf.get_y() + 7.5)
    pdf.multi_cell(pdf.w - 45,8,"       According to the scriptures, worshiping your Ishta Dev gives desired results. Determination of the Ishta Dev or Devi is determined by our past life karmas. There are many methods of determining the deity in astrology. Here, We have used the Jaimini Atmakaraka for Isht Dev decision.",align='L')

    pdf.set_text_color(0,0,0)
    pdf.image(f"{path}/images/{isthaDeva[0]}.jpeg",pdf.w / 2 - 22.5, pdf.get_y() + 15,45,0)
    pdf.set_y(pdf.get_y() + 100)
    pdf.set_font('Karma-Semi', '', 22)
    pdf.cell(0,0,f"{isthaDeva[0]}",align='C')
    pdf.set_draw_color(hex_to_rgb("#8A5A19"))
    pdf.set_xy(22.5,pdf.get_y() + 10)
    pdf.set_font('Karma-Regular', '', 12) 
    pdf.multi_cell(pdf.w - 45,8,f"      {ista_devata_desc[isthadevathaLord]}",align='L')
    
    pdf.add_page()
    pdf.image(f'{path}/babyImages/bg1.png',0,0,pdf.w,pdf.h)
    background_color = hex_to_rgb("#9D9CF9")  
    draw_gradient(pdf, 0, 0, pdf.w, 50, background_color,(255,255,255))
    pdf.set_text_color(hex_to_rgb("#168457"))   
    pdf.set_font('Karma-Heavy', '', 40)
    pdf.set_xy(10, 12)
    pdf.multi_cell(0, 14, f"{name}'s Development \nMile Stones")
    pdf.set_y(pdf.get_y() + 15)
    
    colors = ["#9D9CF9","#E8CEFF","#FFDCC3","#C3DBFF","#FFCEE0"]
    
    pdf.image(f"{path}/babyImages/dasa.png",110,25,90,0)
    
    # dasaOut = dasaPrompt(year,planets,dasa,name,gender)
    dasaOut = [{'dasa': 'Venus', 'bhukthi': 'Mars', 'age': "At Magizh's age, Between 1 to 2", 'prediction': {'insights': "During the Venus Dasa and Mars Bhukti period, Magizh may experience a mix of creativity and assertiveness in pursuing goals. The influence of Venus may bring harmony in relationships and a focus on aesthetics, while Mars' energy can drive ambition and determination. This period may enhance Magizh's social skills and leadership qualities, leading to opportunities for personal growth and achievement.", 'challenges': [{'title': 'Challenges in Communication', 'content': 'Magizh may face challenges in effectively expressing thoughts and emotions. There could be misunderstandings or conflicts in communication, leading to disruptions in relationships and professional interactions.'}, {'title': 'Struggles with Self-Confidence', 'content': 'Magizh might struggle with self-confidence and assertiveness during this period. Inner doubts and indecisiveness could hinder taking bold actions and seizing opportunities, impacting personal and professional growth.'}, {'title': 'Tendency towards Impulsiveness', 'content': 'Magizh may exhibit impulsive behavior and quick temperaments under the influence of Mars. This could lead to hasty decisions, conflicts, and strained relationships if not managed effectively.'}], 'precautions': [{'title': 'Develop Active Listening Skills', 'content': "Parents can encourage Magizh to practice active listening, where he focuses on understanding others' perspectives before responding. This can enhance communication and empathy, fostering healthier relationships and reducing conflicts."}, {'title': 'Encourage Mindfulness Practices', 'content': 'Parents can introduce mindfulness practices to help Magizh manage impulsiveness and enhance self-awareness. Guided meditation, deep breathing exercises, and mindfulness techniques can support Magizh in staying calm and making thoughtful decisions.'}], 'remedies': [{'title': 'Maintain a Balanced Diet', 'content': 'Encourage Magizh to follow a balanced diet rich in fresh fruits, vegetables, and whole grains to nurture physical and mental well-being. Adequate hydration and nutritious meals can support overall health and vitality during this period.'}, {'title': 'Chanting Venus and Mars Mantras', 'content': "Introduce Magizh to chanting Venus and Mars mantras like 'Om Shukraya Namaha' and 'Om Mangalaya Namaha' regularly. These sacred sounds can invoke the positive energies of the respective planets, balancing emotions and promoting harmony in relationships."}, {'title': 'Practice Creative Outlets', 'content': "Encourage Magizh to engage in creative outlets like painting, writing, or music to channel Venusian creativity and Mars' drive constructively. These activities can serve as outlets for expression, reduce stress, and boost confidence and self-expression."}]}}, {'dasa': 'Venus', 'bhukthi': 'Rahu', 'age': "At Magizh's age, Between 2 to 5", 'prediction': {'insights': "During the Venus Dasa and Rahu Bhukti period, Magizh is likely to experience a significant focus on relationships and spiritual growth. This period may bring unexpected changes and opportunities for personal transformation. Magizh's creativity and charm will be highlighted, leading to potential success in artistic pursuits or social endeavors. However, there may be some challenges related to confusion or deception in relationships and a tendency towards escapism. It is essential for Magizh to stay grounded and maintain clarity in decision-making during this time.", 'challenges': [{'title': 'Emotional Turmoil', 'content': 'Magizh may face emotional turbulence and inner conflicts, leading to uncertainty and mood swings during this period.'}, {'title': 'Relationship Struggles', 'content': 'There could be challenges in relationships, including issues of trust and misunderstandings that may create tension.'}, {'title': 'Spiritual Crisis', 'content': 'Magizh may experience a spiritual crisis, feeling disconnected or lost in the search for higher meaning and purpose.'}], 'precautions': [{'title': 'Mindful Communication', 'content': 'Encourage open and honest communication to prevent misunderstandings and conflicts in relationships. Practice active listening and empathy to foster deeper connections.'}, {'title': 'Emotional Stability Practices', 'content': 'Help Magizh develop emotional resilience through mindfulness practices, such as meditation and journaling, to navigate turbulent emotions and maintain inner balance.'}], 'remedies': [{'title': 'Meditation and Mindfulness', 'content': 'Encourage daily meditation practices to center the mind and cultivate inner peace. Mindfulness exercises can help Magizh stay present and grounded during challenging times.'}, {'title': 'Spiritual Healing Mantras', 'content': 'Introduce Magizh to sacred sounds and mantras for spiritual healing and protection. Reciting mantras like the Gayatri mantra or chanting Om can bring peace and clarity to the mind.'}, {'title': 'Healthy Boundaries', 'content': 'Teach Magizh the importance of setting healthy boundaries in relationships to maintain emotional well-being. Encourage self-care practices and assertiveness to protect against emotional overwhelm.'}]}}, {'dasa': 'Venus', 'bhukthi': 'Jupiter', 'age': "At Magizh's age, Between 5 to 8", 'prediction': {'insights': 'During the Venus Dasa and Jupiter Bhukti period, Magizh will experience a period of transformation and growth in various aspects of life. With Venus in the 1st house and Jupiter in the 7th house, there will be a focus on relationships and personal growth. Magizh may find opportunities for creative expression and spiritual development during this time. It is a period to cultivate harmony and balance in both personal and professional relationships, leading to overall well-being and fulfillment in life.', 'challenges': [{'title': 'Career Challenges', 'content': 'Magizh may face challenges related to career stability and opportunities for growth. There may be obstacles in career advancement and achieving professional goals during this period.'}, {'title': 'Emotional Challenges', 'content': 'Magizh may experience emotional ups and downs, leading to mood swings and inner turmoil. It is important to maintain emotional balance and seek support from loved ones during challenging times.'}, {'title': 'Health Challenges', 'content': 'There may be health challenges that Magizh needs to address during this period. It is essential to prioritize health and well-being through diet, exercise, and regular health check-ups.'}], 'precautions': [{'title': 'Communication Skills Development', 'content': 'Encourage Magizh to focus on improving communication skills to navigate challenges in relationships and career. Engage in activities that enhance verbal and written communication abilities.'}, {'title': 'Stress Management Techniques', 'content': 'Teach Magizh stress management techniques such as mindfulness, meditation, and relaxation exercises. Encourage taking breaks and practicing self-care to reduce stress levels.'}], 'remedies': [{'title': 'Regular Exercise Routine', 'content': 'Encourage Magizh to establish a regular exercise routine to maintain physical health and mental well-being. Engage in activities like yoga, walking, or dancing to stay active and reduce stress.'}, {'title': 'Meditation and Mindfulness Practices', 'content': 'Recommend incorporating meditation and mindfulness practices into daily routine to promote mental clarity and emotional stability. Encourage Magizh to spend time in quiet reflection and self-awareness.'}, {'title': 'Chanting Mantras for Peace', 'content': "Introduce Magizh to chanting mantras for peace and harmony. Encourage the repetition of sacred sounds like 'Om' or specific peace mantras to create a calming effect and enhance spiritual growth."}]}}]
    
    for i,dasaNow in enumerate(dasaOut):
        pdf.set_text_color(hex_to_rgb("#966A2F"))
        if i != 0:
            pdf.AddPage(path)
            pdf.set_y(20)
            pdf.set_text_color(0,0,0)
        
        pdf.set_xy(15,pdf.get_y() + 10)
        pdf.set_font('Karma-Heavy', '', 24)
        pdf.cell(0,0,f"{dasaNow['age']}",align='C')
        pdf.set_y(pdf.get_y() + 5)
        status = ""
        if dasaNow['bhukthi'] in dasa_status_table[dasaNow['dasa']][0]:
            status = "Favourable"
        elif dasaNow['bhukthi'] in dasa_status_table[dasaNow['dasa']][1]:
            status = "UnFavourable"
        else:
            status = "Moderate"
        pdf.cell(0,10,f"({status})",align='C')
        y = pdf.get_y() + 5
        pdf.set_font_size(14)
        pdf.set_fill_color(hex_to_rgb("#FFEED7"))
        pdf.rect(pdf.w / 2 - 30, pdf.get_y() + 10 , 60, 40,round_corners=True,corner_radius=5,style='F')
        pdf.set_xy(pdf.w / 2 - 30,pdf.get_y() + 11.5)
        pdf.cell(30,10,f"Dasa", align='C',new_y=YPos.TOP)
        pdf.set_x(pdf.w /2)
        pdf.cell(30,10,f"Bhukthi", align='C')
        pdf.image(f"{path}/babyImages/{dasaNow['dasa']}.png",pdf.w / 2 - 25,pdf.get_y() + 10, 20,20)
        pdf.image(f"{path}/babyImages/{dasaNow['bhukthi']}.png",pdf.w / 2 + 5,pdf.get_y() + 10, 20,20)
        pdf.set_xy(pdf.w / 2 - 30,pdf.get_y() + 28.5)
        pdf.multi_cell(30,10,f"{dasaNow['dasa']}", align='C',new_y=YPos.TOP)
        pdf.set_x(pdf.w / 2)
        pdf.multi_cell(30,10,f"{dasaNow['bhukthi']}", align='C')
        pdf.set_text_color(0,0,0)
        pdf.set_font('Karma-Regular', '', 14) 
        dasaContent = dasaNow['prediction']
        for index , (k, v) in enumerate(dasaContent.items()):
            if pdf.get_y() + 20 >= 260:  
                pdf.AddPage(path)
                pdf.set_y(20)
            
            pdf.ContentDesign("#FFEED7",k.capitalize(),v,path)
            
    planetContent = [
        {'remedies': [{'title': 'Engage in Physical Exercise', 'content': "Engage in physical activities like yoga, running, or any form of exercise to channelize the Sun's energy positively."}, {'title': 'Spend Time in Nature', 'content': 'Spend time outdoors in natural surroundings to connect with the healing energy of the Sun.'}], 'routine': [{'title': 'Morning Meditation', 'content': "Start your day with a morning meditation practice to align your mind and body with the Sun's energy."}, {'title': 'Journaling', 'content': "Maintain a journal to reflect on your thoughts and emotions, allowing the Sun's energy to guide your inner self."}], 'practice': [{'title': 'Surya Mantra Chanting', 'content': "Chant the Surya Mantra 'Om Hram Hreem Hroum Sah Suryaya Namaha' to invoke the energy of the Sun and bring positivity into your life."}, {'title': 'Surya Mudra', 'content': "Practice the Surya Mudra by touching the ring finger to the base of the thumb, enhancing your concentration and vitality with the Sun's energy."}, {'title': 'Chanting Gayatri Mantra', 'content': "Daily chanting of the powerful Gayatri Mantra 'Om Bhur Bhuvah Swaha, Tat Savitur Varenyam, Bhargo Devasya Dheemahi, Dhiyo Yo Nah Prachodayat' to attain spiritual enlightenment and strengthen your connection with the Sun."}]}
,
{'remedies': [{'title': 'Mindful Breathing', 'content': 'Practice deep and mindful breathing exercises to calm the mind and connect with inner emotions. Set aside 10 minutes every day to focus on your breath and bring awareness to the present moment.'}, {'title': 'Journaling', 'content': 'Start a journaling practice to express and release emotions. Write down your thoughts, feelings, and experiences regularly to gain clarity and insight into your emotional state.'}], 'routine': [{'title': 'Morning Meditation', 'content': 'Begin your day with a short meditation session to set a positive tone for the day. Sit in a quiet place, focus on your breath, and visualize a peaceful and harmonious day ahead.'}, {'title': 'Nature Walk', 'content': 'Spend time in nature every day to recharge and ground yourself. Take a walk in the park or garden, breathe in the fresh air, and appreciate the beauty of the natural surroundings.'}], 'practice': [{'title': 'Chandra Mantra', 'content': "Repeat the Chandra Mantra 'Om Chandraya Namaha' 108 times daily to invoke the blessings of the Moon and enhance emotional balance and intuition."}, {'title': 'Chandra Mudra', 'content': 'Perform the Chandra Mudra by placing the tip of the little finger on the base of the thumb and applying gentle pressure. Hold this mudra for 10 minutes to calm the mind and promote emotional stability.'}, {'title': 'Sacred Sounds Meditation', 'content': "Listen to sacred sounds such as Tibetan singing bowls or chants of the Moon mantra 'Shreem' to create a peaceful and harmonious atmosphere. Spend 15 minutes daily in sacred sounds meditation to align with the Moon's energy."}]} ,

{'remedies': [{'title': 'Embrace Nature Therapy', 'content': 'Spend time in nature regularly, such as going for walks in the park or gardening. Connect with the natural world to ground yourself and enhance your mental clarity.'}, {'title': 'Mindful Communication Practice', 'content': 'Practice active listening and thoughtful communication techniques in your interactions. Pay attention to your words and how they impact others to improve your relationships and express yourself effectively.'}], 'routine': [{'title': 'Morning Meditation', 'content': 'Start your day with a short meditation to calm your mind and set a positive tone for the day. Focus on your breath and be present in the moment to enhance mental clarity.'}, {'title': 'Journaling Reflection', 'content': 'Set aside time each day to write down your thoughts, feelings, and experiences. Reflect on your day and gain insights into your inner world for personal growth.'}], 'practice': [{'title': 'Mercury Mantra Chanting', 'content': "Chant the mantra 'Om Budhaya Namaha' to invoke the positive energy of Mercury. Sit in a comfortable position, focus on the sound vibrations, and let the mantra guide your thoughts and emotions."}, {'title': 'Mercury Mudra Practice', 'content': 'Perform the Mercury Mudra by joining the tips of your little finger, ring finger, and thumb while keeping the other fingers straight. Hold this mudra for a few minutes to enhance your communication skills and mental agility.'}, {'title': 'Sacred Sound Meditation', 'content': 'Listen to sacred sounds like the sound of bells or chimes to elevate your consciousness and connect with the divine energy of Mercury. Find a quiet space, close your eyes, and immerse yourself in the soothing vibrations.'}]} 
,
{'remedies': [{'title': 'Balanced Diet', 'content': "Maintain a diet rich in fruits, vegetables, and whole grains to nourish Venus's energy."}, {'title': 'Yoga and Meditation', 'content': 'Practice yoga and meditation daily to calm the mind and enhance artistic abilities.'}], 'routine': [{'title': 'Gratitude Journaling', 'content': 'Start a daily gratitude journal to cultivate a positive outlook and attract love and beauty into your life.'}, {'title': 'Creative Expression', 'content': "Engage in creative activities like painting, dancing, or singing to channel Venus's creativity."}], 'practice': [{'title': 'Venus Mantra', 'content': "Chant the mantra 'Om Shukraya Namaha' to invoke Venus's blessings and enhance relationships and artistic talents."}, {'title': 'Venus Mudra', 'content': 'Practice the Venus Mudra by joining the tips of the thumb, index, and middle fingers to balance emotions and enhance creativity.'}, {'title': 'Sacred Sound Bath', 'content': "Immerse yourself in the healing vibrations of sacred sounds like Tibetan singing bowls or crystal bowls to elevate Venus's energy and promote harmony."}]} 
,
{'remedies': [{'title': 'Transmute Energy through Physical Exercise', 'content': 'Engage in intense physical activities like weightlifting, martial arts, or high-intensity interval training to channel the aggressive Mars energy positively.'}, {'title': 'Practice Mindful Breathing Techniques', 'content': 'Incorporate deep breathing exercises like pranayama to calm the mind and balance the fiery Mars energy.'}], 'routine': [{'title': 'Journaling for Emotional Release', 'content': 'Start a daily journaling practice to express and release any pent-up emotions and thoughts, helping to maintain emotional balance.'}, {'title': 'Morning Meditation for Clarity', 'content': 'Begin each day with a short meditation session to center the mind and set positive intentions for the day ahead.'}], 'practice': [{'title': 'Mantra Chanting: Om Mangalaya Namaha', 'content': "Chant the mantra 'Om Mangalaya Namaha' to invoke the blessings of Mars and enhance courage, strength, and vitality."}, {'title': 'Mudra: Prana Mudra', 'content': 'Perform the Prana Mudra by joining the tips of the ring finger and little finger with the thumb to increase energy levels and improve concentration.'}, {'title': 'Sacred Sounds: Mars Yantra Meditation', 'content': "Visualize and meditate on the Mars Yantra while focusing on the sound 'Ram' to harness the powerful energy of Mars and balance aggression with harmony."}]}
,
{'remedies': [{'title': 'Meditation and Mindfulness', 'content': 'Practice daily meditation and mindfulness techniques to calm the mind and enhance focus. Set aside time each day for quiet reflection and deep breathing exercises.'}, {'title': 'Healthy Diet and Exercise', 'content': 'Maintain a healthy diet rich in fruits, vegetables, and whole grains. Regular exercise, such as yoga or brisk walking, will help in boosting energy levels and overall well-being.'}], 'routine': [{'title': 'Gratitude Journaling', 'content': 'Start a gratitude journal and jot down three things you are thankful for each day. This practice will cultivate a positive mindset and attract more abundance into your life.'}, {'title': 'Morning Affirmations', 'content': 'Begin your day with positive affirmations and intentions. Repeat empowering statements out loud to set the tone for a successful and fulfilling day.'}], 'practice': [{'title': 'Jupiter Mantra Chanting', 'content': "Chant the Jupiter mantra 'Om Brim Brihaspataye Namaha' 108 times daily to invoke the blessings and positive energy of Jupiter. Focus on the sound vibrations and feel the energy flowing within you."}, {'title': 'Jupiter Mudra', 'content': 'Practice the Jupiter mudra by touching the index finger to the thumb while keeping the other fingers straight. Hold this mudra for a few minutes daily to enhance intuition and wisdom.'}, {'title': 'Sacred Sounds Meditation', 'content': "Listen to sacred sounds such as Vedic chants or peaceful music that resonate with Jupiter's energy. Close your eyes, relax, and let the healing vibrations of these sounds elevate your spirit."}]}
,
{'remedies': [{'title': 'Mindfulness Meditation', 'content': 'Practice mindfulness meditation for 10-15 minutes daily to cultivate awareness and reduce stress. Focus on your breath and observe your thoughts without judgment.'}, {'title': 'Healthy Diet', 'content': 'Maintain a balanced diet with whole foods, plenty of fruits and vegetables, and stay hydrated. Limit processed and sugary foods for better physical and mental health.'}], 'routine': [{'title': 'Gratitude Journaling', 'content': "Start a gratitude journal and write down three things you're grateful for each day. This practice can help shift your focus to the positive aspects of your life."}, {'title': 'Physical Exercise', 'content': 'Incorporate regular physical exercise into your routine, such as yoga, walking, or dancing. Physical activity is essential for overall well-being and can boost your mood.'}], 'practice': [{'title': 'Saturn Mantra Chanting', 'content': "Chant the Saturn mantra 'Om Sham Shaneeshwaraya Namaha' 108 times daily to invoke Saturn's disciplined energy and bring stability and focus into your life."}, {'title': 'Shanmukhi Mudra', 'content': 'Practice the Shanmukhi Mudra by using your fingers to close the openings of your ears, eyes, nostrils, and mouth. This mudra helps in calming the mind and enhancing concentration.'}, {'title': 'Sacred Sounds Meditation', 'content': 'Listen to sacred sounds like Tibetan singing bowls or Gregorian chants for relaxation and spiritual connection. Allow the vibrations to resonate with your being and promote inner peace.'}]}
,
{'remedies': [{'title': 'Meditation and Mindfulness', 'content': 'Practice daily meditation and mindfulness exercises to calm the mind and reduce anxiety. Focus on the present moment and observe your thoughts without judgment.'}, {'title': 'Yoga and Pranayama', 'content': 'Engage in regular yoga and pranayama practices to balance the energy of Rahu. Incorporate deep breathing exercises to enhance mental clarity and inner peace.'}], 'routine': [{'title': 'Gratitude Journaling', 'content': 'Start a gratitude journal and write down three things you are grateful for each day. This practice will help shift your focus to positive aspects of life and increase overall happiness.'}, {'title': 'Creative Expression', 'content': "Explore a creative outlet such as painting, writing, or music to channel Rahu's energy positively. Expressing yourself creatively can provide a sense of fulfillment and release pent-up emotions."}], 'practice': [{'title': 'Rahu Mantra Chanting', 'content': "Chant the Rahu Mantra 'Om Rahave Namah' 108 times daily to invoke the positive energy of Rahu. This mantra can help enhance focus, ambition, and success in endeavors."}, {'title': 'Mudra Practice', 'content': 'Perform the Gyan Mudra by touching the tip of the index finger to the tip of the thumb while keeping the other three fingers straight. This mudra enhances concentration and balances the energy flow in the body.'}, {'title': 'Sacred Sounds Meditation', 'content': "Listen to sacred sounds like mantras, chanting, or spiritual music to create a peaceful and harmonious environment. This practice can elevate your mood and spiritual connection with Rahu's energy."}]},
{'remedies': [{'title': 'Cleansing Ritual', 'content': 'Perform a cleansing ritual using water and essential oils to purify the energy around you. This can help release any negative energy associated with Ketu in the 12th house of Virgo.'}, {'title': 'Journaling Practice', 'content': "Start a journaling practice to reflect on your thoughts and emotions. Writing down your feelings can help you understand and process them better, especially with Ketu's influence in the 12th house of Virgo."}], 'routine': [{'title': 'Mindfulness Meditation', 'content': "Practice mindfulness meditation for at least 10 minutes daily. This can help you stay grounded and present, especially with Ketu's energy in the 12th house of Virgo."}, {'title': 'Yoga Routine', 'content': "Incorporate a daily yoga routine focusing on grounding poses. This can help you connect with your body and inner self, aligning with Ketu's energy in the 12th house of Virgo."}], 'practice': [{'title': 'Chanting Mantra', 'content': "Chant the Ketu mantra 'Om Ketave Namaha' 108 times daily. This mantra can help activate Ketu's positive energy and bring clarity, especially with Ketu in the 12th house of Virgo."}, {'title': 'Mudra Practice', 'content': "Practice the Ketu mudra by touching the thumb to the ring finger while keeping the other fingers extended. This mudra can help balance Ketu's energy and promote spiritual growth, beneficial with Ketu in the 12th house of Virgo."}, {'title': 'Sound Healing', 'content': "Listen to sacred sounds like Tibetan singing bowls or chanting Om to cleanse and purify your energy field. This practice can help harmonize your energy with Ketu's influence in the 12th house of Virgo."}]}

]
    
    planetMain = {
        "Sun" : "Soul, Vitality, & Leadership Qualities",
        "Moon" : "Emotions, Intuition, Nurturing  Mind.",
        "Mars" : "Energy, Courage, Passion, and Assertiveness.",
        "Mercury" : "Communications, Intelligence, Adaptability.",
        "Jupiter" : "Wisdom, Expansion, Knowledge, Spirituality.",
        "Venus" :  "Love, Relationships, Beauty, Art, Comforts.",
        "Saturn" : "Discipline, Responsibility, Challenges.",
        "Rahu" :  "Desires, Ambitions, Worldly Attachment." ,
        "Ketu" : "Spirituality, Detachment, Past Life Influence." 
    }
    
    for index,planet in enumerate(planets):
        if planet['Name'] == "Ascendant":
            continue
        planets_table = table[planet['Name']]
        
        if planet['zodiac_lord'] in planets_table[0]:
            planet['status'] = "Favorable"
        elif planet['zodiac_lord'] in planets_table[1]:
            planet['status'] = "Unfavorable"
        else:
            planet['status'] = "Neutral"
            
        if index == 0:
            pdf.AddPage(path,f"Discipline, Habits, Diet, and Lifestyle Based on Planetary Energy")
        else:
            pdf.AddPage(path)
            
        pdf.set_text_color(hex_to_rgb("#966A2F"))
        pdf.set_font('Karma-Heavy', '', 20)
        pdf.set_xy(20,pdf.get_y() + 5)
        pdf.multi_cell(pdf.w - 40,10,f"{planet['Name']} - {planetMain[planet['Name']]}",align='C')
        pdf.set_draw_color(0,0,0)
        pdf.set_fill_color(hex_to_rgb(random.choice(DesignColors)))
        pdf.rect(20, pdf.get_y() + 5, pdf.w - 40, 60, corner_radius=10.0, round_corners=True, style='DF')
        pdf.image(f"{path}/babyImages/{planet['Name']}.png",30,pdf.get_y() + 10,50,50)
        pdf.set_font('Karma-Regular', '', 12) 
        pdf.set_text_color(0,0,0)
        
        x_start = 85
        y_start = pdf.get_y() + 15
        pdf.set_xy(x_start, y_start)

        table_data = [
            ("Sign:", f"{planet['sign']}"),
            ("House:", f"{number[planet['pos_from_asc']]} House"),
            ("Status:", f"{planet['status']}"),
            ("Significance:", f"{planet_quality[planet['Name']][0][planet['pos_from_asc']]}"),
        ]

        for row in table_data:
            pdf.set_font('Karma-Semi', '', 12)
            pdf.cell(30, 10, row[0],new_x=XPos.RIGHT, new_y=YPos.TOP)
            pdf.set_font('Karma-Regular', '', 12)
            pdf.multi_cell(0, 10, row[1], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            y_start += 10
            pdf.set_xy(x_start, y_start)
            
        pdf.set_y(pdf.get_y() + 20)
        
        planetTitle = {
            'strategies' : f"{planet['Name']} Insights",
            'remedies' : "Effective Remedies",
            'routine': "Holistic Routine",
            'practice': "Spiritual Practices",
        }
          
        # con = PlanetPrompt(planet,name,gender)
        con = planetContent[index - 1]
        for k, v in con.items():
            if pdf.get_y() + 40 >= 260:  
                pdf.AddPage(path)
                pdf.set_y(30)
                pdf.set_text_color(0,0,0)
            
            pdf.ContentDesign(random.choice(DesignColors),planetTitle[k],v,path)
            
    pdf.AddPage(path,"Important Checklist for Parents")
    
    pdf.set_y(pdf.get_y() + 12.5)

    pdf.set_y(pdf.get_y() + 10)
    pdf.set_font('Karma-Regular', '', 14)
    pdf.set_text_color(hex_to_rgb("#B26F0B"))

    pdf.set_fill_color(hex_to_rgb(random.choice(DesignColors)))
    pdf.set_draw_color(0,0,0)
    pdf.rect(20, pdf.get_y(), pdf.w - 40, 180, corner_radius=5.0, round_corners=True, style='DF')

    x_start = 30
    y_start = pdf.get_y() + 5
    pdf.set_xy(x_start, y_start)
    
    nakshatrasOrder = nakshatras[nakshatras.index(moon['nakshatra']):] + zodiac[:nakshatras.index(moon['nakshatra'])]
    favourableNakshatra = ""
    for index,nakshatra in enumerate(nakshatrasOrder):
        if index % 9 in [1,3,7]:
            favourableNakshatra += f"{nakshatra}, "
            
    pdf.set_text_color(0,0,0)

    luckyColor = nakshatraColor[moon['nakshatra']]
    
    table_data = [
        (f"Nakshatra:", f"{moon['nakshatra']}"),
        (f"Rasi:", f"{moon['sign']}"),
        (f"Lagnam:", f"{asc['sign']}"),
        ("Favorable Stars:", f"{favourableNakshatra}"),
        (f"Fortune Planets & Lord:", f"{ninthHouseLord}, {isthaDeva[0]}"),
        (f"Dopamine:", f"{panchang['karanam']} - {KaranaLord[panchang['karanam']]} for Achieve Goal"),
        (f"Serotonin:", f"{panchang['thithi']} - {thithiLord[panchang['thithi']]} for Emotional Intelligence"),
        (f"Oxytocin:", f"{panchang['yoga']} - {yogamLord[str(panchang['yoga_index'])]} for Body, Mind, Soul  Transformations "),
        (f"Favourable Times:", f"{favourableDasa}"),
        (f"Favourable Gem Stone:", f"{stones[0]['Gemstone']}, {stones[1]['Gemstone']}, {stones[2]['Gemstone']}"),
        (f"Lucky Color:",f"{luckyColor[0]}, {luckyColor[1]}, {luckyColor[2]}"),
        (f"Lucky Number:",f"{luckyNumber[0]}, {luckyNumber[1]}"),
    ]

    for row in table_data:
        pdf.set_font('Karma-Semi', '', 14)
        pdf.cell(65, 10, row[0], new_x=XPos.RIGHT, new_y=YPos.TOP)
        y_start = pdf.get_y()
        pdf.set_font('Karma-Regular', '', 14)
        pdf.multi_cell(90, 10, row[1],align='L')
        y_start = pdf.get_y()
        pdf.set_xy(x_start, y_start)

    pdf.AddPage(path,"Famous Celebrity Comparisons")
    
    # content = chapterPrompt(planets,8,name,gender)
    content = {'celebrities': [{'name': 'A. R. Rahman', 'field': 'Music', 'description': 'A. R. Rahman, born under Aries Rasi and Bharani Nakshatra, is an Oscar-winning music composer known for his soul-stirring compositions. His creativity and determination have made him a global icon in the music industry.'}, {'name': 'Anushka Sharma', 'field': 'Acting', 'description': 'Anushka Sharma, born under Aries Rasi and Bharani Nakshatra, is a successful Bollywood actress who has redefined the standards of acting in Indian cinema. Her strong willpower and passion for her craft have led her to great heights in the entertainment industry.'}, {'name': 'P. V. Sindhu', 'field': 'Badminton', 'description': 'P. V. Sindhu, born under Aries Rasi and Bharani Nakshatra, is an Olympic silver medalist and one of the top Indian badminton players. Her fierce determination and hard work have brought her numerous accolades in the world of sports.'}, {'name': 'Virat Kohli', 'field': 'Cricket', 'description': 'Virat Kohli, born under Aries Rasi and Bharani Nakshatra, is the captain of the Indian cricket team and one of the greatest cricketers of all time. His aggressive playing style and leadership skills have established him as a cricketing legend.'}, {'name': 'Deepika Padukone', 'field': 'Acting', 'description': 'Deepika Padukone, born under Aries Rasi and Bharani Nakshatra, is a versatile actress who has garnered acclaim for her performances in Bollywood. Her charisma and dedication to her craft have earned her a prominent place in the film industry.'}]}
    
    for celeb in content['celebrities']:
        if pdf.get_y() + 20 >= 260:
            pdf.AddPage(path)
            pdf.set_y(30)
            
        pdf.ContentDesign(random.choice(DesignColors),"",celeb,path)
        
    
    # content = chapterPrompt(planets,9,name,gender)
    content = {'predictions': "Magizh is born with a Libra lagna, which indicates a balanced and harmonious personality. The placement of Venus in the lagna enhances Magizh's charm and charisma. The presence of Venus as the lagna lord in the 1st house of Libra in Vishakha Nakshatra suggests a strong sense of beauty and artistic appreciation in Magizh's life. This placement also indicates a love for balance and harmony in relationships and surroundings.", 'assessment': "Magizh has a pleasant and diplomatic personality with a strong sense of aesthetics and a keen eye for beauty. The influence of Venus in the lagna and 1st house enhances Magizh's social skills and creativity.", 'strength': "Magizh's strength lies in their ability to maintain harmony in relationships, appreciate beauty in all forms, and express themselves artistically. They have a diplomatic approach towards handling conflicts and a natural charm that attracts others towards them.", 'weakness': 'However, Magizh may struggle with indecisiveness and a tendency to prioritize harmony over assertiveness. They may also face challenges in asserting their individuality in certain situations due to a strong desire for peace and balance.', 'action': 'To nurture Magizh, it is essential to encourage their creative pursuits, provide opportunities for self-expression, and help them develop assertiveness in communication and decision-making.', 'overall': "Overall, Magizh is a charming and diplomatic individual with a strong sense of aesthetics and a love for harmony in relationships. They thrive in environments that appreciate beauty and value peace and balance. Nurturing Magizh's creativity and supporting them in developing assertiveness will help them flourish in all aspects of life.", 'recommendations': 'Parenting suggestions for nurturing Magizh include encouraging artistic endeavors, providing opportunities for social interactions to enhance their diplomatic skills, and teaching them to assert their individuality when needed. It is important to support Magizh in finding a balance between harmony and self-expression, and to guide them in making confident decisions while maintaining their sense of beauty and diplomacy.'} 

    
    pdf.AddPage(path,f"Summary Insights for Parents and Child")
    
    for k, v in content.items():
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
            pdf.set_text_color(0,0,0)
        
        pdf.ContentDesign(random.choice(DesignColors),setTitle(k),v,path)
    
    pdf.output(f'{path}/pdf/{name} - babyReport.pdf')
    
def babyReport(dob,location,path,gender,name):
    print("Generating Baby Report")
    planets = find_planets(dob,location)
    print("Planets Found")
    panchang = calculate_panchang(dob,planets[2]['full_degree'],planets[1]['full_degree'],location)
    print("Panchang Calculated")
    for pl in planets:
        print(pl['Name'],pl['sign'],pl['nakshatra'],pl['full_degree'])
        
    for key in panchang.keys():
        print(key,panchang[key])
        
    value = str(input("Do you want to continue? (y/n)"))
    # value = "y"
    
    if value.lower() == 'y':
        dasa = calculate_dasa(dob,planets[2])
        print("Dasa Calculated")    
        # birthchart = generate_birth_navamsa_chart(planets,f'{path}/chart/',dob,location,name)
        birthchart = ""
        print("Birth Chart Generated")
        lat,lon = get_lat_lon(location)
        print("Lat Lon Found")
        dt = datetime.strptime(dob, "%Y-%m-%d %H:%M:%S")
        formatted_date = dt.strftime("%d %B %Y")
        formatted_time = dt.strftime("%I:%M:%S %p")
        
        year = int(dob[:4])
        month = int(dob.split("-")[1])
        
        generateBabyReport(formatted_date,formatted_time,location,lat,lon,planets,panchang,dasa,birthchart,gender,path,year,month,name)
    
    else:
        return "Report Generation Cancelled"
    
    # sender_email = "thepibitech@gmail.com"
    # receiver_email = "guruvijay1925@gmail.com"
    # password = "hprt rnur fesz diud" 
    # message = MIMEMultipart()
    # message["From"] = sender_email
    # message["To"] = receiver_email
    # message["Subject"] = "Life Prediction Report"

    # body = "Your Life Report"
    # message.attach(MIMEText(body, "plain"))
    
    # name = name.split(" ")[0]

    # pdf_filename = f"{path}/pdf/{name} - babyReport.pdf" 
    # with open(pdf_filename, "rb") as attachment:
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(attachment.read()) 
    #     encoders.encode_base64(part)  
    #     part.add_header(
    #         "Content-Disposition",
    #         f"attachment; filename= {os.path.basename(pdf_filename)}",
    #     )
    #     message.attach(part)  

    # try:
    #     server = smtplib.SMTP("smtp.gmail.com", 587)
    #     server.starttls() 
    #     server.login(sender_email, password)  
    #     server.sendmail(sender_email, receiver_email, message.as_string())  
    #     print("Email with PDF attachment sent successfully")
    # except Exception as e:
    #     print(f"Error sending email: {e}")
    # finally:
    #     server.quit()  
    
    # return "Sucess"

babyReport("1993-11-03 17:35:00","Madurai, Tamil Nadu , India",os.getcwd(),"male","Magizh Siranjeevi")