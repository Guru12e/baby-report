import random
import datetime
from math import atan2, cos, radians, sin
from fpdf import FPDF,YPos,XPos
from index import find_planets
from panchang import calculate_panchang
from chart import generate_birth_navamsa_chart
from datetime import datetime
from babyContent import context,chakras,dasa_status_table,table,karagan,exaltation,athmakaraka,ista_devata_desc,ista_devatas,saturn_pos,constitutionRatio,Constitution,elements_data,elements_content,gemstone_content,Gemstone_about,Planet_Gemstone_Desc,wealth_rudra,sign_mukhi,planet_quality,KaranaLord,thithiLord,yogamLord,nakshatraColor,nakshatraNumber,atma_names,thithiContent,karanamContent,chakra_desc,weekPlanet,weekPlanetContent,sunIdentity,moonIdentity,lagnaIdentity,healthContent,healthInsights,education,carrer,planetDesc
from dasa import calculate_dasa
from promptSection import panchangPrompt,physical,dasaPrompt,healthPrompt,chapterPrompt,PlanetPrompt
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
            
    def ContentDesign(self,color,title,content,path,name,image=None):
        if image:
            self.image(f"{path}/icons/{image}", self.w / 2 - 10 , self.get_y() , 20 , 20)
            self.set_y(self.get_y() + 20)
        self.set_text_color(0,0,0)
        self.set_y(self.get_y() + 5)
        self.set_font('Karma-Semi', '', 16)
        if title != "":
            self.set_xy(22.5,self.get_y() + 5)
            roundedBox(self, color, 20 , self.get_y()  - 2.5, self.w - 40, (self.no_of_lines(title,self.w - 45) * 7) + 10, 4)
            self.multi_cell(self.w - 45, 7,title, align='C')
        if isinstance(content, str):
            content = content.replace("child", name)
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
                    v = v.replace('child',name)
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
                    v1 = v1.replace("child", name)
                    if content.index(v1) != len(content) - 1:
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40, (self.no_of_lines(f"      {v1}",self.w - 45) * 7) + 18, 0,status=False)
                    else:
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40, (self.no_of_lines(f"      {v1}",self.w - 45) * 7) + 13, 4)
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40, 10, 0,status=False)
                    
                    self.set_xy(22.5,self.get_y() + 10)
                    self.multi_cell(self.w - 45, 7, f"      {v1}", align='L')
                else:
                    v1['content'] = v1['content'].replace('child', name)
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
            self.draw_labels(x, y_base - bar_height - 15, label, path)
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
            if self.get_string_width(test_line) <= cell_width:
                current_line = test_line
            else:
                lines += 1
                current_line = word + ' '

        if current_line:
            lines += 1

        return lines
    
    def checkNewPage(self,path):
        if self.get_y() + 40 >= 260:
            self.AddPage(path)
            self.set_y(20)
            
    def panchangTable(self, data):
        x_start = 20
        y_start = self.get_y() + 5
        self.set_xy(x_start, y_start)

        for index, row in enumerate(data):
            col_width = (self.w - 40) / 2

            self.set_font('Karma-Regular', '', 14)

            initial_y = self.get_y()
            
            content = max(self.get_string_width(row[0]), self.get_string_width(row[1]))
            
            if index != len(data) - 1:
                roundedBox(self, "#FFDADA", self.w / 2 , self.get_y(), col_width, (content / (col_width - 10)) * 8 + 8, 0,status=False)
                roundedBox(self, "#DAFFDC", 20 , self.get_y(), col_width, (content / (col_width - 10)) * 8 + 8, 0,status=False)
            else:
                roundedBox(self, "#FFDADA", self.w / 2 , self.get_y(), col_width, (content / (col_width - 10)) * 8 + 5, 0,status=False)
                roundedBox(self, "#DAFFDC", 20 , self.get_y(), col_width, (content / (col_width - 10)) * 8 + 5, 0,status=False)
            if index == 0:
                self.multi_cell(col_width, 8, row[0], new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
            else:
                self.cell(10, 8, f"{index}) ", new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
                self.multi_cell(col_width - 10, 8, row[0], new_x=XPos.RIGHT, new_y=YPos.TOP,align='L')

            y_after_col1 = self.get_y()

            self.set_y(initial_y)
            self.set_x(x_start + col_width)

            if index == 0:
                self.multi_cell(col_width, 8, row[1], align='C')
            else:
                self.cell(10, 8, f"{index}) ", align='C')
                self.multi_cell(col_width - 10, 8, row[1], align='L')

            y_after_col2 = self.get_y()

            y_start = max(y_after_col1, y_after_col2)
            self.set_xy(x_start, y_start)

            
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
    pdf.image(f"{path}/icons/pg 2.jpg", pdf.w / 2 - 10, 20, 20, 20)
    pdf.set_y(50)
    pdf.cell(0,10,"Contents",align='C') 
    pdf.set_y(65)
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
    pdf.cell(0,0,"Horoscope Details",align='C')
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
        'Benefic Number :',
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
    pdf.image(f"{path}/chart/{birthchart['birth_chart']}",(pdf.w / 2) - 45,pdf.get_y() + 10,90,90)
    pdf.set_y(145)
    pdf.cell(0,0,'Navamsa Chart',align='C')
    pdf.image(f"{path}/chart/{birthchart['navamsa_chart']}",(pdf.w / 2) - 45,pdf.get_y() + 10,90,90)
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
    pdf.cell(0,0,f"{name}'s Favorable Times",align='C') 
    
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
        
    pdf.AddPage(path)
    pdf.set_xy(20,20)
    pdf.set_font('Karma-Heavy', '' , 26)
    pdf.set_text_color(hex_to_rgb("#966A2F"))
    pdf.multi_cell(pdf.w - 40 , 10, f"{name}'s Five Natural Elements", align='C')
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
                
    max_key1 = max(elements, key=elements.get)
    
    max_value2 = 0
    max_key2 = ""
    
    for k,v in elements.items():
        if k == max_key1:
            continue
        
        if v > max_value2:
            max_value2 = v
            max_key2 = k
    
    dominantElementData = elements_content[max_key1]
    
    pdf.set_text_color(hex_to_rgb("#04650D"))
    pdf.set_fill_color(hex_to_rgb("#BAF596"))
    pdf.set_draw_color(hex_to_rgb("#06FF4C"))
    pdf.rect(22.5,pdf.get_y() + 5,pdf.w - 45,15,round_corners=True,corner_radius=5,style='DF')
    pdf.set_y(pdf.get_y() + 5)
    pdf.set_font_size(14)
    pdf.cell(0,15,f"{name}'s Dominant Element are {max_key1} and {max_key2}",align='C') 
    
    pdf.set_font('Karma-Regular', '', 16) 
    roundedBox(pdf,"#FFF2D7",20,pdf.get_y() + 20, pdf.w - 40,pdf.no_of_lines(dominantElementData[0],pdf.w - 45) * 8 + 5)
    pdf.set_xy(23.5,pdf.get_y() + 22.5)
    pdf.set_text_color(0,0,0)
    pdf.multi_cell(pdf.w - 45,8,dominantElementData[0],align='L')
        
    colors = [
        "#FF0000",
        "#43A458",
        "#B1DC36",
        "#4399FF"
    ]

    x_start = 20
    y_base = pdf.get_y() + 75
    bar_width = 20
    bar_spacing = 10
    max_height = 50

    pdf.draw_bar_chart(x_start, y_base, bar_width, bar_spacing, elements, colors, max_height, path)
    
    y = pdf.get_y() - 45
    for i,(label,value) in enumerate(elements.items()):
        pdf.set_font('Karma-Semi', '', 18)
        pdf.set_text_color(*hex_to_rgb(colors[i]))
        pdf.text(150,y,f'{label}: {value:.2f}%')
        y += 15
    
    pdf.set_text_color(0,0,0)
    pdf.set_y(pdf.get_y() + 15)
    
    pdf.set_font("Times", '', 14)
    pdf.set_xy(22.5,pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 45, 8, f"**Strength** : {dominantElementData[1][0]}, {dominantElementData[1][1]}, {dominantElementData[1][2]}, {dominantElementData[1][3]}",align='L',markdown=True)
    pdf.set_xy(22.5,pdf.get_y())
    pdf.set_font("Times", '', 14)
    pdf.multi_cell(pdf.w - 45, 8, f"**Challenges** : {dominantElementData[2][0]}, {dominantElementData[2][1]}, {dominantElementData[2][2]}, {dominantElementData[2][3]}",align='L',markdown=True)
    
    pdf.set_y(pdf.get_y() + 10)
    pdf.set_font('Karma-Semi', '', 16)
    pdf.cell(0,0,f"Parenting Tips to Balance {max_key1} Element", align='C')	
    pdf.set_xy(22.5,pdf.get_y() + 10)
    pdf.set_font("Times", '', 14)
    pdf.multi_cell(pdf.w - 45, 8, f"    **{dominantElementData[3]['title']}** : {dominantElementData[3]['desc']}",align='L',markdown=True)
    
    
    pdf.AddPage(path,)
    pdf.set_xy(20,20)
    pdf.set_font('Karma-Heavy', '' , 26)
    pdf.set_text_color(hex_to_rgb("#966A2F"))
    pdf.multi_cell(pdf.w - 40 , 10, f"{name}'s  Ayurvedic Body Type", align='C')
    pdf.set_text_color(hex_to_rgb("#04650D"))
    pdf.set_fill_color(hex_to_rgb("#BAF596"))
    pdf.set_draw_color(hex_to_rgb("#06FF4C"))
    pdf.rect(22.5,pdf.get_y() + 5,pdf.w - 45,15,round_corners=True,corner_radius=5,style='DF')
    pdf.set_y(pdf.get_y() + 5)
    pdf.set_font_size(14)
    lagna = list(filter(lambda x : x['Name'] == "Ascendant",planets))[0]
    data = {
        "Pitta": (int(constitutionRatio[moon['zodiac_lord']]['Pitta']) + int(constitutionRatio[lagna['zodiac_lord']]['Pitta'])) / 200 * 100,
        "Kapha": (int(constitutionRatio[moon['zodiac_lord']]['Kapha']) + int(constitutionRatio[lagna['zodiac_lord']]['Kapha'])) / 200 * 100,
        "Vadha": (int(constitutionRatio[moon['zodiac_lord']]['Vata']) + int(constitutionRatio[lagna['zodiac_lord']]['Vata'])) / 200 * 100,
    }
    
    maxValue = max(data, key=data.get)
    constitutionMax = Constitution[maxValue]
    pdf.cell(0,15,f"{name}'s Body is Dominated by {maxValue} Nature",align='C') 
    
    
    pdf.set_font('Karma-Regular', '', 14) 
    roundedBox(pdf,"#D7ECFF",20,pdf.get_y() + 20,pdf.w - 40,pdf.no_of_lines(constitutionMax[0],pdf.w - 45) * 8 + 5)
    pdf.set_xy(22.5,pdf.get_y() + 22.5)
    pdf.set_text_color(0,0,0)
    pdf.multi_cell(pdf.w - 45,8,f"{constitutionMax[0]}",align='L')
    
    colors = [
        "#E34B4B",   
        "#43C316",   
        "#4BDAE3"    
    ]

    x_start = 30
    y_base = pdf.get_y() + 60
    bar_width = 20
    bar_spacing = 20
    max_height = 40

    pdf.draw_bar_chart(x_start, y_base, bar_width, bar_spacing, data, colors, max_height,path)
    pdf.set_y(pdf.get_y() - 35)
    for i,(label,value) in enumerate(data.items()):
        pdf.set_font('Karma-Semi', '', 18)
        pdf.set_text_color(*hex_to_rgb(colors[i]))
        pdf.text(150,pdf.get_y(),f'{label}: {value:.2f}%')
        pdf.set_y(pdf.get_y() + 15)
        
    pdf.set_text_color(0,0,0)
    pdf.set_y(pdf.get_y() + 10)
    pdf.set_font('Karma-Semi', '', 16)
    pdf.cell(0,0,"Impacts on Body Type, Emotions, and Health",align='C')
    
    pdf.set_font("Times", '', 14)
    pdf.set_xy(22.5,pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 45, 8, f"**Body Type** : {constitutionMax[1]}",align='L',markdown=True)
    pdf.set_xy(22.5,pdf.get_y())
    pdf.set_font("Times", '', 14)
    pdf.multi_cell(pdf.w - 45, 8, f"**Emotions** : {constitutionMax[2]}",align='L',markdown=True)
    pdf.set_xy(22.5,pdf.get_y())
    pdf.set_font("Times", '', 14)
    pdf.multi_cell(pdf.w - 45, 8, f"**Health** : {constitutionMax[3]}",align='L',markdown=True)
    
    pdf.set_y(pdf.get_y() + 10)
    pdf.set_font('Karma-Semi', '', 16)
    pdf.cell(0,0,f"Parenting Tips to Balance {max_key1} Dosha", align='C')	
    pdf.set_xy(22.5,pdf.get_y() + 10)
    pdf.set_font("Times", '', 14)
    pdf.multi_cell(pdf.w - 45, 8, f"    **{constitutionMax[4]['title']}** : {constitutionMax[4]['desc']}",align='L',markdown=True)
    
    
    DesignColors = ["#BDE0FE", "#FEFAE0", "#FFC8DD", "#CAF0F8", "#FBE0CE", "#C2BCFF", "#9DE3DB", "#EDBBA3", "#EDF2F4", "#FFD6A5" , "#CBF3DB", "#94D8FD", "#DEE2FF", "#FEEAFA", "#D7AEFF", "#EEE4E1"]
    
    chakrasOrder = ["Root Chakra","Sacral Chakra","Solar Plexus Chakra","Heart Chakra","Throat Chakra","Third Eye Chakra","Crown Chakra"]
    
    pdf.AddPage(path,f"{name}'s Chakras")
    pdf.set_text_color(0,0,0)
    pdf.set_font_size(18)
    childChakras = chakras[planets[0]['sign']][0]
    chakrasContent = chakra_desc[childChakras]
    pdf.set_xy(20,pdf.get_y() + 10)
    pdf.multi_cell(pdf.w - 40,8,f"{name}'s Dominant Chakra is {childChakras}",align='C')
    pdf.set_font('Karma-Regular', '', 14)
    pdf.set_xy(20,pdf.get_y() + 10)
    pdf.multi_cell(pdf.w - 40,8,f"      {chakrasContent[0]}",align='L')
    pdf.set_font("Karma-Heavy", '', 16)
    pdf.set_xy(22.5, pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 45,8, chakrasContent[1],align='C')
    if chakrasOrder.index(childChakras) in [5,6]:
        pdf.image(f"{path}/babyImages/chakra_{chakrasOrder.index(childChakras) + 1}.png",pdf.w / 2 - 20,pdf.get_y() + 5 ,40,0)
    else:
        pdf.image(f"{path}/babyImages/chakra_{chakrasOrder.index(childChakras) + 1}.png",pdf.w / 2 - 15,pdf.get_y() + 10 ,30,0)
    pdf.set_y(pdf.get_y() + 55)
    pdf.set_font('Karma-Heavy', '', 22)
    pdf.cell(0,0,f"{childChakras}",align='C')
    pdf.set_xy(22.5,pdf.get_y() + 10)   
    pdf.set_font('Karma-Semi', '', 16)
    pdf.multi_cell(pdf.w - 45,8,f"Parenting Tips to Increase {name}'s Aura and Energy Level",align='C')
    pdf.set_xy(22.5, pdf.get_y() + 10)
    pdf.set_font('Times', '' , 14)
    pdf.multi_cell(pdf.w - 45,8,f"          **{chakrasContent[2]['title']}** : {chakrasContent[2]['desc']}",align='L',markdown=True)

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
    content = {'child_personality': lagnaIdentity[planets[0]['sign']].replace("child",name).replace("Child",name), 'emotional_needs': moonIdentity[planets[2]['sign']].replace("child",name).replace("Child",name), 'core_identity': sunIdentity[planets[1]['sign']].replace("child",name).replace("Child",name)}
    
    trueTitle = {
        "child_personality" : f"{name}'s Personality",
        "emotional_needs" : f"{name}'s Emotions",
        "core_identity" : f"{name}'s Core Identity"
    }
    
    for index , (k, v) in enumerate(content.items()):
        if pdf.get_y() + 30 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(20)
            
        pdf.ContentDesign(random.choice(DesignColors),trueTitle[k],v,path,name)
    
        
    pdf.AddPage(path,f"Panchangam: A Guide to {name}'s Flourishing Future")
    pdf.set_font('Karma-Regular', '' , 14)
    pdf.set_text_color(0,0,0)
    pdf.set_xy(22.5,pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 45, 8 , "Activating the Panchangam elements (Thithi, Vaaram, Nakshatra, Yogam, Karanam) can potentially bring balance to Magizh's life, fostering positive energies and promoting growth.", align='L')
    pdf.set_y(pdf.get_y() + 5)
    pdf.lineBreak(f"{name} was born on {formatted_date}, {panchang['week_day']} (Vaaram), under {panchang['nakshatra']} Nakshatra, {panchang['paksha']} Paksha {panchang['thithi']} Thithi, {panchang['karanam']} Karanam, and {panchang['yoga']} Yogam",path, "#BAF596")
    
    content = [
        "",
        "Magizh, born on a Saturday, possesses a charismatic and energetic personality that draws others towards him. With a natural flair for leadership and a confident demeanor, he is often the life of the party and the center of attention. Magizh's determination and drive allow him to excel in any endeavor he pursues, making him a force to be reckoned with in both his personal and professional life. His adventurous spirit and daring nature inspire those around him to push beyond their limits and strive for greatness.",
        "Magizh, born under the Bharani Nakshatra, is known for his intense and determined nature. He possesses a strong sense of purpose and tends to be ambitious in achieving his goals. Magizh is also known for his leadership qualities and assertiveness, often taking charge in difficult situations. His life path is marked by challenges that push him to grow and evolve, ultimately leading him towards success and fulfillment in his endeavors.",
        "Magizh, born under the Shiva Yogam, possesses a strong sense of determination and focus in achieving his goals. He is guided by a deep spiritual connection to Shiva, constantly seeking ways to improve and grow on a spiritual level. Magizh's Yogam characteristics empower him to overcome challenges and obstacles, leading to a profound impact on his overall well-being and personal development.",
        "Magizh, born under the Vishti Karanam, has a tendency to be impatient and quick-tempered, leading to a sense of urgency and drive in approaching tasks. Their work habits are characterized by a constant need to stay busy and productive, often taking on multiple projects at once. To achieve success, Magizh focuses on efficient time management and prioritizing tasks based on importance. Despite the challenges posed by their Karanam, Magizh has achieved notable success through their determination and ability to adapt to changing situations."
    ]
    
    colors = ["#E5FFB5","#94FFD2","#B2E4FF","#D6C8FF","#FFDECA"]    
    titles = [f"Tithi Represents {name}'s Emotions, Mental Well-being",f"Vaaram Represents {name}'s Energy & Behaviour",f"Nakshatra Represents {name}'s Personality and Life Path",f"Yogam Represents {name}'s Prosperity and Life Transformation",f"Karanam Represents {name}'s Work and Actions"]
    
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
            pdf.multi_cell(pdf.w - 45,7,f"{name} was born under {panchang['paksha']} {panchang['thithi']}, and the following are Thithi impacts on {name}'s Life ",align='C')
            y = pdf.get_y() + 5
            pdf.set_xy(20,y)
            pdf.set_fill_color(hex_to_rgb("#DAFFDC"))
            pdf.set_font('Karma-Semi', '', 16)
            
            pdf.checkNewPage(path)
            data = [
                (f"Strength",f"Challenges"),
                (positive[0],negative[0]),
                (positive[1],negative[1]),
                (positive[2],negative[2])
            ]
            
            pdf.panchangTable(data)
                
            pdf.checkNewPage(path)
            pdf.set_xy(30,pdf.get_y() + 5)
            pdf.set_fill_color(hex_to_rgb(random.choice(DesignColors)))
            pdf.set_font("Times", '', 14)
            pdf.cell(pdf.w - 60,10,f"Thithi Lord: **{thithiLord[panchang['thithi']]}**",align='C',fill=True,new_y=YPos.NEXT,markdown=True)
                
            pdf.set_font("Times", '', 14)
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.multi_cell(pdf.w - 45,7,f"**Parenting Tips** : {tips['Name']} {tips['Description']} {tips['Execution']}",align='L',markdown=True)
            pdf.set_y(pdf.get_y() + 10)
            
        elif i == 1:
            positive = weekPlanetContent[panchang['week_day']][0]
            negative = weekPlanetContent[panchang['week_day']][1]
            tips = weekPlanetContent[panchang['week_day']][2]
            pdf.checkNewPage(path)
            
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.set_font('Karma-Semi', '', 18)
            pdf.multi_cell(pdf.w - 45, 8,titles[i], align='C')
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.set_font('Karma-Regular', '', 14)
            pdf.multi_cell(pdf.w - 45,7,f"{name} was born on {panchang['week_day']}, and the following are its impacts on {name}'s life:",align='C')
            pdf.checkNewPage(path)
            
            pdf.checkNewPage(path)
            data = [
                (f"Strength",f"Challenges"),
                (positive[0],negative[0]),
                (positive[1],negative[1]),
                (positive[2],negative[2])
            ]
            
            pdf.panchangTable(data)         
                   
            pdf.checkNewPage(path)
            pdf.set_xy(30,pdf.get_y() + 5)
            pdf.set_fill_color(hex_to_rgb(random.choice(DesignColors)))
            pdf.set_font("Times", '', 14)
            pdf.cell(pdf.w - 60,10,f"Rulling Planet: **{weekPlanet[panchang['week_day']]}**",align='C',fill=True,new_y=YPos.NEXT,markdown=True)
            
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.multi_cell(pdf.w - 45,7,f"**Parenting Tips** : {tips['Tip']} {tips['Execution']}",align='L',markdown=True)
            pdf.set_y(pdf.get_y() + 10)
            
        elif i == 4:
            positive = karanamContent[panchang['karanam']][0]
            negative = karanamContent[panchang['karanam']][1]
            tips = karanamContent[panchang['karanam']][2]
            
            pdf.checkNewPage(path)
            
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.set_font('Karma-Semi', '', 18)
            pdf.multi_cell(pdf.w - 45, 8,titles[i], align='C')
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.set_font('Karma-Regular', '', 14)
            pdf.multi_cell(pdf.w - 45,7,f"{name} was born under {panchang['karanam']}, and the following are Karanm impacts on {name}'s life:",align='C')
            pdf.checkNewPage(path)
            
            data = [
                (f"Strength",f"Challenges"),
                (positive[0],negative[0]),
                (positive[1],negative[1]),
                (positive[2],negative[2])
            ]
            
            pdf.panchangTable(data)            
            pdf.checkNewPage(path)
            pdf.set_font("Times", '', 14)
            pdf.set_xy(22.5,pdf.get_y() + 5)
            pdf.multi_cell(pdf.w - 45,7,f"**Parenting Tips** : {tips['Tip']} {tips['Execution']}",align='L',markdown=True)
            pdf.set_y(pdf.get_y() + 10)
        else:
            pdf.ContentDesign(random.choice(DesignColors),titles[i],con,path,name)   

                
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
                
                pdf.ContentDesign(random.choice(DesignColors),titles[index][k],v,path,name)
                    
    sifted = zodiac[zodiac.index(asc['sign']):] + zodiac[:zodiac.index(asc['sign'])]
    pdf.AddPage(path,"Potential Health Challenges and Holistic Wellness Solutions")
    sixth_house = "Aquarius"
    con = healthContent[sixth_house]
    insights = healthInsights[sixth_house]
    pdf.set_y(pdf.get_y() + 5)
    pdf.set_font('Karma-Regular', '', 14)
    pdf.set_text_color(0,0,0) 
    pdf.lineBreak(insights,path,random.choice(DesignColors))
    color = random.choice(DesignColors)
    color2 = random.choice(DesignColors)
    col_width = pdf.w / 2 - 10 - 2.5
    
    pdf.set_xy(20, pdf.get_y() + 12.5)
    pdf.set_font('Karma-Semi', '' , 18)
    pdf.cell(0,0,"Health Issues Based on", align='C')
    x = 10 + col_width
    y = pdf.get_y()
    roundedBox(pdf, color, 10 , pdf.get_y() + 5, col_width, 40)
    roundedBox(pdf, color2 , x + 5 , pdf.get_y() + 5, col_width, 40)
    pdf.set_xy(12.5,pdf.get_y() + 7.5)
    pdf.set_font('Karma-Semi', '' , 15)
    pdf.cell(col_width - 5,8, f"{sixth_house} Sign",align='C')
    pdf.set_xy(12.5, pdf.get_y() + 8)
    pdf.set_font("Times", '' , 14)
    for index,c in enumerate(con[0]):
        text = str(c).split(" (")   
        if index < len(con[0]) - 2:
            roundedBox(pdf,color,10, pdf.get_y() + 2.5, col_width, pdf.no_of_lines(f"{index + 1}) {text[0]} ({text[1]}", col_width - 5) * 8 + 8, status=False)
        elif index == len(con[0]) - 2:
            roundedBox(pdf,color,10, pdf.get_y() + 2.5, col_width, pdf.no_of_lines(f"{index + 1}) {text[0]} ({text[1]}", col_width - 5) * 8 + 5, status=False)
        else:
            roundedBox(pdf,color,10, pdf.get_y() + 2.5, col_width, pdf.no_of_lines(f"{index + 1}) {text[0]} ({text[1]}", col_width - 5) * 8 + 2.5)
        pdf.multi_cell(col_width - 5, 8 , f"{index + 1}) **{text[0]}** ({text[1]}" , align='L', new_x=XPos.LEFT, new_y=YPos.NEXT,markdown=True)
    max_y1 = pdf.get_y()
    pdf.set_xy(x + 7.5,y + 7.5)
    pdf.set_font('Karma-Semi', '' , 15)
    pdf.cell(col_width - 5,8, f"{sixth_house} Dosha Constitution",align='C')
    pdf.set_xy(x + 7.5, pdf.get_y() + 8)
    pdf.set_font("Times", '' , 14)
    for index,c in enumerate(con[1]):
        text = str(c).split(" (")   
        if index != len(con[1]) - 1:
            roundedBox(pdf,color2,x + 5, pdf.get_y() + 2.5, col_width, pdf.no_of_lines(f"{index + 1}) {text[0]} ({text[1]}", col_width - 5) * 8 + 8, status=False)
        else:
            roundedBox(pdf,color2,x + 5, pdf.get_y() + 5, col_width, pdf.no_of_lines(f"{index + 1}) {text[0]} ({text[1]}", col_width - 5) * 8 + 2.5)
            roundedBox(pdf,color2,x + 5, pdf.get_y() + 2.5, col_width, 8, status=False)
                
        pdf.multi_cell(col_width - 5, 8 , f"{index + 1}) **{text[0]}** ({text[1]}" , align='L', new_x=XPos.LEFT, new_y=YPos.NEXT,markdown=True)
    max_y2 = pdf.get_y()
    
    pdf.set_y(max(max_y1,max_y2))    
    pdf.checkNewPage(path)
    content = con[3]['natural']
    pdf.set_y(pdf.get_y() + 20)
    pdf.set_font('Karma-Heavy', '' , 18)
    pdf.cell(0,0, f"Remedial Practices",align='C')
    pdf.set_font_size(16)
    title = [
        "Natural Ayurvedic Remedy",
        "Mudra Practice Remedy",
        "Mindful Food & Diet Remedy"
    ]
    pdf.set_y(pdf.get_y() + 5)
    colors = ["#CBF3DB","#FFD6A5", "#DEE2FF"]
    for i,t in enumerate(title): 
        pdf.set_xy(30,pdf.get_y())
        roundedBox(pdf,colors[i], pdf.w / 2 - 50, pdf.get_y(), 100, 10, corner=10)
        pdf.cell(pdf.w - 60,10,t,align='C')
        pdf.set_y(pdf.get_y() + 15)
    
    pdf.AddPage(path)
    pdf.set_y(20)
    color = colors[0]
    roundedBox(pdf, color, 20, pdf.get_y() + 7.5, pdf.w - 40, 50)
    pdf.image(f"{path}/babyImages/ayur.png",pdf.w / 2 - 10,pdf.get_y() + 7.5,20,20)
    pdf.set_y(pdf.get_y() + 32.5)
    pdf.cell(0,0,"Natural Ayurvedic", align='C')
    pdf.set_font('Karma-Regular', '' , 14) 
    roundedBox(pdf, color, 20, pdf.get_y() + 5, pdf.w - 40, 20)
    pdf.set_xy(22.5, pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 45, 8 , content[0], align='C')
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf, color, 20, pdf.get_y() + 5, pdf.w - 40, pdf.no_of_lines(f"Ingredients: {content[1]}", pdf.w - 45)* 8 + 8)
    pdf.set_xy(22.5, pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 45, 8 , f"**Ingredients:** {content[1]}",markdown=True)
    roundedBox(pdf, color, 20, pdf.get_y(), pdf.w - 40, pdf.no_of_lines(f"How to Make: {content[2]}", pdf.w - 45)* 8 + 8,status=False)
    pdf.set_xy(22.5, pdf.get_y())
    pdf.multi_cell(pdf.w - 45, 8 , f"**How to Make:** {content[2]}",markdown=True)
    roundedBox(pdf, color, 20, pdf.get_y(), pdf.w - 40, pdf.no_of_lines(f"Benefits: {content[3]}", pdf.w - 45)* 8 + 5)
    roundedBox(pdf, color, 20 , pdf.get_y(), pdf.w - 40, 5, status=False)
    pdf.set_xy(22.5, pdf.get_y())
    pdf.multi_cell(pdf.w - 45, 8 , f"**Benefits:** {content[3]}",markdown=True)
    
    content = con[3]['mudra']
    color = colors[1]
    pdf.set_font('Karma-Semi', '' , 16)
    pdf.set_xy(22.5,pdf.get_y() + 20)
    roundedBox(pdf, color, 20, pdf.get_y(), pdf.w - 40, 60)
    pdf.image(f"{path}/babyImages/mudra.png",pdf.w / 2 - 10,pdf.get_y() + 7.5,20,20)
    pdf.set_y(pdf.get_y() + 35)
    pdf.cell(0,0,"Mudra Practice Remedy", align='C')
    pdf.set_font('Karma-Regular', '' , 14) 
    pdf.set_xy(22.5, pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 45, 8 , content[0], align='C')
    roundedBox(pdf, color, 20, pdf.get_y(), pdf.w - 40, 20,status=False)
    pdf.set_font('Karma-Semi', '' , 16)
    pdf.set_xy(22.5,pdf.get_y() + 5)
    pdf.cell(0,0,"Steps",align='L')
    pdf.set_y(pdf.get_y() + 5)
    pdf.set_font('Karma-Regular', '' , 14)
    for i,n in enumerate(content[1]):
        if pdf.get_y() + pdf.no_of_lines(f"{index}) {n}", pdf.w - 60) * 8 > 270:
            pdf.AddPage(path)
            pdf.set_y(20) 
        roundedBox(pdf, color, 20, pdf.get_y() + 5, pdf.w - 40, pdf.no_of_lines(f"{i + 1}) {n}",pdf.w - 60) * 8 + 8,status=False)
        pdf.set_xy(30, pdf.get_y() + 2.5)
        pdf.multi_cell(pdf.w - 60, 8 , f"{i + 1}) {n}" , align='L')
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf,color,20,pdf.get_y() + 5, pdf.w - 40, pdf.no_of_lines(f"Benefits: {content[2]}",pdf.w - 45) * 8 + 5)
    pdf.set_xy(22.5, pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 45, 8 , f"**Benefits:** {content[2]}",markdown=True)
        
    pdf.AddPage(path)
    pdf.set_font('Karma-Semi', '' , 16)
    pdf.set_y(pdf.get_y() + 10)
    roundedBox(pdf, color, 20, pdf.get_y(), pdf.w - 40, 60)
    pdf.image(f"{path}/babyImages/food.png",pdf.w / 2 - 10,pdf.get_y() + 2.5,20,20)
    pdf.set_y(pdf.get_y() + 32.5)
    pdf.cell(0,0,"Mindful Food & Diet Remedy", align='C')
    content = healthContent[sixth_house][3]['foods']
    pdf.set_font('Karma-Heavy', '' , 16) 
    pdf.image(f"{path}/babyImages/tick.png",22.5,pdf.get_y() + 10,10,10)
    pdf.set_xy(32.5, pdf.get_y() + 10)
    pdf.cell(0,10,"Food to Include", align='L')
    pdf.set_y(pdf.get_y() + 7.5)
    pdf.set_font('Karma-Regular', '' , 14) 
    for i,n in enumerate(content[0]):
        if pdf.get_y() + pdf.no_of_lines(f"{index}) {n}", pdf.w - 60) * 8 > 270:
            pdf.AddPage(path)
            pdf.set_y(20) 
        roundedBox(pdf, color, 20, pdf.get_y() + 2.5, pdf.w - 40, pdf.no_of_lines(f"{i + 1}) {n}",pdf.w - 60) * 8 + 8,status=False)
        pdf.set_xy(30, pdf.get_y() + 2.5)
        pdf.multi_cell(pdf.w - 60, 8 , f"{i + 1}) {n}" , align='L')
    roundedBox(pdf, color, 20, pdf.get_y() + 2.5, pdf.w - 40, 15,status=False)
    pdf.image(f"{path}/babyImages/cancel.png",22.5,pdf.get_y() + 5,10,10)
    pdf.set_xy(32.5, pdf.get_y() + 5)
    pdf.set_font('Karma-Heavy', '' , 16) 
    pdf.cell(0,10,"Food to Avoid", align='L')
    pdf.set_y(pdf.get_y() + 7.5)
    pdf.set_font('Karma-Regular', '' , 14) 
    for i,n in enumerate(content[1]):
        if pdf.get_y() + pdf.no_of_lines(f"{index}) {n}", pdf.w - 60) * 8 > 270:
            pdf.AddPage(path)
            pdf.set_y(20) 
        roundedBox(pdf, color, 20, pdf.get_y() + 2.5, pdf.w - 40, pdf.no_of_lines(f"{i + 1}) {n}",pdf.w - 60) * 8 + 8,status=False)
        pdf.set_xy(30, pdf.get_y() + 2.5)
        pdf.multi_cell(pdf.w - 60, 8 , f"{i + 1}) {n}" , align='L')
    roundedBox(pdf, color, 20, pdf.get_y() + 2.5, pdf.w - 40, 15,status=False)
    pdf.image(f"{path}/babyImages/guide.png",22.5,pdf.get_y() + 5,10,10)
    pdf.set_xy(32.5, pdf.get_y() + 5)
    pdf.set_font('Karma-Heavy', '' , 16) 
    pdf.cell(0,10,"Execution Guide", align='L')
    pdf.set_y(pdf.get_y() + 7.5)
    pdf.set_font('Karma-Regular', '' , 14) 
    for i,n in enumerate(content[2]):
        if pdf.get_y() + pdf.no_of_lines(f"{index}) {n}", pdf.w - 60) * 8 > 270:
            pdf.AddPage(path)
            pdf.set_y(20) 
        roundedBox(pdf, color, 20, pdf.get_y() + 2.5, pdf.w - 40, pdf.no_of_lines(f"{i + 1}) {n}",pdf.w - 60) * 8 + 8,status=False)
        pdf.set_xy(30, pdf.get_y() + 2.5)
        pdf.multi_cell(pdf.w - 60, 8 , f"{i + 1}) {n}" , align='L')
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf,color,20,pdf.get_y() + 5, pdf.w - 40, pdf.no_of_lines(f"Benefits: {content[3]}",pdf.w - 45) * 8 + 5)
    pdf.set_xy(22.5, pdf.get_y() + 5)
    pdf.multi_cell(pdf.w - 45, 8 , f"**Benefits:** {content[3]}",markdown=True)
            
    pdf.AddPage(path,f"{name}'s Education and Intellect")
    pdf.set_font('Karma-Semi','', 16)
    pdf.set_y(pdf.get_y() + 10)
    pdf.cell(0,0,f"Insights about {name}'s education and intelligence",align='C')
    pdf.set_font('Karma-Regular', '', 14)
    
    educationTitle = {
        "insights" : "Education and Intellectual Insights",
        "suitable_educational" : "Higher Education Preferences", 
        "cognitive_abilities" : "Learning Approaches", 
        "recommendations" : "How To Do It:"
    }
    
    content = education[moon['sign']]

    con = {'insights': content[0], 'suitable_educational': content[1], 'cognitive_abilities': content[2], 'recommendations': content[4]}
    
    pdf.set_text_color(0, 0, 0)
    
    for index,(k, v) in enumerate(con.items()):
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        if index == 3:
            if pdf.get_y() + 30 >= 260:
                pdf.AddPage(path)
                pdf.set_y(20)
                
            pdf.set_y(pdf.get_y() + 10)
            pdf.set_font('Karma-Semi' , '' , 18)
            pdf.cell(0,0,"Parenting Tip for Academic Excellence:", align='C')
            pdf.set_font_size(15)
            pdf.set_y(pdf.get_y() + 10) 
            pdf.cell(0,0, content[3],align='C')
            pdf.set_y(pdf.get_y() + 5)
            
        pdf.ContentDesign(random.choice(DesignColors),educationTitle[k],v,path,name)
            
    pdf.AddPage(path,"Family and Relationships")
    # con = physical(planets,5,name,gender)
    con = {'family_relationship': "Magizh's family dynamics are influenced by strong connections with his parents and siblings. His relationship with his father (represented by the Sun) is nurturing and supportive, while his relationship with his mother (represented by the Moon) is emotionally fulfilling. In terms of social development, Magizh thrives in building friendships and engaging with peers, seeking harmony and balance in his interactions, influenced by Venus in the 1st House of Libra.", 'approaches': [{'title': 'Building Social Bonds', 'content': 'Magizh approaches social development by prioritizing harmonious relationships and seeking beauty and balance in interactions, influenced by Venus in the 1st House of Libra.'}, {'title': 'Nurturing Relationship with Father', 'content': "Magizh bonds with his father by seeking guidance and support, appreciating his father's warmth and leadership qualities, influenced by the Sun in the 3rd House of Sagittarius."}, {'title': 'Emotional Connection with Mother', 'content': 'Magizh forms a deep emotional bond with his mother, seeking comfort and security in her nurturing presence, influenced by the Moon in the 7th House of Aries.'}], 'challenges': [{'title': 'Overcoming Shyness', 'content': 'Magizh may struggle with shyness and hesitation in forming new friendships and social connections, impacting his social interactions and peer relationships.'}, {'title': 'Balancing Independence and Interdependence', 'content': 'Magizh faces the challenge of balancing his independent nature with the need for partnership and cooperation in relationships, especially with siblings and friends.'}, {'title': 'Navigating Family Expectations', 'content': 'Magizh may experience pressure from family expectations, especially in balancing personal aspirations with familial responsibilities, leading to internal conflicts.'}], 'parenting_support': [{'title': 'Encouraging Communication Skills', 'content': "Parents can support Magizh's social development by encouraging open communication, active listening, and expressive sharing of thoughts and emotions, fostering healthy relationships."}, {'title': 'Promoting Independence', 'content': "Parents can nurture Magizh's independence by allowing him space for self-expression, decision-making, and exploring personal interests, promoting self-confidence and autonomy."}, {'title': 'Cultivating Emotional Intelligence', 'content': 'Parents can help Magizh develop emotional intelligence by teaching him to identify and manage emotions, empathize with others, and navigate interpersonal relationships with empathy and understanding.'}]}
    
    familyTitle = {
        'family_relationship' : "",
        'approaches': f"{name}'s Approaches for Forming Relationships",
        'challenges' : f"Challenges in the {name}'s relationship & social development",
        'parenting_support' : f"Parenting Support for Improve {name}'s Social Developments"
    }
    
    for k, v in con.items():
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),familyTitle[k],v,path,name)
                
    pdf.AddPage(path,f"{name}'s Career and Professions")
    pdf.set_font('Karma-Semi','', 16)
    pdf.set_xy(20,pdf.get_y() + 10)
    pdf.multi_cell(pdf.w - 40,8,"Wondering what the future holds for your child's career journey?",align='L')
    contents = carrer[sifted[9]]
    profess = []
    for k,v in contents[1].items():
        profess.append({
            'title' : k,
            'content' : v
        })
    
    con = {'career_path': contents[0], 'suitable_professions': profess}

    CarrerTitle = {
        "suitable_professions" : f"{name}'s Successful Career Path & Suitable Professions", 
        "business": "Business & Entrepreneurial Potentials"
    }
    
    for index,(k, v) in enumerate(con.items()):
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        if index == 0:    
            pdf.ContentDesign(random.choice(DesignColors),"",v,path,name)
        else:
            for v1 in v:
                v1['content'] = v1['content'].replace(sifted[9], name)
            pdf.ContentDesign(random.choice(DesignColors),CarrerTitle[k],v,path,name)
                                    
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
        
        pdf.ContentDesign(random.choice(DesignColors),subTitle[k],v,path,name)
        
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
        
        pdf.ContentDesign(random.choice(DesignColors),uniqueTitle[k],v,path,name)
        
        
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
        
        pdf.ContentDesign(random.choice(DesignColors),karmicTitle[k],v,path,name)
                            
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
    
    stones = [Planet_Gemstone_Desc[asc['zodiac_lord']],Planet_Gemstone_Desc[fiveHouseLord],Planet_Gemstone_Desc[ninthHouseLord]]
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
            pdf.ContentDesign(random.choice(DesignColors),k,v,path,name)
    
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
            
            pdf.ContentDesign("#FFEED7",k.capitalize(),v,path,name)
    
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
    
    # "Discipline, Habits, Diet, and Lifestyle Based on Planetary Energy"
    
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
            

        pdf.AddPage(path)
            
        pdf.set_text_color(hex_to_rgb("#966A2F"))
        pdf.set_font('Karma-Heavy', '', 20)
        pdf.set_xy(20,pdf.get_y() + 5)
        pdf.multi_cell(pdf.w - 40,10,f"{planet['Name']} - {planetMain[planet['Name']]}",align='C')
        pdf.image(f"{path}/babyImages/{planet['Name']}.png",40,pdf.get_y() + 10,30,30)
        y = pdf.get_y() + 10
        pdf.set_font('Karma-Regular', '', 12) 
        pdf.set_text_color(0,0,0)
        content = planetDesc[planet['Name']]
        if planet['Name'] == "Rahu" or planet['Name'] == "Ketu":
            roundedBox(pdf,random.choice(DesignColors),85,pdf.get_y() + 5,110, pdf.no_of_lines(content[0],105) * 8 + 5)
            pdf.set_xy(90,pdf.get_y() + 7.5)
            pdf.multi_cell(105,8,content[0],align='L')
        else:
            roundedBox(pdf,random.choice(DesignColors),85,pdf.get_y() + 10,110, pdf.no_of_lines(content[0],105) * 8 + 5)
            pdf.set_xy(90,pdf.get_y() + 12.5)
            pdf.multi_cell(105,8,content[0],align='L')
        
        if planet['Name'] == "Ketu":
            y = y + 10
        
        pdf.set_y(y + 40)
        pdf.set_font('Karma-Semi', '' , 16) 
        pdf.cell(0,0,f"Discipline : {content[1][0]}",align='C')
        pdf.set_xy(22.5,pdf.get_y() + 5)
        pdf.set_font('Karma-Regular', '', 14)
        
        smallTitle = {
            1 : "",
            2 : "Steps: ",
            3 : "Lesson: "
        }
        
        for i in range(1,len(content[1])):
            pdf.multi_cell(pdf.w - 45,7,f"{smallTitle[i]}{content[1][i]}",align='L',new_y=YPos.NEXT, new_x=XPos.LEFT)
        pdf.set_y(pdf.get_y() + 5)
        pdf.set_font('Karma-Semi', '' , 16) 
        pdf.cell(0,0,f"Life Lesson : {content[2][0]}",align='C')
        pdf.set_xy(22.5,pdf.get_y() + 5)
        pdf.set_font('Karma-Regular', '', 14)
        
        for i in range(1,len(content[2])):
            pdf.multi_cell(pdf.w - 45,7,f"{smallTitle[i]}{content[2][i]}",align='L',new_y=YPos.NEXT, new_x=XPos.LEFT)
        pdf.set_y(pdf.get_y() + 5)
        pdf.set_font('Karma-Semi', '' , 16) 
        pdf.cell(0,0,f"Food & Diet : {content[4][0]}",align='C')
        pdf.set_xy(22.5,pdf.get_y() + 5)
        pdf.set_font('Karma-Regular', '', 14)
        for i in range(1,len(content[4])):
            pdf.multi_cell(pdf.w - 45,7,f"{smallTitle[i]}{content[4][i]}",align='L',new_y=YPos.NEXT, new_x=XPos.LEFT)
                              
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
            
        pdf.ContentDesign(random.choice(DesignColors),"",celeb,path,name)
        
    
    # content = chapterPrompt(planets,9,name,gender)
    content = {'predictions': "Magizh is born with a Libra lagna, which indicates a balanced and harmonious personality. The placement of Venus in the lagna enhances Magizh's charm and charisma. The presence of Venus as the lagna lord in the 1st house of Libra in Vishakha Nakshatra suggests a strong sense of beauty and artistic appreciation in Magizh's life. This placement also indicates a love for balance and harmony in relationships and surroundings.", 'assessment': "Magizh has a pleasant and diplomatic personality with a strong sense of aesthetics and a keen eye for beauty. The influence of Venus in the lagna and 1st house enhances Magizh's social skills and creativity.", 'strength': "Magizh's strength lies in their ability to maintain harmony in relationships, appreciate beauty in all forms, and express themselves artistically. They have a diplomatic approach towards handling conflicts and a natural charm that attracts others towards them.", 'weakness': 'However, Magizh may struggle with indecisiveness and a tendency to prioritize harmony over assertiveness. They may also face challenges in asserting their individuality in certain situations due to a strong desire for peace and balance.', 'action': 'To nurture Magizh, it is essential to encourage their creative pursuits, provide opportunities for self-expression, and help them develop assertiveness in communication and decision-making.', 'overall': "Overall, Magizh is a charming and diplomatic individual with a strong sense of aesthetics and a love for harmony in relationships. They thrive in environments that appreciate beauty and value peace and balance. Nurturing Magizh's creativity and supporting them in developing assertiveness will help them flourish in all aspects of life.", 'recommendations': 'Parenting suggestions for nurturing Magizh include encouraging artistic endeavors, providing opportunities for social interactions to enhance their diplomatic skills, and teaching them to assert their individuality when needed. It is important to support Magizh in finding a balance between harmony and self-expression, and to guide them in making confident decisions while maintaining their sense of beauty and diplomacy.'} 

    
    pdf.AddPage(path,f"Summary Insights for Parents and Child")
    
    for k, v in content.items():
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
            pdf.set_text_color(0,0,0)
        
        pdf.ContentDesign(random.choice(DesignColors),setTitle(k),v,path,name)
    
    pdf.output(f'{path}/pdf/{name} - babyReport.pdf')
    
def babyReport(dob,location,lat,lon,path,gender,name):
    print("Generating Baby Report")
    planets = find_planets(dob,lat,lon)
    print("Planets Found")
    thithi = ["Pratipada", "Ditiya", "Tritiya", "Chaturthi", "Panchami", "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami", "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima","Amavasya"]
    panchang = calculate_panchang(dob,planets[2]['full_degree'],planets[1]['full_degree'],lat,lon)
    print("Panchang Calculated")
    for pl in planets:
        print(pl['Name'],pl['sign'],pl['nakshatra'],pl['full_degree'])
        
    for key in panchang.keys():
        print(key,panchang[key])
    value = "y"
    
    if value.lower() == 'y':
        dasa = calculate_dasa(dob,planets[2])
        print("Dasa Calculated")    
        # birthchart = generate_birth_navamsa_chart(planets,f'{path}/chart/',dob,location,name)
        birthchart = {
            'birth_chart' : '1.png',
            'navamsa_chart' : '2.png'
        }
        print("Birth Chart Generated")
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

babyReport("1993-11-03 17:35:00","Madurai, Tamil Nadu , India",8.76735,78.13425,os.getcwd(),"male","Guru")