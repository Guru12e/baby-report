import random
import datetime
from math import atan2, cos, radians, sin
from fpdf import FPDF,YPos,XPos
from index import find_planets
from panchang import calculate_panchang
from chart import generate_birth_navamsa_chart
from datetime import datetime
from babyContent import context,chakras,dasa_status_table,table,karagan,exaltation,athmakaraka,ista_devata_desc,ista_devatas,saturn_pos,constitutionRatio,Constitution,elements_data,elements_content,gemstone_content,Gemstone_about,Planet_Gemstone_Desc,wealth_rudra,sign_mukhi,planet_quality,KaranaLord,thithiLord,yogamLord,nakshatraColor,nakshatraNumber,atma_names,thithiContent,karanamContent,chakra_desc,weekPlanet,weekPlanetContent,sunIdentity,moonIdentity,lagnaIdentity,healthContent,healthInsights,education,carrer,planetDesc,subContent,nakshatraContent
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
        ContentImages = {
            'Physical Attributes': "pg 19_physical.png",
            'Outer Personality' : "pg 19_character.png", 
            'Character' : "pg 19_outer.png",
            'Positive Behavior' : "pg 19_behaviour.png",
            'Behavior Challenges' : "pg 19_impact.png",
            f"Parenting Tips For {name}'s Behaviour Challenges" : "pg 35_parenting.png",
            f"{name}'s Emotional State Insights" : "pg 22_emotional.png", 
            f"{name}'s Emotions" : "pg 22_inner worlds.png",
            f"{name}'s Personality" : "pg 14_child.png",
            f"{name}'s Core Identity" : "pg 15_core identity.png",
            f"{name}'s Feelings" : "pg 24_desire.png",
            f"{name}'s Reactions" : "pg 14_emotional.png",
            f"{name}'s Emotional Imbalance Challenges" : "pg 25_build.png",
            f"Parenting Tips": "pg 35_parenting.png",
            f"{name}'s Soul Desire" : "pg 24_soul.png",
            f"Seek For Recognition" : "pg 45_physical.png", 
            "Core Identity" : "pg 15_core identity.png", 
            f"Parenting Tips For Self Identity Challenges" : "pg 26_challenges.png",
            "Education and Intellectual Insights" : "pg 32_unique.png",
            "Higher Education Preferences" : "pg 31.png", 
            "Learning Approaches" : "pg 31_education.png", 
            "How To Do It:" : "pg 84_assesment.png",
            f"{name}'s Approaches for Forming Relationships" : "pg 35_challenges.png",
            f"Parenting Support for Improve {name}'s Social Developments" : "pg_34.png",
            f"{name}'s Successful Career Path & Suitable Professions" : "pg 37.png", 
            "Business & Entrepreneurial Potentials" : "pg 38_business.png",
            "Saturn's Life Lesson" : "pg 47_saturn.png",
            "Rahu's Life Lesson" : "pg 47_rahu.png",
            "Ketu's Life Lesson": "pg 47_ketu.png",
            "Unique Talents in Academics" : "pg 55.png", 
            "Unique Talents in Arts & Creativity" : "pg 44_art.png",
            "Unique Talents in Physical Activity" : "pg 45_physical.png"
        }
        
        
        if title in ContentImages.keys():
            image = ContentImages[title]
        self.set_text_color(0,0,0)
        self.set_y(self.get_y() + 5)
        self.set_font('Karma-Semi', '', 16)
        if title != "":
            self.set_xy(22.5,self.get_y() + 5)
            if image:
                roundedBox(self, color, 20 , self.get_y()  - 2.5, self.w - 40, (self.no_of_lines(title,self.w - 45) * 7) + 30, 4)
                self.image(f"{path}/icons/{image}", self.w / 2 - 7.5, self.get_y() , 15 , 15)
                self.set_y(self.get_y() + 15)
            else:
                roundedBox(self, color, 20 , self.get_y()  - 2.5, self.w - 40, (self.no_of_lines(title,self.w - 45) * 7) + 10, 4)
            self.set_xy(22.5,self.get_y() + 2.5)
            self.multi_cell(self.w - 45, 7,title, align='C')
        if isinstance(content, str):
            content = content.replace("child", name)
            self.set_font('Karma-Regular', '', 14)
            self.set_xy(22.5,self.get_y() + 2.5)
            if title == "":
                self.roundedContent(f"        {content}",color)   
            else:
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
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40, (self.no_of_lines(f"      {v1}",self.w - 45) * 7) + 10, 0,status=False)
                    else:
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40, (self.no_of_lines(f"      {v1}",self.w - 45) * 7) + 5, 4)
                        roundedBox(self, color, 20 , self.get_y(), self.w - 40, 10, 0,status=False)
                    
                    self.set_xy(22.5,self.get_y() + 2.5)
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
            
    def roundedContent(self, content , color):
        roundedBox(self, color, 20 , self.get_y() , self.w - 40, self.no_of_lines(f"        {content}",self.w - 45) * 7 + 7.5)
        self.set_xy(22.5,self.get_y() + 2.5)
        self.multi_cell(self.w - 45, 7 ,f"       {content}",align='L')
            
    def lineBreak(self, content, path,color):
        cell_width = self.w - 45 
        line_height = 7
        max_y = self.h - 20  
        current_y = self.get_y()
        
        if (current_y + (self.get_string_width(content) / cell_width) * line_height) < 250:
            roundedBox(self,color,20,self.get_y(), self.w - 40 , 5 , status=False)
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

            self.set_font('Karma-Regular', '', 13)

            initial_y = self.get_y()
            
            content = max(self.get_string_width(row[0]), self.get_string_width(row[1]))
            
            if index == 0:
                roundedBox(self, "#DAFFDC", 20 + col_width / 2 , self.get_y(), col_width / 2, 5 ,status=False)
                roundedBox(self, "#FFDADA", self.w / 2 , self.get_y(), col_width / 2, 5 ,status=False)
                roundedBox(self, "#FFDADA", self.w / 2 , self.get_y(), col_width, 20)
                roundedBox(self, "#DAFFDC", 20 , self.get_y(), col_width, 20)
            elif index != len(data) - 1:
                roundedBox(self, "#FFDADA", self.w / 2 , self.get_y(), col_width, (content / (col_width - 8)) * 8 + 8, status=False)
                roundedBox(self, "#DAFFDC", 20 , self.get_y(), col_width, (content / (col_width - 8)) * 8 + 8, status=False)
            else:
                roundedBox(self, "#FFDADA", self.w / 2 , self.get_y(), col_width, 5,status=False)
                roundedBox(self, "#FFDADA", self.w / 2 , self.get_y(), col_width, (content / (col_width - 8)) * 8 + 5)
                roundedBox(self, "#DAFFDC", 20 , self.get_y(), col_width, 5,status=False)
                roundedBox(self, "#DAFFDC", 20 , self.get_y(), col_width, (content / (col_width - 8)) * 8 + 5)
                roundedBox(self, "#DAFFDC", 20 + col_width / 2 , self.get_y() + (content / (col_width - 8)) * 8, col_width / 2, 5 ,status=False)
                roundedBox(self, "#FFDADA", self.w / 2 , self.get_y() + (content / (col_width - 8)) * 8, col_width / 2, 5 ,status=False)
                
            if index == 0:
                self.multi_cell(col_width, 8, row[0], new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
            else:
                self.cell(8, 7, f"{index}) ", new_x=XPos.RIGHT, new_y=YPos.TOP, align='C')
                self.multi_cell(col_width - 8, 7, row[0], new_x=XPos.RIGHT, new_y=YPos.TOP,align='L')

            y_after_col1 = self.get_y()

            self.set_y(initial_y)
            self.set_x(x_start + col_width)

            if index == 0:
                self.multi_cell(col_width, 8, row[1], align='C')
            else:
                self.cell(8, 7, f"{index}) ", align='C')
                self.multi_cell(col_width - 8, 7, row[1], align='L')

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
    
    fiveHouseLord = zodiac_lord[((zodiac.index(asc['sign']) + 5) % 12) - 1]
    ninthHouseLord = zodiac_lord[((zodiac.index(asc['sign']) + 9) % 12) - 1]
    
    stones = [Planet_Gemstone_Desc[asc['zodiac_lord']],Planet_Gemstone_Desc[fiveHouseLord],Planet_Gemstone_Desc[ninthHouseLord]]

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
        'Life Stone :',
        'Benefictical Stone :',
        'Lucky Stone :'
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
        f"{luckyNumber[0]},{luckyNumber[1]}",
        f"{stones[0]['Gemstone']}",
        f"{stones[1]['Gemstone']}",
        f"{stones[2]['Gemstone']}"
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
    
    pdf.cell(0,0,"Impacts on Personality",align='C')
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
    
    pdf.AddPage(path)
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
    pdf.multi_cell(pdf.w - 45, 8 , "Activating the Panchangam elements (Thithi, Vaaram, Nakshatra, Yogam, Karanam) can potentially bring balance to child's life, fostering positive energies and promoting growth.", align='L')
    pdf.set_y(pdf.get_y() + 5)
    pdf.lineBreak(f"{name} was born on {formatted_date}, {panchang['week_day']} (Vaaram), under {panchang['nakshatra']} Nakshatra, {panchang['paksha']} Paksha {panchang['thithi']} Thithi, {panchang['karanam']} Karanam, and {panchang['yoga']} Yogam",path, "#BAF596")
    
    colors = ["#E5FFB5","#94FFD2","#B2E4FF","#D6C8FF","#FFDECA"]    
    titles = [f"Tithi Represents {name}'s Emotions, Mental Well-being",f"Vaaram Represents {name}'s Energy & Behaviour",f"Nakshatra Represents {name}'s Personality and Life Path",f"Yogam Represents {name}'s Prosperity and Life Transformation",f"Karanam Represents {name}'s Work and Actions"]
    
    titleImage = ['waningMoon.png' if panchang['thithi_number'] <= 15 else 'waxingMoon.png','week.png','nakshatra.png','yogam.png','karanam.png']
    
    panchangContent = [
        "",
        "",
        "Magizh, born under the Bharani Nakshatra, possesses a dynamic and determined personality. He is known for his strong willpower, ambitious nature, and unwavering focus on achieving his goals. Magizh is often seen as a natural leader, with a charismatic presence that draws others towards him. His life path is marked by transformation and growth, as he navigates challenges with resilience and adaptability. Overall, Magizh's Bharani Nakshatra characteristics make him a force to be reckoned with, capable of achieving great success and making a lasting impact in the world.",
        "Magizh, born under the Shiva Yogam, possesses a deep connection to spirituality and a strong sense of inner peace and tranquility. His goals revolve around achieving spiritual growth, enlightenment, and self-realization. With a profound understanding of the interconnectedness of all things, Magizh strives to spread positivity and uplift others around him, leaving a lasting impact of harmony and balance wherever he goes.",
        ""
    ]
    
    pdf.set_text_color(0,0,0)
    pdf.set_y(pdf.get_y() + 5)
    for i in range(0,5):
        if pdf.get_y() + 50 >= 260:
            pdf.AddPage(path)
            pdf.set_y(30)
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
                
            if pdf.get_y() + 20 > 270:
                pdf.AddPage(path)
                pdf.set_y(20)
            pdf.set_xy(30,pdf.get_y() + 10)
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
            pdf.set_font("Times", '', 14)
            roundedBox(pdf,random.choice(DesignColors),40,pdf.get_y() + 5,pdf.w - 80,10)
            pdf.set_xy(30,pdf.get_y() + 5)
            pdf.cell(pdf.w - 60,10,f"Rulling Planet: **{weekPlanet[panchang['week_day']]}**",align='C',new_y=YPos.NEXT,markdown=True)
            
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
            # con = panchangPrompt(panchang,i,name,gender)
            con = panchangContent[i]
            pdf.ContentDesign(random.choice(DesignColors),titles[i],con,path,name)   
            
    sifted = zodiac[zodiac.index(asc['sign']):] + zodiac[:zodiac.index(asc['sign'])]
    pdf.AddPage(path,"Potential Health Challenges and Holistic Wellness Solutions")
    sixth_house = sifted[5]
    con = healthContent[sixth_house]
    insights = healthInsights[sixth_house].replace("child",name)
    pdf.set_y(pdf.get_y() + 5)
    pdf.set_font('Karma-Regular', '', 14)
    pdf.set_text_color(0,0,0) 
    pdf.roundedContent(insights,random.choice(DesignColors))
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
    pdf.cell(col_width - 5,8, f"Common Health Issues",align='C')
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
    pdf.cell(col_width - 5,8, f"Dosha Constitution Issues",align='C')
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
        roundedBox(pdf,colors[i], pdf.w / 2 - 50, pdf.get_y(), 100, 10, corner=20)
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

                
    # content2 = physical(planets,2,name,gender)
    # content3 = physical(planets,3,name,gender)
    # content4 = physical(planets,4,name,gender)

    content2 = {'physical_attributes': 'Magizh has a balanced body built with a charming face type. His eyes are expressive and hold a sense of harmony. His physical appearance exudes grace and elegance, while his aura is charismatic and magnetic, drawing others towards him.', 'personality': ['Magizh possesses a charming and diplomatic personality, which helps him navigate social situations with ease.', 'He has a strong sense of justice and fairness, making him a reliable and trustworthy individual.', 'Magizh is creative and artistic, with an eye for beauty and design.'], 'character': ['Magizh is cooperative and seeks harmony in all his interactions, making him a peacemaker in his social circles.', 'He is sociable and enjoys connecting with others, forming meaningful relationships.', 'Magizh is adaptable and can easily adjust to new environments and circumstances.'], 'positive_behavior': ['Magizh exhibits a sense of balance and equilibrium in his actions, making thoughtful decisions.', 'He values relationships and shows empathy towards others, creating a supportive environment.', 'Magizh is diplomatic in his communication, resolving conflicts peacefully and effectively.'], 'negative_behavior': ['Magizh may struggle with indecisiveness, finding it challenging to make firm choices.', 'He might have a tendency to avoid confrontation and suppress his true emotions.', 'Magizh could be overly focused on maintaining external harmony, neglecting his own needs and desires.'], 'parenting_tips': 'To help Magizh overcome his negative behaviors and support his growth, encourage him to express his opinions and feelings openly. Teach him the importance of setting boundaries and asserting himself when necessary. Provide opportunities for Magizh to practice decision-making and assertiveness skills, guiding him to prioritize his own well-being while maintaining harmonious relationships with others. Foster a supportive and nurturing environment that values both his diplomatic nature and his individual needs. Encourage Magizh to seek counseling or therapy if needed to address any underlying issues causing his avoidance of conflict and emotional suppression. Remember to praise and reinforce his efforts towards personal growth and self-expression.'}

    content3 = {'emotional_state': 'Magizh, with the Moon positioned in the 7th house of Aries in Bharani nakshatra along with Planets Moon and Jupiter, tends to have a strong sense of independence and a need for personal space. Magizh believes in taking action and being assertive in order to achieve their goals. Emotionally, Magizh is passionate, determined, and sometimes impatient.', 'emotions': ['Passionate and enthusiastic in pursuing their desires', "Can become easily frustrated when things don't go as planned", 'Has a fiery and competitive spirit when faced with challenges'], 'feelings': ['Feels a strong sense of individuality and self-reliance', 'Experiences a drive to constantly seek new experiences and adventures', 'May feel restless or impulsive when restricted or confined'], 'reactions': ['Responds quickly to situations with courage and boldness', 'May become defensive when their independence is questioned', 'Takes the lead and initiates action in group settings'], 'negative_imbalance': ['Tendency towards impulsiveness leading to rash decision-making', "Difficulty in compromising and considering others' perspectives", 'Struggles with anger issues and maintaining harmony in relationships'], 'parenting_tips': "To support Magizh in managing their negative emotional imbalances and foster growth, it is important to encourage self-reflection and mindfulness. Parents can help Magizh by teaching them the importance of taking a pause before reacting impulsively. Encourage open communication and active listening to understand others' viewpoints. Provide outlets for physical activities to channel the excess energy positively. Set boundaries and teach conflict resolution skills to promote healthy relationships. Practice gratitude and positivity to cultivate emotional balance."}

    content4 = {'core_insights': "Magizh, with the Sun positioned in the 3rd house of Sagittarius in Mula nakshatra, is driven by a deep desire for knowledge and intellectual pursuits. His core identity is centered around exploration, seeking truth and meaning, and expressing his beliefs with conviction. His inner strength lies in his optimism, curiosity, and adaptability, which enable him to navigate various challenges with a sense of adventure and purpose. However, Magizh's ego can sometimes be overly proud and self-righteous, leading to conflicts in relationships and a tendency to impose his views on others.", 'recognitions': ['Magizh seeks recognition for his intellectual achievements and philosophical insights.', 'He also craves acknowledgment for his ability to communicate persuasively and inspire others.', 'Magizh desires recognition for his adventurous spirit and willingness to explore new ideas and cultures.'], 'core_identity': ["Magizh's core identity is shaped by his quest for truth and wisdom.", 'His belief in the power of knowledge and education drives his actions and interactions with others.', "Magizh's identity is rooted in his philosophical nature, love for learning, and his ability to inspire those around him."], 'parenting_tips': 'Encourage Magizh to practice humility and empathy in his interactions with others. Teach him to listen actively, consider different perspectives, and appreciate the diversity of opinions and experiences. Guide Magizh to engage in meaningful conversations that foster understanding and mutual respect. By nurturing these qualities, Magizh can develop a more balanced sense of self and build stronger connections with those around him.'}
    
    content = [content2,content3,content4]
    titles = [{
        'physical_attributes': "Physical Attributes",
        'personality': "Outer Personality", 
        'character': "Character",
        'positive_behavior': "Positive Behavior",
        'negative_behavior': "Behavior Challenges",
        'parenting_tips' : f"Parenting Tips For {name}'s Behaviour Challenges" 
        }, {
            'emotional_state' : f"{name}'s Emotional State Insights", 
            'emotions': f"{name}'s Emotions",
            'feelings' : f"{name}'s Feelings",
            'reactions' : f"{name}'s Reactions",
            'negative_imbalance' : f"{name}'s Emotional Imbalance Challenges",
            'parenting_tips' : f"Parenting Tips"
        },{
            'core_insights' : f"{name}'s Soul Desire",
            'recognitions' : f"Seek For Recognition", 
            'core_identity': "Core Identity", 
            'ego': f"{name}'s Soul Ego", 
            'negative_ego': f"{name}'s Ego Challenges", 
            'parenting_tips': f"Parenting Tips For Self Identity Challenges"
         }]

    pdf.AddPage(path,"Outer World - Physical Attributes, Personality, and Behavior")
    pdf.set_text_color(0,0,0)
        
    for index,c in enumerate(content):
        if index == 1:
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
                
            pdf.set_y(pdf.get_y())
            pdf.image(f"{path}/icons/pg 33_personalized.png",pdf.w / 2 - 10,pdf.get_y(),20,20)
            pdf.set_y(pdf.get_y() + 25)
            pdf.set_font('Karma-Semi' , '' , 18)
            pdf.cell(0,0,"Parenting Tip for Academic Excellence:", align='C')
            pdf.set_font_size(15)
            pdf.set_y(pdf.get_y() + 10) 
            pdf.cell(0,0, content[3],align='C')
            pdf.set_y(pdf.get_y() + 5)
            
            if pdf.get_y() + 40 >= 260:  
                pdf.AddPage(path)
                pdf.set_y(30)
            
        pdf.ContentDesign(random.choice(DesignColors),educationTitle[k],v,path,name)
            
    pdf.AddPage(path,"Family and Relationships")
    # con = physical(planets,5,name,gender)
    con = {'family_relationship': "Based on Magizh's astrology details, it can be inferred that Magizh's social development, friendship dynamics, peer interactions, and family relationships are influenced by the placements of planets in the 7th House (Aries), 11th House (Leo), Sun (Sagittarius), Moon (Aries), and Venus (Libra). Magizh's family relationships are characterized by strong bonds with parents and siblings, with a focus on nurturing and supportive interactions. In terms of social development, Magizh tends to form friendships based on mutual respect and shared interests, seeking harmony and balance in relationships.", 'approaches': [{'title': 'Building Relationships with Father (Sun in Sagittarius)', 'content': 'Magizh can bond with the father by engaging in intellectual discussions, exploring new ideas and beliefs together, and participating in activities that promote personal growth and expansion of knowledge.'}, {'title': 'Bonding with Mother (Moon in Aries)', 'content': 'Magizh can connect with the mother through emotional expression, support in times of need, and engaging in physical activities together to foster a sense of closeness and security.'}, {'title': 'Strengthening Sibling Relationships', 'content': 'Magizh can enhance sibling relationships by fostering open communication, being supportive and understanding, and engaging in collaborative activities that promote mutual growth and bonding.'}, {'title': 'Developing Friendships', 'content': 'Magizh can build friendships by being a good listener, showing empathy and understanding, and participating in social activities that align with shared values and interests.'}], 'parenting_support': [{'title': 'Encouraging Open Communication', 'content': 'Parents can encourage Magizh to express thoughts and feelings openly, create a safe space for dialogue, and actively listen to his concerns and experiences to strengthen the parent-child relationship.'}, {'title': 'Promoting Independence', 'content': 'Parents can support Magizh in developing independence, decision-making skills, and autonomy by allowing him to take on responsibilities and make choices within a safe and supportive environment.'}, {'title': 'Cultivating Emotional Intelligence', 'content': "Parents can help Magizh develop emotional intelligence by teaching him to identify and manage his emotions, understand others' perspectives, and communicate effectively in various social settings."}]}
    
    familyTitle = {
        'family_relationship' : "",
        'approaches': f"{name}'s Approaches for Forming Relationships",
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
    pdf.set_y(pdf.get_y() + 5)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Karma-Regular', '', 14)
    eigth_house = sifted[7]
    con = subContent[eigth_house]
    pdf.lineBreak(con[0].replace('child',name).replace('Child',name),path,random.choice(DesignColors))
    
    pdf.set_y(pdf.get_y() + 5)
        
    pdf.ContentDesign(random.choice(DesignColors),f"{name}'s Hidden Challenges",con[1],path,name)
    
    content = con[2]['manifestation']
    pdf.AddPage(path)
    pdf.set_y(pdf.get_y() + 10)
    if eigth_house == "Scorpio":
        pdf.set_y(pdf.get_y() - 5)
    color = random.choice(DesignColors)
    roundedBox(pdf,color,20, pdf.get_y(), pdf.w - 40, 90)
    pdf.image(f"{path}/babyImages/mani.png",22.5,pdf.get_y() + 2.5,20,20)
    pdf.set_font('Karma-Semi', '', 18)
    pdf.set_y(pdf.get_y() + 2.5)
    pdf.cell(0,10,"Manifestation Remedy",align='C')
    pdf.set_font_size(13)
    pdf.set_xy(30, pdf.get_y() + 15)
    pdf.multi_cell(pdf.w - 60, 8,content[0],align='C')
    pdf.set_font('Karma-Regular', '', 12)
    pdf.set_xy(40, pdf.get_y())
    pdf.multi_cell(pdf.w - 80, 8, f"{content[1]}",align='C')
    pdf.set_xy(22.5, pdf.get_y())
    pdf.set_font('Karma-Heavy', '' , 16) 
    pdf.cell(0,10,"How To Do It:", align='L')
    pdf.set_font('Karma-Regular', '' , 14)
    pdf.set_y(pdf.get_y() + 7.5)
    for i,n in enumerate(content[2]):
        n = n.replace("child",name).replace("Child",name)
        roundedBox(pdf, color, 20, pdf.get_y() + 2.5, pdf.w - 40, pdf.no_of_lines(f"{i + 1}) {n}",pdf.w - 60) * 8 + 16,status=False)
        pdf.set_xy(30, pdf.get_y() + 2.5)
        if eigth_house == "Scorpio":
            pdf.set_xy(30, pdf.get_y() - 2.5)
        pdf.multi_cell(pdf.w - 60, 8 , f"{i + 1}) {n}" , align='L')
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf,color,20,pdf.get_y(), pdf.w - 40, pdf.no_of_lines(f"Counts: {content[3]}",pdf.w - 45) * 8 + 10,status=False)
    pdf.set_xy(22.5, pdf.get_y())
    pdf.multi_cell(pdf.w - 45, 8 , f"**Counts:** {content[3]}",markdown=True)
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf,color,20,pdf.get_y(), pdf.w - 40, pdf.no_of_lines(f"Why it works: {content[4]}",pdf.w - 45) * 8 + 5)
    pdf.set_xy(22.5, pdf.get_y())
    pdf.multi_cell(pdf.w - 45, 8 , f"**Why it works:** {content[4]}",markdown=True)
            
    content = con[2]['quantum']
    pdf.set_y(pdf.get_y() + 10)
    color = random.choice(DesignColors)
    roundedBox(pdf,color,20, pdf.get_y(), pdf.w - 40, 90)
    pdf.image(f"{path}/babyImages/atom.png",22.5,pdf.get_y() + 2.5,20,20)
    pdf.set_font('Karma-Semi', '', 18)
    pdf.set_y(pdf.get_y() + 2.5)
    pdf.cell(0,10,"Quantum Physics Concept Remedy",align='C')
    pdf.set_font_size(13)
    pdf.set_xy(30, pdf.get_y() + 15)
    pdf.multi_cell(pdf.w - 60, 8,content[0],align='C')
    pdf.set_font('Karma-Regular', '', 12)
    pdf.set_xy(40, pdf.get_y())
    pdf.multi_cell(pdf.w - 80, 8, f"{content[1]}",align='C')
    pdf.set_xy(22.5, pdf.get_y())
    pdf.set_font('Karma-Heavy', '' , 16) 
    pdf.cell(0,10,"How To Do It:", align='L')
    pdf.set_font('Karma-Regular', '' , 14)
    pdf.set_y(pdf.get_y() + 7.5)
    for i,n in enumerate(content[2]):
        n = n.replace("child",name).replace("Child",name)
        roundedBox(pdf, color, 20, pdf.get_y() + 2.5, pdf.w - 40, pdf.no_of_lines(f"{i + 1}) {n}",pdf.w - 60) * 8 + 16,status=False)
        pdf.set_xy(30, pdf.get_y() + 2.5)
        if eigth_house == "Scorpio":
            pdf.set_xy(30, pdf.get_y() - 2.5)
        pdf.multi_cell(pdf.w - 60, 8 , f"{i + 1}) {n}" , align='L')
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf,color,20,pdf.get_y(), pdf.w - 40, pdf.no_of_lines(f"Counts: {content[3]}",pdf.w - 45) * 8 + 10,status=False)
    pdf.set_xy(22.5, pdf.get_y())
    pdf.multi_cell(pdf.w - 45, 8 , f"**Counts:** {content[3]}",markdown=True)
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf,color,20,pdf.get_y(), pdf.w - 40, pdf.no_of_lines(f"Why it works: {content[4]}",pdf.w - 45) * 8 + 5)
    pdf.set_xy(22.5, pdf.get_y())
    pdf.multi_cell(pdf.w - 45, 8 , f"**Why it works:** {content[4]}",markdown=True)
    
    content = con[2]['healing']
    pdf.AddPage(path)
    pdf.set_y(pdf.get_y() + 10)
    if eigth_house == "Scorpio" or eigth_house == "Cancer":
        pdf.set_y(pdf.get_y() - 5)
    color = random.choice(DesignColors)
    roundedBox(pdf,color,20, pdf.get_y(), pdf.w - 40, 90)
    pdf.image(f"{path}/babyImages/heart.png",22.5,pdf.get_y() + 2.5,20,20)
    pdf.set_font('Karma-Semi', '', 18)
    pdf.set_y(pdf.get_y() + 2.5)
    pdf.cell(0,10,"Healing Remedy",align='C')
    pdf.set_font_size(13)
    pdf.set_xy(30, pdf.get_y() + 15)
    pdf.multi_cell(pdf.w - 60, 8,content[0],align='C')
    pdf.set_font('Karma-Regular', '', 12)
    pdf.set_xy(40, pdf.get_y())
    pdf.multi_cell(pdf.w - 80, 8, f"{content[1]}",align='C')
    pdf.set_xy(22.5, pdf.get_y())
    pdf.set_font('Karma-Heavy', '' , 16) 
    pdf.cell(0,10,"How To Do It:", align='L')
    pdf.set_font('Karma-Regular', '' , 14)
    if eigth_house == "Scorpio":
        pdf.set_font_size(13)
    pdf.set_y(pdf.get_y() + 7.5)
    for i,n in enumerate(content[2]):
        n = n.replace("child",name).replace("Child",name)
        roundedBox(pdf, color, 20, pdf.get_y() + 2.5, pdf.w - 40, pdf.no_of_lines(f"{i + 1}) {n}",pdf.w - 60) * 8 + 16,status=False)
        pdf.set_xy(30, pdf.get_y() + 2.5)
        if eigth_house == "Scorpio":
            pdf.set_xy(30, pdf.get_y() - 2.5)
        pdf.multi_cell(pdf.w - 60, 8 , f"{i + 1}) {n}" , align='L')
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf,color,20,pdf.get_y(), pdf.w - 40, pdf.no_of_lines(f"Counts: {content[3]}",pdf.w - 45) * 8 + 10,status=False)
    pdf.set_xy(22.5, pdf.get_y())
    pdf.multi_cell(pdf.w - 45, 8 , f"**Counts:** {content[3]}",markdown=True)
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf,color,20,pdf.get_y(), pdf.w - 40, pdf.no_of_lines(f"Why it works: {content[4]}",pdf.w - 45) * 8 + 5)
    pdf.set_xy(22.5, pdf.get_y())
    pdf.multi_cell(pdf.w - 45, 8 , f"**Why it works:** {content[4]}",markdown=True)
            
    content = con[2]['mudra']
    pdf.set_y(pdf.get_y() + 10)
    color = random.choice(DesignColors)
    roundedBox(pdf,color,20, pdf.get_y(), pdf.w - 40, 90)
    pdf.image(f"{path}/babyImages/mudra.png",22.5,pdf.get_y() + 2.5,20,20)
    pdf.set_font('Karma-Semi', '', 18)
    pdf.set_y(pdf.get_y() + 2.5)
    pdf.cell(0,10,"Mudra Remedy",align='C')
    pdf.set_font_size(13)
    pdf.set_xy(30, pdf.get_y() + 15)
    pdf.multi_cell(pdf.w - 60, 8,content[0],align='C')
    pdf.set_font('Karma-Regular', '', 12)
    pdf.set_xy(40, pdf.get_y())
    pdf.multi_cell(pdf.w - 80, 8, f"{content[1]}",align='C')
    pdf.set_xy(22.5, pdf.get_y())
    pdf.set_font('Karma-Heavy', '' , 16) 
    pdf.cell(0,10,"How To Do It:", align='L')
    pdf.set_font('Karma-Regular', '' , 14)
    if eigth_house == "Scorpio":
        pdf.set_font_size(13)
    pdf.set_y(pdf.get_y() + 7.5)
    for i,n in enumerate(content[2]):
        n = n.replace("child",name).replace("Child",name)
        roundedBox(pdf, color, 20, pdf.get_y() + 2.5, pdf.w - 40, pdf.no_of_lines(f"{i + 1}) {n}",pdf.w - 60) * 8 + 16,status=False)
        pdf.set_xy(30, pdf.get_y() + 2.5)
        if eigth_house == "Scorpio" or eigth_house == "Cancer":
            pdf.set_xy(30, pdf.get_y() - 2.5)
        pdf.multi_cell(pdf.w - 60, 8 , f"{i + 1}) {n}" , align='L')
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf,color,20,pdf.get_y(), pdf.w - 40, pdf.no_of_lines(f"Counts: {content[3]}",pdf.w - 45) * 8 + 10,status=False)
    pdf.set_xy(22.5, pdf.get_y())
    pdf.multi_cell(pdf.w - 45, 8 , f"**Counts:** {content[3]}",markdown=True)
    pdf.set_font('Times', '' , 14)
    roundedBox(pdf,color,20,pdf.get_y(), pdf.w - 40, pdf.no_of_lines(f"Why it works: {content[4]}",pdf.w - 45) * 8 + 5)
    pdf.set_xy(22.5, pdf.get_y())
    pdf.multi_cell(pdf.w - 45, 8 , f"**Why it works:** {content[4]}",markdown=True)
        
    pdf.AddPage(path,"Unique Talents and Natural Skills")
    
    uniqueTitle = {
        'insights': "", 
        'education' : "Unique Talents in Academics", 
        'arts_creative' :"Unique Talents in Arts & Creativity",
        'physical_activity': "Unique Talents in Physical Activity"
    }
    # con = chapterPrompt(planets,0,name,gender)
    
    con = {'education': [{'title': 'Analytical Skills', 'content': 'Magizh has a natural talent for analyzing information and making logical connections. With Mercury positioned in the 3rd house of Sagittarius, in Mula nakshatra, he is likely to have a deep curiosity and a thirst for knowledge. Encourage him to explore various subjects and engage in intellectual pursuits to enhance his analytical abilities.'}, {'title': 'Communication Skills', 'content': 'Due to Mercury in the 3rd house of Sagittarius, Magizh possesses excellent communication skills. He is likely to be articulate, expressive, and persuasive in his speech. Foster his communication skills by encouraging him to participate in debates, public speaking, or writing activities.'}, {'title': 'Adventurous Learning', 'content': 'With Mercury in Sagittarius in Mula nakshatra, Magizh excels in adventurous learning experiences. He may thrive in environments that offer hands-on learning, travel opportunities, and exposure to diverse cultures. Encourage him to pursue academic interests that challenge his intellect and broaden his horizons.'}], 'arts_creative': [{'title': 'Visual Arts', 'content': 'Magizh has a natural talent for visual arts, thanks to Venus positioned in the 1st house of Libra in Vishakha nakshatra. He may excel in painting, drawing, or graphic design. Provide him with opportunities to explore and develop his artistic skills through classes, workshops, or creative projects.'}, {'title': 'Harmonious Expression', 'content': 'With Venus in the 1st house of Libra, Magizh possesses a talent for harmonious expression in his artistic endeavors. He may have a keen sense of aesthetics and a knack for creating beauty. Encourage him to express himself through art, music, or design to tap into his creative potential.'}, {'title': 'Emotional Sensitivity', 'content': 'Venus in Libra in Vishakha nakshatra endows Magizh with emotional sensitivity and empathy. He may excel in artistic fields that require emotional depth and understanding. Nurture his emotional intelligence by encouraging him to explore poetry, music, or theatre to enhance his creative abilities.'}], 'physical_activity': [{'title': 'Endurance and Stamina', 'content': 'Magizh possesses strong physical abilities, particularly in endurance and stamina, with Mars in the 2nd house of Scorpio in Jyeshtha nakshatra. He may excel in activities that require physical strength and perseverance. Support his interest in sports, martial arts, or other physical pursuits to enhance his physical abilities.'}, {'title': 'Competitive Spirit', 'content': 'With Mars in Scorpio in Jyeshtha nakshatra, Magizh has a competitive spirit and enjoys challenges. He may thrive in competitive sports or activities that push his limits. Encourage him to engage in healthy competition to channel his energy effectively and achieve personal growth.'}, {'title': 'Leadership Skills', 'content': 'Mars in Scorpio in Jyeshtha nakshatra indicates that Magizh has strong leadership qualities. He may naturally take charge in group activities and inspire others to follow his lead. Foster his leadership skills by providing opportunities for him to take on roles of responsibility and lead by example.'}]}
    
    for index,(k, v) in enumerate(con.items()):
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
        
        pdf.ContentDesign(random.choice(DesignColors),uniqueTitle[k],v,path,name)
        
        
    pdf.AddPage(path,"Karmic Life Lessons")        
    # con = chapterPrompt(planets,7,name,gender)
    
    con = {'child_responsibility_discipline': "Magizh's karmic life lesson based on Saturn in the Fifth house of Aquarius sign emphasizes the importance of taking responsibility and embracing discipline in all aspects of life. Magizh should avoid being too laid-back or reckless, as Saturn urges him to learn the value of structure and commitment. By cultivating a sense of duty and maturity, Magizh can overcome challenges related to authority and self-discipline.", 'child_desire_ambition': "Magizh's karmic life lesson based on Rahu in the Sixth house of Pisces sign highlights the need to balance and control desires and ambitions. He should avoid indulging in excessive desires or taking shortcuts in pursuit of his ambitions. Rahu's placement suggests that Magizh's purpose in life lies in overcoming illusions and developing a deeper spiritual connection. By staying grounded and focusing on inner growth, Magizh can fulfill his true potential.", 'child_spiritual_wisdom': "Magizh's karmic life lesson based on Ketu in the 12th house of Virgo sign signifies a journey towards spiritual wisdom and detachment. He should avoid getting too attached to material possessions and worldly pursuits, as Ketu encourages letting go of attachments and embracing spiritual insights. Magizh's destiny is aligned with seeking solitude, introspection, and unraveling the mysteries of life. By detaching from material desires and seeking spiritual knowledge, Magizh can fulfill his spiritual destiny."}

    
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
    dasaOut = [{'dasa': 'Venus', 'bhukthi': 'Mars', 'age': "At Magizh's age, Between 1 to 2", 'prediction': {'insights': "During Magizh's Venus Dasa and Mars Bhukti period, the focus will be on relationships and transformation. With Venus in the 1st house of Libra in Vishakha nakshatra and Mars in the 2nd house of Scorpio in Jyeshtha nakshatra, there may be challenges related to self-worth and communication, but also opportunities for growth and assertiveness. Magizh's Moon sign Aries adds a fiery and dynamic energy to the mix, guiding him towards leadership and independence.", 'favourable': ['1. Success in professional endeavors: Magizh will excel in his career and receive recognition for his hard work and dedication, leading to new opportunities for growth and advancement.', '2. Strengthened relationships: Magizh will experience deeper connections with loved ones, fostering a sense of support and unity in his personal life.', '3. Enhanced creativity and self-expression: Magizh will find inspiration and creative outlets to express himself, leading to personal satisfaction and fulfillment.'], 'unfavourable': ['1. Communication challenges: Magizh may face misunderstandings or conflicts in his interactions with others, requiring patience and understanding to overcome obstacles.', '2. Financial strain: Magizh may encounter financial setbacks or unexpected expenses, requiring careful budgeting and financial planning to manage resources effectively.', '3. Health concerns: Magizh may experience health issues or fatigue during this period, necessitating self-care and prioritization of well-being.'], 'parenting_tips': 'Strategic Support and Communication Building - Encourage Magizh to express his feelings and thoughts openly, and actively listen to his concerns to foster trust and understanding. Implement regular family meetings to discuss challenges and solutions together, creating a supportive and connected environment. Additionally, practice stress-relief activities like mindfulness or yoga with Magizh to promote emotional balance and resilience during difficult times.'}}, {'dasa': 'Venus', 'bhukthi': 'Rahu', 'age': "At Magizh's age, Between 2 to 5", 'prediction': {'insights': 'Magizh, during the Venus Dasa and Rahu Bhukti period, is likely to experience a mix of positive and challenging situations. Venus in the 1st house of Libra in Vishakha nakshatra indicates a focus on relationships and harmony, while Rahu in the 6th house of Pisces in Revati nakshatra suggests unexpected changes and challenges ahead. With Moon sign Aries, there may be a strong sense of individuality and drive for success.', 'favourable': ['During this period, Magizh may experience increased creativity and artistic talents, leading to recognition and success in creative pursuits.', 'There is a possibility of positive developments in personal relationships, leading to stronger bonds with loved ones and a sense of emotional fulfillment.', 'Magizh may have opportunities for personal growth and self-improvement, leading to a greater sense of confidence and inner peace.'], 'unfavourable': ['Magizh may face challenges in maintaining balance in relationships, leading to conflicts and misunderstandings with others.', 'There may be difficulties in handling financial matters and investments, requiring cautious decision-making to avoid losses.', 'Health issues or unexpected obstacles in career and personal life may arise, causing stress and instability.'], 'parenting_tips': 'To navigate Magizh\'s Dasa and Bhukti period\'s unfavorable results, implement the "Emotional Regulation Technique". Guide Magizh to identify and regulate their emotions effectively by practicing mindfulness and deep breathing exercises. Encourage open communication and provide a safe space to express feelings. Teach problem-solving skills to help Magizh face challenges confidently and seek support when needed. Foster a supportive and understanding environment to navigate through tough times with resilience and emotional strength.'}}, {'dasa': 'Venus', 'bhukthi': 'Jupiter', 'age': "At Magizh's age, Between 5 to 8", 'prediction': {'insights': "During Magizh's Venus Dasa and Jupiter Bhukti period, there may be significant changes in relationships and partnerships due to the influence of Venus in the 1st house of Libra and Jupiter in the 7th house of Aries. Magizh's strong willpower and adventurous spirit, as indicated by the Moon in Aries, will play a key role in shaping these predictions.", 'favourable': ['Magizh is likely to experience a boost in creativity and artistic pursuits, leading to recognition and success in his endeavors.', "Improved communication skills and networking opportunities may enhance Magizh's social connections and bring about new opportunities for growth and expansion in his career.", 'The positive influence of Jupiter in the 7th house may bring about a harmonious and supportive relationship with his partner, fostering mutual understanding and deepening emotional bonds.'], 'unfavourable': ['Magizh may face challenges in maintaining a work-life balance, leading to stress and exhaustion in his daily routine.', 'There could be misunderstandings or conflicts in close relationships, requiring patience and effective communication to resolve differences.', 'Financial setbacks or unexpected expenses may arise, prompting Magizh to reevaluate his financial management and budgeting strategies.'], 'parenting_tips': "To navigate Magizh's Dasa Bhukti unfavourable results, the 'Emotional Regulation Technique' can be effective. Encourage Magizh to express his emotions through journaling or art, practice mindfulness techniques to manage stress, and engage in physical activities to release pent-up energy. Provide a safe space for Magizh to share his feelings and thoughts openly, and offer guidance on problem-solving and conflict resolution skills. Encouraging healthy outlets for emotional expression and promoting self-care practices will empower Magizh to navigate through challenging times with resilience and positivity."}}]
    
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
            
            pdf.ContentDesign(random.choice(DesignColors),setTitle(k),v,path,name)
    
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
        if planet['Name'] == "Ketu":
            pdf.set_y(pdf.get_y() - 7.5)
        color = random.choice(DesignColors)
        roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40, 40)
        pdf.set_y(pdf.get_y() + 7.5)
        pdf.set_font('Karma-Semi', '' , 16) 
        pdf.cell(0,0,f"Teach Discipline : {content[1][0]}",align='C')
        pdf.set_xy(22.5,pdf.get_y() + 5)
        pdf.set_font('Karma-Regular', '', 14)
        
        smallTitle = {
            1 : f"{planet['Name']} Guide to {name}: ",
            2 : "",
            3 : f"Say to {name}: "
        }
        
        for i in range(1,len(content[1])):
            content[2][i] = content[2][i].replace("child",name).replace("Child",name)
            if i != len(content[1]) - 1:
                roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40, pdf.no_of_lines(f"{smallTitle[i]}{content[1][i]}",pdf.w - 45) * 7 + 7,status=False)
            else:
                roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40 , pdf.no_of_lines(f"{smallTitle[i]}{content[1][i]}",pdf.w - 45) * 7 + 7)
                roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40 , 5,status=False)
            content[1][i] = content[1][i].replace("child",name).replace("Child",name)
            pdf.multi_cell(pdf.w - 45,7,f"{smallTitle[i]}{content[1][i]}",align='L',new_y=YPos.NEXT, new_x=XPos.LEFT)
        pdf.set_y(pdf.get_y() + 15)
        if planet['Name'] == "Ketu":
            pdf.set_y(pdf.get_y() - 5)
        color = random.choice(DesignColors)
        roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40, 40)
        pdf.set_font('Karma-Semi', '' , 16) 
        pdf.set_y(pdf.get_y() + 7.5)
        pdf.cell(0,0,f"Teach Life Lesson : {content[2][0]}",align='C')
        pdf.set_xy(22.5,pdf.get_y() + 5)
        pdf.set_font('Karma-Regular', '', 14)
        
        for i in range(1,len(content[2])):
            content[2][i] = content[2][i].replace("child",name).replace("Child",name)
            if i != len(content[1]) - 1:
                roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40, pdf.no_of_lines(f"{smallTitle[i]}{content[2][i]}",pdf.w - 45) * 7 + 7,status=False)
            else:
                roundedBox(pdf,color ,20,pdf.get_y(),pdf.w-40 , pdf.no_of_lines(f"{smallTitle[i]}{content[2][i]}",pdf.w - 45) * 7 + 7)
                roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40 , 5,status=False)
            pdf.multi_cell(pdf.w - 45,7,f"{smallTitle[i]}{content[2][i]}",align='L',new_y=YPos.NEXT, new_x=XPos.LEFT)
        pdf.set_y(pdf.get_y() + 15)
        if planet['Name'] == "Ketu":
            pdf.set_y(pdf.get_y() - 5)
        color = random.choice(DesignColors)
        roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40, 40)
        pdf.set_font('Karma-Semi', '' , 16) 
        pdf.set_y(pdf.get_y() + 7.5)
        pdf.cell(0,0,f"Teach Food & Diet : {content[4][0]}",align='C')
        pdf.set_xy(22.5,pdf.get_y() + 5)
        pdf.set_font('Karma-Regular', '', 14)
        for i in range(1,len(content[4])):
            content[2][i] = content[2][i].replace("child",name).replace("Child",name)
            if i != len(content[1]) - 1:
                roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40, pdf.no_of_lines(f"{smallTitle[i]}{content[4][i]}",pdf.w - 45) * 7 + 7,status=False)
            else:
                roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40 , pdf.no_of_lines(f"{smallTitle[i]}{content[4][i]}",pdf.w - 45) * 7 + 7)
                roundedBox(pdf, color ,20,pdf.get_y(),pdf.w-40 , 5,status=False)
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
    content = nakshatraContent[moon['nakshatra']]
    
    x_start = 20
    y_start = pdf.get_y() + 5
    pdf.set_xy(x_start, y_start)
    pdf.set_text_color(0,0,0)

    table_data = [
        (f"Name", f"Fields", "Characteristics"),
        (f"{content[0]['name']}", f"{content[0]['famous']}",f"{content[0]['nakshatra']}"),
        (f"{content[1]['name']}", f"{content[1]['famous']}",f"{content[1]['nakshatra']}"),
        (f"{content[2]['name']}", f"{content[2]['famous']}",f"{content[2]['nakshatra']}"),
    ]
    
    for row in table_data:
        pdf.set_font('Karma-Regular', '', 14)
        pdf.cell(50, 10, row[0], new_x=XPos.RIGHT, new_y=YPos.TOP,border=1,align='C')
        pdf.set_font('Karma-Regular', '', 14)
        pdf.cell(50, 10, row[1], new_x=XPos.RIGHT, new_y=YPos.TOP,border=1,align='C')
        pdf.set_font('Karma-Regular', '', 14)
        pdf.multi_cell(50, 10, row[2],align='L',border=1)
        y_start = pdf.get_y()
        pdf.set_xy(x_start, y_start)    
    
    # content = chapterPrompt(planets,9,name,gender)
    content = {'overall': 'Magizh is a Libra ascendant with a strong influence of Venus in the 1st house, indicating a charming and diplomatic personality. The placement of Mars in the 2nd house of Scorpio suggests determination and strength in communication. The presence of Sun, Mercury, and Jupiter in the 3rd house of Sagittarius highlights intelligence and communication skills. Saturn in the 4th house of Capricorn signifies discipline and responsibility in the home environment. Aquarius in the 5th house with Saturn indicates a love for intellectual pursuits and a structured approach to creativity.', 'recommendations': 'To nurture Magizh, it is important to encourage their diplomatic skills and charm. Providing opportunities for effective communication and expression of ideas will further enhance their strengths. Encouraging disciplined and responsible behavior at home will help in fostering a sense of structure and security. Supporting their love for intellectual pursuits and creativity will also be beneficial for their overall development.', 'action': 'Action Plan: 1. Encourage diplomatic skills and charm through social interactions. 2. Foster effective communication and expression of ideas. 3. Establish a sense of discipline and responsibility at home. 4. Support intellectual pursuits and creativity.'}

    
    pdf.AddPage(path,f"Summary Insights for Parents and Child")
    
    summaryTitle = {
        "overall" : f"{name}'s Overall Astrology Summary",
        "strength" : f"{name}'s Strengths",
        "weakness": f"{name}'s Weakness",
        "recommendations" : "Recommendations for Parents",
        "action" : "Actions for Parents",
    }
    
    for k, v in content.items():
        if pdf.get_y() + 40 >= 260:  
            pdf.AddPage(path)
            pdf.set_y(30)
            pdf.set_text_color(0,0,0)
        
        pdf.ContentDesign(random.choice(DesignColors),summaryTitle[k],v,path,name)
    
    pdf.output(f'{path}/pdf/{name} - babyReport.pdf')
    
def babyReport(dob,location,lat,lon,path,gender,name):
    print("Generating Baby Report")
    planets = find_planets(dob,lat,lon)
    print("Planets Found")
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
        birthchart = generate_birth_navamsa_chart(planets,f'{path}/chart/',dob,location,name)
        # birthchart = {
        #     'birth_chart' : '1.png',
        #     'navamsa_chart' : '2.png'
        # }
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

babyReport("2023-12-23 03:03:00","Madurai, Tamil Nadu , India",9.939093, 78.121719,os.getcwd(),"male","Magizh Siranjeevi")