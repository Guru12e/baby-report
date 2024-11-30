import math
import random
from math import atan2, cos, radians, sin
from fpdf import FPDF,YPos
from index import find_planets
from panchang import calculate_panchang
from chart import generate_birth_navamsa_chart
from datetime import datetime
from index import get_lat_lon
from babyContent import context,chakras,characteristics,dasa_status_table,table,karagan,exaltation,athmakaraka,ista_devata_desc,ista_devatas,ista_images,saturn_pos,Sade_Sati_Analysis,constitutionRatio,Constitution,elements_data,elements_content,gemstone_content,Gemstone_about,Planet_Gemstone_Desc,career_rudra,health_rudra,wealth_rudra,sign_mukhi,planet_quality
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
            self.set_font('Karma-Heavy', '', 32)
            self.set_y(25)
            self.cell(0, 0, f"{title}", align='C') 
            
    def ContentDesign(self,color,title,content,path):
        self.set_text_color(0,0,0)
        self.set_y(self.get_y() + 5)
        self.set_font('Karma-Semi', '', 16)
        self.set_xy(22.5,self.get_y() + 5)
        if title != "":
            roundedBox(self, color, 20 , self.get_y()  - 2.5, self.w - 40, (self.no_of_lines(title,self.w - 45) * 7) + 10, 4)
            self.multi_cell(self.w - 45, 7,title, align='C')
        if isinstance(content, str):
            self.set_font('Karma-Regular', '', 14)
            self.set_xy(22.5,self.get_y() + 2.5)
            self.lineBreak(f"        {content}",path,color)
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
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40,titleWidth + contentWidth + 10, 0,status=False)
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
            
            if b['bhukthi'] in dasa_status_table[dasa][0]:
                self.set_fill_color(*hex_to_rgb("#DAFFDC"))
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
            roundedBox(self, color, 20 , self.get_y() , self.w - 40, self.no_of_lines(f"        {content}",self.w - 45) * 7 + 5, 4)
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
                        
    def draw_pie_slice(self, x_center, y_center, outer_radius, start_angle, end_angle, color, gap_angle = 1):
        self.set_fill_color(hex_to_rgb(color))
        adjusted_start_angle = start_angle + gap_angle / 2
        adjusted_end_angle = end_angle - gap_angle / 2

        x_start = x_center + outer_radius * math.cos(math.radians(adjusted_start_angle))
        y_start = y_center + outer_radius * math.sin(math.radians(adjusted_start_angle))
        points = [(x_center, y_center), (x_start, y_start)]

        steps = 100  
        for step in range(steps + 1):
            angle = adjusted_start_angle + (adjusted_end_angle - adjusted_start_angle) * step / steps
            x = x_center + outer_radius * math.cos(math.radians(angle))
            y = y_center + outer_radius * math.sin(math.radians(angle))
            points.append((x, y))

        self.polygon(points, style="F")

    
    def draw_pie_chart(self, x_center, y_center, outer_radius, data, colors,gap_angle = 1):
        total = sum(data.values())  
        start_angle = 0  

        for i, (label, value) in enumerate(data.items()):
            end_angle = start_angle + (value / total) * 360
            color = colors[i % len(colors)] 

            self.draw_pie_slice(x_center, y_center, outer_radius, start_angle, end_angle, color,gap_angle)
            start_angle = end_angle


    def draw_inner_circle(self, x_center, y_center, inner_radius, color):
        self.set_fill_color(*color)
        self.ellipse(x_center - inner_radius, y_center - inner_radius, 2 * inner_radius, 2 * inner_radius, style="F")
        
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
    
    def IndexPage(self,path,title,no):
        self.AddPage(path)
        self.set_font('Karma-Heavy', '', 28)
        self.set_text_color(hex_to_rgb("#966A2F"))
        self.set_y(self.get_y() + 30)
        self.multi_cell(0,10,title,align='C')
        self.image(f'{path}/babyImages/chapter{no}.png',(self.w / 2) - 50,(self.h / 2) - 50,100,0)
        self.set_xy(self.w - 85,self.h - 50)
        self.cell(0,10,"CHAPTER")
        self.set_font_size(64)
        self.set_xy(self.w - 35,self.get_y() - 3.5)
        self.cell(0,10,f"{no}")
            
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in range(0, 6, 2))
        
def generateBabyReport(formatted_date,formatted_time,location,lat,lon,planets,panchang,dasa,birthchart,gender,path,year,month,name = None):
    pdf = PDF('P', 'mm', 'A4')
    
    pdf.set_auto_page_break(True)
    
    pdf.add_font('Karma-Heavy', '', f'{path}/fonts/Merienda-Bold.ttf')
    pdf.add_font('Karma-Semi', '', f'{path}/fonts/Merienda-Regular.ttf') 
    pdf.add_font('Karma-Regular', '', f'{path}/fonts/Karma-Regular.ttf')
    
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
        if pdf.get_y() + (pdf.get_string_width(c['title']) / (pdf.w - 30))  >= 240:
            pdf.AddPage(path)
            pdf.set_y(30)
            
        pdf.set_font('Karma-Semi', '', 18)
        pdf.set_xy(30,pdf.get_y() + 5)
        pdf.multi_cell(pdf.w - 60,10,f"{context.index(c) + 1}. {c['title']}",align='L') 
        pdf.set_font('Karma-Regular', '', 14) 
    
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
    
    left_column_text = (
        'Name :\n'
        'Date Of Birth :\n'
        'Time Of Birth :\n'
        'Time Zone :\n'
        'Place Of Birth :\n'
        'Longitude & Latitude :\n'
        'Birth Star - Star Pada :\n'
        'Birth Rasi - Rasi Lord :\n'
        'Lagna (Ascentant) - Lagna Lord :\n'
        'Thidhi (Lunar Day) :\n'
        'week day :\n'
        'Sunrise :\n'
        'Sunset : \n'
        'Nakshatra Lord :\n'
        'Karanam :\n'
        'Yogam :\n'
    )

    right_column_text = (
        f"{name}\n"
        f"{formatted_date}\n"
        f"{formatted_time}\n"
        '05:30\n'
        f"{location}\n"
        f"{lat:.3f} {lon:.3f}\n"
        f"{panchang['nakshatra']} - {planets[1]['pada']}\n"
        f"{planets[1]['sign']} - {planets[1]['zodiac_lord']}\n"
        f"{planets[-1]['sign']} - {planets[-1]['zodiac_lord']}\n"
        f"{panchang['thithi']}\n"
        f"{panchang['week_day']}\n"
        f"{panchang['sunrise']}\n"
        f"{panchang['sunset']}\n"
        f"{planets[1]['nakshatra_lord']}\n"
        f"{panchang['karanam']}\n"
        f"{panchang['yoga']}\n"
    )

    pdf.multi_cell(90, 10, left_column_text, align='R')

    pdf.set_xy(110,60)
    pdf.set_font('Karma-Regular', '', 16)
    pdf.multi_cell(90, 10, right_column_text, align='L')
    
    name = name.split(" ")[0]
    
    pdf.AddPage(path)
    pdf.set_font('Karma-Heavy', '', 26)  
    pdf.set_y(30)
    pdf.cell(0,0,'Birth Chart',align='C')
    pdf.image(f'{path}/chart/{birthchart['birth_chart']}',(pdf.w / 2) - 45,pdf.get_y() + 10,90,90)
    # pdf.image(f'{path}/chart/1.png',(pdf.w / 2) - 45,pdf.get_y() + 10,90,90)
    pdf.set_y(145)
    pdf.cell(0,0,'Navamsa Chart',align='C')
    pdf.image(f'{path}/chart/{birthchart['navamsa_chart']}',(pdf.w / 2) - 45,pdf.get_y() + 10,90,90)
    # pdf.image(f'{path}/chart/1.png',(pdf.w / 2) - 45,pdf.get_y() + 10,90,90)
    pdf.set_y(pdf.get_y() + 110)

    pdf.set_font('Karma-Regular', '', 18) 
    for b in dasa[planets[1]['nakshatra_lord']]:
        if (b['start_year'] <= year <= b['end_year']):
            if not (year == b['end_year'] and b['end_month'] >= month):
                pdf.cell(0,0,f"Dasa : {planets[1]['nakshatra_lord']} Bhukthi : {b['bhukthi']}",align='C')
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
    
    pdf.draw_pie_chart(75,110, 35, elements, colors,gap_angle=0)
    pdf.draw_inner_circle(75, 110, 20, (255, 255, 255))
    
    y = 82.5
    for i,(label,value) in enumerate(elements.items()):
        pdf.set_fill_color(*hex_to_rgb(colors[i]))
        pdf.rect(130,y - 6,8,8,round_corners=True,corner_radius=5,style='F')
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
    
    pdf.AddPage(path,f"{name}'s Constitution")
    roundedBox(pdf,"#D7ECFF",20,pdf.get_y() + 9,pdf.w - 40,65)
    pdf.set_xy(22.5,pdf.get_y() + 10)
    pdf.set_font('Karma-Regular', '', 16) 
    pdf.set_text_color(0,0,0)
    pdf.multi_cell(pdf.w - 45,8,"       Acccording to ayurveda, On the basis of Vata,Pitta and Kapha, each child's body is of Vata Dominant and some of Pitta dominant. This is on the basis of the excess of dosha inside the body , its nature is determined.Here,We have tried to determine the ayurvedic nature on astrological basis. However this is no substitute for professional medical or ayurvedic advice. Please go only to an authorized doctor for any health-related treatment or Consultation.",align='L')
    
    moon = list(filter(lambda x : x['Name'] == "Moon",planets))[0]
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

    pdf.draw_pie_chart(75, 140, 35, data, colors)
    pdf.draw_inner_circle(75, 140, 20, (255, 255, 255))
    pdf.set_y(120)
    for i,(label,value) in enumerate(data.items()):
        pdf.set_fill_color(*hex_to_rgb(colors[i]))
        pdf.rect(135,pdf.get_y() - 6,8,8,round_corners=True,corner_radius=5,style='F')
        pdf.set_font('Karma-Semi', '', 18)
        pdf.set_text_color(*hex_to_rgb(colors[i]))
        pdf.text(150,pdf.get_y(),f'{label}: {value:.2f}%')
        pdf.set_y(pdf.get_y() + 20)
        
    pdf.set_xy(25,182.5)
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
        pdf.image(f"{path}/babyImages/chakra_{chakrasOrder.index(chakra) + 1}.png",pdf.w / 2 - 35,pdf.get_y() + 5,70,70)
        pdf.set_y(pdf.get_y() + 80)
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
    roundedBoxBorder(pdf,"#FFE769","#C5A200",20,y,planets[0]['Name'],planets[0]['sign'],path)
    roundedBoxBorder(pdf,"#D1C4E9","#A394C6",80,y,planets[-1]['Name'],planets[-1]['sign'],path)
    roundedBoxBorder(pdf,"#B3E5FC","#82B3C9",140,y,planets[1]['Name'],planets[1]['sign'],path)
    pdf.set_y(pdf.get_y() + 10)
    
    # content = chapterPrompt(planets,6,name,gender)
    content = {'child_personality': "Grishma's outward persona is grounded, analytical, and detail-oriented, reflecting their Virgo Lagnam. They possess a practical approach to life, with a keen eye for efficiency and organization. Grishma's physical attributes may exude a sense of modesty and a sliver of reserve, yet they communicate a sense of competence and reliability. In interactions, Grishma tends to be helpful and attentive, always seeking to improve and serve others with their diligent and meticulous nature.", 'emotional_needs': "Grishma's emotional needs, influenced by their Moon in the Fifth house of Capricorn, revolve around a desire for stability, structure, and recognition. They seek validation for their efforts and accomplishments, craving respect and appreciation. Grishma finds comfort in setting goals, pursuing ambitions, and establishing a secure foundation for their emotional well-being. The need for disciplined expression of creativity and a sense of purpose drives their inner emotional world.", 'core_identity': "At the core, Grishma's sense of self is shaped by the Sun in the Eighth house of Aries, infusing them with passion, intensity, and a profound urge for transformation. They aspire to embrace challenges, conquer obstacles, and delve deep into the mysteries of life. Grishma's motivations stem from a hunger for self-discovery, a desire for empowerment, and a relentless drive to uncover hidden truths. Their inner self radiates with courage, strength, and a transformative spirit that is not afraid to confront the darkness within and emerge stronger."}
    
    for index , (k, v) in enumerate(content.items()):
        if pdf.get_y() + 30 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(20)
            
        pdf.ContentDesign(random.choice(DesignColors),setTitle(k),v,path)
    
        
    pdf.AddPage(path)
    pdf.set_font('Karma-Heavy', '', 26) 
    
    pdf.set_xy(30,20)
    pdf.set_text_color(hex_to_rgb("#966A2F"))
    pdf.multi_cell(pdf.w - 60,10,"Panchangam : Your Child’s Path to Growth and Success",align='C')
    pdf.set_font("Karma-Regular", '', 14)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(22.5, pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 45, 7 ,"         Panchangam is an ancient Indian guide that helps understand a child's favorable and unfavorable times, aligning their actions with cosmic energies. Using Panchangam helps make better choices for growth, success, and well-being in areas like career, relationships, and spirituality. It serves as a roadmap for life's opportunities and challenges,namely:", align='L')
    pdf.set_font('Karma-Semi', '', 14)
    pdf.set_xy(60, pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 120, 8 , "• Tithi (Lunar Day)\n• Vara (Day of the Week)\n• Nakshatra (Lunar Constellation)\n• Yoga (Lunar-Solar Combination)\n• Karana (Half of a Tithi)", align='L')
    pdf.set_font('Karma-Regular', '', 14)
    
    colors = ["#E5FFB5","#94FFD2","#B2E4FF","#D6C8FF","#FFDECA"]    
    titles = ["Tithi - Your Child's Emotions, Mental Well-being","Varam - Your Child's Career, Energy, and Key Life Decisions","Nakshatra - Your Child's Personality and Life Path","Yogam - Your Child's Path to Prosperity ","Karanam  - Your Child's Actions & Work "]
    
    titleImage = ['waningMoon.png' if panchang['thithi_number'] <= 15 else 'waxingMoon.png','week.png','nakshatra.png','yogam.png','karanam.png']
        
    panchangTitle = [
        {
            "child_thithi_insights" : f"{name}'s Thithi is {panchang['paksha']} Paksha {panchang['thithi']}",
            "life_challenges" : "Life Challenges", 
            "actionable_remedies" : "Effective Remedies",
        },
        {
            "child_week_insights" : f"{name}'s week is {panchang['week_day']}", 
            "life_challenges" : "Life Challenges", 
            "actionable_remedies" : "Effective Remedies"
        },
        {
            "child_nakshatra_insights" : f"{name}'s Nakshatra is {panchang['nakshatra']}",
            "life_challenges" : "Life Challenges",
            "actionable_remedies" : "Effective Remedies"
        },
        {
            "child_yogam_insights" : f"{name}'s Yogam is {panchang['yoga']}", 
            "life_challenges" : "Life Challenges", 
            "actionable_remedies" : "Effective Remedies"
        },
        {
            "child_karanam_insights" : f"{name}'s Karanam is {panchang['karanam']}",
            "life_challenges" : "Life Challenges", 
            "actionable_remedies" : "Effective Remedies"
        }
    ]
    
    content = [
        {'child_thithi_insights': 'Grishma was born on Krishna Paksha Ashtami, indicating that they possess a sharp intellect, creative thinking, and a strong sense of independence. They are likely to be practical, goal-oriented, and have a natural leadership quality. Emotionally, they may experience inner conflicts between their desire for personal freedom and the need for emotional connection in relationships. However, they have the ability to overcome challenges with their determination and focus.', 'life_challenges': 'Grishma may face challenges in maintaining a balance between their personal goals and emotional relationships. They may struggle with impatience and a tendency to be overly critical of themselves and others. It is important for them to work on managing their emotions effectively and nurturing supportive relationships to avoid feeling isolated or detached.', 'actionable_remedies': [{'title': 'Mindfulness Meditation Physical Activity Physical Activity Physical Activity', 'content': 'Encourage Grishma to practice mindfulness meditation for 10-15 minutes daily to quiet their mind, reduce stress, and improve emotional regulation.'}, {'title': 'Journaling', 'content': 'Suggest Grishma keep a journal to write down their thoughts and emotions, helping them gain clarity, identify patterns, and release pent-up feelings.'}, {'title': 'Physical Activity', 'content': 'Encourage Grishma to engage in regular physical activity like yoga, dancing, or walking to release emotional tension, improve mood, and boost overall well-being.'}, {'title': 'Healthy Communication Skills', 'content': 'Guide Grishma to work on developing healthy communication skills to express their emotions effectively, set boundaries, and build harmonious relationships.'}, {'title': 'Self-compassion Practice', 'content': 'Urge Grishma to practice self-compassion by being kind and forgiving towards themselves, acknowledging their worth, and embracing their strengths and flaws with love and acceptance.'}]},
        {'child_week_insights': 'Grishma was born on Tuesday, which is ruled by the planet Mars. Children born on Tuesday are often known for their courage, leadership qualities, and determination. They tend to be energetic, assertive, and driven individuals who excel in competitive environments. Grishma may possess a strong sense of independence and a natural ability to take charge of situations. This Vaaram can instill a sense of passion and motivation in the child to pursue their goals with vigor.', 'life_challenges': "However, being born on Tuesday, Grishma may also face challenges related to impulsiveness, aggression, and a tendency to be quick-tempered. It's important to channel this energetic and assertive nature positively to avoid conflicts and misunderstandings. Additionally, the influence of Mars can sometimes lead to a lack of patience and a tendency to act impulsively, which may hinder long-term decision-making and relationships.", 'actionable_remedies': [{'title': 'Mindful Meditation', 'content': 'Encourage Grishma to practice mindful meditation daily to calm the mind, reduce impulsiveness, and improve focus. This practice will help the child channel their energy positively and cultivate patience and clarity in decision-making.'}, {'title': 'Physical Exercise and Sports', 'content': 'Engage Grishma in physical activities and sports to channel their energy constructively. Regular exercise not only improves physical health but also helps in releasing pent-up emotions and reducing aggressive tendencies. Sports can teach the child teamwork, discipline, and sportsmanship.'}, {'title': 'Anger Management Techniques', 'content': 'Teach Grishma anger management techniques and coping strategies to deal with moments of frustration and anger. Encourage deep breathing exercises, counting to 10 before reacting, and expressing emotions through writing or art. These techniques will help the child regulate emotions and respond thoughtfully in challenging situations.'}, {'title': 'Yoga Practice', 'content': 'Introduce Grishma to yoga practice, which combines physical postures, breathing techniques, and meditation. Yoga can help in balancing energy, promoting relaxation, and enhancing emotional well-being. The child will learn to connect mind and body, leading to inner peace and emotional stability.'}, {'title': 'Stress-Relief Activities', 'content': "Incorporate stress-relief activities like painting, listening to music, or spending time in nature in Grishma's routine. These activities can help the child unwind, release tension, and recharge. Creating a peaceful environment and encouraging self-care practices will promote emotional balance and resilience."}]},
        {'child_nakshatra_insights': 'Grishma, born under the Dhanishta Nakshatra, is likely to be ambitious, determined, and creative. They possess leadership qualities and have a strong sense of responsibility. Grishma may excel in artistic or creative endeavors and have a knack for innovation. However, they may also be prone to impulsiveness and may need to balance their desire for success with patience and practicality.', 'life_challenges': 'One of the potential life challenges for Grishma born under Dhanishta Nakshatra could be struggles with authority figures or dealing with power dynamics. They may find it challenging to navigate hierarchical structures and may face resistance from those in positions of power. It is important for Grishma to learn how to assert themselves confidently while respecting authority.', 'actionable_remedies': [{'title': 'Meditation and Mindfulness Practices', 'content': 'Encourage Grishma to practice daily meditation and mindfulness exercises to cultivate inner peace and clarity. This can help reduce impulsiveness and enhance focus and self-awareness.'}, {'title': 'Yoga and Physical Exercise', 'content': "Regular yoga practice and physical exercise can help channel Grishma's energy positively, reduce stress, and improve overall well-being. It can also enhance discipline and control over emotions."}, {'title': 'Journaling and Self-Reflection', 'content': 'Encourage Grishma to maintain a journal for self-reflection. By writing down thoughts and feelings, they can gain insight into their emotions and behaviors, leading to personal growth and self-awareness.'}, {'title': 'Seek Mentorship and Guidance', 'content': 'Grishma may benefit from seeking mentorship or guidance from experienced individuals in their field of interest. This can provide valuable insights, advice, and support in navigating challenges and achieving their goals.'}, {'title': 'Connect with Nature', 'content': 'Spending time in nature can help Grishma ground themselves, find peace, and gain perspective. Encourage regular outdoor activities, such as hiking or gardening, to foster a deeper connection with the natural world.'}]},
        {'child_yogam_insights': "Grishma, born under the Brahma Yogam, is destined for creativity, wisdom, and leadership. They possess a strong sense of spirituality and a natural inclination towards intellectual pursuits. Their Yogam signifies a deep connection to the divine and a desire to seek knowledge and understanding. Grishma's journey will be filled with opportunities for growth and self-realization, leading them towards a path of enlightenment and fulfillment.", 'life_challenges': 'However, Grishma may face challenges in maintaining balance between their spiritual pursuits and the practical aspects of life. They might struggle with doubt and indecisiveness at times, and the pressure to fulfill their spiritual duties while navigating the material world could cause inner conflict and confusion.', 'actionable_remedies': [{'title': 'Meditation and Mindfulness Practices', 'content': 'Encourage Grishma to incorporate daily meditation and mindfulness practices into their routine. This will help them stay grounded, calm their mind, and connect with their inner wisdom and spirituality.'}, {'title': 'Creative Expression', 'content': 'Encourage Grishma to express their creativity through art, writing, or music. This will help them channel their spiritual energy and emotions, foster self-expression, and enhance their sense of fulfillment and purpose.'}, {'title': 'Yoga and Physical Exercise', 'content': 'Encourage Grishma to practice yoga or engage in regular physical exercise to maintain a healthy mind-body connection. Physical activity will help them release stress, improve focus, and boost their overall well-being, aligning with their spiritual journey.'}, {'title': 'Journaling and Reflection', 'content': 'Encourage Grishma to keep a journal for self-reflection and introspection. This practice will help them gain clarity, understand their thoughts and emotions, and track their spiritual growth and insights over time.'}, {'title': 'Volunteer and Service Work', 'content': 'Encourage Grishma to engage in volunteer or service work to connect with others on a spiritual level. Giving back to the community and helping those in need will deepen their sense of compassion, gratitude, and purpose, aligning with their Yogam.'}]},
        {'child_karanam_insights': 'Grishma, born under the Kaulava Karanam, is likely to be energetic, ambitious, and perseverant in her pursuits. She is skilled at problem-solving, possesses a strong work ethic, and approaches tasks with precision and focus. Grishma thrives in environments that require innovation and creativity, often excelling in leadership roles due to her decisive nature and ability to inspire others.', 'life_challenges': 'However, Grishma may face challenges related to impatience, stubbornness, and a tendency to be overly critical of herself and others. These traits can lead to conflicts in relationships and hinder her personal growth and success.', 'actionable_remedies': [{'title': 'Practice Patience and Mindfulness', 'content': 'Encourage Grishma to practice mindfulness and cultivate patience in her daily life. This can be achieved through activities like meditation, deep breathing exercises, or yoga, which help her stay calm and focused in challenging situations.'}, {'title': 'Develop Empathy and Understanding', 'content': 'Guide Grishma to work on developing empathy and understanding towards others. Encourage her to actively listen, consider different perspectives, and practice compassion to improve her relationships and communication skills.'}, {'title': 'Seek Feedback and Self-Reflection', 'content': 'Encourage Grishma to seek feedback from trusted sources and engage in self-reflection. This will help her gain valuable insights into her strengths and areas for improvement, leading to personal growth and enhanced self-awareness.'}, {'title': 'Set Realistic Goals and Prioritize Tasks', 'content': 'Help Grishma set realistic goals and prioritize tasks to avoid feeling overwhelmed. Break down larger tasks into smaller manageable steps, create a schedule, and focus on one task at a time to enhance productivity and reduce stress.'}, {'title': 'Practice Gratitude and Positivity', 'content': 'Encourage Grishma to practice gratitude and focus on the positive aspects of her life. Keeping a gratitude journal, expressing appreciation towards others, and shifting her mindset towards positivity can enhance her overall well-being and resilience.'}]}
    ]

    
    pdf.set_text_color(0,0,0)
    pdf.set_y(pdf.get_y() + 5)
    for i in range(0,5):
        if i != 0:
            pdf.AddPage(path)
            pdf.set_y(20)
        con = content[i]
        # con = panchangPrompt(panchang,i,name,gender)
        pdf.image(f"{path}/babyImages/{titleImage[i]}",pdf.w / 2 - 10,pdf.get_y(),20,20) 
        pdf.set_xy(45,pdf.get_y() + 30)
        pdf.set_font('Karma-Semi', '', 18)
        roundedBox(pdf, "#62DAFF", 40 , pdf.get_y() - 2.5 , pdf.w - 80, (pdf.no_of_lines(titles[i],pdf.w - 85) * 8) + 5, 5)
        pdf.multi_cell(pdf.w - 90,8,f"{titles[i]}",align='C')
        pdf.set_font('Karma-Regular', '', 14)
        pdf.set_text_color(0, 0, 0)
        
        for index , (k, v) in enumerate(con.items()):
            if pdf.get_y() + 30 >= 260:  
                pdf.AddPage(path)
                pdf.set_y(20)
                
            pdf.ContentDesign(colors[i],f"{panchangTitle[i][k]}",v,path)    
            
    pdf.IndexPage(path,"Physical Attributes, Personality,\n and Behavior",1)
    
    # content1 = physical(planets,1,name,gender)
    # content2 = physical(planets,2,name,gender)
    # content3 = physical(planets,3,name,gender)
    # content4 = physical(planets,4,name,gender)
    
    content1 = "The child with Virgo lagna and Mercury in Pisces in Revati Nakshatra might have a slim and delicate body built. They could have a graceful and gentle appearance with a soft oval or round face. Their eyes may be large, expressive, and watery, giving them a dreamy and sensitive look. The child may exude a calm and serene aura, adding to their compassionate and imaginative nature. Overall, they may have a charming and ethereal physical presence that captures attention effortlessly."
        
    content2 = {'outer_personality': 'Grishma is a child with a solid and structured outer personality. They may exhibit qualities of determination, discipline, and responsibility. Their physical appearance may be characterized by a mature and serious demeanor, with a focus on achieving their goals.', 'character': [{'title': 'Determined and Goal-Oriented', 'content': 'Grishma is likely to be highly determined and focused on their goals, with a strong sense of ambition and perseverance.'}, {'title': 'Responsible and Disciplined', 'content': 'Grishma shows traits of responsibility and discipline in their actions, taking their duties seriously and striving for excellence.'}, {'title': 'Mature and Serious', 'content': "Grishma's outer persona may exude a sense of maturity and seriousness, displaying wisdom beyond their years."}, {'title': 'Structured and Organized', 'content': 'Grishma is inclined towards a structured and organized approach in their activities, preferring order and methodical planning.'}, {'title': 'Independent and Self-Reliant', 'content': 'Grishma tends to exhibit independence and self-reliance in their behavior, seeking to handle challenges on their own.'}], 'behaviour': [{'title': 'Reserved and Observant', 'content': 'Grishma may display a reserved nature, observing their surroundings keenly before actively engaging with others.'}, {'title': 'Methodical Decision-Making', 'content': 'Grishma approaches decision-making in a methodical manner, weighing the pros and cons before reaching a conclusion.'}, {'title': 'Patient and Persistent', 'content': 'Grishma exhibits patience and persistence in their endeavors, persevering through challenges with a calm and determined attitude.'}, {'title': 'Focused and Detail-Oriented', 'content': "Grishma's behavior reflects a focused and detail-oriented approach, paying attention to the intricacies of tasks and projects."}, {'title': 'Pragmatic and Realistic', 'content': 'Grishma tends to be pragmatic and realistic in their outlook, preferring practical solutions over idealistic notions.'}], 'negative_impact': [{'title': 'Rigid and Inflexible', 'content': 'Grishma may struggle with rigidity and inflexibility, finding it challenging to adapt to changing circumstances or alternative perspectives.'}, {'title': 'Overly Serious', 'content': "Grishma's seriousness may sometimes lead to a lack of lightheartedness and playfulness, impacting their ability to relax and enjoy leisure activities."}, {'title': 'Overly Critical', 'content': 'Grishma could exhibit a tendency towards being overly critical, both of themselves and others, which may strain interpersonal relationships.'}, {'title': 'Stubbornness', 'content': "Grishma's stubborn nature may hinder their ability to collaborate and compromise, leading to conflicts in social interactions."}, {'title': 'Conventional Thinking', 'content': "Grishma's adherence to conventional thinking may limit their creativity and innovative problem-solving skills, hindering out-of-the-box solutions."}], 'parenting_tips': [{'title': 'Encourage Flexibility and Adaptability', 'content': 'To help Grishma overcome rigidity, encourage activities that promote flexibility and adaptability, such as engaging in diverse hobbies or trying new experiences regularly.'}, {'title': 'Cultivate a Sense of Humor', 'content': "Introduce humor and light-heartedness into Grishma's environment to balance out their seriousness and promote a more relaxed attitude towards life."}, {'title': 'Foster Open Communication', 'content': 'Promote open communication with Grishma to address their tendency towards criticism, encouraging constructive feedback and mutual understanding in interactions.'}, {'title': 'Encourage Teamwork and Collaboration', 'content': 'Provide opportunities for Grishma to engage in group activities that emphasize teamwork and collaboration, fostering skills in cooperation and compromise.'}, {'title': 'Support Creative Exploration', 'content': 'Encourage Grishma to explore creative outlets and unconventional thinking to broaden their perspectives and enhance their problem-solving abilities.'}]}
    
    content3 = {'inner_worlds': "Grishma's inner emotional world is deeply influenced by their astrological placements, including their Moon Sign in Dhanishta Nakshatra, Mars in the 5th House of Capricorn, Saturn in the 4th House of Sagittarius, and Mercury in the 7th House of Pisces.", 'emotional_needs': [{'title': 'Structured Stability', 'content': 'Grishma thrives in environments that provide structure, routine, and stability. Predictability and clear boundaries help them feel secure and grounded.'}, {'title': 'Intellectual Stimulation', 'content': 'Grishma craves mental stimulation, engaging activities, and opportunities to learn and grow intellectually. Introducing new concepts and encouraging exploration can fulfill this need.'}, {'title': 'Emotional Expression', 'content': 'Grishma benefits from spaces where they can freely express their emotions without judgment. Encouraging open communication and validating their feelings nurtures their emotional well-being.'}, {'title': 'Independence and Autonomy', 'content': 'Grishma values autonomy and independence. Allowing them to make choices, take responsibility, and assert their individuality fosters their confidence and self-esteem.'}, {'title': 'Creative Outlets', 'content': "Grishma's inner world is enriched by creative outlets such as art, music, or imaginative play. Providing opportunities for self-expression through creativity is essential for their emotional fulfillment."}], 'impact': [{'title': 'Overthinking and Anxiety', 'content': 'Grishma may struggle with overthinking and anxiety due to their analytical nature. It is essential to help them manage stress, practice mindfulness, and develop coping mechanisms.'}, {'title': 'Control Issues', 'content': "Grishma's need for structure and stability can sometimes lead to control issues. Encouraging flexibility, adaptability, and teaching them to let go of the need for control can support their emotional growth."}, {'title': 'Emotional Bottling', 'content': 'Grishma may suppress emotions at times, leading to emotional bottling. Creating a safe space for them to express their feelings and teaching healthy emotional release strategies is crucial.'}, {'title': 'Seeking Perfection', 'content': "Grishma's quest for perfection can create inner pressure and self-criticism. Encouraging self-compassion, embracing mistakes as learning opportunities, and nurturing self-acceptance is vital."}, {'title': 'Difficulty in Trusting Others', 'content': "Grishma's independence may make it challenging for them to trust others deeply. Building trust through consistent support, honest communication, and demonstrating reliability is key."}], 'remedies': [{'title': 'Establishing a Routine', 'content': 'Create a consistent daily routine that provides structure and stability for Grishma. Include designated times for learning, play, emotional expression, and relaxation.'}, {'title': 'Mindfulness Practices', 'content': 'Introduce Grishma to mindfulness practices such as deep breathing, meditation, or yoga to help them manage anxiety, improve focus, and cultivate inner calm.'}, {'title': 'Encouraging Creative Exploration', 'content': "Support Grishma's creative pursuits by providing art supplies, musical instruments, or other outlets for self-expression. Encourage them to explore different forms of creativity."}, {'title': 'Promoting Emotional Intelligence', 'content': "Teach Grishma about emotions, empathy, and effective communication. Encourage them to identify and express their feelings, understand others' perspectives, and resolve conflicts peacefully."}, {'title': 'Building Trust through Reliability', 'content': 'Demonstrate consistency and reliability in your interactions with Grishma. Keep your promises, listen attentively, and show genuine care and support to foster trust and emotional connection.'}]}
    
    content4 ={'core_identity': "Grishma's core identity is influenced by their Virgo Lagna, Pisces Moon in Dhanishta nakshatra, and Aries Sun in Bharani nakshatra. This combination creates a blend of analytical, imaginative, and assertive traits in their personality. Grishma may have a practical approach to life, a deep emotional nature, and a strong will to pursue their desires.", 'recognitions': [{'title': 'Need for Acknowledgment', 'content': 'Grishma seeks acknowledgment through their analytical abilities and attention to detail. They strive for recognition by showcasing their practical problem-solving skills and efficient work ethic, earning appreciation for their precision and dedication.'}, {'title': 'Desire for Validation', 'content': 'Grishma craves validation for their creativity and assertiveness. They yearn for approval of their innovative ideas and assertive actions, seeking validation for their leadership qualities and independent spirit.'}, {'title': 'Yearning for Respect', 'content': 'Grishma desires respect for their emotional depth and intuition. They seek recognition for their intuitive insights and emotional intelligence, aiming to be valued for their sensitivity and compassion towards others.'}, {'title': 'Recognition for Courage', 'content': 'Grishma yearns for acknowledgment of their boldness and determination. They seek recognition for their courage to take risks and face challenges head-on, striving to be appreciated for their fearless and pioneering spirit.'}, {'title': 'Appreciation for Communication Skills', 'content': 'Grishma values acknowledgment for their communication prowess. They seek recognition for their ability to express ideas effectively and engage others in meaningful conversations, aiming to be appreciated for their clarity and eloquence in speech.'}],  'remedies': [{'title': 'Mindfulness Practices', 'content': 'Grishma can benefit from mindfulness practices such as meditation and yoga to enhance self-awareness and emotional balance. These practices can help them cultivate inner peace, reduce stress, and develop a deeper connection with their inner self, promoting a sense of emotional well-being and clarity of thought.'}, {'title': 'Journaling for Self-reflection', 'content': 'Grishma can engage in journaling as a tool for self-reflection and introspection. Writing down thoughts, emotions, and experiences can help them understand their inner world better, gain insights into their emotions and behaviors, and foster self-awareness and personal growth.'}, {'title': 'Setting Boundaries', 'content': 'Grishma may benefit from setting clear boundaries in relationships and work settings to maintain a healthy balance between giving and receiving. Establishing boundaries can help them protect their emotional well-being, assert their needs and values, and cultivate self-respect and healthy relationships.'}, {'title': 'Seeking Professional Guidance', 'content': 'Grishma can seek professional guidance from a therapist or counselor to explore and address their emotional needs and inner conflicts. Therapy sessions can provide a safe space for self-exploration, emotional healing, and developing coping strategies to manage stress and enhance emotional well-being.'}, {'title': 'Engaging in Creative Outlets', 'content': 'Grishma can explore creative outlets such as art, music, or dance to channel their emotions and express their inner creativity. Engaging in creative activities can serve as a therapeutic outlet, allowing them to express their emotions, enhance self-expression, and tap into their imaginative potential for personal growth and fulfillment.'}]}

    
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
    
    pdf.AddPage(path)
    pdf.set_y(30)
    pdf.set_text_color(0,0,0)
        
    for index,c in enumerate(content):
        if pdf.get_y() + 40 >= 260:
            pdf.AddPage(path)
            pdf.set_y(30)
        pdf.set_text_color(0, 0, 0)
        if isinstance(c, str):
            pdf.set_font('Karma-Semi', '', 18)
            pdf.set_xy(45,pdf.get_y() + 20)
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
                    
    pdf.IndexPage(path,"Health & Wellness",2)
    pdf.AddPage(path)
    pdf.set_y(30)
    pdf.set_font('Karma-Heavy', '', 28)
    pdf.set_text_color(0, 0, 0)
    pdf.set_y(30)
    pdf.cell(0,0,"Health & Wellness",align='C')
    # con = healthPrompt(planets,0,name,gender)        
    con = {'health_insights': "Based on the child's astrology details, we can see a complex interplay of planets and houses influencing the child's health. The placement of Mars in the 5th house of Capricorn, Saturn in the 4th house of Sagittarius, and Mercury in the 7th house of Pisces indicates a mix of energy and communication-related health challenges. The presence of Moon, Mars, and Ketu in the 5th and 8th houses may also bring emotional and digestive health concerns. Overall, the child may need to focus on balancing these energies to maintain good health and well-being.", 'challenges': [{'title': 'Digestive Disorders', 'content': 'The presence of Ketu in the 6th house of Aquarius and Moon in the 5th house of Capricorn indicates potential digestive issues that the child may face.'}, {'title': 'Emotional Instability', 'content': "The placement of Moon, Mars, and Ketu in the 5th and 8th houses suggests emotional challenges that may impact the child's mental well-being."}, {'title': 'Communication Issues', 'content': 'With Mercury in the 7th house of Pisces, the child may experience communication difficulties or speech-related disorders.'}, {'title': 'Skin Problems', 'content': 'The influence of Mars in the 5th house of Capricorn could lead to skin-related issues like acne or rashes.'}, {'title': 'Joint Pains', 'content': 'The presence of Saturn in the 4th house of Sagittarius may indicate potential joint-related problems that the child may encounter.'}], 'natural_remedies': [{'title': 'Aloe Vera Gel', 'content': 'Aloe vera gel can help soothe digestive issues and promote healthy digestion.'}, {'title': 'Tulsi Leaves', 'content': 'Tulsi leaves have antibacterial properties that can aid in managing skin problems and promoting overall well-being.'}, {'title': 'Ginger Tea', 'content': 'Ginger tea can be beneficial for improving digestion and alleviating joint pains.'}, {'title': 'Neem Oil', 'content': 'Neem oil is known for its anti-inflammatory properties and can help with skin issues.'}, {'title': 'Triphala Powder', 'content': 'Triphala powder can support digestive health and detoxification of the body.'}], 'nutrition_tips': [{'title': 'Probiotic-Rich Foods', 'content': "Include probiotic-rich foods like yogurt and kefir in the child's diet to support gut health."}, {'title': 'Omega-3 Fatty Acids', 'content': 'Ensure the child consumes sources of omega-3 fatty acids like fish, flaxseeds, or chia seeds for overall wellness.'}, {'title': 'Leafy Greens', 'content': 'Incorporate leafy greens like spinach and kale to provide essential nutrients for skin health and overall vitality.'}, {'title': 'Turmeric', 'content': 'Add turmeric to meals for its anti-inflammatory properties, beneficial for joint health.'}, {'title': 'Healthy Fats', 'content': 'Include sources of healthy fats like avocados and nuts to support brain function and overall well-being.'}], 'wellness_routines': [{'title': 'Yoga and Meditation', 'content': 'Encourage the child to practice yoga and meditation to reduce stress, improve mental clarity, and promote emotional balance.'}, {'title': 'Daily Exercise', 'content': 'Engage in daily physical activities to strengthen the body, improve digestion, and boost overall immunity.'}, {'title': 'Ayurvedic Massage', 'content': 'Regular ayurvedic massages using herbal oils can help relax the body, improve circulation, and support skin health.'}, {'title': 'Breathing Exercises', 'content': 'Teach the child simple breathing exercises to enhance lung capacity, reduce anxiety, and promote overall well-being.'}, {'title': 'Sound Therapy', 'content': 'Introduce sound therapy techniques like listening to calming music or sounds to promote relaxation and emotional well-being.'}], 'lifestyle_suggestions': [{'title': 'Balanced Diet', 'content': 'Ensure the child follows a balanced diet rich in nutrients to support overall health and address specific health challenges.'}, {'title': 'Adequate Hydration', 'content': 'Encourage the child to stay hydrated by drinking enough water throughout the day for optimal digestion and skin health.'}, {'title': 'Regular Sleep Patterns', 'content': 'Establish consistent sleep routines to promote restful sleep, mental clarity, and emotional stability.'}, {'title': 'Limit Screen Time', 'content': 'Set boundaries on screen time to reduce eye strain, improve sleep quality, and support overall well-being.'}, {'title': 'Outdoor Activities', 'content': 'Encourage outdoor activities to boost physical health, mental well-being, and overall vitality.'}], 'preventive_tips': [{'title': 'Regular Check-ups', 'content': "Schedule regular health check-ups to monitor the child's well-being and address any health concerns proactively."}, {'title': 'Stress Management', 'content': 'Teach stress management techniques to help the child cope with emotional challenges and maintain mental well-being.'}, {'title': 'Good Hygiene Practices', 'content': 'Promote good hygiene practices like frequent handwashing to prevent infections and maintain overall health.'}]}


    pdf.set_text_color(0, 0, 0)
    for k, v in con.items():
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),setTitle(k),v,path)
        
    pdf.IndexPage(path,"Education And Intelligence",3)
                        
    pdf.AddPage(path)
    pdf.set_font('Karma-Heavy', '', 28)
    pdf.set_text_color(0, 0, 0)
    pdf.set_y(30)
    pdf.cell(0,0,f"{name}'s Education &  Academics",align='C')
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
    con = {'insights': "Based on Grishma's astrology chart, she has a strong foundation for education and intellectual pursuits. Her planets and house placements indicate a natural inclination towards learning and cognitive development. Grishma is likely to excel in academic endeavors and possess unique cognitive abilities that align with her natural talents and interests.", 'suitable_educational': [{'title': 'Psychology', 'content': 'Grishma could excel in psychology due to her deep understanding of human behavior and emotions.'}, {'title': 'Engineering', 'content': 'Engineering could be a suitable field for Grishma, given her analytical skills and practical approach to problem-solving.'}, {'title': 'Creative Writing', 'content': 'Grishma may have a talent for creative writing, expressing her thoughts and ideas eloquently.'}, {'title': 'Fine Arts', 'content': 'Fine arts could be a fulfilling pursuit for Grishma, allowing her to explore her creativity and artistic talents.'}, {'title': 'Astrology', 'content': 'With her strong planetary influences, Grishma could have a natural affinity for astrology and a deep understanding of cosmic energies.'}, {'title': 'Medical Science', 'content': 'Grishma may have a knack for medical science, with a keen interest in healing and wellness.'}, {'title': 'Computer Science', 'content': 'Computer science could be a rewarding field for Grishma, leveraging her logical thinking and problem-solving abilities.'}], 'cognitive_abilities': [{'title': 'Analytical Thinking', 'content': 'Grishma possesses strong analytical thinking skills, enabling her to dissect complex problems and find effective solutions.'}, {'title': 'Emotional Intelligence', 'content': 'Grishma has a high level of emotional intelligence, allowing her to empathize with others and navigate social interactions with ease.'}, {'title': 'Creativity', 'content': 'Grishma exhibits creativity in her approach to tasks and problem-solving, thinking outside the box to generate innovative ideas.'}, {'title': 'Attention to Detail', 'content': 'Grishma pays attention to detail, ensuring accuracy and precision in her work and academic pursuits.'}, {'title': 'Logical Reasoning', 'content': 'Grishma demonstrates logical reasoning abilities, making sound judgments and decisions based on rational thinking.'}], 'recommendations': [{'title': 'Utilize Mind Mapping Techniques', 'content': 'Grishma can benefit from mind mapping techniques to visualize complex concepts and enhance her understanding of subjects.'}, {'title': 'Practice Active Recall', 'content': 'Engaging in active recall techniques can help Grishma retain information better and improve her long-term memory.'}, {'title': 'Develop a Study Routine', 'content': 'Creating a consistent study routine will assist Grishma in staying organized and dedicated to her academic goals.'}, {'title': 'Participate in Group Discussions', 'content': "Joining group discussions and study sessions can enhance Grishma's communication skills and broaden her knowledge through collaborative learning."}, {'title': 'Seek Mentorship', 'content': 'Grishma should seek mentorship from professionals in her field of interest to gain insights and guidance for her academic and career pursuits.'}]}
    
    pdf.set_text_color(0, 0, 0)
    
    for index,(k, v) in enumerate(con.items()):
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),educationTitle[k],v,path)
        
    pdf.IndexPage(path,"Family And Relationship",4)
    
    pdf.AddPage(path)
    # con = physical(planets,5,name,gender)
    con = {'family_relationship': "Based on Grishma's astrological placements, her social development, friendship dynamics, and family relationships are influenced by the positions of the 11th House, 7th House, Sun, Moon, and Venus. Grishma's approach to relationships with her parents, siblings, and peers is shaped by these planetary influences, leading to specific challenges and opportunities in her social and family interactions.", 'approaches': [{'title': 'Nurturing Friendships', 'content': 'Grishma may naturally excel in forming and maintaining friendships due to the supportive influences of the 11th House, enhancing her social circle and bringing joy through peer interactions.'}, {'title': 'Strong Family Bonds', 'content': 'With a harmonious placement of Venus in the 9th House, Grishma is likely to have close relationships with family members, especially siblings, fostering a sense of unity and mutual support within the family.'}, {'title': 'Effective Communication', 'content': 'Mercury in the 7th House empowers Grishma with effective communication skills, aiding in building meaningful connections with others, including her parents and peers.'}, {'title': 'Emotional Connections', 'content': 'The presence of Moon in the 5th House suggests that Grishma values emotional connections in her relationships, seeking nurturing and supportive interactions with loved ones.'}], 'challenges': [{'title': 'Overcoming Shyness', 'content': 'Grishma may struggle with shyness or hesitancy in forming new relationships, necessitating encouragement and support in social settings to overcome barriers to connection.'}, {'title': 'Balancing Independence and Dependence', 'content': 'The influence of Saturn in the 4th House may pose challenges in balancing independence and dependence within family dynamics, requiring conscious effort to maintain healthy boundaries.'}, {'title': 'Navigating Emotional Sensitivity', 'content': "Grishma's emotional sensitivity, indicated by Moon in the 5th House, can lead to challenges in managing emotions in relationships, requiring tools for emotional regulation and communication."}, {'title': 'Conflict Resolution Skills', 'content': 'The presence of Mars in the 5th and 8th Houses suggests the need for developing conflict resolution skills, particularly in family dynamics, to navigate disagreements effectively and maintain harmony.'}, {'title': 'Peer Pressure and Influence', 'content': 'Rahu in the 11th House may expose Grishma to peer pressure and influence, posing challenges in decision-making and maintaining individuality within friendships and social circles.'}], 'parenting_support': [{'title': 'Encouraging Social Activities', 'content': "Parents can support Grishma's social development by encouraging participation in group activities, clubs, or team sports to enhance her interpersonal skills and broaden her social network."}, {'title': 'Open Communication Channels', 'content': 'Creating open communication channels within the family can help Grishma express her thoughts and emotions freely, fostering deeper connections and understanding with parents and siblings.'}, {'title': 'Emotional Regulation Techniques', 'content': 'Teaching Grishma emotional regulation techniques, such as mindfulness exercises or journaling, can aid in managing her emotional sensitivity and navigating challenging situations with peers and family members.'}, {'title': 'Building Conflict Resolution Skills', 'content': 'Parents can role model and teach Grishma healthy conflict resolution strategies, such as active listening and compromise, to empower her in resolving conflicts constructively and maintaining positive relationships.'}, {'title': 'Empowering Individuality', 'content': 'Encouraging Grishma to embrace her individuality and unique perspectives can help her navigate peer pressure and influence, fostering confidence in her own identity and decisions within social interactions.'}]}
    
    familyTitle = {
        'family_relationship' : "Family Relationships and Social Development",
        'approaches': "Child’s Approaches for Forming Relationships",
        'challenges' : "Challenges in the child's  relationship & social development",
        'parenting_support' : "Parenting Support for Improve Child’s Social Developments"
    }
    
    for k, v in con.items():
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),familyTitle[k],v,path)
        
    pdf.IndexPage(path,"Career And Professions",5)
        
    pdf.AddPage(path)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Karma-Heavy', '', 28)
    pdf.set_text_color(0, 0, 0)
    pdf.set_y(30)
    pdf.cell(0,0,"Career & Professions",align='C')
    pdf.set_font('Karma-Semi','', 16)
    pdf.set_xy(20,pdf.get_y() + 10)
    pdf.multi_cell(pdf.w - 40,8,"Wondering what the future holds for your child's career journey?",align='L')
    # con = chapterPrompt(planets,4,name,gender)
    con = {'career_path': 'Based on the astrological positions of planets and houses for Grishma, it is predicted that their career path will be strongly influenced by their natural talents, abilities, and interests. The positions of Mars, Saturn, Mercury, Jupiter, and other planets indicate a potential for success in specific fields. Their Janma Nakshatra, Rashi, and Lagna Lords provide insights into suitable career paths and business potentials.', 'suitable_professions': [{'title': 'Marketing Manager in Technology Sector', 'content': 'Grishma has strong leadership qualities indicated by the placement of Mars in the 5th house. This suits roles like Marketing Manager where strategic planning and execution are crucial.'}, {'title': 'Financial Analyst in Banking Sector', 'content': 'With the influence of Saturn in the 4th house, Grishma may excel in analytical roles like Financial Analyst in the Banking sector, utilizing their attention to detail.'}, {'title': 'Software Developer in IT Industry', 'content': 'Mercury in the 7th house suggests proficiency in communication and technology, making Software Development a suitable career choice for Grishma.'}, {'title': 'Entrepreneur in Creative Industry', 'content': 'The placement of Jupiter in the 2nd house and Venus in the 9th house indicates entrepreneurial skills, especially in the Creative industry.'}, {'title': 'Psychologist in Healthcare Sector', 'content': 'The influence of Moon, Mars, and Ketu in the 5th and 8th houses suggests a potential interest in Psychology, particularly in the Healthcare sector.'}, {'title': 'Human Resources Manager in Corporate Sector', 'content': 'With Rahu in the 11th house and Moon in the 5th house, Grishma may thrive in people-oriented roles like Human Resources Manager in the Corporate sector.'}, {'title': 'Consultant in Social Services Sector', 'content': 'The placement of Sun in the 8th house and Saturn in the 4th house indicates a strong sense of responsibility, ideal for a Consultant role in the Social Services sector.'}], 'business': [{'title': 'Digital Marketing Agency', 'content': "Grishma's prowess in strategic planning and leadership, as indicated by Mars in the 5th house, could lead to success in establishing a Digital Marketing Agency."}, {'title': 'Financial Consultancy Firm', 'content': 'Utilizing the analytical skills suggested by Saturn in the 4th house, Grishma could excel in starting a Financial Consultancy Firm.'}, {'title': 'Tech Startup', 'content': 'With a strong inclination towards technology and communication skills highlighted by Mercury in the 7th house, Grishma may thrive in starting a Tech Startup.'}, {'title': 'Creative Design Studio', 'content': 'The entrepreneurial skills indicated by Jupiter in the 2nd house and Venus in the 9th house make Grishma suitable for starting a Creative Design Studio.'}, {'title': 'Wellness Center', 'content': 'Given the interest in Psychology, Healthcare, and people-oriented roles, a Wellness Center focusing on mental health could be a successful business venture for Grishma.'}]}

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
            
    pdf.IndexPage(path,"Subconscious Mind",6)
                        
    pdf.AddPage(path)
    # con = chapterPrompt(planets,5,name,gender)
    con = {'subconscious_mind': "Based on Grishma's astrology details, their subconscious mind may have limiting beliefs related to self-worth, communication, relationships, and emotions due to the placements of planets in different houses. There may be fears surrounding authority figures, responsibilities, and expressing emotions openly. It's essential to address these subconscious beliefs to overcome obstacles and achieve success.", 'personalized_affirmations': [{'title': 'Self-Worth Affirmation', 'content': 'I am worthy of love, success, and abundance. I embrace my unique qualities and value.'}, {'title': 'Communication Affirmation', 'content': 'I express myself clearly and confidently. My voice is powerful and valuable.'}, {'title': 'Relationship Affirmation', 'content': 'I attract positive and loving relationships into my life. I deserve healthy connections.'}, {'title': 'Emotional Healing Affirmation', 'content': 'I allow myself to feel and release emotions. I am worthy of inner peace and emotional balance.'}, {'title': 'Success Affirmation', 'content': 'I am capable of achieving my goals and dreams. Success follows me in everything I do.'}], 'visualizations': [{'title': 'Self-Love Visualization', 'content': 'Visualize a bright light surrounding you, filling you with love and acceptance. See yourself radiating confidence and self-worth.'}, {'title': 'Clear Communication Visualization', 'content': 'Imagine a stream of clear water flowing through your throat chakra, helping you communicate with clarity and honesty.'}, {'title': 'Healthy Relationship Visualization', 'content': 'Visualize yourself surrounded by a circle of light, attracting positive and supportive relationships that align with your highest good.'}, {'title': 'Emotional Release Visualization', 'content': 'Picture a release of colorful balloons symbolizing your emotions lifting away, leaving you feeling light and free.'}, {'title': 'Success Manifestation Visualization', 'content': 'Visualize yourself achieving your greatest success, feeling the emotions of accomplishment and fulfillment.'}], 'meditations': [{'title': 'Self-Worth Meditation', 'content': "Sit in a comfortable position, close your eyes, and repeat the affirmation 'I am worthy' with each breath. Feel a sense of worthiness filling your being."}, {'title': 'Communication Meditation', 'content': 'Focus on your throat chakra during meditation, visualizing it glowing with blue light. Imagine speaking your truth with ease and confidence.'}, {'title': 'Relationship Healing Meditation', 'content': 'Imagine a pink light of love surrounding your heart chakra during meditation. Send love to yourself and others, healing past relationship wounds.'}, {'title': 'Emotional Balance Meditation', 'content': 'Sit in meditation and observe your emotions without judgment. Allow them to flow and release, bringing inner peace and balance.'}, {'title': 'Success Visualization Meditation', 'content': 'Visualize yourself achieving your goals during meditation. Feel the emotions of success and abundance filling your being.'}]}

    subTitle = {
        "subconscious_mind" : "Child’s SubConscious Mind Insights",
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
        
    pdf.AddPage(path)
    
    uniqueTitle = {
        'insights': "Childs Unique Talents & Natural Values ", 
        'education' : "Unique Talents in Academics ", 
        'arts_creative' :"Unique Talents in Arts & creativity ",
        'physical_activity': "Unique Talents in Physical Activity"
    }
    # con = chapterPrompt(planets,0,name,gender)
    con = {'insights': 'Grishma, with a Virgo ascendant and Mercury placed in the 7th House of Pisces, possesses a blend of analytical and intuitive abilities. Their intellectual prowess is heightened by a strong connection to imaginative realms, enhancing their communication skills and creative problem-solving. The positioning of Jupiter in the 2nd House of Libra further amplifies their sense of harmony and beauty, leading to a balanced approach in various aspects of life. Mars in the 5th House of Capricorn, alongside Moon and Ketu, ignites a passion for ambitious pursuits and emotional depth. Saturn in the 4th House of Sagittarius instills a sense of responsibility and discipline in family matters and foundations.', 'education': [{'title': 'Analytical Mind', 'content': 'Grishma displays a natural talent for analytical thinking and logical reasoning, excelling in subjects that require systematic approaches and critical analysis.'}, {'title': 'Creative Communication', 'content': 'Their ability to express ideas creatively and intuitively makes them proficient in language arts, writing, and public speaking, captivating audiences with their unique style.'}, {'title': 'Adaptive Learning', 'content': "Grishma's flexible learning style allows them to adapt quickly to new environments and concepts, facilitating continuous growth and knowledge acquisition."}, {'title': 'Research Aptitude', 'content': 'With a keen interest in delving deep into subjects, Grishma demonstrates excellent research skills and a thirst for uncovering hidden truths and unconventional perspectives.'}, {'title': 'Versatile Education', 'content': 'Their diverse interests and versatile nature enable Grishma to excel in a wide range of subjects, showcasing adaptability and a holistic approach to learning.'}], 'arts_creative': [{'title': 'Harmonious Expressions', 'content': "Grishma's artistic talents shine through in their ability to create harmonious compositions, be it in music, art, or design, reflecting their innate sense of balance and aesthetics."}, {'title': 'Emotional Artistry', 'content': 'Their creative expressions are deeply rooted in emotional resonance, allowing them to convey complex feelings and experiences through various artistic mediums with profound impact.'}, {'title': 'Innovative Imagination', 'content': "Grishma's imaginative prowess fuels their innovative spirit, leading to unique and original creations that push boundaries and inspire others in the artistic realm."}, {'title': 'Aesthetic Appreciation', 'content': 'With a natural eye for beauty and aesthetics, Grishma possesses a keen sense of visual harmony and design, influencing their creative endeavors with elegance and style.'}, {'title': 'Expressive Storytelling', 'content': 'Their storytelling abilities are marked by vivid imagery, evocative narratives, and a gift for weaving compelling tales that captivate and enchant their audience.'}], 'physical_activity': [{'title': 'Energetic Pursuits', 'content': "Grishma's physical activities are characterized by high energy levels and a zest for movement, excelling in dynamic sports and outdoor adventures that challenge their physical abilities."}, {'title': 'Mindful Movement', 'content': 'Their approach to physical hobbies involves a mindful connection between body and mind, emphasizing balance, flexibility, and coordination in activities like yoga, dance, or martial arts.'}, {'title': 'Competitive Spirit', 'content': 'Grishma thrives in competitive environments, showcasing determination, resilience, and a drive to excel in sports and games that test their endurance and strategic thinking.'}, {'title': 'Adventure Seeker', 'content': 'Their passion for exploration and excitement leads Grishma to engage in adrenaline-pumping activities, seeking new thrills and experiences that push their boundaries and ignite their adventurous spirit.'}, {'title': 'Team Player', 'content': 'In group sports and collaborative activities, Grishma demonstrates strong teamwork skills, social awareness, and a natural ability to synchronize with others, fostering a sense of unity and camaraderie in shared physical pursuits.'}]}

    for index,(k, v) in enumerate(con.items()):
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),uniqueTitle[k],v,path)
        
        
    pdf.AddPage(path)
    pdf.set_font('Karma-Heavy', '', 28)
    pdf.set_y(30)
    pdf.cell(0,0,"Karmic Life Lessons ",align='C')
    pdf.set_y(pdf.get_y() + 5)
        
    # con = chapterPrompt(planets,7,name,gender)
    con = {'child_responsibility_discipline': "Grishma's karmic life lessons related to Saturn are influenced by Saturn's placement in the 4th house of Sagittarius. This placement indicates that Grishma's life lessons revolve around establishing a sense of emotional security and stability within the family. Saturn here emphasizes the importance of responsibility, discipline, and hard work in building a strong foundation for emotional fulfillment. Grishma is likely to face challenges that test their patience and perseverance in creating a harmonious home environment. It is crucial for Grishma to embrace responsibilities with maturity and dedication, fostering a sense of stability and security for themselves and their loved ones. Avoiding escapism or neglecting family duties will be key to navigating Saturn's karmic influence in a positive light.", 'child_desire_ambition': "Grishma's karmic life lessons related to Rahu stem from Rahu's placement in the 11th house of Cancer. This positioning signifies a strong desire for social recognition, material wealth, and fulfillment of ambitious aspirations. Grishma may possess a natural drive for success and achievement, seeking to establish themselves in social circles and pursue their goals with determination. However, Rahu's influence can lead to obsessions with status and material possessions, creating a tendency towards self-centeredness and manipulation in pursuit of desires. Grishma should be cautious of becoming overly fixated on external validation and material gains, prioritizing genuine connections and ethical pursuits over superficial achievements to balance Rahu's karmic lessons.", 'child_spiritual_wisdom': "Grishma's karmic life lessons related to Ketu are shaped by Ketu's placement in the 5th house of Capricorn. This placement indicates a strong emphasis on spiritual growth, inner wisdom, and detachment from material pursuits. Grishma is likely to possess an innate wisdom and a deep introspective nature, prioritizing introspection and self-discovery over external gratifications. Ketu's influence in the 5th house encourages Grishma to seek spiritual fulfillment through creative expression, education, and cultivating a sense of inner purpose. It is essential for Grishma to embrace detachment from ego-driven desires and societal expectations, focusing on inner spiritual wisdom and self-realization. Avoiding attachment to external validations and worldly pleasures will be crucial in navigating Ketu's karmic influence positively."}
    
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
                            
    pdf.AddPage(path,"Sadhesati Analysis")
    roundedBox(pdf,"#D2CEFF",20,35,pdf.w-40,40,5)
    pdf.set_font('Karma-Regular', '', 14)
    pdf.set_xy(22.5,36.5)
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
        sadhesati_status = ""
        start_time = current_saturn['Start Date']
        end_time = current_saturn['End Date']
    elif previous_sign == current_saturn['Sign']:
        sadhesati_status = ""
        prev = saturn_pos[saturn_pos.index(current_saturn) + 1]
        start_time = prev['Start Date']
        end_time = prev['End Date']
        end_date = datetime.strptime(end_time, "%B %d, %Y")
        if end_date < datetime.now():
            sadhesati_status = "not " 
            saturn_pos.remove(saturn_pos[saturn_pos.index(current_saturn) + 1])
            next_saturn = get_next_sade_sati(saturn_pos,moon['sign'])
            start_time = next_saturn['Start Date']
            end_time = next_saturn['End Date']
    elif next_sign == current_saturn['Sign']:
        sadhesati_status = ""
        next = saturn_pos[saturn_pos.index(current_saturn) - 1]
        start_time = next['Start Date']
        end_time = next['End Date']
        end_date = datetime.strptime(end_time, "%B %d, %Y")
        if end_date < datetime.now():
            sadhesati_status = "not " 
            saturn_pos.remove(saturn_pos[saturn_pos.index(current_saturn) - 1])
            next_saturn = get_next_sade_sati(saturn_pos,moon['sign'])
            start_time = next_saturn['Start Date']
            end_time = next_saturn['End Date']
    else:
        sadhesati_status = "not " 
        next_saturn = get_next_sade_sati(saturn_pos,moon['sign'])
        start_time = next_saturn['Start Date']
        end_time = next_saturn['End Date']

    pdf.set_text_color(hex_to_rgb("#B26F0B"))
    pdf.set_fill_color(hex_to_rgb("#F5E7D2"))
    pdf.set_draw_color(hex_to_rgb("#B26F0B"))
    pdf.rect(20,80,pdf.w - 40,15,corner_radius=40.0,round_corners=True,style='DF')
    pdf.set_y(88)
    pdf.cell(0,0,f"Your Child currently {sadhesati_status}undergoing Sadhesati.",align='C')
    pdf.set_text_color(hex_to_rgb("#B26F0B"))
    pdf.set_fill_color(hex_to_rgb("#FFD4D4"))
    pdf.set_draw_color(hex_to_rgb("#B32727"))
    pdf.rect(35,100,pdf.w - 70,15,corner_radius=40.0,round_corners=True,style='DF')
    pdf.set_y(100)
    pdf.cell(0,15,f"Start Date: {start_time}, End Date : {end_time}",align='C')
    pdf.set_text_color(0,0,0)
    roundedBox(pdf,"#FFCEE0",20,120,pdf.w-40,80)
    pdf.set_xy(22.5,122.5)
    pdf.set_font('Karma-Semi', '', 18) 
    pdf.multi_cell(pdf.w - 45,8,"Sadhesati Overview and Effects",align='L')
    pdf.set_xy(22.5,132.5)
    pdf.set_font('Karma-Regular', '', 12) 
    pdf.multi_cell(pdf.w - 45,8,"       Sade Sati is a significant astrological period lasting seven and a half years, during which Saturn transits over the Moon's position and the two adjacent houses in a birth chart. This phase often brings challenges, including emotional stress, financial instability, and personal setbacks. The impact of Sade Sati can vary based on Saturn's placement and other planetary influences in the birth chart. Remedies such as performing Saturn-related pujas, wearing specific gemstones, and engaging in charitable activities can help alleviate the negative effects and provide support during this period.",align='L')
    
    roundedBox(pdf,"#FFCEE0",20,205,pdf.w-40,60)
    pdf.set_xy(22.5,210)
    pdf.set_font('Karma-Semi', '', 18) 
    pdf.cell(0,0,"Effects on Sade Sati dosha on individual 's life")
    pdf.set_font('Karma-Regular', '', 14)
    for k in Sade_Sati_Analysis:
        if pdf.get_y() + 40 >= 270:
            pdf.AddPage(path)
            pdf.set_y(30)
            roundedBox(pdf,"#FFCEE0",20,30,pdf.w-40,167.5)
        pdf.set_xy(22.5,pdf.get_y() + 5)
        pdf.multi_cell(pdf.w - 45,8,f"      {k}",align='L')
    pdf.image(f'{path}/babyImages/end.png',(pdf.w / 2) - 15,210,30,0)
    
    asc = list(filter(lambda x: x['Name'] == 'Ascendant', planets))[0]
    
    pdf.AddPage(path,"Lucky Stone")
    roundedBox(pdf,"#D2CEFF",25,40,pdf.w-50,35)
    pdf.set_xy(30,42)
    pdf.set_text_color(hex_to_rgb("#2F2B5E"))
    pdf.set_font('Karma-Regular', '', 13)
    pdf.multi_cell(pdf.w - 60,8,f"Based on the analysis of your child's Aura, we have selected several gemstones for you. These stones are chosen to complement your child astrological profile, with the potential to enhance your child fortune and overall well-being.",align='L')
    
    stone = Planet_Gemstone_Desc[asc['zodiac_lord']]
    
    pdf.set_text_color(0,0,0)
    pdf.set_font('Karma-Heavy', '', 26)
    pdf.set_y(85)
    pdf.cell(0,0,f"{stone['Gemstone']}",align='C')
    if stone['Gemstone'] == "Ruby" or stone['Gemstone'] == "Red Coral" or stone['Gemstone'] == "Emerald":
            pdf.image(f"{path}/babyImages/stone_bg.png",pdf.w / 2 - 22.5, 135,45,0)           
    else:
        pdf.image(f"{path}/babyImages/stone_bg.png",pdf.w / 2 - 22.5, 130,45,0)           
    pdf.image(f"{path}/babyImages/{stone['Gemstone']}.png",pdf.w / 2 - 22.5, 100,45,0)
    pdf.set_xy(15,150)
    pdf.set_font('Karma-Regular', '', 14)
    pdf.multi_cell(pdf.w - 30,8,f"      {gemstone_content[asc['sign']]} \n\n        {stone['Description']}",align='L')
    pdf.AddPage(path)
    pdf.set_font('Karma-Heavy', '', 22)
    pdf.set_xy(20,30)
    pdf.cell(0,0,f"About {stone['Gemstone']}:",align='L')
    for v in Gemstone_about[stone['Gemstone']]:
        pdf.set_font('Karma-Regular', '', 16) 
        pdf.set_xy(22.5,pdf.get_y() + 5)
        pdf.multi_cell(pdf.w - 45,8,f'» {v}',align='L')
    pdf.image(f'{path}/babyImages/end.png',(pdf.w / 2) - 15,pdf.get_y() + 20,30,0)
    
    pdf.AddPage(path,"Rudraksha Suggestions")
    pdf.image(f"{path}/babyImages/rudra.png",pdf.w / 2 - 32.5, 40,65,0)
    roundedBox(pdf,"#FDF0D5",25,110,pdf.w-50,37.5)
    pdf.set_xy(30,112)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Karma-Regular', '', 13)
    pdf.multi_cell(pdf.w - 60,8,f"Learn about your child's Rudraksha to improve various aspects of your life. Rudraksha beads have unique properties that, when worn near the heart, can affect your child brain in different ways depending on their type. This can help change your child's mood and mindset.",align='L')
    pdf.set_xy(22.5,160)
    pdf.set_font('Karma-Semi', '', 18)
    pdf.cell(pdf.w - 45,0,"Why Rudraksha for wealth and prosperity?",align='L')
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
    
    pdf.AddPage(path)
    pdf.set_xy(22.5,30)
    pdf.set_font('Karma-Semi', '', 18)
    pdf.cell(pdf.w - 45,0,"Why Rudraksha for health and vitality?",align='L')
    pdf.set_font('Karma-Regular', '', 13)
    roundedBox(pdf,"#CCFFF0",25,37.5,pdf.w - 50,pdf.no_of_lines(f"      {health_rudra[asc['sign']]}", pdf.w - 55) * 8 + 40)
    pdf.image(f"{path}/babyImages/{sign_mukhi[asc['sign']][0]}.png",pdf.w / 2 - 22.5 - 10, 45,20,0)
    pdf.image(f"{path}/babyImages/rudraPlus.png",pdf.w / 2 - 22.5 + 15, 50,10,0)
    pdf.image(f"{path}/babyImages/{sign_mukhi[asc['sign']][1]}.png",pdf.w / 2 - 22.5 + 30, 45,20,0)
    pdf.set_xy(pdf.w / 2 - 22.5 - 10,70)
    pdf.cell(20,0,f"{sign_mukhi[asc['sign']][0]}",align='C')
    pdf.set_xy(pdf.w / 2 - 22.5 + 25,70)
    pdf.cell(20,0,f"{sign_mukhi[asc['sign']][1]}",align='C')
    pdf.set_xy(27.5,75)
    pdf.multi_cell(pdf.w - 55,8,f"      {health_rudra[asc['sign']]}")
    
    pdf.set_xy(22.5,165)
    pdf.set_font('Karma-Semi', '', 18)
    pdf.cell(pdf.w - 45,0,"Why Rudraksha for career and education?",align='L')
    pdf.set_font('Karma-Regular', '', 13)
    roundedBox(pdf,"#F2FFCC",25,172.5,pdf.w - 50,pdf.no_of_lines(f"      {career_rudra[asc['sign']]}", pdf.w - 55) * 8 + 40)
    pdf.image(f"{path}/babyImages/{sign_mukhi[asc['sign']][0]}.png",pdf.w / 2 - 22.5 - 10, 180,20,0)
    pdf.image(f"{path}/babyImages/rudraPlus.png",pdf.w / 2 - 22.5 + 15, 185,10,0)
    pdf.image(f"{path}/babyImages/{sign_mukhi[asc['sign']][1]}.png",pdf.w / 2 - 22.5 + 30, 180,20,0)
    pdf.set_xy(pdf.w / 2 - 22.5 - 10,205)
    pdf.cell(20,0,f"{sign_mukhi[asc['sign']][0]}",align='C')
    pdf.set_xy(pdf.w / 2 - 22.5 + 25,205)
    pdf.cell(20,0,f"{sign_mukhi[asc['sign']][1]}",align='C')
    pdf.set_xy(27.5,210)
    pdf.multi_cell(pdf.w - 55,8,f"      {career_rudra[asc['sign']]}")
    
    pdf.AddPage(path)
    pdf.set_xy(20,20)
    pdf.set_font('Karma-Heavy', '', 24)
    pdf.set_text_color(hex_to_rgb("#966A2F"))
    pdf.multi_cell(pdf.w - 40,10,f"{name}'s Soul Desire and Soul Planet",align='C')
    roundedBox(pdf,"#FFD7D7",20,35,pdf.w - 40,50)
    pdf.set_font('Karma-Semi', '', 20)
    pdf.set_text_color(0,0,0)
    pdf.set_y(42)
    pdf.cell(0,0,'AtmaKaraka',align='C')
    pdf.set_text_color(hex_to_rgb("#940000"))
    pdf.set_font_size(12)
    pdf.set_xy(30,48)
    pdf.multi_cell(pdf.w - 60,8,"Atmakaraka, a Sanskrit term for 'soul indicator' is the planet with the highest degree in your birth chart. It reveals your deepest desires and key strengths and weaknesses. Understanding your Atmakaraka can guide you toward your true purpose and inspire meaningful changes in your life.",align='L')
    atma = list(filter(lambda x: x['order'] == 1,planets))[0]
    if atma['Name'] == "Ascendant":
        atma = list(filter(lambda x: x['order'] == 2,planets))[0]
    pdf.image(f'{path}/babyImages/atma_{atma['Name']}.jpeg',pdf.w / 2 - 22.5, 95,45,0)
    roundedBox(pdf,"#FFE7E7",45,182,pdf.w - 90,12)
    pdf.set_y(182)
    pdf.set_font('Karma-Semi', '', 20)
    pdf.cell(0,12,f'{atma['Name']} is your Atmakaraka',align='C')
    pdf.set_xy(22.5,200)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Karma-Regular', '', 18) 
    pdf.multi_cell(pdf.w - 45,8,f"      {athmakaraka[atma['Name']]}",align='L')
    
    pdf.AddPage(path,f"{name}'s Favourable God")
    roundedBox(pdf,"#D7FFEA",20,35,pdf.w-40,40)
    pdf.set_font('Karma-Regular', '', 14) 
    pdf.set_text_color(hex_to_rgb("#365600"))
    pdf.set_xy(22.5,37.5)
    pdf.multi_cell(pdf.w - 45,8,"       According to the scriptures, worshiping your Ishta Dev gives desired results. Determination of the Ishta Dev or Devi is determined by our past life karmas. There are many methods of determining the deity in astrology. Here, We have used the Jaimini Atmakaraka for Isht Dev decision.",align='L')

    pdf.set_fill_color(*hex_to_rgb("#D2FFC3"))
    pdf.rect(60,85,pdf.w - 120,15,corner_radius=100.0,round_corners=True,style='F')
    pdf.set_text_color(hex_to_rgb("#0C7D11"))
    pdf.set_font('Karma-Semi', '', 20) 
    pdf.set_y(85)
    pdf.cell(0,15,f"{name}'s Ishta Devatas",align='C')
    asc = list(filter(lambda x: x['Name'] == "Ascendant",planets))[0]
    ninthHouseLord = zodiac_lord[((zodiac.index(asc['sign']) + 9) % 12) - 1]

    signLord = list(filter(lambda x: x['Name'] == ninthHouseLord,planets))[0]

    isthadevathaLord = list(filter(lambda x: x['Name'] == signLord['Name'],planets))[0]['nakshatra_lord']
    
    isthaDeva = ista_devatas[isthadevathaLord]
    pdf.set_text_color(0,0,0)
    pdf.image(f"{path}/{ista_images[isthadevathaLord][0]}",45, 110,45,0)
    pdf.set_xy(67.5 - (pdf.get_string_width(f"{isthaDeva[0]}") / 2), 195)
    pdf.cell(pdf.get_string_width(f"{isthaDeva[0]}"),0,f"{isthaDeva[0]}",align='L')
    pdf.image(f"{path}/{ista_images[isthadevathaLord][1]}",120, 110,45,0)
    pdf.set_xy(120, 195)
    pdf.cell(0,0,f"{isthaDeva[1]}",align='L')
    pdf.set_draw_color(hex_to_rgb("#8A5A19"))
    pdf.rect(20,202.5,pdf.w - 40,72.5,corner_radius=100.0,round_corners=True,style='D')
    pdf.set_xy(22.5,203.5)
    pdf.set_font('Karma-Regular', '', 11) 
    pdf.multi_cell(pdf.w - 45,8,f"{ista_devata_desc[isthadevathaLord].capitalize()}",align='L')
    
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
    dasaOut = [{'dasa': 'Rahu', 'bhukthi': 'Rahu', 'age': "At Grishma's age, Between 4 to 7", 'prediction': {'insights': "During the Rahu Dasa and Rahu Bhukti period, there will be intense transformative energies at play. This period is likely to bring sudden and unexpected changes in the Guru's life, particularly in areas related to friendships, social circles, and desires. It can be a time of intense self-discovery and a shift in perspectives, leading to new opportunities for growth and expansion.", 'challenges': [{'title': 'Emotional Turmoil', 'content': 'The Guru may experience emotional upheavals and inner conflicts during this period, leading to uncertainty and anxiety.'}, {'title': 'Power Struggles', 'content': 'There might be power struggles or conflicts with authority figures, leading to challenges in asserting independence.'}, {'title': 'Unpredictable Events', 'content': 'The Guru may face unexpected events or disruptions that can derail plans and cause stress and instability.'}, {'title': 'Risk of Deception', 'content': 'There is a risk of being deceived or misled by others, leading to trust issues and potential conflicts.'}, {'title': 'Health Concerns', 'content': 'The Guru may experience health-related challenges or unexpected issues that require attention and care.'}], 'precautions': [{'title': 'Self-Reflection and Meditation', 'content': 'Encourage the Guru to introspect and meditate regularly to maintain inner balance and clarity amidst the chaos.'}, {'title': 'Healthy Boundaries', 'content': 'Advise the Guru to establish healthy boundaries in relationships and interactions to avoid being taken advantage of.'}, {'title': 'Financial Planning', 'content': 'Focus on financial stability and long-term planning to mitigate the impact of financial uncertainties during this period.'}, {'title': 'Regular Exercise and Wellness Routine', 'content': 'Promote a regular exercise and wellness routine to manage stress and maintain physical health during this intense phase.'}, {'title': 'Seeking Counsel', 'content': 'Suggest seeking counsel from trusted mentors or guides to navigate through challenges and make informed decisions.'}], 'remedies': [{'title': 'Yoga and Mindfulness Practices', 'content': 'Encourage the Guru to practice yoga, mindfulness, or other calming activities to ease emotional stress and foster inner peace.'}, {'title': 'Engagement in Creative Outlets', 'content': 'Support the Guru in engaging in creative outlets or hobbies to channel the intense energies constructively and find emotional release.'}, {'title': 'Gratitude Journaling', 'content': 'Recommend maintaining a gratitude journal to focus on positive aspects of life and cultivate a mindset of gratitude amidst difficulties.'}, {'title': 'Community Support', 'content': 'Encourage participation in community activities or seeking support from friends and loved ones to build a strong support system during challenging times.'}, {'title': 'Charity and Service', 'content': 'Suggest engaging in charitable activities or service to others as a way to redirect energies positively and find fulfillment in giving back to the community.'}]}}, {'dasa': 'Rahu', 'bhukthi': 'Jupiter', 'age': "At Grishma's age, Between 7 to 9", 'prediction': {'insights': 'During the Rahu Dasa and Jupiter Bhukti period, the Guru may experience significant transformation and growth in relationships, spirituality, and career pursuits. This period could bring unexpected opportunities and expansion in various areas of life, leading to a deeper understanding of self and others. The influence of Rahu and Jupiter may enhance creativity, intuition, and wisdom, guiding the Guru towards new endeavours and spiritual insights.', 'challenges': [{'title': 'Overwhelm and Confusion', 'content': 'The Guru may feel overwhelmed by the multitude of opportunities and experiences, leading to confusion and indecision. Balancing various aspects of life may pose a challenge during this period.'}, {'title': 'Risk of Impulsivity', 'content': 'There is a risk of acting impulsively or taking unnecessary risks, especially in financial matters. The Guru should exercise caution and prudence to avoid hasty decisions.'}, {'title': 'Strained Relationships', 'content': 'Relationships, especially with family members and partners, may face challenges due to conflicting priorities and misunderstandings. Communication and patience are essential to navigate these issues.'}, {'title': 'Health Concerns', 'content': 'Health issues related to stress and anxiety may arise during this period. The Guru should prioritize self-care, proper nutrition, and regular exercise to maintain physical and mental well-being.'}, {'title': 'Career Instability', 'content': 'Career changes or instability in professional life could be a concern. The Guru may need to adapt to new roles or responsibilities, requiring flexibility and resilience.'}], 'precautions': [{'title': 'Maintain Balance and Focus', 'content': 'Encourage the Guru to maintain a balance between work, relationships, and personal growth. Setting priorities and focusing on important goals can help manage overwhelming situations.'}, {'title': 'Exercise Caution in Decisions', 'content': 'Advise the Guru to think carefully before making major decisions, especially financial ones. Seeking advice from trusted sources and considering long-term consequences can prevent impulsive actions.'}, {'title': 'Enhance Communication Skills', 'content': 'Support the Guru in improving communication with loved ones and colleagues. Encourage open dialogue, active listening, and clarity in expressing thoughts and emotions to avoid misunderstandings.'}, {'title': 'Prioritize Health and Well-being', 'content': 'Emphasize the importance of self-care practices such as meditation, yoga, and mindfulness to reduce stress and maintain physical health. A balanced diet and regular exercise routine can boost overall well-being.'}, {'title': 'Adapt to Changes in Career', 'content': 'Prepare the Guru to embrace changes in the professional sphere with a positive mindset. Developing new skills, networking, and staying adaptable to evolving opportunities can help navigate career challenges effectively.'}], 'remedies': [{'title': 'Meditation and Mindfulness Practices', 'content': 'Encourage the Guru to incorporate daily meditation and mindfulness practices to enhance clarity of thought, emotional stability, and spiritual growth. These practices can help reduce stress and enhance focus.'}, {'title': 'Seek Mentorship and Guidance', 'content': 'Recommend seeking guidance from mentors, spiritual leaders, or experts in relevant fields to gain insights and support in decision-making processes. Learning from experienced individuals can provide valuable perspectives.'}, {'title': 'Connect with Nature', 'content': 'Suggest spending time in nature regularly to rejuvenate and reconnect with natural rhythms. Nature walks, gardening, or outdoor activities can improve mental well-being and foster a sense of grounding and peace.'}, {'title': 'Express Gratitude Daily', 'content': 'Encourage the Guru to practice gratitude by reflecting on things they are thankful for each day. Gratitude journaling or expressing appreciation to others can cultivate a positive outlook and attract more blessings into their life.'}, {'title': 'Creative Outlets for Expression', 'content': 'Promote engaging in creative outlets such as art, music, writing, or dance to channel emotions and thoughts constructively. Creative expression can serve as a therapeutic tool and enhance self-discovery during this transformative period.'}]}}, {'dasa': 'Rahu', 'bhukthi': 'Saturn', 'age': "At Grishma's age, Between 9 to 12", 'prediction': {'insights': 'During the Rahu Dasa and Saturn Bhukti period, Guru may experience intense transformation and unexpected events that can impact relationships and career decisions. This period may bring significant changes and challenges, urging the Guru to adapt and grow in new directions.', 'challenges': [{'title': 'Emotional Turmoil', 'content': 'Guru may face emotional upheavals and inner conflicts during this period, leading to mood swings and uncertainty in decision-making.'}, {'title': 'Career Instability', 'content': "The Guru's career may face disruptions or obstacles during this phase, requiring patience and strategic planning to navigate through challenges."}, {'title': 'Health Concerns', 'content': 'There might be health issues or stress-related problems that the Guru needs to address with caution and proper care.'}, {'title': 'Financial Struggles', 'content': 'Financial setbacks or unexpected expenses may arise, necessitating prudent financial management and budgeting during this period.'}, {'title': 'Relationship Strain', 'content': 'Relationships, especially with family and colleagues, may face strain or misunderstandings, requiring open communication and patience to resolve conflicts.'}], 'precautions': [{'title': 'Maintain Emotional Balance', 'content': 'Encourage the Guru to practice mindfulness, meditation, or seek counseling to manage emotions and maintain mental well-being during challenging times.'}, {'title': 'Career Planning', 'content': 'Support the Guru in setting realistic goals, updating skills, and exploring new career opportunities to overcome obstacles and ensure professional growth.'}, {'title': 'Prioritize Health', 'content': 'Emphasize the importance of regular exercise, balanced diet, and stress-reducing activities to maintain physical health and well-being throughout the period.'}, {'title': 'Financial Planning', 'content': 'Assist the Guru in creating a budget, saving for emergencies, and avoiding impulsive financial decisions to mitigate financial challenges and improve stability.'}, {'title': 'Open Communication', 'content': 'Encourage open and honest communication in relationships, foster understanding, and resolve conflicts through patience, empathy, and active listening.'}], 'remedies': [{'title': 'Daily Meditation', 'content': 'Recommend daily meditation practice to calm the mind, reduce stress, and enhance clarity and focus in decision-making during challenging times.'}, {'title': 'Career Guidance', 'content': 'Seek career counseling or mentorship to identify strengths, weaknesses, and potential opportunities for professional development and success.'}, {'title': 'Healthy Lifestyle Changes', 'content': 'Promote healthy lifestyle habits such as regular exercise, balanced meals, and sufficient rest to boost immunity, energy levels, and overall well-being.'}, {'title': 'Financial Consultation', 'content': 'Consult a financial advisor to create a strategic financial plan, invest wisely, and build savings for long-term security and stability.'}, {'title': 'Relationship Counseling', 'content': 'Consider couples therapy or communication workshops to improve relationships, strengthen emotional bonds, and resolve conflicts effectively for harmonious interactions.'}]}}]

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
        pdf.image(f'{path}/babyImages/{dasaNow['dasa']}.png',pdf.w / 2 - 25,pdf.get_y() + 10, 20,20)
        pdf.image(f'{path}/babyImages/{dasaNow['bhukthi']}.png',pdf.w / 2 + 5,pdf.get_y() + 10, 20,20)
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
    
    contents = [
        {'strategies': [{'title': 'Embrace Leadership Qualities', 'content': 'Encourage your child to take on leadership roles and responsibilities to boost their confidence and assertiveness.'}, {'title': 'Develop Self-Identity', 'content': 'Help your child explore their individuality and develop a strong sense of self-identity through self-expression activities.'}, {'title': 'Emphasize Self-Improvement', 'content': 'Encourage your child to focus on self-improvement and personal growth to enhance their inner strength and resilience.'}], 'remedies': [{'title': 'Life Skills Teachings', 'content': 'Teach your child essential life skills such as time management, communication, and problem-solving to empower them in various aspects of life.'}, {'title': 'Food & Diet', 'content': "Include foods rich in vitamin D and Omega-3 fatty acids in your child's diet to support their overall well-being and mental clarity."}, {'title': 'Manifestations', 'content': 'Encourage your child to set clear goals and manifest their desires through visualization and positive affirmations for success.'}, {'title': 'Affirmations', 'content': 'Guide your child to practice daily affirmations that reinforce self-confidence, courage, and positivity in their thoughts and actions.'}, {'title': 'Visualizations', 'content': 'Support your child in visualizing themselves achieving their aspirations and dreams, fostering a positive mindset and motivation towards their goals.'}], 'routine': [{'title': 'Morning Routine', 'content': 'Start the day with a gratitude journaling practice to cultivate a positive mindset and set intentions for the day ahead.'}, {'title': 'Midday Routine', 'content': 'Encourage regular breaks for mindful breathing exercises to reduce stress and enhance focus and productivity.'}, {'title': 'Evening Routine', 'content': 'Incorporate a relaxing bedtime routine with calming activities like reading or gentle yoga to promote restful sleep and recharge for the next day.'}], 'practice': [{'title': 'Mantra Chanting', 'content': "Guide your child to chant the Sun mantra 'Om Suryaya Namaha' to invoke the energy of the Sun and enhance vitality and strength."}, {'title': 'Mudra Practice', 'content': 'Teach your child the Surya Mudra by joining the ring finger with the thumb to balance the fire element and boost confidence and self-esteem.'}, {'title': 'Sacred Sounds Meditation', 'content': 'Introduce your child to sacred sounds meditation with the Gayatri Mantra to elevate consciousness, promote inner wisdom, and connect with divine light.'}]},
        {'strategies': [{'title': 'Embrace Confidence', 'content': 'Encourage your child to embrace their confidence and believe in their abilities. Positive affirmations and self-assurance will help them shine in all areas of life.'}, {'title': 'Seek Balance', 'content': 'Teach your child the importance of balance in their emotions and actions. Encourage them to find harmony in their relationships and responsibilities.'}, {'title': 'Self-Expression is Key', 'content': 'Support your child in expressing their emotions and thoughts openly. Encourage creative outlets and communication to enhance self-expression.'}], 'remedies': [{'title': 'Life Skills Teachings', 'content': 'Teach your child problem-solving skills and decision-making abilities to navigate challenges with confidence and clarity.'}, {'title': 'Food & Diet', 'content': 'Include foods rich in Omega-3 fatty acids, such as salmon and walnuts, to support mood stability and emotional balance.'}, {'title': 'Manifestations', 'content': 'Encourage your child to set clear goals and manifest their dreams through visualization techniques and positive affirmations.'}, {'title': 'Affirmations', 'content': 'Practice daily affirmations with your child to boost their self-esteem and cultivate a positive mindset.'}, {'title': 'Visualizations', 'content': 'Guide your child in visualization exercises to imagine their desired outcomes and manifest success in all aspects of life.'}], 'routine': [{'title': 'Mindful Breathing', 'content': 'Encourage your child to practice mindful breathing exercises to reduce stress, increase focus, and promote emotional stability. Inhale positivity and exhale negativity.'}, {'title': 'Creative Expression', 'content': 'Allocate time for your child to engage in creative activities such as art, music, or writing. Creative expression is a powerful outlet for emotions and thoughts.'}, {'title': 'Physical Activity', 'content': "Promote regular physical activity to boost your child's energy levels, mood, and overall well-being. Encourage outdoor play, yoga, or sports for a healthy lifestyle."}], 'practice': [{'title': 'Mantra Chanting', 'content': "Introduce your child to chanting the Sun mantra 'Om Suryaya Namaha' to invoke the energy of the Sun and enhance vitality and positivity. Repeat the mantra with focus and devotion."}, {'title': 'Mudra Practice', 'content': 'Teach your child the Surya Mudra by joining the ring finger and thumb to activate the solar energy within. Encourage them to practice this mudra daily for increased self-confidence and self-expression.'}, {'title': 'Sacred Sounds Meditation', 'content': "Guide your child in a sacred sounds meditation with the sound 'Ram'. This sound resonates with the Solar Plexus Chakra, promoting self-confidence, courage, and inner strength. Encourage them to meditate on this sound for inner peace and empowerment."}]},
        {'strategies': [{'title': 'Communication Skills Development', 'content': 'Focus on developing strong communication skills through activities like writing, speech, and storytelling to enhance the positive effects of Mercury in the 7th house.'}, {'title': 'Logical Thinking Enhancement', 'content': "Engage in puzzles, games, and activities that boost logical thinking to harness Mercury's analytical abilities in the 7th house."}, {'title': 'Networking Opportunities', 'content': 'Encourage participation in group activities, clubs, or social events to improve networking abilities and create positive connections with others.'}], 'remedies': [{'title': 'Mindful Listening Technique', 'content': 'Practice active listening by maintaining eye contact, asking questions, and summarizing to improve communication skills and connect deeply with others.'}, {'title': 'Creative Writing Exercises', 'content': "Engage in creative writing prompts to enhance Mercury's expressive abilities and tap into imaginative thinking for personal growth."}, {'title': 'Visualization Techniques', 'content': "Use visualization exercises to stimulate Mercury's creativity and problem-solving skills, aiding in decision-making and innovation."}], 'routine': [{'title': 'Journaling Practice', 'content': 'Encourage daily journaling to organize thoughts, express feelings, and improve self-reflection for emotional clarity and mental development.'}, {'title': 'Mindfulness Meditation', 'content': 'Incorporate mindfulness meditation to reduce stress, enhance focus, and promote mental clarity, allowing Mercury in the 7th house to function optimally.'}, {'title': 'Brain Teasers Challenge', 'content': "Include brain teasers and puzzles in the daily routine to sharpen cognitive abilities, boost memory, and foster Mercury's intellect."}], 'practice': [{'title': 'Mercury Mantra Chanting', 'content': "Recite the 'Om Budhaya Namaha' mantra to invoke Mercury's positive attributes for improved communication skills, intelligence, and learning abilities."}, {'title': 'Buddhi Mudra Practice', 'content': 'Perform the Buddhi Mudra by touching the tip of the little finger to the tip of the thumb on both hands to enhance mental clarity, focus, and decision-making skills.'}, {'title': 'Sacred Sounds Meditation', 'content': "Listen to sacred sounds like the sound of flowing water or ringing bells to calm the mind, improve concentration, and activate Mercury's energy for positive effects."}]},
        {'strategies': [{'title': 'Creative Expression', 'content': 'Encourage your child to express their creativity through art, music, or dance to enhance their Venus energy in the 9th house of Taurus. This will help them tap into their artistic talents and boost their self-expression.'}, {'title': 'Cultivate Relationships', 'content': 'Teach your child the importance of building strong and meaningful relationships with family and friends. Encouraging social interactions and fostering connections will support their Venus placement in the 9th house.'}, {'title': 'Explore Cultural Diversity', 'content': 'Expose your child to different cultures, traditions, and belief systems to broaden their perspective and enhance their Venus energy in the 9th house. This will help them appreciate diversity and expand their knowledge.'}], 'remedies': [{'title': 'Life Skills Teachings', 'content': 'Teach your child valuable life skills such as communication, empathy, and conflict resolution to strengthen their Venus placement in the 9th house of Taurus. These skills will help them navigate relationships effectively.'}, {'title': 'Food & Diet', 'content': "Include foods that are known to boost Venus energy such as fruits, nuts, and dairy products in your child's diet. This will support their Venus placement in the 9th house and promote harmony and love."}, {'title': 'Manifestations', 'content': 'Encourage your child to visualize and manifest their desires through positive affirmations and creative visualization techniques. This practice will align with their Venus energy in the 9th house and help them attract abundance.'}, {'title': 'Affirmations', 'content': 'Guide your child to practice affirmations that focus on self-love, beauty, and harmony to strengthen their Venus placement in the 9th house. Repeat affirmations daily to reinforce positive beliefs about themselves.'}, {'title': 'Visualizations', 'content': 'Engage your child in visualizations that evoke feelings of love, joy, and gratitude to enhance their Venus energy in the 9th house. This practice will stimulate their creativity and bring a sense of fulfillment.'}], 'routine': [{'title': 'Daily Creative Outlet', 'content': 'Encourage your child to engage in a daily creative outlet such as drawing, painting, or playing music to nurture their Venus energy in the 9th house. This routine will provide a channel for self-expression and emotional release.'}, {'title': 'Gratitude Practice', 'content': 'Guide your child to practice gratitude daily by reflecting on the things they are thankful for. This routine will enhance their Venus placement in the 9th house and cultivate a positive mindset.'}, {'title': 'Mindful Relationships', 'content': 'Teach your child the importance of mindful relationships by encouraging active listening, empathy, and kindness. This routine will support their Venus energy in the 9th house and promote harmonious connections.'}], 'practice': [{'title': 'Mantra Chanting', 'content': "Introduce your child to the Venus mantra 'Om Shukraya Namaha' and guide them in chanting it regularly to activate their Venus energy in the 9th house. This practice will promote love, beauty, and harmony in their life."}, {'title': 'Mudra Practice', 'content': 'Teach your child the Venus mudra by bringing the tips of the thumb and the index finger together to create a circle. Encourage them to hold this mudra while meditating to enhance their Venus placement in the 9th house.'}, {'title': 'Sacred Sounds Meditation', 'content': 'Guide your child in a sacred sounds meditation practice by listening to soothing music or chants that resonate with Venus energy. This practice will help them connect with their inner beauty and creativity.'}]},
        {'strategies': [{'title': 'Embrace Leadership Qualities', 'content': 'Grishma, you possess natural leadership qualities that can be enhanced by taking charge of situations and guiding others towards success.'}, {'title': 'Express Creativity Through Action', 'content': 'Grishma, channel your creative energy into action by initiating new projects and ventures that reflect your unique talents and ideas.'}, {'title': 'Embrace Independence and Self-Expression', 'content': 'Grishma, embrace your independence and express yourself authentically without fear of judgment or approval from others.'}], 'remedies': [{'title': 'Life Skills Teachings', 'content': 'Grishma, focus on developing communication and interpersonal skills to navigate social interactions with ease and confidence.'}, {'title': 'Food & Diet', 'content': 'Grishma, incorporate vitamin-rich foods like oranges, carrots, and bell peppers into your diet to boost energy levels and vitality.'}, {'title': 'Manifestations', 'content': 'Grishma, practice visualization techniques to manifest your goals and desires with clarity and intention.'}, {'title': 'Affirmations', 'content': 'Grishma, create personalized affirmations that reinforce your self-worth, confidence, and abilities to achieve success in all aspects of life.'}, {'title': 'Visualizations', 'content': 'Grishma, visualize yourself surrounded by a radiant golden light that fills you with strength, courage, and positivity each day.'}], 'routine': [{'title': 'Morning Affirmations', 'content': 'Grishma, start your day with positive affirmations to set the tone for a successful and fulfilling day ahead.'}, {'title': 'Mindful Breathing Exercises', 'content': 'Grishma, practice deep breathing exercises throughout the day to calm the mind, reduce stress, and increase focus and clarity.'}, {'title': 'Reflective Journaling', 'content': 'Grishma, end your day by journaling your thoughts, emotions, and achievements to reflect on your growth and progress.'}], 'practice': [{'title': 'Sun Mantra Chanting', 'content': "Grishma, chant the 'Om Suryaya Namaha' mantra to invoke the energy of the Sun for vitality, courage, and positive transformation."}, {'title': 'Sun Mudra Practice', 'content': 'Grishma, practice the Surya Mudra by joining the ring finger with the thumb to activate the Solar Plexus Chakra and boost confidence and self-esteem.'}, {'title': 'Sun Sacred Sounds Meditation', 'content': 'Grishma, listen to the sacred sounds of the Sun like the Gayatri Mantra to connect with the divine energy of the Sun for mental clarity, focus, and inner strength.'}]},
        {'strategies': [{'title': 'Embrace Your Inner Strength', 'content': 'Grishma, your Moon in the 5th house of Capricorn in Dhanishta Nakshatra shows that you have a strong sense of self and inner power. Embrace this strength and use it to overcome challenges in your life.'}, {'title': 'Cultivate Creativity and Expression', 'content': 'Your Moon placement suggests that you have a creative and expressive nature. Explore different forms of art, music, or writing to enhance your creative abilities and express your emotions effectively.'}, {'title': 'Nurture Your Emotional Health', 'content': 'It is important for you to prioritize your emotional well-being. Practice self-care routines such as meditation, journaling, or seeking therapy to nurture your emotional health.'}], 'remedies': [{'title': 'Life Skills Teachings', 'content': 'Learn new skills or hobbies that ignite your passion and creativity. This could be anything from painting to dancing to cooking. Engaging in activities that bring you joy will uplift your spirits.'}, {'title': 'Food & Diet', 'content': 'Include foods rich in omega-3 fatty acids, such as salmon, walnuts, and chia seeds, in your diet to support your emotional stability and mental clarity. Stay hydrated and mindful of your eating habits to maintain a healthy relationship with food.'}, {'title': 'Manifestations', 'content': 'Practice visualization techniques to manifest your desires and goals. Create a vision board or write down your intentions to attract positive energy and opportunities into your life.'}, {'title': 'Affirmations', 'content': "Repeat positive affirmations daily to boost your self-confidence and inner strength. Affirmations such as 'I am powerful and capable of achieving my dreams' can help you stay motivated and focused on your path."}, {'title': 'Visualizations', 'content': 'Immerse yourself in guided visualizations to relax your mind and tap into your subconscious. Visualize yourself surrounded by a bright, protective light that shields you from negativity and empowers you with positivity.'}], 'routine': [{'title': 'Morning Meditation', 'content': 'Start your day with a 10-minute meditation practice to center yourself and set positive intentions for the day ahead. Focus on your breath and visualize a calm, peaceful energy surrounding you.'}, {'title': 'Creative Expression Time', 'content': "Allocate time each day for creative expression, whether it's through drawing, writing, or playing music. Allow yourself to freely express your emotions and thoughts through your chosen creative outlet."}, {'title': 'Evening Reflection Journal', 'content': 'Before bed, spend a few minutes journaling about your day. Reflect on your experiences, emotions, and accomplishments. This practice will help you unwind and process your thoughts before sleep.'}], 'practice': [{'title': 'Mantra Chanting', 'content': "Chant the 'Om Suryaya Namaha' mantra to invoke the energy of the Sun and enhance your inner power. Sit in a comfortable position, close your eyes, and chant the mantra with sincerity and devotion."}, {'title': 'Mudra Practice', 'content': 'Perform the Surya Mudra by touching the ring finger to the base of the thumb and applying gentle pressure. This mudra activates the solar plexus chakra and boosts confidence and self-esteem.'}, {'title': 'Sacred Sounds Meditation', 'content': 'Listen to the sacred sounds of the Sun, such as solar plexus chakra tuning forks or sun gong vibrations, to align with the energy of the Sun and enhance your personal power. Allow the sound waves to resonate within you and uplift your spirit.'}]},
        {'strategies': [{'title': 'Embrace Creativity', 'content': 'Grishma, with Mercury placed in the 7th House of Pisces in Revati Nakshatra, can enhance her creativity by exploring art, music, or writing as outlets for self-expression.'}, {'title': 'Focus on Communication', 'content': 'Grishma should focus on improving her communication skills to express her thoughts and ideas effectively in both personal and professional relationships.'}, {'title': 'Embrace Intuition', 'content': 'Grishma is encouraged to trust her intuition and inner wisdom, as Mercury in Pisces enhances intuitive abilities.'}], 'remedies': [{'title': 'Life Skill Teachings', 'content': 'Grishma can enhance her Mercury energy by learning new skills related to communication, such as public speaking or writing workshops.'}, {'title': 'Food & Diet', 'content': "Including brain-boosting foods like nuts, seeds, and fish in her diet can support Grishma's cognitive abilities and mental clarity."}, {'title': 'Manifestations', 'content': 'Encouraging positive self-talk and affirmations can help Grishma manifest her goals and aspirations related to communication and intellectual pursuits.'}, {'title': 'Affirmations', 'content': "Grishma can affirm statements like 'I communicate confidently and clearly' to reinforce positive communication habits and beliefs."}, {'title': 'Visualizations', 'content': 'Visualizing herself confidently expressing her ideas and thoughts can help Grishma overcome any communication challenges and enhance her Mercury energy.'}], 'routine': [{'title': 'Morning Journaling', 'content': 'Grishma can start her day by journaling her thoughts and ideas, allowing her to organize her mind and clarify her communication goals for the day.'}, {'title': 'Mid-day Meditation Break', 'content': 'Taking a short meditation break in the middle of the day can help Grishma reset and recharge her mental energy for improved communication throughout the day.'}, {'title': 'Evening Reflection', 'content': 'Reflecting on her communication experiences during the day can help Grishma identify areas for improvement and set intentions for better communication in the future.'}], 'practice': [{'title': 'Mercury Mantra', 'content': "Grishma can chant the 'Om Budhaya Namaha' mantra to invoke the positive energies of Mercury and enhance her communication skills."}, {'title': 'Mercury Mudra', 'content': 'Practicing the Mercury mudra, where the tips of the little finger, ring finger, and thumb touch, can help Grishma balance her Mercury energy and improve communication abilities.'}, {'title': 'Sacred Sounds', 'content': 'Listening to calming sacred sounds like the sound of flowing water or bells ringing can help Grishma relax and enhance her mental clarity and communication skills.'}]},
        {'strategies': [{'title': 'Embrace Creativity and Beauty', 'content': 'Grishma, with Venus placed in the 9th house of Taurus sign in Rohini Nakshatra, you are naturally inclined towards creativity and beauty. Embrace this aspect of yourself by exploring different art forms and surrounding yourself with aesthetically pleasing surroundings.'}, {'title': 'Cultivate Harmonious Relationships', 'content': 'Your Venus placement in the 9th house signifies a desire for harmonious relationships. Focus on cultivating strong and balanced connections with others, both in personal and professional settings, to enhance your overall well-being.'}, {'title': 'Value Self-worth and Self-expression', 'content': 'With Venus in the 9th house, it is important for you to value your self-worth and embrace self-expression. Allow yourself to shine authentically and confidently in all aspects of your life.'}], 'remedies': [{'title': 'Self-love Manifestation', 'content': 'Practice daily affirmations of self-love and worthiness. Visualize yourself surrounded by love and abundance, and believe in your own beauty and uniqueness.'}, {'title': 'Beauty Food Diet', 'content': 'Incorporate beauty-boosting foods such as berries, avocados, and leafy greens into your diet. These foods will nourish your Venus energy and enhance your natural beauty from within.'}, {'title': 'Artistic Visualization', 'content': 'Engage in artistic visualization exercises to enhance your creativity and artistic skills. Imagine yourself creating beautiful art pieces or expressing yourself through various artistic mediums.'}, {'title': 'Gratitude Affirmations', 'content': "Practice daily gratitude affirmations to enhance your appreciation for life's beauty and abundance. Express gratitude for the beauty around you and within yourself."}, {'title': 'Harmony Life Skills', 'content': 'Develop life skills that promote harmony in your relationships and environments. Practice active listening, empathy, and conflict resolution to maintain balanced and harmonious connections.'}], 'routine': [{'title': 'Morning Beauty Ritual', 'content': 'Start your day with a morning beauty ritual that includes skincare, grooming, and self-care practices. This will boost your confidence and enhance your natural beauty from the inside out.'}, {'title': 'Creative Expression Time', 'content': "Set aside dedicated time each day for creative expression, whether it's through art, music, writing, or any other form of artistic outlet. Allow yourself to freely express your creativity and inner beauty."}, {'title': 'Evening Self-care Routine', 'content': 'Wind down in the evening with a self-care routine that includes relaxation techniques, beauty treatments, and time for reflection. This will help you unwind and rejuvenate for the next day.'}], 'practice': [{'title': 'Venus Mantra Chanting', 'content': "Chant the Venus mantra 'Om Shukraya Namaha' daily to invoke the blessings of Venus and enhance your sense of beauty, love, and harmony."}, {'title': 'Venus Mudra Practice', 'content': 'Practice the Venus mudra by touching the tips of your thumb and ring finger together while keeping the other fingers extended. This mudra activates Venus energy and promotes love, creativity, and beauty.'}, {'title': 'Sacred Beauty Sound Meditation', 'content': 'Engage in a sacred beauty sound meditation by listening to soothing music or sounds that uplift your spirit and connect you to your inner beauty. Allow the sound vibrations to harmonize your Venus energy and enhance your sense of beauty and grace.'}]},
        {'strategies': [{'title': 'Utilize Determination and Discipline', 'content': 'Grishma, your Mars placement in the 5th House of Capricorn Sign in Uttara Ashadha Nakshatra indicates that you have a strong sense of determination and discipline. Use this energy to set clear goals and work towards them with perseverance.'}, {'title': 'Embrace Responsibility and Leadership', 'content': 'Grishma, with Mars in your 5th House, you are naturally inclined towards taking on responsibilities and leadership roles. Embrace this quality and use it to inspire and motivate others around you.'}, {'title': 'Channel Creativity and Passion', 'content': 'Grishma, your Mars placement suggests that you have a lot of creative energy and passion. Channel this energy into creative projects or hobbies that ignite your passion and bring you joy.'}], 'remedies': [{'title': 'Life Skills Teachings', 'content': 'Grishma, to enhance your Mars energy, focus on developing skills related to leadership, organization, and decision-making. These skills will help you harness the power of Mars in your life.'}, {'title': 'Food & Diet', 'content': 'Grishma, include foods that are rich in iron and protein in your diet to fuel your Mars energy. Foods like spinach, lentils, and lean meats can help boost your vitality and strength.'}, {'title': 'Manifestations', 'content': 'Grishma, practice visualization techniques to manifest your goals and desires. Imagine yourself achieving success and abundance in all areas of your life to align with the energy of Mars.'}, {'title': 'Affirmations', 'content': "Grishma, use affirmations like 'I am strong and determined' and 'I take on challenges with courage and confidence' to reinforce the positive qualities of Mars within you."}, {'title': 'Visualizations', 'content': 'Grishma, visualize a fiery red light surrounding you, symbolizing the energy and passion of Mars. Imagine this light empowering you to take action and overcome obstacles in your path.'}], 'routine': [{'title': 'Powerful Morning Routine', 'content': 'Grishma, start your day with a morning meditation to center yourself and connect with your inner strength. Set intentions for the day ahead and visualize yourself accomplishing your goals with ease.'}, {'title': 'Creative Expression Break', 'content': "Grishma, take a break during your day to engage in a creative activity that sparks your passion. Whether it's painting, writing, or dancing, allow yourself to express your creative energy freely."}, {'title': 'Reflective Evening Routine', 'content': 'Grishma, before bed, reflect on your day and acknowledge your achievements and challenges. Practice gratitude for the opportunities that came your way and set intentions for a successful tomorrow.'}], 'practice': [{'title': 'Mars Mantra Chanting', 'content': "Grishma, chant the Mars mantra 'Om Mangalaya Namaha' to invoke the energy of Mars within you. Repeat this mantra daily to align with the fierce and dynamic qualities of Mars."}, {'title': 'Mars Mudra Practice', 'content': 'Grishma, practice the Mars mudra by touching your thumb to your ring finger and extending the other fingers straight. This mudra helps activate Mars energy and increase vitality.'}, {'title': 'Sacred Sounds Meditation', 'content': 'Grishma, listen to sacred sounds like drumming or chanting that resonate with Mars energy. Allow these sounds to uplift your spirit and energize your being with the power of Mars.'}]},
        {'strategies': [{'title': 'Embrace Your Leadership Qualities', 'content': 'Grishma, your Jupiter in the 2nd House of Libra Sign in Vishakha Nakshatra indicates strong leadership qualities. Embrace your natural ability to inspire and guide others towards success.'}, {'title': 'Cultivate Financial Wisdom', 'content': 'Grishma, with Jupiter in the 2nd House, focus on cultivating financial wisdom and stability. Make sound investments and prioritize saving for the future.'}, {'title': 'Expand Your Communication Skills', 'content': 'Grishma, your Jupiter placement encourages you to expand your communication skills. Stay open to learning new languages or improving your public speaking abilities.'}], 'remedies': [{'title': 'Practice Gratitude Daily', 'content': 'Grishma, start each day by expressing gratitude for the blessings in your life. This practice will attract abundance and positivity towards you.'}, {'title': 'Mindful Financial Planning', 'content': 'Grishma, create a detailed financial plan that aligns with your long-term goals. Monitor your expenses and savings diligently to achieve financial stability.'}, {'title': 'Self-Reflection and Growth', 'content': 'Grishma, engage in regular self-reflection to identify areas for personal growth. Set realistic goals and work towards fulfilling your aspirations.'}, {'title': 'Positive Affirmations for Success', 'content': 'Grishma, recite positive affirmations daily to boost your confidence and attract success. Believe in your abilities and trust in the Universe to manifest your desires.'}, {'title': 'Visualization for Abundance', 'content': 'Grishma, practice visualization techniques to manifest abundance in your life. Visualize yourself achieving your financial goals and living a fulfilling life.'}], 'routine': [{'title': 'Gratitude Journaling', 'content': 'Grishma, start a gratitude journal to jot down things you are thankful for each day. This practice will cultivate a positive mindset and enhance your overall well-being.'}, {'title': 'Financial Check-In', 'content': 'Grishma, set aside time each week to review your finances. Track your expenses, savings, and investments to stay on top of your financial goals.'}, {'title': 'Language Learning Sessions', 'content': 'Grishma, dedicate time to learning a new language or refining your communication skills. Join language classes or practice with online resources to expand your linguistic abilities.'}], 'practice': [{'title': 'Sun Mantra Chanting', 'content': "Grishma, chant the Sun mantra 'Om Suryaya Namaha' to invoke the energy of the Sun for vitality and leadership. Sit in a comfortable position, focus on the mantra, and chant it with devotion."}, {'title': 'Hasta Mudra Practice', 'content': 'Grishma, perform the Hasta Mudra by pressing the thumb and the ring finger together. This mudra enhances communication skills and promotes mental clarity. Practice it daily for positive effects.'}, {'title': 'Sacred Sound Healing with Crystal Singing Bowls', 'content': 'Grishma, experience the healing vibrations of crystal singing bowls to harmonize your energy with the Sun. Find a quiet space, listen to the soothing sounds, and let go of any stress or tension.'}]},      
        {'strategies': [{'title': 'Embrace Self-Discipline', 'content': 'Grishma, your Saturn in the 4th House of Sagittarius signifies a need for structure and order in your emotional life. Embrace self-discipline to create a stable and secure inner foundation.'}, {'title': 'Cultivate Patience', 'content': 'With Saturn in Purva Ashadha Nakshatra, cultivate patience in your actions and decisions. Trust in the timing of the universe and practice perseverance in all your endeavors.'}, {'title': 'Seek Inner Wisdom', 'content': 'Grishma, with Saturn in Sagittarius, seek inner wisdom and spiritual growth. Connect with your intuition and explore deep philosophical teachings to expand your understanding.'}], 'remedies': [{'title': 'Life Skills Teachings', 'content': 'Grishma, incorporate time management and organizational skills into your daily routine. Prioritize tasks and set realistic goals to enhance productivity and efficiency.'}, {'title': 'Food & Diet', 'content': 'Focus on a balanced diet rich in whole foods and nutrients to nourish your body and mind. Incorporate foods that promote grounding and stability, such as root vegetables and grains.'}, {'title': 'Manifestations', 'content': 'Practice visualization techniques to manifest your desires and goals into reality. Create a vision board or journal to document your aspirations and stay focused on your intentions.'}, {'title': 'Affirmations', 'content': 'Repeat positive affirmations daily to reprogram your subconscious mind. Affirm your worth, strength, and resilience to overcome obstacles and manifest abundance in all areas of your life.'}, {'title': 'Visualizations', 'content': 'Engage in guided visualizations to connect with your inner wisdom and intuition. Visualize yourself in a state of balance and harmony, surrounded by a radiant light that guides you towards your highest potential.'}], 'routine': [{'title': 'Morning Meditation', 'content': 'Grishma, start your day with a morning meditation practice to center yourself and cultivate inner peace. Set aside 10-15 minutes for mindful breathing and reflection to set a positive tone for the day.'}, {'title': 'Journaling', 'content': 'Allocate time for journaling in the evening to reflect on your thoughts and emotions. Write down your experiences, insights, and gratitude to enhance self-awareness and promote emotional healing.'}, {'title': 'Nature Walks', 'content': "Spend time in nature regularly to recharge and connect with the earth's grounding energy. Take leisurely walks in parks or gardens to stimulate your senses and foster a sense of tranquility."}], 'practice': [{'title': 'Mantra Chanting', 'content': "Grishma, practice chanting the mantra 'Om Sham Shanaischaraya Namaha' to invoke Saturn's blessings and guidance. Sit in a comfortable position, focus on the mantra, and chant with sincerity and devotion."}, {'title': 'Mudra Activation', 'content': "Engage in the Shuni Mudra by placing the tip of your middle finger to the base of your thumb and pressing gently. This mudra enhances focus, discipline, and inner strength, aligning with Saturn's energy."}, {'title': 'Sacred Sounds Meditation', 'content': 'Immerse yourself in sacred sounds meditation by listening to Tibetan singing bowls or Vedic chants. Allow the vibrations to resonate within you, harmonizing your energy and promoting spiritual upliftment.'}]},
        {'strategies': [{'title': 'Reflecting on Emotional Well-being', 'content': "Grishma, it's essential to prioritize your emotional well-being and understand the impact of your Rahu placement in the 11th House. Dive deep into your emotions and seek ways to nurture and heal your inner self."}, {'title': 'Building Authentic Connections', 'content': 'Grishma, focus on building authentic connections with others to help balance the influence of Rahu in the 11th House. Engage in meaningful conversations, show vulnerability, and create genuine relationships to support your emotional growth.'}, {'title': 'Setting Boundaries in Relationships', 'content': 'Grishma, establish healthy boundaries in your relationships to prevent emotional overwhelm due to your Rahu placement in the 11th House. Respect your needs and communicate openly to maintain harmonious interactions.'}], 'remedies': [{'title': 'Mindful Expression Through Creativity', 'content': 'Grishma, engage in creative outlets like painting, writing, or dancing to express your emotions and thoughts. Let your creativity flow freely as a form of emotional release and self-expression.'}, {'title': 'Nourishing Foods for Emotional Balance', 'content': 'Grishma, incorporate nourishing foods like leafy greens, fruits, and herbal teas into your diet to support emotional balance. Pay attention to what you eat and how it makes you feel to enhance your emotional well-being.'}, {'title': 'Daily Affirmations for Self-Love', 'content': "Grishma, practice daily affirmations that promote self-love and acceptance. Repeat positive statements like 'I am worthy,' 'I am enough,' and 'I deserve love' to cultivate a compassionate relationship with yourself."}, {'title': 'Visualization for Emotional Healing', 'content': 'Grishma, engage in visualization exercises where you imagine yourself surrounded by healing light and love. Visualize emotional wounds being healed and replaced with peace, strength, and positivity to support your inner growth.'}, {'title': 'Setting Intentions for Emotional Clarity', 'content': 'Grishma, set intentions each day to cultivate emotional clarity and awareness. Reflect on your feelings, acknowledge them without judgment, and set intentions to navigate your emotions with mindfulness and compassion.'}], 'routine': [{'title': 'Gratitude Journaling', 'content': "Grishma, start a gratitude journal where you write down three things you're thankful for each day. Cultivate a mindset of gratitude to uplift your spirits and focus on the positive aspects of your life."}, {'title': 'Mindful Breathing Exercises', 'content': 'Grishma, practice mindful breathing exercises to calm your mind and connect with your emotions. Take slow, deep breaths and focus on the sensations of breathing to center yourself and promote emotional balance.'}, {'title': 'Morning Affirmations and Intentions', 'content': 'Grishma, begin your day with positive affirmations and set intentions for how you want to feel and act. Start your morning with empowering statements and visualize a harmonious day ahead to cultivate emotional well-being.'}], 'practice': [{'title': 'Surya Mantra for Confidence', 'content': "Grishma, chant the Surya Mantra 'Om hram hreem hroum sah suryaya namah' to boost your confidence and inner strength. Repeat this mantra daily to invoke the energy of the Sun and enhance your self-assurance."}, {'title': 'Anjali Mudra for Gratitude', 'content': 'Grishma, practice Anjali Mudra by bringing your palms together in front of your heart in a gesture of gratitude. Close your eyes, take a deep breath, and express gratitude for the blessings in your life to cultivate a sense of appreciation and peace.'}, {'title': 'Sacred Sounds Meditation with Aum', 'content': "Grishma, engage in a Sacred Sounds Meditation by chanting the sacred sound 'Aum' to align with the universal energy and awaken your inner light. Sit in a comfortable position, chant 'Aum' slowly, and feel the vibrations resonating within you for spiritual upliftment."}]},
        {'strategies': [{'title': 'Embrace Inner Wisdom', 'content': 'Grishma, with Ketu placed in the 5th house of Capricorn sign in Shravana Nakshatra, you have a strong connection to your inner wisdom. Embrace this wisdom and trust your instincts in decision-making.'}, {'title': 'Cultivate Creativity and Expression', 'content': 'Grishma, explore your creative side and express yourself freely. Use your unique perspective to bring innovative ideas to the forefront and enhance your communication skills.'}, {'title': 'Embrace Change and Transformation', 'content': 'Grishma, embrace change as a means for growth and transformation. Allow yourself to let go of old patterns and beliefs that no longer serve you, and welcome new opportunities with open arms.'}], 'remedies': [{'title': 'Life Skills Teachings', 'content': 'Grishma, focus on developing your organizational skills and time management to enhance productivity and efficiency in your daily tasks.'}, {'title': 'Food & Diet', 'content': 'Grishma, incorporate foods rich in vitamin D and antioxidants into your diet to boost your energy levels and promote overall well-being.'}, {'title': 'Manifestations', 'content': 'Grishma, practice positive affirmations and visualization techniques to manifest your goals and desires with clarity and intention.'}, {'title': 'Affirmations', 'content': 'Grishma, start your day with empowering affirmations to cultivate a positive mindset and attract abundance and success into your life.'}, {'title': 'Visualizations', 'content': 'Grishma, visualize yourself surrounded by a bright, radiant light to enhance your creativity, intuition, and inner wisdom.'}], 'routine': [{'title': 'Morning Meditation', 'content': 'Grishma, start your day with a morning meditation to center yourself, connect with your inner guidance, and set positive intentions for the day ahead.'}, {'title': 'Daily Journaling', 'content': 'Grishma, take time each day to journal your thoughts, emotions, and experiences. Reflect on your day and set goals for personal growth and self-improvement.'}, {'title': 'Evening Reflection', 'content': 'Grishma, end your day with an evening reflection practice. Review your achievements, challenges, and lessons learned to cultivate gratitude and mindfulness.'}], 'practice': [{'title': 'Mantra Chanting', 'content': 'Grishma, practice chanting the Om mantra to align with the universal energy and enhance your spiritual connection with the divine.'}, {'title': 'Mudra Meditation', 'content': 'Grishma, incorporate the Surya Mudra (Sun Mudra) into your meditation practice to activate the solar plexus chakra and boost your confidence and vitality.'}, {'title': 'Sacred Sounds Healing', 'content': 'Grishma, listen to sacred sounds such as Tibetan singing bowls or mantras to promote relaxation, inner peace, and balance in your mind, body, and spirit.'}]}
    ]
    
        
    for planet in planets:
        if planet['Name'] == "Ascendant":
            continue
        planet_status = []
        for pl in table[planet["Name"]]:
            if planet["zodiac_lord"] in pl:
                planet_status = status[table[planet["Name"]].index(pl)]
                planet['status'] = planet_status[0]
        if len(planet_status) == 0:
            planet_status = status[0] 
            planet['status'] = planet_status[0]  
            
        pdf.AddPage(path)
        if planets.index(planet)  == 0:
            pdf.set_xy(30,20)
            pdf.set_font('Karma-Heavy', '', 26)
            pdf.multi_cell(pdf.w - 60,10,f"Energize {name}'s Planets for Favorable Outcomes", align='C')
            pdf.set_y(pdf.get_y() + 5)
            
        pdf.set_text_color(hex_to_rgb("#966A2F"))
        pdf.set_font('Karma-Heavy', '', 20)
        pdf.set_xy(20,pdf.get_y() + 5)
        pdf.multi_cell(pdf.w - 40,10,f"{planet['Name']} - {planetMain[planet['Name']]}",align='C')
        pdf.image(f'{path}/babyImages/{planet['Name']}.png',20,pdf.get_y() + 5,50,50)
        pdf.set_font('Karma-Regular', '', 12) 
        pdf.set_text_color(0,0,0)
        pdf.set_xy(87.5,pdf.get_y() + 5)
        pdf.multi_cell(107.5,6,f"       The {planet['Name']} is positioned at approximately {planet['full_degree']:.2f} degrees in the zodiac sign of {planet['sign']}, symbolizing {planet_quality[planet['Name']][1][planet['sign']]}. Residing in the {planet['nakshatra']} nakshatra, which is ruled by {planet['nakshatra_lord']} , this placement enhances its {planet_quality[planet['Name']][2][planet['nakshatra']]} in the {planet['pada']}, the {planet['Name']}'s energy is particularly influential for those with {planet['sign']} as their ascendant, occupying the {number[planet['pos_from_asc']]} house from their ascendant. This alignment is generally {planet['status']},promoting {planet_quality[planet['Name']][0][planet['pos_from_asc']]}",align='L')
        pdf.set_font('Karma-Semi', '', 22)
        pdf.set_xy(22.5 ,pdf.get_y() + 20)
        pdf.multi_cell(pdf.w - 45,7,f"{planet['Name']} is in {number[planet['pos_from_asc']]} House in {name}'s Horoscope",align='C')
        
        planetTitle = {
            'strategies' : f"{planet['Name']} Insights",
            'remedies' : "Effective Remedies",
            'routine': "Holistic Routine",
            'practice': "Spiritual Practices",
        }
  
        # con = PlanetPrompt(planet,name,gender)
        con = contents[planets.index(planet)]
        for k, v in con.items():
            if pdf.get_y() + 40 >= 260:  
                pdf.AddPage(path)
                pdf.set_y(30)
                pdf.set_text_color(0,0,0)
            
            pdf.ContentDesign(random.choice(DesignColors),planetTitle[k],v,path)
        
    
    pdf.output(f'{path}/pdf/{name} - babyReport.pdf')
    
def babyReport(dob,location,path,gender,name):
    print("Generating Baby Report")
    planets = find_planets(dob,location)
    print("Planets Found")
    panchang = calculate_panchang(dob,location)
    print("Panchang Calculated")
    dasa = calculate_dasa(dob,planets[1])
    print("Dasa Calculated")    
    birthchart = generate_birth_navamsa_chart(planets,f'{path}/chart/',dob,location,name)
    print("Birth Chart Generated")
    # birthchart = ''
    lat,lon = get_lat_lon(location)
    print("Lat Lon Found")
    # lat , lon = 9.9261153,78.1140983
    dt = datetime.strptime(dob, "%Y-%m-%d %H:%M:%S")
    formatted_date = dt.strftime("%d %B %Y")
    formatted_time = dt.strftime("%I:%M:%S %p")
    
    year = int(dob[:4])
    month = int(dob.split("-")[1])
    
    generateBabyReport(formatted_date,formatted_time,location,lat,lon,planets,panchang,dasa,birthchart,gender,path,year,month,name)
    
    sender_email = "thepibitech@gmail.com"
    receiver_email = "guruvijay1925@gmail.com"
    password = "hprt rnur fesz diud" 
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Life Prediction Report"

    body = "Your Life Report"
    message.attach(MIMEText(body, "plain"))
    
    name = name.split(" ")[0]

    pdf_filename = f"{path}/pdf/{name} - babyReport.pdf" 
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read()) 
        encoders.encode_base64(part)  
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(pdf_filename)}",
        )
        message.attach(part)  

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls() 
        server.login(sender_email, password)  
        server.sendmail(sender_email, receiver_email, message.as_string())  
        print("Email with PDF attachment sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()  
    
    return "Sucess"
