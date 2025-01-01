context = [
    "Child Astrology Details",
    "Birth Chart Analysis",
    "Child's Life Path (Favorable and Unfavorable Timings)",
    "Pancha Bhoota: Fire, Air, Water, Ether, Earth Compositions in the Child's Body",
    "Child's Ayurvedic Body Type (Vata, Pitta, Kapa)",
    "Dominant Chakra (Energy Center of the Child)",
    "Child's True Self (Sun, Moon, Ascendant/Lagna)",
    "Child's Panchangam Growth Drivers",
    "Potential Health Challenges and Holistic Wellness Solutions",
    "Outer World - Physical Attributes, Personality, and Behavior",
    "Inner World - Emotional Needs and Soul Desire",
    "Education and Intellect (Educational Preferences and Cognitive Ability)",
    "Family and Relationships",
    "Career and Professions (Including Business and Entrepreneurship Potential)",
    "Subconscious Mind Analysis",
    "Unique Talents and Natural Skills (Mars, Venus, Mercury Analysis)",
    "Karmic Life Lessons (Influences of Saturn, Rahu, and Ketu)",
    "Sade Sati Analysis",
    "Life Stones and Benefic/Lucky Stones",
    "Rudraksha Recommendations",
    "Atma Karga & Ishta Devata (Fortune Lord for the Child)",
    "Child Development Milestones",
    "Discipline, Habits, Diet, and Lifestyle Based on Planetary Energy",
    "Important Checklist for Parents",
    "Famous Celebrity Comparisons",
    "Summary Insights for Parents and Child"
]


chakras = {
    "Aries": ["Solar Plexus Chakra"],  
    "Taurus": ["Sacral Chakra"], 
    "Gemini": ["Throat Chakra"],  
    "Cancer": ["Heart Chakra"],  
    "Leo": ["Solar Plexus Chakra"], 
    "Virgo": ["Throat Chakra"], 
    "Libra": ["Heart Chakra"],  
    "Scorpio": ["Solar Plexus Chakra"],  
    "Sagittarius": ["Third Eye Chakra"], 
    "Capricorn": ["Root Chakra"], 
    "Aquarius": ["Root Chakra"], 
    "Pisces": ["Crown Chakra"], 
}

chakra_desc = {
    "Crown Chakra" : [
        "A dominant crown chakra (Sahasrara) in children supports a strong sense of connection to the world, higher consciousness, and spiritual awareness. Children with an active crown chakra are often open-minded, wise beyond their years, and feel a sense of inner peace.",
        "If imbalanced, they may appear disconnected, overly introspective, or lack direction.",
        {
            "title": "Quiet Reflection and Nature Time",
            "desc" : "Encourage activities that promote peace and spiritual connection, such as quiet time in nature, deep breathing exercises, or gentle meditation. Help them find moments of stillness to reflect or simply enjoy their surroundings. This supports the crown chakra, fostering a sense of balance and boosting their overall energy."
        }
    ],
    "Third Eye Chakra": [
        "A dominant third eye chakra (Ajna) in children supports intuition, imagination, and strong mental clarity. Children with an active third eye chakra are perceptive, creative, and insightful. They often have a vivid imagination and are naturally curious.",
        "If imbalanced, they may struggle with focus, have vivid dreams that cause fear, or become overly analytical.",
        {
            "title": "Mindfulness and Visualization Activities",
            "desc": "Encourage activities that promote inner focus and imagination, such as guided meditation, quiet time with books, or visualizing positive outcomes. Foster opportunities for them to express their thoughts and ask questions. This nurtures the third eye chakra, enhancing their intuition and boosting their energy."
        }
    ],
    "Throat Chakra": [
        "A dominant throat chakra (Vishuddha) in children supports clear communication, self-expression, and confidence in speaking. Children with a strong throat chakra are articulate, expressive, and able to share their thoughts and feelings easily.",
        "If imbalanced, they may struggle with expressing themselves, become shy, or overtalk and dominate conversations.",
        {
            "title": "Expressive Activities",
            "desc": "Encourage activities that promote verbal expression, such as storytelling, singing, or playing musical instruments. Create a safe space where your child feels comfortable sharing their thoughts and feelings. This supports the throat chakra, enhancing their confidence and energy."
        }
    ],
    "Heart Chakra": [
        "A dominant heart chakra (Anahata) in children promotes love, compassion, and a strong sense of connection with others. Children with a balanced heart chakra are empathetic, caring, and able to build healthy relationships.",
        "If imbalanced, they may become overly sensitive, clingy, or struggle with self-love and setting boundaries.",
        {
            "title": "Acts of Kindness and Connection",
            "desc": "Encourage activities that foster compassion and emotional bonding, such as helping others, sharing, and spending quality time together. Engage in activities like group games or family rituals that emphasize love and connection. This nurtures the heart chakra, boosting their emotional energy and strengthening their aura."
        }
    ],
    "Sacral Chakra": [
        "A dominant sacral chakra (Swadhisthana) in children nurtures creativity, emotional expression, and healthy social interactions. Children with a strong sacral chakra are imaginative, enthusiastic, and able to form meaningful connections.",
        "If imbalanced, they may become overly emotional, overly dependent, or struggle with self-expression.",
        {
            "title": "Creative and Playful Activities",
            "desc": "Encourage activities that foster creativity and emotional expression, such as drawing, dancing, or playing with water. Provide opportunities for free play and social interactions with peers to help them connect with their emotions and build confidence. This supports the sacral chakra, enhancing their energy and vitality."
        }
    ],
    "Solar Plexus Chakra": [
        "A dominant solar plexus chakra (Manipura) in children promotes confidence, willpower, and a strong sense of self. It drives their passions and motivates them to take initiative and pursue their goals.",
        "However, when imbalanced, children may become overly competitive, controlling, or easily frustrated.",
        {
            "title": "Confidence-Building Activities",
            "desc": "Encourage your child to take on activities that promote independence and self-expression, such as sports, arts, or leadership roles in group activities. Provide praise and support to reinforce their sense of achievement and self-worth. This helps balance their solar plexus chakra, boosting their energy and strengthening their aura."
        }
    ],
    "Root Chakra": [
        "A dominant root chakra (Muladhara) in children provides a sense of security, stability, and grounding. Children with a strong root chakra feel safe, confident, and connected to their surroundings.",
        "If imbalanced, they may feel anxious, fearful, or struggle with trust and comfort in new situations.",
        {
            "title": "Grounding Activities",
            "desc": "Incorporate activities that promote stability and connection, such as outdoor play, nature walks, or simple exercises like standing on one leg. Create a consistent daily routine to help your child feel secure and supported. This strengthens their root chakra, enhancing their sense of safety and energy."
        }
    ]
}

dasa_status_table = {
    "Sun": 
        [["Sun", "Moon", "Jupiter", "Mars"], ["Rahu", "Ketu", "Saturn"]],
    "Moon": [
        ["Sun", "Moon", "Jupiter", "Mars"], ["Rahu", "Ketu", "Saturn"]],
    "Mars": 
        [["Sun", "Moon", "Jupiter"], ["Rahu", "Ketu", "Saturn"]],
    "Mercury": 
        [["Venus", "Sun"], ["Rahu", "Ketu"]],
    "Jupiter": 
        [["Sun", "Moon", "Jupiter", "Mars"], ["Rahu", "Ketu", "Saturn"]],
    "Venus": 
        [["Venus", "Mercury", "Moon"], []],
    "Saturn": 
        [["Mercury"], ["Sun", "Rahu", "Ketu", "Saturn"]],
    "Rahu": 
        [["Venus", "Jupiter"], ["Rahu", "Ketu", "Saturn", "Sun", "Moon"]],
    "Ketu": 
        [["Venus", "Jupiter"], ["Rahu", "Ketu", "Saturn", "Sun", "Moon"]]
}

table = {
   "Sun": [["Moon", "Mars", "Jupiter"], ["Saturn", "Venus", "Rahu", "Ketu"], ["Mercury"]],
  "Moon": [["Sun", "Jupiter"], ["Saturn", "Rahu", "Ketu"], ["Mars", "Venus", "Mercury"]],
  "Mars": [["Sun", "Moon", "Jupiter"], ["Saturn", "Venus", "Rahu", "Ketu"], ["Mercury"]],
  "Mercury": [["Venus", "Rahu"], ["Moon", "Mars", "Jupiter"], ["Sun", "Saturn"]],
  "Jupiter": [["Sun", "Moon", "Mars"], ["Venus", "Mercury", "Rahu", "Ketu"], ["Saturn"]],
  "Venus": [["Mercury", "Saturn", "Rahu"], ["Sun", "Moon", "Mars", "Jupiter"], []],
  "Saturn": [["Venus", "Mercury", "Rahu"], ["Sun", "Moon", "Mars", "Jupiter"], []],
  "Rahu": [["Mercury", "Venus", "Saturn"], ["Sun", "Moon", "Mars", "Jupiter"], []],
  "Ketu": [["Mars", "Jupiter"], ["Sun", "Moon", "Venus"], ["Saturn", "Mercury"]],
}

exaltation = {
    "Sun" :	["Aries","Libra"],
    "Moon":	["Taurus","Scorpio"],
    "Mercury":["Virgo","Pisces"],	
    "Venus": ["Pisces","Virgo"],
    "Mars":	["Capricorn","Cancer"],		
    "Jupiter": ["Cancer","Capricorn"],
    "Saturn": ["Libra","Aries"]	,
    "Rahu":	["Taurus","Scorpio"],
    "Ketu":	["Scorpio","Taurus"]
}

karagan = {
    "Sun" : "Pithrukaragam",
    'Moon' : "Mathrukaragm",
    "Mars":"Sagotharakaragam",
    "Mercury": "Vidya Karagam",
    "Jupiter":"Dhana Karagam",
    "Venus": "Kalathra Karagam",
    "Saturn" : "Ayul Karagam",
    "Rahu": "Pitha mahakaragan",
    "Ketu": "Matha Mahakaragan",
    "Ascendant" : "Uyir Karagan",
}

athmakaraka = {
    "Sun": "As your Atmakaraka, the Sun represents a life path focused on self-expression, leadership, and personal authority. Your journey is about understanding your inner strength, embracing your role as a leader, and using your confidence to inspire others. The Sun pushes you toward positions of power and responsibility, encouraging you to shine in your endeavors. Balancing personal ambition with humility is key to fulfilling your life's purpose.",

"Moon": "With the Moon as your Atmakaraka, your soul's journey is centered around emotional growth, nurturing, and inner peace. You are called to develop your intuition, empathy, and emotional intelligence. The Moon emphasizes sensitivity, family, and relationships, guiding you toward finding fulfillment in caring for others and creating emotional balance. Prioritizing self-care and learning to manage emotional boundaries are vital aspects of your growth.",

"Mars": "When Mars is your Atmakaraka, your life's journey revolves around action, courage, and taking decisive steps toward your goals. Mars signifies a path of independence and assertiveness, pushing you to face challenges head-on and develop resilience. This planet's fiery energy encourages boldness and ambition, but you must learn to control impulsiveness and channel your energy productively. Strengthening your willpower and patience will help you succeed.",

"Mercury": "With Mercury as your Atmakaraka, your soul's journey focuses on communication, intellect, and adaptability. You are drawn to knowledge, learning, and mental agility. Mercury's influence encourages you to develop clarity in speech, critical thinking, and the ability to connect with others through language. Your life's purpose involves using your intellect wisely, embracing curiosity, and continuously growing through education and social interactions.",

"Jupiter": "As your Atmakaraka, Jupiter signifies a life path aimed at wisdom, expansion, and spiritual growth. You are called to seek knowledge, teach, and guide others on their journey. Jupiter fosters generosity, optimism, and a sense of justice, urging you to pursue truth and higher purpose. Your soul's growth is tied to balancing material success with moral and spiritual development, leading you toward greater fulfillment and abundance.",

"Venus": "With Venus as your Atmakaraka, your life's journey revolves around love, beauty, and harmony. Venus encourages you to explore the deeper meanings of relationships, aesthetics, and material pleasures. You are driven to create balance in your personal life and seek joy through love and artistic expression. Embracing the pleasures of life without attachment, while nurturing meaningful connections, is essential for your growth.",

"Saturn": "As your Atmakaraka, Saturn signifies a soul's journey of discipline, responsibility, and mastering life's challenges. You are called to develop patience, perseverance, and a strong work ethic. Saturn's influence teaches you the value of long-term planning and resilience. Your path may involve overcoming hardships, but the rewards for your dedication and hard work will be lasting. Learning to balance structure with flexibility is key to your growth.",

"Rahu": "With Rahu as your Atmakaraka, your life's purpose revolves around material desires, unconventional paths, and seeking worldly success. Rahu encourages you to break away from traditional boundaries and explore new, often uncharted, territories. Your soul's journey is one of exploration and ambition, but balancing material pursuits with spiritual awareness is crucial. Embracing change and learning to navigate illusions are key to your personal growth.",

"Ketu": "When Ketu is your Atmakaraka, your soul's journey is focused on spiritual detachment, wisdom, and breaking free from material attachments. Ketu pushes you to look beyond the physical world and explore deeper, mystical truths. Your life's path may involve releasing old patterns, seeking inner peace, and embracing solitude. Learning to integrate spiritual growth with practical life is essential for your fulfillment."

}

ista_devata_desc = {
    "Sun": "Reverence for both Lord Shiva and Lord Vishnu as your Ista Devata offers a balanced approach to spiritual devotion. Lord Shiva, known as the destroyer and transformer, represents the energy of transformation, destruction of ego, and spiritual rebirth. His worship helps in overcoming obstacles, embracing change, and purifying one's consciousness. Lord Vishnu, the preserver and protector, embodies the energy of sustenance, protection, and divine order. His worship brings blessings of stability, wisdom, and support in maintaining harmony in life. Combining the worship of Lord Shiva and Lord Vishnu harmonizes the transformative and preserving energies, providing a holistic approach to spiritual growth.",
    "Moon": "Reverence for both Lord Chandra and Goddess Lakshmi as your Ista Devata offers a balanced approach to emotional and spiritual nourishment. Lord Chandra, the lunar deity, represents the energies of emotion, intuition, and mental clarity. His worship helps in calming the mind, enhancing emotional stability, and fostering inner peace. Goddess Lakshmi, the goddess of prosperity and abundance, embodies the energy of well-being, fortune, and harmony. Her worship brings blessings of material and spiritual wealth, and supports the fulfillment of desires and stability in life. Combining the worship of Lord Chandra and Goddess Lakshmi harmonizes emotional well-being and prosperity, providing a comprehensive approach to personal growth and inner fulfillment.",
   "Mars": "Reverence for both Lord Kartikeya and Goddess Durga as your Ista Devata offers a balanced approach to courage and strength. Lord Kartikeya, the deity of war and victory, represents the energy of bravery, leadership, and overcoming challenges. His worship helps in enhancing personal power, assertiveness, and success in endeavors. Goddess Durga, the fierce protector, embodies the energy of strength, resilience, and the destruction of negative forces. Her worship brings blessings of protection, victory over adversities, and empowerment. Combining the worship of Lord Kartikeya and Goddess Durga harmonizes the energies of strength and protection, providing a robust approach to achieving personal goals and overcoming obstacles.",
   "Mercury": "Reverence for both Lord Vishnu and Goddess Saraswati as your Ista Devata offers a balanced approach to intellect and communication. Lord Vishnu, the preserver and protector, represents the energy of wisdom, harmony, and divine order. His worship supports mental clarity, intellectual growth, and effective communication. Goddess Saraswati, the goddess of knowledge and arts, embodies the energy of learning, creativity, and eloquence. Her worship enhances cognitive abilities, artistic talents, and fluency in speech. Combining the worship of Lord Vishnu and Goddess Saraswati harmonizes intellectual and communicative strengths, providing a comprehensive approach to mental and creative development.",
   "Jupiter": "Reverence for both Lord Brihaspati and Goddess Lakshmi as your Ista Devata offers a balanced approach to wisdom and prosperity. Lord Brihaspati, the guru of the gods, represents the energy of knowledge, teaching, and spiritual guidance. His worship supports the enhancement of wisdom, ethical conduct, and growth in learning. Goddess Lakshmi, the goddess of prosperity and abundance, embodies the energy of material success, well-being, and fortune. Her worship brings blessings of financial stability, abundance, and overall prosperity. Combining the worship of Lord Brihaspati and Goddess Lakshmi harmonizes intellectual and material blessings, providing a comprehensive approach to achieving success and wisdom.",
   "Venus": "Reverence for both Goddess Lakshmi and Lord Krishna as your Ista Devata offers a balanced approach to love, beauty, and harmony. Goddess Lakshmi, the goddess of prosperity and beauty, represents the energy of material abundance, elegance, and attraction. Her worship enhances personal charm, aesthetic appreciation, and harmonious relationships. Lord Krishna, known for his divine love and charisma, embodies the energy of love, joy, and divine playfulness. His worship brings blessings of deep emotional connections, joy in relationships, and spiritual fulfillment. Combining the worship of Goddess Lakshmi and Lord Krishna harmonizes the energies of love and material success, providing a holistic approach to personal and relational happiness.",
   "Saturn": "Reverence for both Lord Shani and Lord Shiva as your Ista Devata offers a balanced approach to discipline and transformation. Lord Shani, the deity associated with Saturn, represents the energy of discipline, responsibility, and justice. His worship helps in overcoming challenges, embracing hard work, and gaining resilience. Lord Shiva, the destroyer and transformer, embodies the energy of profound change, liberation, and spiritual rebirth. His worship supports the release of past burdens, personal transformation, and the development of inner strength. Combining the worship of Lord Shani and Lord Shiva harmonizes the energies of discipline and transformation, providing a comprehensive approach to navigating life's challenges and spiritual evolution.",
  "Rahu": "Reverence for both Lord Ganesha and Goddess Durga as your Ista Devata offers a balanced approach to overcoming obstacles and transformation. Lord Ganesha, the remover of obstacles, represents the energy of wisdom, success, and new beginnings. His worship helps in navigating challenges, fostering creativity, and removing barriers to progress. Goddess Durga, the fierce protector, embodies the energy of strength, resilience, and the destruction of negative forces. Her worship supports the triumph over difficulties, empowerment, and transformation. Combining the worship of Lord Ganesha and Goddess Durga harmonizes the energies of removal of obstacles and personal strength, providing a robust approach to achieving success and personal growth.",
  "Ketu": "Reverence for both Lord Hanuman and Goddess Kali as your Ista Devata offers a balanced approach to spiritual liberation and transformation. Lord Hanuman, the deity of strength and devotion, represents the energy of courage, selfless service, and spiritual dedication. His worship helps in overcoming fears, enhancing inner strength, and deepening devotion. Goddess Kali, the goddess of time and change, embodies the energy of profound transformation, liberation, and the destruction of ignorance. Her worship supports the release of attachments, personal growth, and spiritual awakening. Combining the worship of Lord Hanuman and Goddess Kali harmonizes the energies of strength and liberation, providing a comprehensive approach to achieving spiritual and personal transformation."    
}

ista_devatas = {
    "Sun": ["Lord Shiva"],
    "Moon": ["Goddess Parvati"],
    "Mars": ["Lord Kartikeya"],
    "Mercury": ["Goddess Saraswati"],
    "Jupiter": ["Lord Brihaspati"],
    "Venus": ["Goddess Lakshmi"],
    "Saturn": ["Lord Bhairava"],
    "Rahu": ["Goddess Durga"],
    "Ketu": ["Lord Hanuman"]
}

atma_names = {
    "Sun": "Lord Shiva",
    "Moon": "Goddess Parvathi",
    "Mercury": "Goddess Saraswathi",
    "Mars": "Lord karthikeyan",
    "Jupiter": "Lord Guru",
    "Venus": "Goddess Lakshmi",
    "Saturn":"Lord Bhairava",
    "Ketu": "Lord Hanuman",
    "Rahu": "Goddess Durga",
}

ista_images = {
    "Sun": ["images/god_sun_mercury_jupiter.jpeg","images/god_sun_moon_venus.jpeg"],
    "Moon": ["images/god_sun_moon_venus.jpeg","images/god_moon.jpeg"],
    "Mercury": ["images/god_mercury.jpeg","images/god_sun_mercury_jupiter.jpeg"],
    "Venus": ["images/god_sun_moon_venus.jpeg","images/god_venus.jpeg"],
    "Saturn": ["images/god_saturn.jpeg","images/god_saturn_mars.jpeg"],
    "Jupiter": ["images/god_jupiter.jpeg","images/god_sun_mercury_jupiter.jpeg"],
    "Rahu": ["images/god_rahu.jpeg","images/god_rahu_2.jpeg"],
    "Ketu": ["images/god_ketu_2.jpeg","images/god_ketu.jpeg"],
    "Mars": ["images/god_mars.jpeg","images/god_saturn_mars.jpeg"],
}


saturn_pos = [
    {
      "Sign": "Capricorn",
      "Start Date": "January 23, 2020",
      "End Date": "January 17, 2023"
    },
    {
        "Sign": "Aquarius",
        "Start Date": "January 17, 2023",
        "End Date": "March 29, 2025"
    },
    {
        "Sign": "Pisces",
        "Start Date": "March 29, 2025",
        "End Date": "June 02, 2027"
    },
    {
        "Sign": "Aries",
        "Start Date": "June 02, 2027",
        "End Date": "August 08, 2029"
    },
    {
        "Sign": "Taurus",
        "Start Date": "August 08, 2029",
        "End Date": "May 30, 2032"
    },
    {
        "Sign": "Gemini",
        "Start Date": "May 30, 2032",
        "End Date": "July 12, 2034"
    },
    {
        "Sign": "Cancer",
        "Start Date": "July 12, 2034",
        "End Date": "August 27, 2036"
    },
    {
        "Sign": "Leo",
        "Start Date": "August 27, 2036",
        "End Date": "October 22, 2038"
    },
    {
        "Sign": "Virgo",
        "Start Date": "October 22, 2038",
        "End Date": "January 27, 2041"
    },
    {
        "Sign": "Libra",
        "Start Date": "January 27, 2041",
        "End Date": "December 11, 2043"
    },
    {
        "Sign": "Scorpio",
        "Start Date": "December 11, 2043",
        "End Date": "December 07, 2046"
    },
    {
        "Sign": "Sagittarius",
        "Start Date": "December 07, 2046",
        "End Date": "March 06, 2049"
    },
    {
        "Sign": "Capricorn",
        "Start Date": "March 06, 2049",
        "End Date": "February 24, 2052"
    },
    {
        "Sign": "Aquarius",
        "Start Date": "February 24, 2052",
        "End Date": "May 14, 2054"
    },
    {
        "Sign": "Pisces",
        "Start Date": "May 14, 2054",
        "End Date": "April 06, 2057"
    },
    {
        "Sign": "Aries",
        "Start Date": "April 06, 2057",
        "End Date": "May 27, 2059"
    },
    {
        "Sign": "Taurus",
        "Start Date": "May 27, 2059",
        "End Date": "July 10, 2061"
    },
    {
        "Sign": "Gemini",
        "Start Date": "July 10, 2061",
        "End Date": "August 23, 2063"
    },
    {
        "Sign": "Cancer",
        "Start Date": "August 23, 2063",
        "End Date": "October 12, 2065"
    },
    {
        "Sign": "Leo",
        "Start Date": "October 12, 2065",
        "End Date": "August 29, 2068"
    },
    {
        "Sign": "Virgo",
        "Start Date": "August 29, 2068",
        "End Date": "November 04, 2070"
    },
    {
        "Sign": "Libra",
        "Start Date": "November 04, 2070",
        "End Date": "February 05, 2073"
    },
    {
        "Sign": "Scorpio",
        "Start Date": "February 05, 2073",
        "End Date": "January 16, 2076"
    },
    {
        "Sign": "Sagittarius",
        "Start Date": "January 16, 2076",
        "End Date": "January 14, 2079"
    },
    {
        "Sign": "Capricorn",
        "Start Date": "January 14, 2079",
        "End Date": "April 11, 2081"
    },
    {
        "Sign": "Pisces",
        "Start Date": "April 11, 2081",
        "End Date": "March 19, 2084"
    },
    {
        "Sign": "Aries",
        "Start Date": "March 19, 2084",
        "End Date": "May 21, 2086"
    },
    {
        "Sign": "Taurus",
        "Start Date": "May 21, 2086",
        "End Date": "July 17, 2088"
    },
    {
        "Sign": "Gemini",
        "Start Date": "July 17, 2088",
        "End Date": "September 18, 2090"
    },
    {
        "Sign": "Cancer",
        "Start Date": "September 18, 2090",
        "End Date": "July 02, 2093"
    },
    {
        "Sign": "Leo",
        "Start Date": "July 02, 2093",
        "End Date": "August 18, 2095"
    },
    {
        "Sign": "Virgo",
        "Start Date": "August 18, 2095",
        "End Date": "October 11, 2097"
    },
    {
        "Sign": "Libra",
        "Start Date": "October 11, 2097",
        "End Date": "December 25, 2099"
    }
]

Sade_Sati_Analysis =  [
  "Sade Sati is a significant seven-and-a-half-year period during which Saturn transits over the natal Moon and the two adjacent houses in a birth chart. This phase often brings various life challenges, including emotional stress, financial difficulties, and personal setbacks. The impact of Sade Sati can lead to instability in multiple areas of life, and its intensity depends on the specific planetary positions and overall chart configuration.",
  
  "Career and financial stability can be notably affected during Sade Sati, leading to unexpected setbacks and disruptions. Individuals may face obstacles in achieving their career goals, and financial instability might arise. This period can cause a sense of insecurity and frustration, impacting professional growth and financial security. Effective remedies can help manage these challenges and support stability.",
  
  "Personal relationships are also impacted during Sade Sati, often leading to conflicts and emotional turbulence. The stress of this period can create difficulties in maintaining harmonious relationships with family and friends. Individuals may encounter recurring issues and misunderstandings, affecting relationship stability and satisfaction. Addressing these challenges is crucial for maintaining healthy connections.",
  
  "To mitigate the effects of Sade Sati, various remedies are recommended, such as performing Saturn-related pujas, wearing specific gemstones, and engaging in charitable activities. Regular prayers, fasting on Saturdays, and seeking astrological guidance can also be beneficial. These practices aim to balance Saturn's influence and provide support during the Sade Sati period, helping individuals navigate through this challenging phase more effectively."
]


elements_data = {
    "Fire": ["Aries", "Leo", "Sagittarius"],
    "Earth": ["Taurus", "Virgo", "Capricorn"],
    "Air": ["Gemini", "Libra", "Aquarius"],
    "Water": ["Cancer", "Scorpio", "Pisces"]
}

Constitution = {
  "Kapha" : [
      "Children with a dominant Kapha dosha are gentle, calm, and nurturing. They are patient, loving, and enjoy stability and routine. However, they can also be prone to lethargy, stubbornness, and weight gain if not properly stimulated.",
      "Stocky or solid build, smooth and soft skin, tends to gain weight easily.",
      "Calm and affectionate, but may be prone to laziness or resistance to change.",
      "Prone to colds, congestion, and slower digestion, Respiratory Issues.",
      {
          "title" : "Active Lifestyle & Light Diet",
          "desc": "Incorporate activities that keep them active, such as dancing, hiking, or playing sports, to avoid lethargy and promote energy. Provide a diet with light, warm foods and include spices like ginger and black pepper to stimulate digestion. Limit heavy, oily, and overly sweet foods. Create a routine that introduces variety to keep them engaged and prevent stagnation."
      }
    ],
  "Pitta": [
    "Children with a dominant Pitta dosha are confident, ambitious, and highly intelligent. They are natural leaders and have strong determination. However, they can also be prone to impatience, irritability, and a fiery temperament when stressed.",
    "Medium build, muscular, warm body temperature, often with a glowing complexion.",
    "Focused, competitive, and passionate; can become easily frustrated or angry.",
    "Prone to skin rashes, excessive sweating, digestive issues, and overheating.",
    {
        "title": "Cooling Diet & Calming Activities",
        "desc": "Include foods that have cooling properties, such as cucumbers, melons, and leafy greens. Avoid spicy, acidic, or overly salty foods. Encourage calming activities like swimming, yoga, or relaxing play to help reduce their intense energy. Establish a peaceful routine with regular breaks to prevent overstimulation and promote emotional balance."
    }
],
"Vadha": [
    "Children with a dominant Vadha dosha are lively, imaginative, and quick to learn. They are often energetic, creative, and curious but may also be prone to anxiety and restlessness. Their energy can be inconsistent, shifting quickly from one activity to another.",
    "Thin, lean frame; dry skin; often cold hands and feet.",
    "Quick to excitement, can be anxious or overly sensitive.",
    "Prone to digestive issues, dry skin, irregular sleep, and joint stiffness.",
    {
        "title": "Warm, Nourishing Diet & Routine",
        "desc": "Provide a diet that includes warm, moist foods like soups, stews, and whole grains. Include healthy fats (e.g., avocados, nuts) and spices like cinnamon and ginger to support digestion. Establish a daily routine with consistent meal times and calming activities, such as warm baths or gentle stretches, to create stability and reduce anxiety."
    }
]

}
constitutionRatio = {
  "Sun": {
    'Pitta': 70,
     'Vata': 20,
    'Kapha': 10,
  },
   "Moon" : {
     'Kapha': 60,
     'Vata': 30,
     'Pitta': 10,
   },
    "Mercury" : {
    'Vata': 60,
    'Pitta': 30,
    'Kapha': 10,
    },
    "Venus" : {
    'Kapha': 50,
    'Pitta': 30,
    'Vata': 20,
  },
  "Mars" : {
  'Pitta': 80,
  'Vata': 15,
  'Kapha': 5,
  },
  "Jupiter" : {
   'Kapha': 60,
  'Pitta': 30,
  'Vata': 10,
},
 "Saturn" : {
'Vata': 70,
'Kapha': 20,
'Pitta': 10,
 },
 "Rahu" : {
'Vata': 80,
'Pitta': 15,
'Kapha': 5,
 },
  "Ketu" :{
  'Pitta': 70,
  'Vata': 25,
  'Kapha': 5,
  },
}



elements_content = {
    "Earth": [ 
        "Children with a dominant earth element are grounded, reliable, and nurturing. They are practical, patient, and enjoy activities that provide stability. They are natural caretakers but may sometimes struggle with adaptability or taking risks.",
        ["Dependability", "patience", "responsibility", "strong work ethic."],
        ["Over-cautiousness", "resistance to change", "potential stubbornness", "worry"],
        {
        "title": "Encourage New Experiences",
        "desc" : "Introduce activities that promote flexibility and exploration, such as trying new hobbies, outdoor adventures, or creative arts. This helps them become more adaptable and open to change."
        },
        {
        "Fire" : "Engage in energetic play or leadership activities to boost confidence and enthusiasm.",
        "Water" : "Include storytelling, imaginative play, or water-based activities to enhance emotional depth and adaptability.",
        "Air" : "Foster creative play, music, and dance to improve communication and mental agility."
        }
    ],
    "Air": [  
        "Children with a dominant air element are curious, imaginative, and highly social. They love exploring ideas, communicating, and engaging in creative activities. They are quick thinkers but may sometimes struggle with focus and consistency.",
        ["Creativity", "adaptability", "strong communication", "quick thinking"],
        ["Lack of focus", "indecisiveness", "restlessness", "scattered attention"],
        {
            "title": "Structured Routine",
            "desc": "Incorporate a clear daily schedule with defined tasks and breaks to help them stay focused and organized. Include activities that balance their creativity with structure, such as guided activities and goal-setting."
        },
        {
            "Earth": "Include activities like building projects and nature walks to promote stability and patience.",
            "Fire": "Engage in high-energy games and physical activities to enhance confidence and motivation.",
            "Water": "Introduce calming activities like storytelling or water play to foster emotional depth."
        }
    ],
    "Water": [  
        "Children with a dominant water element are sensitive, empathetic, and intuitive. They have a strong emotional depth and are often in tune with their surroundings. They excel in creative and imaginative play but may struggle with self-confidence or setting boundaries.",
        ["Emotional intelligence", "empathy", "creativity", "adaptability"],
        ["Over-sensitivity", "shyness", "difficulty with assertiveness", "prone to anxiety"],
        {
            "title": "Confidence-Building Activities",
            "desc": "Encourage activities that foster self-assurance and resilience, such as role-playing games or taking part in group activities where they can express themselves. This helps build emotional strength and assertiveness."
        },
        {
            "Earth": "Engage in hands-on activities like gardening or building to promote stability and confidence.",
            "Fire": "Include energetic play and leadership activities to boost enthusiasm and motivation.",
            "Air": "Encourage storytelling, music, and creative play to enhance communication and mental agility."
        }
    ],
    "Fire": [  
        "Children with a dominant fire element are full of energy, confidence, and enthusiasm. They are natural leaders, passionate, and driven to explore new challenges. However, they may struggle with impulsivity, impatience, and emotional intensity.",
        ["Leadership", "high energy", "motivation", "creativity"],
        ["Impulsivity", "impatience", "difficulty focusing", "quick temper"],
        {
            "title": "Mindful Breaks",
            "desc": "Incorporate calming activities such as deep breathing, guided imagery, or short yoga sessions to help your child learn to manage their energy and emotions. Schedule these during transitions or before bedtime to create balance."
        },
        {
            "Earth": "Encourage activities like building, gardening, and hands-on crafts to promote stability and patience.",
            "Water": "Introduce water play or storytelling to enhance emotional awareness and adaptability.",
            "Air": "Foster creative play, music, or dance to boost communication and open-mindedness."
        }
    ]
}


gemstone_content = {
  "Aries" : "As an Aries ascendant, Mars, the ruling planet of your ascendant, endows you with dynamic energy and a pioneering spirit. Mars, known for its assertive and action-oriented qualities, influences your personality with courage and enthusiasm. To enhance the positive effects of Mars and bolster your vitality, it's recommended to wear a red coral gemstone. This stone is believed to amplify Mars's beneficial energies, bringing strength and confidence while aligning you with your inherent drive and determination.",
"Taurus" : "As a Taurus ascendant, Venus, the ruling planet of your ascendant, imbues you with a sense of beauty, harmony, and stability. Venus's influence enhances your appreciation for the finer things in life and fosters a nurturing and affectionate nature. To further amplify Venus's positive attributes and attract abundance, it is recommended to wear a diamond. This gemstone is believed to strengthen Venus's qualities, bringing clarity, luxury, and prosperity, while aligning you with your natural elegance and creativity.",
"Gemini" : "As a Gemini ascendant, Mercury, the ruling planet of your ascendant, enhances your intellect, communication skills, and adaptability. Mercury's influence bestows you with curiosity and a keen mind, driving your desire for knowledge and versatility. To boost Mercury's beneficial effects and support your mental agility, it is recommended to wear an emerald. This gemstone is thought to amplify Mercury's positive traits, fostering clearer communication, greater intellect, and enhanced creative expression, while harmonizing with your dynamic and versatile nature.", 
"Cancer" : "As a Cancer ascendant, the Moon, the ruling planet of your ascendant, brings a nurturing and intuitive quality to your personality. The Moon's influence enhances your emotional sensitivity, imagination, and strong connection to home and family. To amplify the Moon's positive traits and support your emotional well-being, it is recommended to wear a pearl. This gemstone is believed to strengthen the Moon's beneficial energies, promoting calmness, intuition, and inner peace, while aligning with your compassionate and empathetic nature.", 
"Leo" : "As a Leo ascendant, the Sun, the ruling planet of your ascendant, infuses you with vibrant energy, leadership qualities, and a natural sense of confidence. The Sun's influence enhances your charisma, creativity, and ability to shine in various aspects of life. To further harness the Sun's powerful attributes and bolster your personal strength, it is recommended to wear a ruby. This gemstone is believed to amplify the Sun's positive energies, enhancing your vitality, self-esteem, and leadership abilities, while resonating with your bold and ambitious spirit", 
"Virgo" : "As a Virgo ascendant, Mercury, the ruling planet of your ascendant, enhances your analytical skills, attention to detail, and practical approach to life. Mercury's influence sharpens your intellect and supports your ability to organize and refine various aspects of your world. To further amplify Mercury's beneficial traits and bolster your mental clarity, it is recommended to wear an emerald. This gemstone is believed to strengthen Mercury's positive energies, promoting clear communication, analytical prowess, and intellectual growth, while harmonizing with your meticulous and methodical nature.", 
"Libra" : "As a Libra ascendant, Venus, the ruling planet of your ascendant, endows you with a deep appreciation for beauty, balance, and harmony. Venus's influence enhances your sense of fairness, creativity, and charm, guiding you towards elegant and harmonious relationships. To further elevate Venus's positive qualities and attract prosperity, it is recommended to wear a diamond. This gemstone is believed to amplify Venus's beneficial energies, enhancing your aesthetic sensibility, fostering loving relationships, and bringing clarity and abundance into your life, perfectly aligning with your refined and diplomatic nature.",
"Scorpio" : "As a Scorpio ascendant, Mars, the ruling planet of your ascendant, infuses you with intense passion, determination, and transformative energy. Mars's influence sharpens your focus and resilience, driving you to pursue your goals with unwavering intensity. To further enhance Mars's positive qualities and support your dynamic nature, it is recommended to wear a red coral. This gemstone is believed to amplify Mars's beneficial energies, boosting your courage, vitality, and personal power, while resonating with your deeply driven and transformative spirit.", 
"Sagittarius" : "As a Sagittarius ascendant, Jupiter, the ruling planet of your ascendant, bestows you with a sense of optimism, adventure, and a quest for knowledge. Jupiter's influence enhances your enthusiasm for exploration, growth, and expansion. To further amplify Jupiter's positive attributes and support your aspirations, it is recommended to wear a yellow sapphire. This gemstone is believed to strengthen Jupiter's beneficial energies, promoting wisdom, abundance, and prosperity, while aligning with your expansive and philosophical nature.", 
"Capricorn" : "As a Capricorn ascendant, Saturn, the ruling planet of your ascendant, instills a sense of discipline, responsibility, and determination in your character. Saturn's influence enhances your ability to work hard, stay focused, and achieve long-term goals. To further harness Saturn's positive qualities and support your efforts, it is recommended to wear a blue sapphire. This gemstone is believed to amplify Saturn's beneficial energies, fostering clarity, wisdom, and perseverance, while aligning with your practical and ambitious nature.", 
"Aquarius" : "As an Aquarius ascendant, Saturn, the ruling planet of your ascendant, infuses you with a unique blend of innovation, determination, and a strong sense of responsibility. Saturn's influence enhances your ability to think forward, embrace change, and work diligently towards your visionary goals. To further strengthen Saturn's positive attributes and support your progressive nature, it is recommended to wear a blue sapphire. This gemstone is believed to amplify Saturn's beneficial energies, promoting clarity, discipline, and success, while resonating with your forward-thinking and ambitious spirit.", 
"Pisces" : "As a Pisces ascendant, Jupiter, the ruling planet of your ascendant, enriches you with a deep sense of compassion, intuition, and a desire for spiritual growth. Jupiter's influence enhances your creative and empathetic nature, guiding you towards wisdom and understanding. To further amplify Jupiter's positive attributes and support your dreams, it is recommended to wear a yellow sapphire. This gemstone is believed to strengthen Jupiter's beneficial energies, fostering prosperity, insight, and spiritual enlightenment, while aligning with your imaginative and empathetic essence.", 
}

Gemstone_about= {
    "Red Coral": [
      "1. Red coral should be set in a copper ring, as copper enhances its effects.",
      "2. The recommended weight of red coral is between 5 to 7 carats.",
      "3. It should be purchased and set on a Tuesday, particularly during the waxing phase of the Moon.",
      "4. The coral must touch the skin when worn for full effect.",
      "5. Cleanse the coral by soaking it in honey overnight before wearing it.",
      "6. Chant the mantra 'Om Mangalaya Namah' 108 times while holding the ring.",
      "7. The ideal time to wear red coral is one hour after sunrise on a Tuesday.",
      "8. Wear the ring on the ring finger of the right hand for optimal results.",
      "9. Red coral helps in overcoming lethargy and boosting physical energy.",
      "10. Alternatives include Carnelian and Red Aventurine, both of which can substitute coral in certain cases."
    ],
    "Ruby": [
      "1. Ruby should be set in a gold or panchdhatu ring for best results.",
      "2. It is recommended to wear a ruby of 5 carats or more.",
      "3. The ideal day to purchase and set ruby is Sunday, during the Shukla Paksha (waxing phase).",
      "4. The stone must touch the skin to harness the Sun's power.",
      "5. Cleanse the ruby by immersing it in a mixture of honey and Ganga water.",
      "6. Chant the mantra 'Om Surya Namah' 108 times before wearing the ring.",
      "7. Ruby should be worn one hour after sunrise on a Sunday.",
      "8. The ring is traditionally worn on the ring finger of the right hand.",
      "9. Ruby enhances self-confidence and leadership qualities.",
      "10. Alternatives include Red Garnet and Spinel, both offering similar benefits."
    ],
    "Pearl": [
      "1. Pearl should be set in a silver ring to enhance its calming effects.",
      "2. The pearl should weigh a minimum of 6 carats for noticeable results.",
      "3. It should be worn on a Monday during the waxing phase of the Moon.",
      "4. The pearl must touch the skin to absorb lunar energy.",
      "5. Cleanse the pearl by placing it in a bowl of Ganga water overnight.",
      "6. Chant 'Om Chandraya Namah' 108 times before wearing the pearl.",
      "7. Wear the pearl on a Monday morning, an hour after sunrise.",
      "8. The ring should be worn on the little finger of the right hand.",
      "9. Pearl promotes emotional balance and mental peace.",
      "10. Alternatives include Moonstone and White Coral, offering similar lunar benefits."
    ],
    "Emerald": [
      "1. Emerald should be set in gold for prosperity-related benefits.",
      "2. The emerald should be at least 4 to 6 carats in weight.",
      "3. Purchase and set it on a Wednesday in the waxing phase of the Moon.",
      "4. The emerald must touch the skin for full effect.",
      "5. Cleanse the emerald by soaking it in saltwater overnight.",
      "6. Recite the mantra 'Om Budhaya Namah' 108 times before wearing the ring.",
      "7. Wear the emerald on a Wednesday morning, an hour after sunrise.",
      "8. It is recommended to wear the ring on the little finger of the right hand.",
      "9. Emerald aids in intellectual clarity and communication.",
      "10. Peridot and Green Tourmaline are acceptable substitutes."
    ],
    "Diamond": [
      "1. Diamond should be set in white gold or platinum for the best effect.",
      "2. A diamond weighing at least 1 to 1.5 carats is recommended.",
      "3. It should be purchased on a Friday during the waxing moon.",
      "4. Ensure the diamond touches your skin when wearing it.",
      "5. Cleanse the diamond by keeping it under moonlight overnight.",
      "6. Chant the mantra 'Om Shukraya Namah' 108 times before wearing the ring.",
      "7. Wear the diamond ring on a Friday morning, an hour after sunrise.",
      "8. It should be worn on the middle finger of the right hand.",
      "9. Diamond improves luxury, comfort, and marital harmony.",
      "10. White Sapphire and Zircon are alternatives with similar qualities."
    ],
    "Yellow Sapphire": [
      "1. Yellow sapphire should be set in gold for spiritual growth.",
      "2. A stone weighing between 5 to 7 carats is ideal.",
      "3. Buy and wear it on a Thursday, during the waxing phase.",
      "4. Ensure the sapphire touches the skin while wearing it.",
      "5. Cleanse the sapphire by dipping it in turmeric water overnight.",
      "6. Recite the mantra 'Om Brihaspataye Namah' 108 times before wearing it.",
      "7. Wear the yellow sapphire ring on Thursday, an hour after sunrise.",
      "8. It should be worn on the index finger of the right hand.",
      "9. Yellow sapphire promotes wisdom, wealth, and spirituality.",
      "10. Citrine and Topaz serve as acceptable substitutes."
    ],
     "Blue Sapphire": [
        "1. Blue Sapphire should be set in a ring made of silver or platinum to amplify its positive effects.",
        "2. The sapphire should weigh at least 5 carats to ensure its impact on the wearer.",
        "3. Wear the sapphire on a Saturday, preferably during the waxing phase of the Moon.",
        "4. The sapphire must touch the skin to channel the energy of Saturn effectively.",
        "5. Cleanse the sapphire by soaking it in a mixture of milk and honey overnight.",
        "6. Chant 'Om Sham Shanicharaya Namah' 108 times before wearing the sapphire.",
        "7. Wear the sapphire on a Saturday morning, an hour after sunrise.",
        "8. The ring should be worn on the middle finger of the right hand.",
        "9. Blue Sapphire is known to bring discipline, focus, and financial stability.",
        "10. Alternatives include Lapis Lazuli and Tanzanite, which offer similar benefits."
    ],
    
    "Hessonite": [
        "1. Hessonite should be set in a ring of gold or copper to enhance its positive qualities.",
        "2. The gemstone should weigh at least 6 carats for effective results.",
        "3. Wear the hessonite on a Saturday, during the waxing Moon phase, for best effects.",
        "4. The gemstone must be in direct contact with the skin to harness its energy.",
        "5. Cleanse the hessonite by washing it in a mixture of honey and water overnight.",
        "6. Chant 'Om Rahave Namah' 108 times before wearing the hessonite.",
        "7. Wear the hessonite on a Saturday morning, an hour after sunrise.",
        "8. The ring should be worn on the middle finger of the right hand.",
        "9. Hessonite is believed to remove obstacles and bring success in career and finances.",
        "10. Alternatives include Garnet and Citrine, providing similar benefits."
    ],
    
    "Cat's Eye": [
        "1. Cat's Eye should be set in a gold or silver ring to maximize its protective qualities.",
        "2. The gemstone should weigh a minimum of 5 carats to be effective.",
        "3. Wear the Cat's Eye on a Tuesday during the waxing Moon phase for best results.",
        "4. The gemstone must touch the skin to properly channel Ketu's energy.",
        "5. Cleanse the Cat's Eye by soaking it in a mixture of raw milk and honey overnight.",
        "6. Chant 'Om Ketave Namah' 108 times before wearing the Cat's Eye.",
        "7. Wear the Cat's Eye on a Tuesday morning, an hour after sunrise.",
        "8. The ring should be worn on the index finger of the right hand.",
        "9. Cat's Eye is known to protect against negative energies and bring mental clarity.",
        "10. Alternatives include Chrysoberyl and Tiger's Eye, offering similar protective properties."
    ]
  }


Planet_Gemstone_Desc = {
  "Sun": {
    "Gemstone": "Ruby",
    "Description": "Ruby is known for its vibrant red color and is associated with the Sun. It is believed to enhance vitality, leadership qualities, and confidence. Ruby can help in overcoming obstacles and bringing success and honor. It also promotes creativity and enthusiasm, making it beneficial for those seeking to boost their energy and assertiveness.",
  },
  "Moon": {
    "Gemstone": "Pearl",
    "Description": "Pearl is linked to the Moon and is valued for its calming effects and emotional balance. It is said to enhance intuition, wisdom, and mental clarity. Wearing a pearl is believed to bring serenity and stability, making it ideal for those seeking to improve their emotional well-being and strengthen their relationships."
  },
  "Mars": {
    "Gemstone": "Red Coral",
    "Description": "Red Coral is connected to Mars and is known for its energizing and protective qualities. It is believed to enhance courage, physical strength, and determination. Red Coral can help overcome challenges and improve assertiveness, making it a useful gemstone for those seeking to boost their confidence and drive."
  },
  "Mercury": {
    "Gemstone": "Emerald",
    "Description": "Emerald is associated with Mercury and is valued for its stimulating and intellectual properties. It is believed to enhance communication skills, intelligence, and creativity. Wearing an emerald can improve focus and analytical abilities, making it beneficial for those seeking mental clarity and effective communication."
  },
  "Jupiter": {
    "Gemstone": "Yellow Sapphire",
    "Description": "Yellow Sapphire is linked to Jupiter and is known for its auspicious and expansive qualities. It is believed to enhance wisdom, prosperity, and good fortune. Wearing a yellow sapphire can bring success, growth, and positive changes, making it ideal for those seeking to improve their financial and personal well-being."
  },
  "Venus": {
    "Gemstone": "Diamond",
    "Description": "Diamond is associated with Venus and is valued for its brilliance and clarity. It is believed to enhance love, beauty, and luxury. Wearing a diamond can bring harmony, success in relationships, and financial prosperity, making it a powerful gemstone for those seeking to attract and enjoy life's pleasures."
  },
  "Saturn": {
    "Gemstone": "Blue Sapphire",
    "Description": "Blue Sapphire is connected to Saturn and is known for its profound and transformative qualities. It is believed to enhance discipline, responsibility, and wisdom. Wearing a blue sapphire can help in overcoming challenges and achieving long-term success, making it beneficial for those seeking stability and personal growth."
  },
  "Rahu": {
    "Gemstone": "Hessonite Garnet",
    "Description": "Hessonite Garnet is associated with Rahu and is valued for its protective and balancing properties. It is believed to mitigate the negative effects of Rahu and bring clarity and stability. Wearing hessonite garnet can help in overcoming obstacles and achieving success in various areas of life, making it useful for those facing difficulties."
  },
  "Ketu": {
    "Gemstone": "Cat's Eye",
    "Description": "Cat's Eye is linked to Ketu and is known for its unique and transformative qualities. It is believed to provide protection, insight, and spiritual growth. Wearing a cat's eye gemstone can help in overcoming fears and challenges, making it beneficial for those seeking to enhance their spiritual awareness and personal development."
  }
}

career_rudra= {
    "Aries": "Aries individuals, known for their dynamic and pioneering nature, can benefit from the 1 Mukhi Rudraksha, which enhances leadership skills, focus, and determination. This bead helps them excel in competitive environments and climb the career ladder effectively. Pairing it with the 9 Mukhi Rudraksha supports them by providing protection and boosting personal strength, aiding in overcoming professional challenges and achieving career goals. Together, these Rudrakshas help Aries ascendants achieve success and recognition in their chosen fields.",
    "Taurus": "Taurus ascendants can enhance their career prospects with the 5 Mukhi Rudraksha, which promotes stability and focus, essential for career growth. This bead supports perseverance and effective management of responsibilities. The 14 Mukhi Rudraksha complements this by amplifying their ability to attract opportunities and gain recognition. This combination ensures that Taurus individuals can advance in their careers and achieve long-term success through a balanced and determined approach.",
    "Gemini": "Gemini ascendants can benefit from the 3 Mukhi Rudraksha, which boosts creativity, mental clarity, and adaptability—key traits for success in various careers. This bead helps them navigate changes and opportunities effectively. Adding the 4 Mukhi Rudraksha further enhances their communication skills and intellectual abilities, critical for career advancement and educational achievements. Together, these Rudrakshas support Gemini individuals in excelling academically and professionally.",
    "Cancer": "Cancer ascendants can benefit from the 2 Mukhi Rudraksha, which promotes emotional stability and harmonious relationships, essential for a successful career. This bead helps them navigate workplace dynamics and achieve career goals. The 5 Mukhi Rudraksha supports overall well-being and focus, contributing to academic and professional success. This combination helps Cancer individuals create a supportive environment for career growth and educational achievements.",
    "Leo": "Leos can enhance their career and educational success with the 1 Mukhi Rudraksha, which amplifies their leadership qualities, confidence, and focus. This bead supports their ambitions and helps them stand out in competitive fields. The 6 Mukhi Rudraksha complements this by fostering self-discipline and improving organizational skills. Together, these Rudrakshas ensure that Leo ascendants achieve their career goals and excel in their educational pursuits.",
    "Virgo": "Virgo ascendants can benefit from the 4 Mukhi Rudraksha, which enhances intellectual abilities, communication skills, and attention to detail—important for career and educational success. This bead supports effective learning and professional growth. The 2 Mukhi Rudraksha provides emotional balance and harmony, aiding in managing stress and maintaining focus. This combination helps Virgo individuals excel academically and professionally through careful planning and execution.",
    "Libra": "Libras can achieve career success and academic excellence with the 6 Mukhi Rudraksha, which enhances self-discipline, focus, and decision-making skills. This bead supports them in managing career responsibilities effectively. The 8 Mukhi Rudraksha complements this by promoting personal growth and attracting opportunities. Together, these Rudrakshas help Libra ascendants navigate their career and educational paths with balance and clarity.",
    "Scorpio": "Scorpio ascendants can benefit from the 2 Mukhi Rudraksha, which supports emotional stability and interpersonal skills, crucial for career advancement. This bead helps them manage complex professional relationships and challenges. Adding the 7 Mukhi Rudraksha enhances their career prospects by attracting opportunities and providing protection against setbacks. This combination ensures that Scorpio individuals can achieve their career and educational goals through resilience and strategic thinking.",
    "Sagittarius": "Sagittarius ascendants can enhance their career and educational prospects with the 5 Mukhi Rudraksha, which supports overall health, stability, and focus. This bead helps them manage their ambitious pursuits effectively. The 9 Mukhi Rudraksha further supports this by providing protection and boosting confidence, aiding in overcoming obstacles and achieving success. Together, these Rudrakshas help Sagittarius individuals thrive in their professional and academic endeavors.",
    "Capricorn": "Capricorns can benefit from the 6 Mukhi Rudraksha, which enhances self-discipline, focus, and organizational skills—key traits for career advancement and academic success. This bead supports their ambitious nature and helps them achieve their goals. The 14 Mukhi Rudraksha complements this by attracting opportunities and promoting prosperity. Together, these Rudrakshas help Capricorn ascendants excel in their careers and educational pursuits through disciplined efforts and strategic planning.",
    "Aquarius": "Aquarius ascendants can benefit from the 8 Mukhi Rudraksha, which boosts energy, creativity, and personal growth, essential for career and educational success. This bead helps them harness their innovative ideas effectively. Adding the 4 Mukhi Rudraksha enhances their intellectual clarity and communication skills, supporting academic and professional achievements. This combination helps Aquarius individuals excel through their unique insights and skills.",
    "Pisces": "Pisces ascendants can enhance their career and education with the 7 Mukhi Rudraksha, which supports emotional stability, creativity, and prosperity. This bead helps them manage their professional and academic challenges effectively. The 2 Mukhi Rudraksha provides additional emotional balance and harmony, aiding in focus and decision-making. Together, these Rudrakshas help Pisces individuals achieve their career and educational goals through a balanced and intuitive approach."
  }

health_rudra = {
  "Aries": "Aries individuals are known for their energetic and pioneering spirit, which can sometimes lead to burnout and stress. To enhance their vitality and balance, they can benefit from wearing the 1 Mukhi Rudraksha. This bead is believed to amplify their natural energy, focus, and leadership qualities, helping them stay centered and driven. Complementing this with the 9 Mukhi Rudraksha provides additional support by offering protection from negative energies and boosting personal strength. Together, these Rudrakshas can help Aries ascendants maintain high energy levels, manage stress effectively, and achieve their ambitious goals.",
  "Taurus": "Taurus ascendants are grounded and practical but may occasionally struggle with stress and emotional strain. The 5 Mukhi Rudraksha is ideal for promoting overall health, stability, and emotional balance. It supports physical vitality and helps in managing stress. Pairing this with the 14 Mukhi Rudraksha enhances prosperity and personal power, further supporting their well-being. The 14 Mukhi bead is known for its ability to attract positive energies and improve financial stability. Together, these Rudrakshas help Taurus individuals achieve a balanced and stable life.",
  "Gemini": "Gemini ascendants are intellectually curious and versatile, often juggling multiple responsibilities. The 3 Mukhi Rudraksha is beneficial for boosting mental clarity, creativity, and overall energy levels. It helps in overcoming mental fatigue and maintaining focus. To further support their well-being, the 4 Mukhi Rudraksha can be used, enhancing communication skills and intellectual abilities. This combination of Rudrakshas allows Gemini individuals to manage their diverse interests effectively while maintaining physical and mental vitality.",
  "Cancer": "Cancer individuals are deeply intuitive and emotionally sensitive, which can lead to emotional and physical challenges. The 2 Mukhi Rudraksha is highly supportive for emotional balance and boosting the immune system. It helps in soothing emotional turbulence and promoting overall well-being. Adding the 5 Mukhi Rudraksha further enhances physical health and mental peace. This bead is widely known for its general health benefits and ability to harmonize energies. Combining these Rudrakshas helps Cancer ascendants manage their emotional depth while improving their physical vitality.",
  "Leo": "Leos, with their vibrant personality and strong leadership qualities, often experience high demands on their energy and focus. The 1 Mukhi Rudraksha is perfect for amplifying their natural confidence and boosting their energy levels. This bead enhances their leadership abilities and provides a sense of unity and purpose. The 6 Mukhi Rudraksha complements this by promoting self-discipline and increasing vitality. It helps in managing stress and maintaining physical strength. Together, these Rudrakshas support Leo ascendants in balancing their dynamic lifestyle.",
  "Virgo": "Virgo ascendants are meticulous and detail-oriented, which can sometimes lead to mental and physical stress. The 4 Mukhi Rudraksha enhances communication, intellectual abilities, and mental clarity. It supports stress management and promotes overall health. Pairing this with the 2 Mukhi Rudraksha provides emotional balance and harmony, helping to alleviate stress and emotional strain. This combination allows Virgo individuals to maintain their analytical prowess while ensuring that their emotional and physical health are well-supported.",
  "Libra": "Libras seek balance and harmony but may face challenges in maintaining physical and emotional equilibrium. The 6 Mukhi Rudraksha is beneficial for enhancing self-discipline and boosting energy levels, promoting overall health. To support their quest for harmony, the 8 Mukhi Rudraksha can be added, which enhances spiritual growth and vitality. Together, these Rudrakshas help Libra ascendants achieve a balanced and harmonious life, improving both their physical well-being and emotional stability.",
  "Scorpio": "Scorpio ascendants are intense and passionate, often facing emotional and physical strain. The 2 Mukhi Rudraksha is excellent for emotional stability and overall health, helping to manage intense emotions and stress. Complementing this with the 7 Mukhi Rudraksha offers prosperity and protection, which aids in enhancing personal strength and resilience. This combination supports Scorpio individuals in maintaining emotional balance, boosting physical vitality, and providing protection from negative influences.",
  "Sagittarius": "Sagittarius ascendants are adventurous and energetic, with a strong desire for new experiences. The 5 Mukhi Rudraksha supports overall health and vitality, helping them manage stress and maintain high energy levels. The 9 Mukhi Rudraksha further enhances this by providing protection and increasing personal strength. Together, these Rudrakshas help Sagittarius individuals balance their adventurous spirit with physical well-being and resilience, allowing them to explore new horizons while maintaining good health.",
  "Capricorn": "Capricorns are disciplined and ambitious, often pushing themselves to achieve their goals. The 6 Mukhi Rudraksha enhances physical strength and self-discipline, supporting their rigorous lifestyle. Pairing this with the 14 Mukhi Rudraksha provides additional benefits by promoting authority, prosperity, and protection. This combination supports Capricorn individuals in managing their demanding responsibilities while maintaining robust health and achieving professional success.",
  "Aquarius": "Aquarius ascendants are innovative and forward-thinking, often dealing with high levels of mental activity and stress. The 8 Mukhi Rudraksha supports increased energy, spiritual growth, and vitality. To enhance their intellectual clarity and communication, the 4 Mukhi Rudraksha can be added. This combination helps Aquarius individuals manage their mental and physical demands, improving overall well-being and supporting their visionary approach to life.",
  "Pisces": "Pisces individuals are intuitive and sensitive, which can lead to emotional and physical challenges. The 7 Mukhi Rudraksha supports emotional stability, protection, and overall health. Adding the 2 Mukhi Rudraksha provides additional benefits by promoting harmony and reducing stress. Together, these Rudrakshas help Pisces ascendants manage their emotional depth, improve physical vitality, and maintain a balanced and harmonious life."
}

wealth_rudra={
    "Aries": "Aries individuals can significantly benefit from the 1 Mukhi Rudraksha, which enhances their leadership abilities and attracts wealth by amplifying their focus and personal power. Pairing this with the 9 Mukhi Rudraksha provides additional benefits by offering protection and drawing positive energies, which can lead to substantial financial gains and stability. This combination supports Aries ascendants in leveraging their dynamic nature to achieve notable prosperity.",
    "Taurus": "Taurus ascendants, known for their practical approach, can enhance their wealth with the 5 Mukhi Rudraksha, which promotes stability and supports steady financial growth. The 14 Mukhi Rudraksha complements this by attracting prosperity and removing financial obstacles. Together, these Rudrakshas ensure that Taurus individuals experience consistent financial success and stability.",
    "Gemini": "Gemini ascendants can benefit from the 3 Mukhi Rudraksha, which boosts mental clarity and creativity, essential for generating wealth and new opportunities. Adding the 4 Mukhi Rudraksha further enhances their communication skills and intellectual abilities, critical for financial success. This combination helps Gemini individuals effectively manage and grow their wealth through innovative and articulate approaches.",
    "Cancer": "Cancer ascendants can attract wealth and stability with the 2 Mukhi Rudraksha, which supports emotional balance and harmonious relationships, creating a favorable environment for financial growth. The 5 Mukhi Rudraksha adds to this by promoting overall health and stability, ensuring that Cancer individuals achieve financial prosperity through a balanced and nurturing approach.",
    "Leo": "Leos can enhance their financial success with the 1 Mukhi Rudraksha, which amplifies their leadership qualities and attracts wealth by increasing their personal power and focus. The 6 Mukhi Rudraksha complements this by improving self-discipline and financial management skills. Together, these Rudrakshas help Leo ascendants achieve their financial goals and maintain prosperity.",
    "Virgo": "Virgo ascendants can benefit from the 4 Mukhi Rudraksha, which enhances their intellectual abilities and communication skills, essential for financial success. The 2 Mukhi Rudraksha provides additional support by promoting emotional balance and better decision-making. This combination helps Virgo individuals manage their finances meticulously and achieve wealth through thoughtful planning and execution.",
    "Libra": "Libras can achieve financial stability and growth with the 6 Mukhi Rudraksha, which enhances self-discipline and financial management. The 8 Mukhi Rudraksha adds to this by attracting abundance and prosperity, supporting their quest for balance and harmony. This combination ensures that Libra ascendants achieve financial success through disciplined efforts and a harmonious approach.",
    "Scorpio": "Scorpio ascendants can attract wealth and overcome financial challenges with the 2 Mukhi Rudraksha, which provides emotional stability and harmony. The 7 Mukhi Rudraksha enhances this by attracting prosperity and providing protection against financial losses. Together, these Rudrakshas support Scorpio individuals in achieving financial stability and growth through a balanced and resilient approach.",
    "Sagittarius": "Sagittarius ascendants can enhance their financial prospects with the 5 Mukhi Rudraksha, which supports overall health and stability, crucial for financial success. The 9 Mukhi Rudraksha complements this by providing protection and attracting prosperity. This combination helps Sagittarius individuals explore new opportunities and achieve financial success while maintaining stability.",
    "Capricorn": "Capricorns can achieve financial success and stability with the 6 Mukhi Rudraksha, which enhances self-discipline and financial management skills. The 14 Mukhi Rudraksha further supports this by attracting wealth and removing obstacles. Together, these Rudrakshas help Capricorn individuals maintain long-term prosperity through disciplined efforts and strategic planning.",
    "Aquarius": "Aquarius ascendants can benefit from the 8 Mukhi Rudraksha, which boosts energy and attracts abundance, supporting financial growth. Adding the 4 Mukhi Rudraksha enhances their intellectual clarity and communication, essential for wealth creation. This combination helps Aquarius individuals leverage their innovative ideas for financial success and prosperity.",
    "Pisces": "Pisces ascendants can enhance their financial stability with the 7 Mukhi Rudraksha, which supports wealth attraction and protection. The 2 Mukhi Rudraksha provides additional benefits by promoting emotional balance and reducing stress, creating a favorable environment for financial growth. Together, these Rudrakshas help Pisces individuals achieve financial success through balanced and harmonious approaches."
}

sign_mukhi = {
  "Aries": ["1 muki", "9 muki"],
  "Taurus": ["5 muki", "14 muki"],
  "Gemini": ["3 muki", "4 muki"],
  "Cancer": ["2 muki", "5 muki"],
  "Leo": ["1 muki", "6 muki"],
  "Virgo": ["4 muki", "2 muki"],
  "Libra": ["6 muki", "8 muki"],
  "Scorpio": ["2 muki", "7 muki"],
  "Sagittarius": ["5 muki", "9 muki"],
  "Capricorn": ["6 muki", "14 muki"],
  "Aquarius": ["8 muki", "4 muki"],
  "Pisces": ["7 muki", "2 muki"]
}

planet_quality = {
    "Sun" : [{
    1: "Self-identity and Vitality",
    2: "Wealth and Values",
    3: "Communication and Courage",
    4: "Home and Emotional Stability",
    5: "Creativity and Intelligence",
    6: "Service and Health",
    7: "Partnerships and Diplomacy",
    8: "Transformation and Introspection",
    9: "Wisdom and Spirituality",
    10: "Career and Reputation",
    11: "Friendships and Aspirations",
    12: "Spirituality and Isolation"
}
,{
    "Aries": "Leadership and Assertiveness",
    "Taurus": "Stability and Determination",
    "Gemini": "Communication and Versatility",
    "Cancer": "Nurturing and Emotional Depth",
    "Leo": "Confidence and Charisma",
    "Virgo": "Practicality and Service",
    "Libra": "Diplomacy and Charm",
    "Scorpio": "Intensity and Passion",
    "Sagittarius": "Optimism and Adventure",
    "Capricorn": "Discipline and Authority",
    "Aquarius": "Innovation and Independence",
    "Pisces": "Creativity and Sensitivity"
},
    {
    "Ashwini": "Dynamic and Healing",
    "Bharani": "Creative and Transformative",
    "Krittika": "Strong-willed and Nurturing",
    "Rohini": "Creative and Sensual",
    "Mrigashira": "Curious and Adaptable",
    "Ardra": "Intense and Passionate",
    "Punarvasu": "Optimistic and Restorative",
    "Pushya": "Nurturing and Supportive",
    "Ashlesha": "Intuitive and Mysterious",
    "Magha": "Regal and Authoritative",
    "Purva Phalguni": "Romantic and Charismatic",
    "Uttara Phalguni": "Generous and Stable",
    "Hasta": "Skillful and Resourceful",
    "Chitra": "Artistic and Aesthetic",
    "Swati": "Independent and Balanced",
    "Vishakha": "Goal-oriented and Driven",
    "Anuradha": "Loyal and Cooperative",
    "Jyeshtha": "Intelligent and Protective",
    "Mula": "Intense and Transformational",
    "Purva Ashadha": "Victorious and Confident",
    "Uttara Ashadha": "Responsible and Ambitious",
    "Shravana": "Listening and Knowledgeable",
    "Dhanishta": "Wealthy and Energetic",
    "Shatabhisha": "Mystical and Healing",
    "Purva Bhadrapada": "Transformative and Philosophical",
    "Uttara Bhadrapada": "Spiritual and Compassionate",
    "Revati": "Imaginative and Caring"
}
],
    "Moon" : [{
    1: "Emotions and Intuition",
    2: "Security and Values",
    3: "Mental Agility and Communication",
    4: "Comfort and Nurturing",
    5: "Creativity and Romance",
    6: "Service and Health",
    7: "Relationships and Cooperation",
    8: "Emotional Depth and Transformation",
    9: "Philosophy and Long-distance Travel",
    10: "Public Image and Career",
    11: "Friendships and Social Connections",
    12: "Introspection and Spirituality"
}
,{
    "Aries": "Impulsiveness and Passion",
    "Taurus": "Security and Comfort",
    "Gemini": "Curiosity and Adaptability",
    "Cancer": "Emotional Depth and Nurturing",
    "Leo": "Generosity and Warmth",
    "Virgo": "Analytical and Practicality",
    "Libra": "Harmony and Relationship-focused",
    "Scorpio": "Intensity and Emotional Insight",
    "Sagittarius": "Optimism and Freedom",
    "Capricorn": "Responsibility and Seriousness",
    "Aquarius": "Unconventional and Humanitarian",
    "Pisces": "Imagination and Empathy"
},
{
    "Ashwini": "Energetic and Impulsive",
    "Bharani": "Emotionally Intense and Protective",
    "Krittika": "Nurturing and Strong-willed",
    "Rohini": "Sensual and Loving",
    "Mrigashira": "Curious and Adaptable",
    "Ardra": "Emotionally Intense and Passionate",
    "Punarvasu": "Restorative and Hopeful",
    "Pushya": "Supportive and Caring",
    "Ashlesha": "Intuitive and Deeply Emotional",
    "Magha": "Proud and Authoritative",
    "Purva Phalguni": "Romantic and Charismatic",
    "Uttara Phalguni": "Stable and Supportive",
    "Hasta": "Resourceful and Skillful",
    "Chitra": "Artistic and Social",
    "Swati": "Balanced and Diplomatic",
    "Vishakha": "Goal-oriented and Enthusiastic",
    "Anuradha": "Loyal and Friendly",
    "Jyeshtha": "Protective and Resourceful",
    "Mula": "Intense and Investigative",
    "Purva Ashadha": "Victorious and Bold",
    "Uttara Ashadha": "Responsible and Ambitious",
    "Shravana": "Knowledgeable and Observant",
    "Dhanishta": "Energetic and Social",
    "Shatabhisha": "Mystical and Healing",
    "Purva Bhadrapada": "Transformative and Deep",
    "Uttara Bhadrapada": "Spiritual and Compassionate",
    "Revati": "Imaginative and Gentle"
    }
    ],
    "Mars" : [{
    1: "Courage and Assertiveness",
    2: "Financial Drive and Values",
    3: "Initiative and Communication",
    4: "Emotional Strength and Family",
    5: "Creativity and Competitive Spirit",
    6: "Service and Health",
    7: "Passionate Partnerships and Conflict",
    8: "Transformation and Intensity",
    9: "Adventurous Spirit and Philosophy",
    10: "Ambition and Career Success",
    11: "Goals and Friendships",
    12: "Isolation and Hidden Energies"
}
,{
    "Aries": "Courage and Initiative",
    "Taurus": "Determination and Patience",
    "Gemini": "Versatility and Quick-thinking",
    "Cancer": "Protectiveness and Sensitivity",
    "Leo": "Confidence and Ambition",
    "Virgo": "Diligence and Precision",
    "Libra": "Diplomatic and Balanced",
    "Scorpio": "Intensity and Drive",
    "Sagittarius": "Adventurous and Energetic",
    "Capricorn": "Disciplined and Strategic",
    "Aquarius": "Innovative and Eccentric",
    "Pisces": "Compassionate and Intuitive"
},
{
    "Ashwini": "Dynamic and Action-oriented",
    "Bharani": "Passionate and Transformative",
    "Krittika": "Strong-willed and Courageous",
    "Rohini": "Creative and Sensual",
    "Mrigashira": "Curious and Quick-thinking",
    "Ardra": "Intense and Driven",
    "Punarvasu": "Optimistic and Energetic",
    "Pushya": "Supportive and Protective",
    "Ashlesha": "Intense and Mysterious",
    "Magha": "Regal and Authoritative",
    "Purva Phalguni": "Romantic and Bold",
    "Uttara Phalguni": "Stable and Determined",
    "Hasta": "Skillful and Resourceful",
    "Chitra": "Artistic and Ambitious",
    "Swati": "Independent and Balanced",
    "Vishakha": "Goal-oriented and Motivated",
    "Anuradha": "Loyal and Supportive",
    "Jyeshtha": "Protective and Assertive",
    "Mula": "Intense and Transformative",
    "Purva Ashadha": "Confident and Victorious",
    "Uttara Ashadha": "Ambitious and Hardworking",
    "Shravana": "Knowledgeable and Analytical",
    "Dhanishta": "Energetic and Prosperous",
    "Shatabhisha": "Mystical and Strong-willed",
    "Purva Bhadrapada": "Transformative and Philosophical",
    "Uttara Bhadrapada": "Spiritual and Wise",
    "Revati": "Compassionate and Gentle"
}
],
    "Mercury" : [{
    1: "Communication and Adaptability",
    2: "Intellect and Financial Acumen",
    3: "Curiosity and Sibling Relations",
    4: "Emotional Intelligence and Family Ties",
    5: "Creativity and Expression",
    6: "Analytical Skills and Service",
    7: "Negotiation and Partnerships",
    8: "Research and Depth of Thought",
    9: "Philosophical Mind and Learning",
    10: "Career Communication and Public Image",
    11: "Social Networks and Aspirations",
    12: "Introspection and Hidden Knowledge"
}
,{
    "Aries": "Direct and Quick-thinking",
    "Taurus": "Practical and Stable",
    "Gemini": "Witty and Versatile",
    "Cancer": "Emotional and Intuitive",
    "Leo": "Charismatic and Creative",
    "Virgo": "Analytical and Detail-oriented",
    "Libra": "Diplomatic and Fair-minded",
    "Scorpio": "Intense and Investigative",
    "Sagittarius": "Philosophical and Optimistic",
    "Capricorn": "Pragmatic and Methodical",
    "Aquarius": "Inventive and Original",
    "Pisces": "Imaginative and Dreamy"
}
,
    {
    "Ashwini": "Quick-thinking and Innovative",
    "Bharani": "Creative and Versatile",
    "Krittika": "Analytical and Determined",
    "Rohini": "Nurturing and Artistic",
    "Mrigashira": "Curious and Communicative",
    "Ardra": "Intense and Perceptive",
    "Punarvasu": "Optimistic and Adaptive",
    "Pushya": "Supportive and Wise",
    "Ashlesha": "Intuitive and Analytical",
    "Magha": "Authoritative and Charismatic",
    "Purva Phalguni": "Creative and Expressive",
    "Uttara Phalguni": "Stable and Rational",
    "Hasta": "Skillful and Resourceful",
    "Chitra": "Artistic and Perceptive",
    "Swati": "Diplomatic and Balanced",
    "Vishakha": "Goal-oriented and Persuasive",
    "Anuradha": "Loyal and Supportive",
    "Jyeshtha": "Intelligent and Resourceful",
    "Mula": "Investigative and Intense",
    "Purva Ashadha": "Confident and Charismatic",
    "Uttara Ashadha": "Pragmatic and Responsible",
    "Shravana": "Knowledgeable and Observant",
    "Dhanishta": "Energetic and Prosperous",
    "Shatabhisha": "Mystical and Analytical",
    "Purva Bhadrapada": "Transformative and Philosophical",
    "Uttara Bhadrapada": "Spiritual and Compassionate",
    "Revati": "Imaginative and Caring"
}

    ],
    "Venus" : [{
    1: "Charm and Beauty",
    2: "Material Wealth and Values",
    3: "Artistic Communication",
    4: "Harmony and Comfort in Home",
    5: "Romance and Creativity",
    6: "Service and Relationships",
    7: "Partnerships and Love",
    8: "Transformation through Relationships",
    9: "Philosophy and Travel",
    10: "Career in Arts and Diplomacy",
    11: "Friendships and Social Harmony",
    12: "Spiritual Love and Isolation"
}
,{
    "Aries": "Passionate and Independent",
    "Taurus": "Sensual and Loyal",
    "Gemini": "Playful and Social",
    "Cancer": "Caring and Nurturing",
    "Leo": "Romantic and Generous",
    "Virgo": "Practical and Discerning",
    "Libra": "Charming and Diplomatic",
    "Scorpio": "Intense and Deeply Affectionate",
    "Sagittarius": "Adventurous and Open-minded",
    "Capricorn": "Responsible and Committed",
    "Aquarius": "Unique and Unconventional",
    "Pisces": "Dreamy and Romantic"
},{
    "Ashwini": "Dynamic and Charming",
    "Bharani": "Passionate and Sensual",
    "Krittika": "Nurturing and Generous",
    "Rohini": "Creative and Loving",
    "Mrigashira": "Curious and Playful",
    "Ardra": "Intense and Passionate",
    "Punarvasu": "Optimistic and Restorative",
    "Pushya": "Supportive and Caring",
    "Ashlesha": "Deeply Emotional and Intuitive",
    "Magha": "Regal and Charismatic",
    "Purva Phalguni": "Romantic and Generous",
    "Uttara Phalguni": "Stable and Loyal",
    "Hasta": "Skillful and Practical",
    "Chitra": "Artistic and Aesthetic",
    "Swati": "Balanced and Diplomatic",
    "Vishakha": "Goal-oriented and Social",
    "Anuradha": "Loyal and Supportive",
    "Jyeshtha": "Protective and Intuitive",
    "Mula": "Intense and Mysterious",
    "Purva Ashadha": "Bold and Victorious",
    "Uttara Ashadha": "Responsible and Ambitious",
    "Shravana": "Knowledgeable and Compassionate",
    "Dhanishta": "Energetic and Prosperous",
    "Shatabhisha": "Mystical and Healing",
    "Purva Bhadrapada": "Philosophical and Transformative",
    "Uttara Bhadrapada": "Spiritual and Compassionate",
    "Revati": "Caring and Imaginative"
}

    
    ],
    "Jupiter" : [{
    1: "Optimism and Growth",
    2: "Wealth and Values",
    3: "Wisdom and Communication",
    4: "Emotional Security and Nurturing",
    5: "Creativity and Children",
    6: "Service and Improvement",
    7: "Abundance in Partnerships",
    8: "Transformation and Spiritual Depth",
    9: "Higher Learning and Travel",
    10: "Career Success and Recognition",
    11: "Friendships and Aspirations",
    12: "Spirituality and Hidden Wisdom"
}
,{
    "Aries": "Courageous and Enthusiastic",
    "Taurus": "Grounded and Abundant",
    "Gemini": "Curious and Communicative",
    "Cancer": "Nurturing and Protective",
    "Leo": "Generous and Creative",
    "Virgo": "Analytical and Practical",
    "Libra": "Social and Harmonious",
    "Scorpio": "Transformative and Intense",
    "Sagittarius": "Adventurous and Philosophical",
    "Capricorn": "Disciplined and Ambitious",
    "Aquarius": "Innovative and Humanitarian",
    "Pisces": "Spiritual and Compassionate"
}
,
    {
    "Ashwini": "Energetic and Optimistic",
    "Bharani": "Transformative and Generous",
    "Krittika": "Nurturing and Wise",
    "Rohini": "Creative and Abundant",
    "Mrigashira": "Curious and Knowledge-seeking",
    "Ardra": "Intense and Passionate",
    "Punarvasu": "Hopeful and Restorative",
    "Pushya": "Supportive and Nurturing",
    "Ashlesha": "Deep and Intuitive",
    "Magha": "Regal and Authoritative",
    "Purva Phalguni": "Romantic and Charismatic",
    "Uttara Phalguni": "Stable and Generous",
    "Hasta": "Resourceful and Skillful",
    "Chitra": "Artistic and Expansive",
    "Swati": "Balanced and Innovative",
    "Vishakha": "Goal-oriented and Enthusiastic",
    "Anuradha": "Loyal and Supportive",
    "Jyeshtha": "Protective and Wise",
    "Mula": "Transformative and Intense",
    "Purva Ashadha": "Victorious and Optimistic",
    "Uttara Ashadha": "Responsible and Ambitious",
    "Shravana": "Knowledgeable and Spiritual",
    "Dhanishta": "Energetic and Wealthy",
    "Shatabhisha": "Healing and Mystical",
    "Purva Bhadrapada": "Transformative and Philosophical",
    "Uttara Bhadrapada": "Spiritual and Compassionate",
    "Revati": "Imaginative and Gentle"
}

    ],
    "Saturn" : [{
    1: "Discipline and Responsibility",
    2: "Financial Stability and Values",
    3: "Caution in Communication",
    4: "Emotional Security through Structure",
    5: "Seriousness in Creativity",
    6: "Hard Work and Service",
    7: "Commitment and Challenges in Partnerships",
    8: "Depth and Transformation",
    9: "Wisdom through Experience",
    10: "Career Ambition and Recognition",
    11: "Social Responsibility and Friendships",
    12: "Isolation and Spiritual Lessons"
}
,{
    "Aries": "Disciplined and Assertive",
    "Taurus": "Patient and Practical",
    "Gemini": "Cautious and Thoughtful",
    "Cancer": "Protective and Structured",
    "Leo": "Authoritative and Serious",
    "Virgo": "Detail-oriented and Responsible",
    "Libra": "Balanced and Just",
    "Scorpio": "Intense and Transformative",
    "Sagittarius": "Philosophical and Responsible",
    "Capricorn": "Ambitious and Hardworking",
    "Aquarius": "Innovative and Detached",
    "Pisces": "Spiritual and Sacrificial"
}
,
   {
    "Ashwini": "Disciplined and Energetic",
    "Bharani": "Transformative and Serious",
    "Krittika": "Responsible and Strong-willed",
    "Rohini": "Stable and Nurturing",
    "Mrigashira": "Analytical and Curious",
    "Ardra": "Intense and Disciplined",
    "Punarvasu": "Restorative and Optimistic",
    "Pushya": "Supportive and Grounded",
    "Ashlesha": "Intense and Perceptive",
    "Magha": "Authoritative and Strong",
    "Purva Phalguni": "Romantic and Creative",
    "Uttara Phalguni": "Responsible and Stable",
    "Hasta": "Skillful and Practical",
    "Chitra": "Ambitious and Creative",
    "Swati": "Balanced and Diplomatic",
    "Vishakha": "Goal-oriented and Driven",
    "Anuradha": "Loyal and Committed",
    "Jyeshtha": "Protective and Intense",
    "Mula": "Transformative and Intense",
    "Purva Ashadha": "Confident and Victorious",
    "Uttara Ashadha": "Responsible and Hardworking",
    "Shravana": "Knowledgeable and Wise",
    "Dhanishta": "Energetic and Prosperous",
    "Shatabhisha": "Healing and Strong-willed",
    "Purva Bhadrapada": "Philosophical and Transformative",
    "Uttara Bhadrapada": "Compassionate and Spiritual",
    "Revati": "Gentle and Caring"
}

    ],
    "Rahu" : [{
    1: "Desire for Identity and Recognition",
    2: "Materialism and Values",
    3: "Innovative Communication",
    4: "Emotional Intensity and Family Focus",
    5: "Unconventional Creativity",
    6: "Service through Innovation",
    7: "Unconventional Partnerships",
    8: "Transformation and Obsession",
    9: "Quest for Knowledge",
    10: "Ambitious Career",
    11: "Social Aspirations and Uniqueness",
    12: "Spiritual Mystique and Isolation"
}
,{
    "Aries": "Ambitious and Driven",
    "Taurus": "Materialistic and Sensual",
    "Gemini": "Curious and Innovative",
    "Cancer": "Protective and Emotionally Intense",
    "Leo": "Attention-seeking and Creative",
    "Virgo": "Detail-oriented and Analytical",
    "Libra": "Relationship-focused and Social",
    "Scorpio": "Transformative and Intense",
    "Sagittarius": "Adventurous and Optimistic",
    "Capricorn": "Ambitious and Career-focused",
    "Aquarius": "Unconventional and Forward-thinking",
    "Pisces": "Spiritual and Mystical"
}
,
    {
    "Ashwini": "Ambitious and Driven",
    "Bharani": "Transformative and Intense",
    "Krittika": "Strong and Determined",
    "Rohini": "Creative and Sensual",
    "Mrigashira": "Innovative and Curious",
    "Ardra": "Passionate and Intense",
    "Punarvasu": "Hopeful and Restorative",
    "Pushya": "Supportive and Protective",
    "Ashlesha": "Mysterious and Intuitive",
    "Magha": "Regal and Authoritative",
    "Purva Phalguni": "Romantic and Charismatic",
    "Uttara Phalguni": "Stable and Generous",
    "Hasta": "Resourceful and Skilled",
    "Chitra": "Artistic and Ambitious",
    "Swati": "Independent and Balanced",
    "Vishakha": "Goal-oriented and Motivated",
    "Anuradha": "Loyal and Supportive",
    "Jyeshtha": "Protective and Intense",
    "Mula": "Transformative and Deep",
    "Purva Ashadha": "Confident and Victorious",
    "Uttara Ashadha": "Ambitious and Responsible",
    "Shravana": "Knowledgeable and Spiritual",
    "Dhanishta": "Energetic and Wealthy",
    "Shatabhisha": "Mystical and Healing",
    "Purva Bhadrapada": "Transformative and Philosophical",
    "Uttara Bhadrapada": "Spiritual and Wise",
    "Revati": "Imaginative and Gentle"
}

    ],
    "Ketu" : [{
    1: "Detachment from Identity",
    2: "Letting Go of Material Values",
    3: "Spiritual Communication",
    4: "Emotional Isolation",
    5: "Spiritual Creativity",
    6: "Service without Attachment",
    7: "Karmic Relationships",
    8: "Mystical Transformation",
    9: "Spiritual Wisdom",
    10: "Career in Spiritual Fields",
    11: "Detached Friendships",
    12: "Deep Spiritual Insights"
}
,{
    "Aries": "Detachment and Independence",
    "Taurus": "Letting Go of Materialism",
    "Gemini": "Introspection and Communication",
    "Cancer": "Emotional Depth and Withdrawal",
    "Leo": "Letting Go of Ego",
    "Virgo": "Critical and Analyzing",
    "Libra": "Detachment from Relationships",
    "Scorpio": "Mystical and Transformative",
    "Sagittarius": "Spiritual Quest and Freedom",
    "Capricorn": "Focus on Inner Growth",
    "Aquarius": "Detachment and Humanitarianism",
    "Pisces": "Intuitive and Dreamy"
},
{
    "Ashwini": "Independent and Detached",
    "Bharani": "Transformative and Introspective",
    "Krittika": "Self-disciplined and Strong",
    "Rohini": "Sensual and Grounded",
    "Mrigashira": "Curious and Detached",
    "Ardra": "Introspective and Intense",
    "Punarvasu": "Restorative and Reflective",
    "Pushya": "Supportive and Nurturing",
    "Ashlesha": "Deeply Intuitive and Mysterious",
    "Magha": "Regal and Detached",
    "Purva Phalguni": "Romantic and Reflective",
    "Uttara Phalguni": "Stable and Responsible",
    "Hasta": "Resourceful and Practical",
    "Chitra": "Artistic and Reflective",
    "Swati": "Balanced and Detached",
    "Vishakha": "Goal-oriented and Introspective",
    "Anuradha": "Loyal and Reflective",
    "Jyeshtha": "Protective and Self-aware",
    "Mula": "Intense and Transformational",
    "Purva Ashadha": "Confident and Philosophical",
    "Uttara Ashadha": "Ambitious and Responsible",
    "Shravana": "Knowledgeable and Reflective",
    "Dhanishta": "Energetic and Detached",
    "Shatabhisha": "Mystical and Introspective",
    "Purva Bhadrapada": "Philosophical and Transformative",
    "Uttara Bhadrapada": "Spiritual and Introspective",
    "Revati": "Gentle and Compassionate"
}

    ],
} 


nakshatraColor = {
  "Ashwini": ["Red", "Orange", "Yellow"],
  "Bharani": ["White", "Pink", "Blue"],
  "Krittika": ["Red", "Pink", "White"],
  "Rohini": ["Red", "Pink", "Green"],
  "Mrigashira": ["White", "Yellow", "Pink"],
  "Aridra": ["Blue", "Green", "Silver"],
  "Punarvasu": ["White", "Green", "Yellow"],
  "Pushya": ["White", "Yellow", "Gold"],
  "Ashlesha": ["Silver", "White", "Red"],
  "Magha": ["Gold", "Yellow", "Red"],
  "Purva Phalguni": ["Red", "Orange", "Pink"],
  "Uttara Phalguni": ["Orange", "Yellow", "Red"],
  "Hasta": ["White", "Yellow", "Pink"],
  "Chitra": ["Red", "Yellow", "Orange"],
  "Swati": ["White", "Light Blue", "Green"],
  "Vishakha": ["Red", "Yellow", "Green"],
  "Anuradha": ["White", "Red", "Pink"],
  "Jyeshtha": ["Silver", "Blue", "Green"],
  "Mula": ["Red", "Black", "Brown"],
  "Purva Ashadha": ["Yellow", "Red", "Pink"],
  "Uttara Ashadha": ["Golden", "Red", "Yellow"],
  "Shravana": ["White", "Green", "Yellow"],
  "Dhanishta": ["Gold", "White", "Pink"],
  "Shatabhisha": ["Blue", "Green", "Black"],
  "Purva Bhadrapada": ["Purple", "Red", "Yellow"],
  "Uttara Bhadrapada": ["Yellow", "White", "Red"],
  "Revati": ["White", "Green", "Pink"]
}

nakshatraNumber = {
  "Ashwini": [1, 9],
  "Bharani": [2, 6],
  "Krittika": [3, 5],
  "Rohini": [2, 7],
  "Mrigashira": [1, 3],
  "Aridra": [5, 8],
  "Punarvasu": [3, 6],
  "Pushya": [4, 9],
  "Ashlesha": [8, 7],
  "Magha": [1, 4],
  "Purva Phalguni": [3, 6],
  "Uttara Phalguni": [2, 9],
  "Hasta": [5, 8],
  "Chitra": [3, 6],
  "Swati": [6, 9],
  "Vishakha": [1, 3],
  "Anuradha": [2, 6],
  "Jyeshtha": [4, 7],
  "Mula": [9, 5],
  "Purva Ashadha": [3, 7],
  "Uttara Ashadha": [4, 8],
  "Shravana": [2, 5],
  "Dhanishta": [1, 6],
  "Shatabhisha": [3, 8],
  "Purva Bhadrapada": [1, 4],
  "Uttara Bhadrapada": [2, 7],
  "Revati": [3, 9]
}


thithiLord = {
  "Pratipada": "Agni (Fire God)",
  "Ditiya": "Brahma (Creator God)",
  "Tritiya": "Gauri (Goddess of Harmony)",
  "Chaturthi": "Ganapati (Remover of Obstacles)",
  "Panchami": "Saraswati (Goddess of Knowledge)",
  "Shashthi": "Kartikeya (God of War and Victory)",
  "Saptami": "Surya (Sun God)",
  "Ashtami": "Rudra (Form of Shiva)",
  "Navami": "Durga (Goddess of Power)",
  "Dashami": "Yama (God of Discipline)",
  "Ekadashi": "Vishnu (Preserver of the Universe)",
  "Dwadashi": "Aditi (Mother of the Gods)",
  "Trayodashi": "Kamadeva (God of Love and Desire)",
  "Chaturdashi": "Shiva (Destroyer of Negativity)",
  "Purnima": "Chandra (Moon God)",
  "Amavasya": "Pitra (Ancestors)"
}

thithiContent = {
    "Pratipada": [ 
        [
        "Energetic and enthusiastic",
        "Strong leadership qualities",
        "Innovative and creative thinking"
      ], [
        "Impulsiveness and restlessness",
        "Difficulty handling criticism",
        "Prone to overreaction in stressful situations"
      ], {
        "Name": "Fire Focus Exercise",
        "Description": "Channel their energy through physical activities.",
        "Execution": "Enroll them in martial arts or dance classes to help them discipline their energy. Introduce daily journaling for emotional reflection."
      }
    ],
    "Ditiya": [[
        "Curious and eager to learn",
        "Good at building relationships",
        "Balanced and thoughtful in decision-making"
      ],[
        "Overthinking tendencies",
        "Can be overly dependent on others",
        "Hesitant to take risks"
      ], {
        "Name": "Daily Curiosity Hour",
        "Description": "Encourage curiosity with fun educational activities.",
        "Execution": "Set aside an hour daily for puzzles, storytelling, or experiments to enhance learning and decision-making skills."
      }
],
    "Tritiya": [ [
        "Charming and sociable",
        "Naturally peaceful and harmonious",
        "Strong aesthetic sense"
      ],
       [
        "Avoids conflict at all costs",
        "Struggles with assertiveness",
        "Suppresses emotions"
      ],
      {
        "Name": "Conflict Resolution Roleplay",
        "Description": "Teach healthy communication and assertiveness.",
        "Execution": "Use role-playing to practice standing up for themselves and expressing emotions constructively."
      }
],
    "Chaturthi": [ [
        "Strong problem-solving abilities",
        "Resilient and determined",
        "Optimistic outlook"
      ],
       [
        "Can be stubborn and inflexible",
        "Overly focused on details",
        "Prone to frustration with delays"
      ],
      {
        "Name": "Obstacle Course Game",
        "Description": "Promote patience and flexibility.",
        "Execution": "Set up an obstacle course at home that includes unexpected challenges to teach patience and adaptability."
      }
],
    "Panchami": [[
        "Highly intelligent and creative",
        "Loves learning and exploring new ideas",
        "Artistic and musical talents"
      ],
       [
        "Overwhelmed by expectations",
        "Tendency to withdraw when criticized",
        "Struggles with perfectionism"
      ],
      {
        "Name": "Creative Expression Hour",
        "Description": "Provide a space for artistic expression.",
        "Execution": "Encourage activities like painting, music, or writing, focusing on the process rather than results."
      }
],
    "Shashthi": [ [
        "Bold and adventurous",
        "Strong leadership qualities",
        "Confident in challenges"
      ],
       [
        "Overly competitive",
        "Impulsive decisions",
        "May struggle with teamwork"
      ],
      {
        "Name": "Teamwork Building Games",
        "Description": "Foster cooperation through group activities.",
        "Execution": "Organize family board games or team sports to emphasize collaboration."
      }
],
    "Saptami": [ [
        "Radiant and charismatic",
        "Natural leadership abilities",
        "Optimistic and inspiring"
      ],
       [
        "Egoistic or overconfident tendencies",
        "Struggles to accept failure",
        "Prone to dominating others"
      ],
      {
        "Name": "Leadership Sharing Activities",
        "Description": "Teach humility and collaborative leadership.",
        "Execution": "Rotate leadership roles in group activities, stressing teamwork and listening."
      }
],
    "Ashtami": [[
        "Emotionally resilient",
        "Strong problem-solving skills",
        "Determined and fearless"
      ],
       [
        "Prone to anger and intense emotions",
        "Can be secretive",
        "May resist authority"
      ],
      {
        "Name": "Emotional Expression Journal",
        "Description": "Help your child process emotions constructively.",
        "Execution": "Encourage daily journaling with writing or drawing to manage intense feelings."
      }
],
    "Navami": [ [
        "Strong-willed and courageous",
        "Great at handling challenges",
        "Highly protective of loved ones"
      ],
       [
        "Can be overly defensive",
        "May struggle with controlling anger",
        "Prone to burnout due to high expectations"
      ],
       {
        "Name": "Stress Release Techniques",
        "Description": "Teach healthy ways to handle stress and anger.",
        "Execution": "Introduce breathing exercises or nature walks to help them decompress and build emotional resilience."
      }
],
    "Dashami": [ [
        "Disciplined and goal-oriented",
        "Fair and just in decision-making",
        "Highly responsible and reliable"
      ],
       [
        "Can be overly rigid",
        "Struggles to adapt to changes",
        "Prone to self-imposed pressure"
      ],
       {
        "Name": "Flexible Thinking Challenges",
        "Description": "Encourage adaptability through creative problem-solving.",
        "Execution": "Use activities like 'What if' scenarios to help them think flexibly and embrace change."
      }
],
    "Ekadashi": [ [
        "Spiritually inclined and introspective",
        "Focused and determined",
        "Generous and kind-hearted"
      ],
       [
        "May isolate themselves during stress",
        "Prone to perfectionism",
        "Can be overly idealistic"
      ],
       {
        "Name": "Mindful Listening Sessions",
        "Description": "Help your child process emotions and stay grounded.",
        "Execution": "Spend dedicated time listening to your child's thoughts and guiding them through their concerns without judgment."
      }
],
    "Dwadashi": [ [
        "Generous and nurturing",
        "Strong family-oriented values",
        "Highly optimistic and hopeful"
      ],
       [
        "Prone to over-giving and neglecting self",
        "Difficulty setting boundaries",
        "May struggle with dependency on others' approval"
      ],
       {
        "Name": "Self-Care Time",
        "Description": "Teach your child the importance of self-care.",
        "Execution": "Encourage activities like reading or hobbies that they can enjoy independently, reinforcing the value of personal space."
      }
],
    "Trayodashi": [ [
        "Charming and affectionate",
        "Highly creative and artistic",
        "Emotionally intelligent and understanding"
      ],
       [
        "Can be overly sensitive to rejection",
        "Prone to mood swings",
        "May struggle with focusing on long-term goals"
      ],
       {
        "Name": "Emotion Mapping Game",
        "Description": "Help your child identify and manage emotions.",
        "Execution": "Create a fun chart with emotions and teach them to label what they feel during different situations to promote self-awareness."
      }
],
    "Chaturdashi": [[
        "Highly intuitive and insightful",
        "Strong inner strength and determination",
        "Great at finding solutions under pressure"
      ],
       [
        "Prone to emotional intensity",
        "May have difficulty trusting others",
        "Can become reclusive during stress"
      ],
       {
        "Name": "Trust-Building Activities",
        "Description": "Encourage openness and build trust.",
        "Execution": "Engage in shared activities like gardening or cooking, fostering open conversations and mutual understanding."
      }
],
    "Purnima": [ [
        "Highly intuitive and empathetic",
        "Balances logic and emotion well",
        "Inspires others with emotional intelligence"
      ],
       [
        "Overly sensitive to criticism",
        "Prone to emotional highs and lows",
        "Easily distracted by external influences"
      ],
       {
        "Name": "Moon Meditation Ritual",
        "Description": "Cultivate emotional balance through calming practices.",
        "Execution": "On full moon nights, guide your child in meditation or breathing exercises to calm their emotions."
      }
],
    "Amavasya": [ [
        "Deeply introspective and wise",
        "Strong intuitive abilities",
        "Empathetic and compassionate"
      ],
       [
        "Prone to overthinking and worry",
        "May experience emotional lows",
        "Sensitive to negative energy around them"
      ],
       {
        "Name": "Gratitude Reflection Practice",
        "Description": "Foster positivity and emotional wellness.",
        "Execution": "Encourage writing or discussing three daily gratitudes to promote a positive mindset."
      }
]
}

KaranaLord =  {
  "Bava": "Vishnu",
  "Balava": "Brahma",
  "Kaulava": "Shakti (Durga)",
  "Taitila": "Indra",
  "Garaja": "Nandi",
  "Vanija": "Kubera",
  "Vishti": "Yama",
  "Shakuni": "Shakuni (Mystic)",
  "Chatushpada": "Rudra (Shiva)",
  "Nagava": "Nagava Devata (Serpent God)",
  "Kinstughna": "Vishnu"
}

karanamContent =  {
  "Bava": [[
        "Quick to start tasks with enthusiasm.",
        "Creative and innovative approach to problem-solving.",
        "Can motivate others and lead group activities."
      ],
    [
        "May lack focus and jump from one task to another.",
        "Tendency to lose interest quickly and abandon tasks.",
        "Can be impulsive and not think things through before acting."
      ],
       {
        "Tip": "Create a structured schedule with clear goals.",
        "Execution": "Break down big tasks into smaller, manageable steps with a clear timeline. Praise their progress to encourage them to stay focused and complete tasks."
      }
],
  "Balava": [[
        "Energetic and enthusiastic in completing tasks.",
        "Able to multitask and handle several things at once.",
        "Very adaptable to different situations and changes."
      ],
    [
        "May struggle with focusing on a single task for long.",
        "Can become easily distracted and forgetful.",
        "Tends to rush through tasks, impacting quality."
      ],
       {
        "Tip": "Set designated focus times with breaks.",
        "Execution": "Create a timer-based approach where they work on one task for a set period and then take short breaks. This helps improve focus and productivity."
      }
],
  "Kaulava": [ [
        "Diligent and consistent in task completion.",
        "Well-organized and tends to follow routines.",
        "Takes time to plan and ensure accuracy in work."
      ],
    [
        "May become overly cautious and hesitant to take risks.",
        "Can be resistant to change and new approaches.",
        "Might overthink and delay task completion."
      ],
       {
        "Tip": "Introduce gradual change and new activities.",
        "Execution": "Help them practice flexibility by gently encouraging them to try new methods or activities with reassurance."
      }
],
  "Taitila": [ [
        "Methodical and practical in approaching tasks.",
        "Strong attention to detail and precision.",
        "Reliable and consistent in their work."
      ],
    [
        "May become perfectionist, leading to frustration.",
        "Tends to avoid tasks if they feel they won't be perfect.",
        "Can be slow to adapt to unexpected changes."
      ],
       {
        "Tip": "Encourage a balance between effort and relaxation.",
        "Execution": "Praise their hard work but reassure them that making mistakes is part of learning. Offer positive reinforcement when they try new things without expecting perfection."
      }
],
  "Garaja": [ [
        "Independent and self-reliant.",
        "Able to handle tasks without constant supervision.",
        "Can focus and remain determined to finish tasks."
      ],
    [
        "May become stubborn and resist help.",
        "Can struggle with expressing emotions or asking for help.",
        "Might avoid tasks that they feel are too difficult."
      ],
       {
        "Tip": "Promote open communication and encourage teamwork.",
        "Execution": "Encourage them to express their needs and feelings. Let them know it's okay to ask for help, and praise collaborative efforts."
      }
],
  "Vanija": [ [
        "Creative and resourceful.",
        "Able to think outside the box to solve problems.",
        "Strong ability to manage tasks effectively."
      ],
    [
        "Can become distracted by new ideas and abandon projects.",
        "May find it difficult to stick to routines or fixed plans.",
        "Can become overly involved in side projects at the cost of main tasks."
      ],
       {
        "Tip": "Help them prioritize their tasks and ideas.",
        "Execution": "Create a priority list for their tasks and set clear goals for each. Help them focus on one thing at a time while encouraging their creativity."
      }
],
  "Vishti": [ [
        "Hardworking and diligent in completing tasks.",
        "Persistent in achieving long-term goals.",
        "Takes pride in their work and accomplishments."
      ],
    [
        "Can become stubborn and refuse to change their methods.",
        "May struggle with adapting to sudden changes.",
        "Can become overwhelmed by taking on too much responsibility."
      ],
       {
        "Tip": "Teach flexibility and the importance of rest.",
        "Execution": "Encourage them to try new methods and take breaks when necessary. Remind them that flexibility is important for growth and managing stress."
      }
],
  "Shakuni": [[
        "Strategic thinker and planner.",
        "Able to foresee potential challenges and plan accordingly.",
        "Focused on achieving set goals with efficiency."
      ],
    [
        "Can become overly calculative and detached emotionally.",
        "Might avoid social interactions to focus on tasks.",
        "Can be prone to manipulation or taking shortcuts."
      ],
       {
        "Tip": "Encourage social interactions and emotional awareness.",
        "Execution": "Foster their emotional intelligence by encouraging teamwork and group activities. Teach them to value relationships alongside strategic planning."
      }
],
  "Chatushpada": [[
        "Creative and independent thinker.",
        "Can easily adapt to changing circumstances.",
        "Strong ability to handle multiple tasks simultaneously."
      ],
      [
        "Can become erratic and unpredictable in their actions.",
        "May struggle with commitment to long-term projects.",
        "Might avoid responsibility and opt for shortcuts."
      ],
      {
        "Tip": "Help them build consistency and commitment.",
        "Execution": "Encourage them to stay committed to one task at a time and celebrate the completion of small milestones. Use consistency as a reward mechanism."
      }
],
  "Nagava": [ [
        "Good at handling complex tasks.",
        "Strong sense of responsibility and commitment.",
        "Deeply focused on achieving set objectives."
      ],
    [
        "Can be secretive and reluctant to share thoughts.",
        "May become overly serious and rigid in approach.",
        "Might neglect their emotional or social needs while pursuing goals."
      ],
       {
        "Tip": "Foster open communication and emotional expression.",
        "Execution": "Encourage them to open up about their feelings and balance their work with social activities. Help them understand the importance of emotional well-being."
      }
],
  "Kinstughna": [ [
        "Highly energetic and motivated to complete tasks.",
        "Quick to act on new ideas and challenges.",
        "Has a natural ability to inspire others to join efforts."
      ],
    [
        "Can become impulsive and make rash decisions.",
        "Tends to be restless and may not complete tasks properly.",
        "May struggle with patience and attention to detail."
      ],
       {
        "Tip": "Encourage calm and thoughtful decision-making.",
        "Execution": "Teach them to pause and think before acting, especially in important decisions. Implement decision-making steps that involve thinking through pros and cons."
      }
]
}

yogamLord = {
  "1": "Shiva",
  "2": "Vishnu",
  "3": "Chandra (Moon)",
  "4": "Lakshmi",
  "5": "Parvati",
  "6": "Rudra (Shiva)",
  "7": "Indra",
  "8": "Yama",
  "9": "Durga",
  "10": "Vayu",
  "11": "Vishwadeva",
  "12": "Dhruva (Pole Star)",
  "13": "Kali (Chandi)",
  "14": "Gauri (Parvati)",
  "15": "Indra",
  "16": "Ganesha",
  "17": "Shiva",
  "18": "Lakshmi",
  "19": "Vishnu",
  "20": "Shiva",
  "21": "Ganesha",
  "22": "Brahma",
  "23": "Lakshmi",
  "24": "Vishnu",
  "25": "Brahma",
  "26": "Indra",
  "27": "Yama"
}

weekPlanet = {
    "Sunday": "Sun",
    "Monday": "Moon",
    "Tuesday": "Mars",
    "Wednesday": "Mercury",
    "Thursday": "Jupiter",
    "Friday": "Venus",
    "Saturday": "Saturn"
}

weekPlanetContent = {
    "Sunday" : [ [
        "Leadership qualities and confidence",
        "High energy and vitality",
        "Strong willpower and determination"
      ],
    [
        "Can be overly dominant or stubborn",
        "Tendency to be self-centered or arrogant",
        "May face challenges with authority or teamwork"
      ],
    {
        "Tip": "Encourage healthy leadership by giving them small responsibilities and tasks they can lead.",
        "Execution": "Provide opportunities where your child can take charge, such as leading a group activity or planning family events. Praise their efforts to build confidence while teaching them to listen to others."
      }
],
    "Monday" : [[
        "Emotional sensitivity and empathy",
        "Strong nurturing and caring nature",
        "Good intuition and creativity"
      ],
    [
        "Prone to mood swings or emotional vulnerability",
        "Can be overly dependent or shy",
        "May struggle with decision-making due to sensitivity"
      ],
    {
        "Tip": "Create a calm and nurturing environment that allows them to express their emotions freely.",
        "Execution": "Spend quiet time with them, use stories or art to help them express feelings, and ensure they feel safe and supported. Offer reassurance and practice calming activities like deep breathing."
      }
],
    "Tuesday" : [ [
        "High energy, motivation, and enthusiasm",
        "Strong will and determination",
        "Bold, confident, and courageous nature"
      ],
    [
        "Can be impulsive or aggressive",


        "May have a quick temper",
        "Struggles with patience and can be headstrong"
      ],
    {
        "Tip": "Channel their energy into physical activities that build discipline.",
        "Execution": "Enroll them in sports or activities that require teamwork and controlled energy, such as martial arts or group games. Praise their progress and teach them techniques to manage frustration."
      }
],
    "Wednesday" : [ [
        "Sharp intellect and quick learning",
        "Excellent communication and language skills",
        "Adaptable and curious nature"
      ],
    [
        "Prone to overthinking or nervousness",
        "Can be inconsistent or distracted",
        "May have trouble focusing on one task at a time"
      ],
    {
        "Tip": "Encourage structured learning and creative play that taps into their curiosity.",
        "Execution": "Introduce puzzles, science kits, or activities that require them to use logic and creativity. Use visual schedules to help them stay on task, and praise their achievements."
      }
],
    "Thursday" : [ [
        "Positive and optimistic outlook",
        "Strong sense of fairness and generosity",
        "Great potential for wisdom and deep thinking"
      ],
    [
        "Can be overly idealistic or overconfident",
        "May struggle with practicality",
        "Tendency to be complacent or lazy at times"
      ],
    {
        "Tip": "Promote balanced growth through activities that encourage both exploration and practical tasks.",
        "Execution": "Incorporate activities that combine fun with learning, like educational games or group projects. Remind them to set achievable goals and celebrate their small successes."
      }
],
    "Friday" : [ [
        "Creative, artistic, and imaginative",
        "Social and affectionate nature",
        "Strong sense of beauty and harmony"
      ],
    [
        "Can be overly sensitive or overly concerned with appearance",
        "May seek validation and be influenced by others",
        "Can be indecisive or prone to procrastination"
      ],
    {
        "Tip": "Foster their creativity with art and music while building self-confidence.",
        "Execution": "Provide opportunities for creative expression, such as drawing, playing an instrument, or dance. Reinforce their strengths and teach them to focus on their true self, not just external opinions."
      }
],
    "Saturday" : [ [
        "Responsible and disciplined",
        "Strong work ethic and perseverance",
        "Good at problem-solving and planning"
      ],
    [
        "Can be overly serious or pessimistic",
        "May have low self-esteem or be critical of themselves",
        "Struggles with flexibility or adapting to change"
      ],
    {
        "Tip": "Encourage balance by helping them manage stress and build confidence.",
        "Execution": "Introduce activities that mix routine with play, like structured but fun chores or projects. Recognize their hard work, and gently remind them that mistakes are part of learning."
      }
]
}


sunIdentity = {
  "Aries" : "child, born with Sun in Mesha (Aries) has a strong and confident core identity. Child is energetic, independent, and eager to take on new challenges. The desire to lead and start new things shapes child's sense of self. Child's personality is bold, and child is not afraid to act quickly. Child's natural courage and enthusiasm drive actions and decisions, making child a go-getter.",
  "Taurus": "child, born with Sun in Vrishabha (Taurus) has a steady and grounded core identity. Child values stability, comfort, and material security. Determination and persistence drive child to work hard for goals. Child's approach to life is patient and methodical, seeking lasting rewards. Child thrives on reliability, and emotional security forms the foundation of personal identity.",
  "Gemini": "child, born with Sun in Mithuna (Gemini) has an adaptable and curious core identity. Child is intellectually driven, always seeking knowledge and new experiences. Child's identity is shaped by communication and social interactions, making child versatile and quick-witted. Child's ability to connect with others and adapt to different environments defines core nature.",
  "Cancer": "child, born with Sun in Karka (Cancer) has a sensitive and nurturing core identity. Child's sense of self is closely tied to family and home life. Emotions guide child's decisions and actions, with a strong desire to care for others. Child's identity is rooted in deep emotional connections, loyalty, and the need to protect loved ones.",
  "Leo": "child, born with Sun in Simha (Leo) has a confident and vibrant core identity. Child craves attention, recognition, and creative self-expression. Child's identity is built on self-esteem, personal achievements, and the desire to inspire others. Child's natural leadership abilities shine through, and the spotlight fuels inner confidence.",
  "Virgo": "child, born with Sun in Kanya (Virgo) has a practical and analytical core identity. Child is focused on details and constantly strives for self-improvement. Child's identity is shaped by a strong sense of duty and desire to be of service. Child's self-worth comes from helping others and solving problems with precision.",
  "Libra": "child, born with Sun in Tula (Libra) has a balanced and harmonious core identity. Child values relationships, fairness, and beauty in life. A strong desire for harmony and peace shapes child's sense of self. Child's identity is formed through partnerships, and the need for social interaction and compromise guides decisions.",
  "Scorpio": "child, born with Sun in Vrischika (Scorpio) has a powerful and intense core identity. Child's identity is driven by passion, determination, and a deep need for transformation. Child is not afraid to confront challenges and explore the unknown. Emotional depth and resilience define child's sense of self and personal power.",
  "Sagittarius": "child, born with Sun in Dhanu (Sagittarius) has an adventurous and philosophical core identity. Child's sense of self is defined by a love for freedom, exploration, and knowledge. Optimism and a desire to expand horizons guide child's path. Child values truth and strives for growth, both intellectually and spiritually.",
  "Capricorn": "child, born with Sun in Makara (Capricorn) has a disciplined and ambitious core identity. Child's identity is shaped by a strong sense of responsibility and determination to succeed. Child values hard work and is focused on achieving long-term goals. Practicality and perseverance drive child's sense of self and personal growth.",
  "Aquarius": "child, born with Sun in Kumbha (Aquarius) has an independent and innovative core identity. Child's sense of self is shaped by a desire for individuality and a deep connection to humanity. Intellectual curiosity and a strong sense of social justice guide child's path. Child is driven by the need to bring change and new ideas to the world.",
  "Pisces": "child, born with Sun in Meena (Pisces) has a compassionate and imaginative core identity. Child's identity is deeply connected to emotions, dreams, and spirituality. Intuition and empathy define child's sense of self, and a desire to help others is a central part of child's nature. Artistic expression and a rich inner world are essential for child's personal fulfillment."
}


moonIdentity = {
    "Aries": "child's Rashi Sign is Mesham A Mesha Rashi (Aries Moon Sign) child is always energetic, quick to act, and emotionally expressive. Child experiences emotions intensely and reacts quickly to situations. Emotional nature is often spontaneous, leading to both excitement and frustration. Child has a strong desire for independence and can feel frustrated when restricted. However, child's enthusiasm helps overcome emotional challenges, bringing a positive and dynamic energy to daily life.",
    "Taurus": "child's Rashi Sign is Vrishabha Rashi (Taurus Moon Sign) child is always calm, stable, and emotionally grounded. Child values security and comfort, often seeking peace in familiar surroundings. Emotions are steady, and child is slow to anger, but when upset, emotions can linger for a while. Child has a strong attachment to loved ones and feels safe in nurturing relationships.",
    "Gemini": "child's Rashi Sign is Mithuna Rashi (Gemini Moon Sign) child is always curious, communicative, and emotionally versatile. Child's emotions are constantly changing, reflecting a need for mental stimulation. Child expresses feelings easily, but may quickly move on to other emotions. Child enjoys social interactions and feels emotionally energized through conversation and sharing ideas.",
    "Cancer": "child's Rashi Sign is Karka Rashi (Cancer Moon Sign) child is always sensitive, nurturing, and emotionally protective. Child's emotions are deep and influenced by family and home life. Intuitive and empathetic, child can sense the moods of others and is highly attuned to emotional needs. When upset, child seeks comfort in familiar surroundings and close relationships.",
    "Leo": "child's Rashi Sign is Simha Rashi (Leo Moon Sign) child is always confident, warm-hearted, and emotionally expressive. Child's emotions are strong, and child craves attention and appreciation. Child's emotional state is often tied to recognition and praise, feeling joyful when admired and hurt when ignored. Child's positive attitude and enthusiasm light up the environment.",
    "Virgo": "child's Rashi Sign is Kanya Rashi (Virgo Moon Sign) child is always practical, analytical, and emotionally reserved. Child's emotions are often controlled, and child seeks logical solutions to emotional challenges. Sensitivity is directed toward others' needs, with child tending to offer care and support. Child may feel anxious or worried when things are disorganized or uncertain.",
    "Libra": "child's Rashi Sign is Tula Rashi (Libra Moon Sign) child is always balanced, harmonious, and emotionally diplomatic. Child seeks fairness in all relationships and can be easily affected by conflict. Emotions are balanced, with child striving for peace and avoiding emotional confrontations. Child is happiest when surrounded by beauty and harmony.",
    "Scorpio": "child's Rashi Sign is Vrischika Rashi (Scorpio Moon Sign) child is always intense, passionate, and emotionally profound. Child experiences emotions deeply and may struggle to express them at times. Child's emotional world is private, but when feelings are shared, they are intense and transformative. Trust is essential for child to open up emotionally.",
    "Sagittarius": "child's Rashi Sign is Dhanu Rashi (Sagittarius Moon Sign) child is always optimistic, adventurous, and emotionally independent. Child's emotions are free-spirited and tend to be linked to a desire for exploration and new experiences. Emotional reactions are quick but not lasting, with child seeking freedom to express feelings openly and without restriction.",
    "Capricorn": "child's Rashi Sign is Makara Rashi (Capricorn Moon Sign) child is always disciplined, reserved, and emotionally strong. Child's emotions are steady, but child tends to hide vulnerabilities and may not easily express feelings. Child feels secure through structure and achievement and may become upset if personal goals are disrupted. Emotional stability is a key trait.",
    "Aquarius": "child's Rashi Sign is Kumbha Rashi (Aquarius Moon Sign) child is always intellectual, independent, and emotionally detached. Child's emotions are often influenced by logical thinking and the desire for individuality. Child may struggle with expressing emotions in conventional ways and seeks mental stimulation over emotional connection. Child values personal space and freedom.",
    "Pisces": "child's Rashi Sign is Meena Rashi (Pisces Moon Sign) child is always compassionate, dreamy, and emotionally sensitive. Child's emotions are deep and often clouded by imagination. Child can easily absorb the emotions of others, making them empathetic but also vulnerable. Sensitive nature leads to emotional fluctuations, with child often seeking comfort and retreat in solitude or creative expression."
}

lagnaIdentity = {
  "Aries": "child's Born Lagna is Mesha Lagna. child is always energetic, confident, and independent. Child has a natural ability to lead and take initiative. Strong drive helps child face challenges with courage. Child's enthusiasm and vitality inspire others to act. Adventurous spirit pushes child to explore new experiences and overcome obstacles.",
  "Taurus": "child's Born Lagna is Vrishabha Lagna. child is always calm, reliable, and practical. Child has a strong connection to stability and enjoys comfort. Persistent nature helps child achieve goals with patience and consistency. Child's love for beauty and harmony creates peace and balance in surroundings.",
  "Gemini": "child's Born Lagna is Mithuna Lagna. child is always curious, communicative, and adaptable. Child enjoys learning new things and has a natural ability to express ideas. Social and quick-thinking nature helps child connect easily with others. Versatility allows child to thrive in various situations.",
  "Cancer": "child's Born Lagna is Karka Lagna. child is always nurturing, sensitive, and protective. Child forms strong emotional bonds with family and friends. Intuitive nature helps child understand the feelings of others. Caring personality motivates child to protect and care for loved ones.",
  "Leo": "child's Born Lagna is Simha Lagna. child is always confident, creative, and charismatic. Child has natural leadership qualities and loves being in the spotlight. Courageous nature drives child to pursue big dreams and achieve greatness. Child's strong sense of self-worth and loyalty inspires others.",
  "Virgo": "child's Born Lagna is Kanya Lagna. child is always intelligent, detail-oriented, and organized. Child has a sharp mind and enjoys tasks that require critical thinking. Analytical nature helps child excel in planning and problem-solving. Child's practical approach makes them reliable and efficient.",
  "Libra": "child's Born Lagna is Tula Lagna. child is always charming, diplomatic, and fair-minded. Child values balance and seeks harmony in relationships. Ability to see all perspectives helps child mediate conflicts. Child's love for beauty and art brings creativity and aesthetics to life.",
  "Scorpio": "child's Born Lagna is Vrischika Lagna. child is always intense, passionate, and determined. Child has a deep curiosity about life and seeks to uncover hidden truths. Resilient nature helps child overcome obstacles and stay focused on goals. Powerful will enables child to achieve great success.",
  "Sagittarius": "child's Born Lagna is Dhanu Lagna. child is always optimistic, adventurous, and philosophical. Child has a strong desire for freedom and exploration. Enthusiastic nature drives child to seek new knowledge and experiences. Positive outlook and thirst for growth inspire those around them.",
  "Capricorn": "child's Born Lagna is Makara Lagna. child is always disciplined, responsible, and ambitious. Child has a strong sense of duty and works hard to achieve long-term goals. Persistent nature helps child overcome challenges. Practical approach and determination drive child toward success.",
  "Aquarius": "child's Born Lagna is Kumbha Lagna. child is always innovative, independent, and humanitarian. Child values individuality and enjoys exploring new ideas. Intellectual and open-minded nature drives child to bring about change. Child's desire to improve the world motivates them to act in unique ways.",
  "Pisces": "child's Born Lagna is Meena Lagna. child is always compassionate, imaginative, and intuitive. Child has a strong connection to emotions and a deep sense of empathy. Creative nature drives child to explore artistic or spiritual pursuits. Sensitive personality makes child understanding and caring toward others."
}

healthContent =  {
  "Aries" : [
      [
          "Headaches (due to excess heat and energy in the head region)",
          "Upper Respiratory Issues (e.g., sinus infections, throat irritation)",
          "Skin Problems (acne, rashes, inflammation)",
          "Ear Infections (frequent due to fiery nature)",
          "High Fever (prone to fevers, especially during infections)"
      ],
      [
          "Digestive Issues (irregular appetite, acid reflux)",
          "Inflammation (swollen joints, painful conditions)",
          "Weak Immunity (frequent cold, infections)",
          "Fatigue (due to overstimulation and lack of rest)"
      ],
      [
          "Fire (Pitta)",
          "Skin Burns (sensitive to extreme heat or sun exposure)",
          "Acid Reflux (heartburn, gastritis)",
          "Overheating (prone to hot flushes and dehydration)",
          "Inflammatory Conditions (joint pain, sore muscles)"
      ],
      {
          "natural" : [
              "Cooling Herbal Tea (Pitta Balancing)",
              "1 tsp of Chamomile, 1 tsp of Mint leaves, 1 tsp of Fennel seeds.",
              "Boil 1 cup of water, add all ingredients, and steep for 5 minutes. Drink once daily.",
              "Soothes inflammation, reduces digestive issues, balances excess heat."
          ],
          "mudra" : [
              "Prithvi Mudra (Earth Element Mudra)",
              [
                  "Sit in a comfortable position.",
                  "Touch the tip of your ring finger to the tip of your thumb.",
                  "Keep the other fingers straight and relaxed.",
                  "Hold for 5-10 minutes daily."
              ],
              "Balances fiery energy, reduces inflammation, and promotes calmness."
          ],
          "energy" : [
              "Reiki (Root and Solar Plexus Chakras)",
              [
                  "Sit or lie down in a relaxed position.",
                  "Focus on your child's root chakra (base of spine) and solar plexus (above the navel).",
                  "Place your hands over the areas and channel calming energy for 10-15 minutes."
              ],
              "Promotes grounding, relieves digestive discomfort, calms the body's fiery tendencies."
          ],
          "meditation": [
              "Grounding Meditation (for fire element balancing)",
              [
                  "Sit in a comfortable, upright position.",
                  "Close the eyes and focus on deep, slow breaths.",
                  "Visualize roots growing from the feet into the earth, drawing cool, grounding energy.",
                  "Continue for 10-15 minutes."
              ]
          ],
          "foods" : [
              [
                  "Coconut water (for hydration and cooling effect)",
                  "Cucumber (for reducing internal heat)",
                  "Aloe vera juice (to cool the digestive system)"
              ],
              [
                  "Spicy foods (can aggravate the fire element)",
                  "Fried and oily foods (can lead to inflammation and digestive issues)"
              ],
              [
                  "Drink 1 cup of coconut water daily, especially during hot weather.",
                  "Include fresh cucumber slices in meals.",
                  "Drink aloe vera juice in the morning (1/4 cup mixed with water)."
              ],
              "These foods cool the body, reduce inflammation, and balance the fiery energy."
          ]
      }
  ],
  "Taurus": [
      [
          "Throat Problems (sore throat, tonsillitis)",
          "Stomach Disorders (slow digestion, bloating)",
          "Respiratory Issues (sinus congestion)",
          "Neck and Shoulder Tension (stiffness, pain)",
          "Heavy Weight Gain (prone to being overweight)"
      ],
      [
          "Digestive Issues (constipation, sluggish metabolism)",
          "Joint and Muscle Pain (due to sedentary lifestyle)",
          "Weak Circulation (cold hands, feet, sluggish blood flow)",
          "Kidney Stones or Urinary Issues (slow-moving metabolic processes)"
      ],
      [
          "Earth (Prithvi)",
          "Stomach and Digestion (poor absorption of nutrients, slow digestion)",
          "Throat and Neck Problems (chronic tension, stiffness)",
          "Obesity or Weight Gain (due to slower metabolism and excess earth element)",
          "Swollen Limbs (due to fluid retention)"
      ],
      {
          "natural": [
              "Triphala Herbal Powder (for digestion)",
              "1 tsp of Triphala powder, 1 cup of warm water.",
              "Mix Triphala powder in warm water and drink before bedtime.",
              "Aids digestion, relieves constipation, detoxifies the body, balances the earth element."
          ],
          "mudra": [
              "Vayu Mudra (Air Element Mudra)",
              [
                  "Sit comfortably with your back straight.",
                  "Fold your index finger to touch the base of the thumb.",
                  "Press the thumb gently over the folded index finger.",
                  "Hold for 10-15 minutes daily."
              ],
              "Helps balance excess earth energy, relieves digestive issues, improves flexibility."
          ],
          "energy": [
              "Reiki (Throat and Solar Plexus Chakras)",
              [
                  "Sit or lie down in a relaxed position.",
                  "Focus on the throat chakra (neck area) and the solar plexus (above the navel).",
                  "Place your hands over these areas and channel healing energy for 10-15 minutes."
              ],
              "Relieves throat discomfort, enhances digestion, and supports metabolic balance."
          ],
          "meditation": [
              "Earth Connection Meditation",
              [
                  "Sit comfortably with your feet on the ground, close your eyes.",
                  "Imagine roots growing from your feet deep into the earth.",
                  "Breathe deeply, feeling connected to the earth and grounded.",
                  "Continue for 10-15 minutes."
              ]
          ],
          "foods": [
              [
                  "Ginger (helps with digestion and stomach discomfort)",
                  "Leafy greens (rich in nutrients, supports digestion)",
                  "Cucumber (helps with hydration and detox)"
              ],
              [
                  "Heavy, greasy foods (slow digestion and increase weight)",
                  "Dairy products in excess (can cause bloating and mucus buildup)"
              ],
              [
                  "Include ginger tea after meals to aid digestion.",
                  "Add leafy greens like spinach or kale in salads or soups.",
                  "Drink cucumber water (slices in water) for hydration and detox."
              ],
              "These foods promote healthy digestion, prevent weight gain, and support detoxification."
          ]
      }
  ],
  "Gemini": [
      [
          "Respiratory Issues (asthma, allergies, frequent colds)",
          "Nervous System Disorders (tension headaches, nerve pain)",
          "Throat Problems (hoarseness, coughs, speech issues)",
          "Digestive Issues (irregular bowel movements, bloating)",
          "Excessive Nervous Energy (restlessness, hyperactivity)"
      ],
      [
          "Digestive Sensitivity (gastritis, indigestion, acid reflux)",
          "Respiratory Weakness (prone to coughing, breathing difficulties)",
          "Nervous System Imbalance (frequent headaches, muscle twitches)",
          "Weak Immune System (frequent colds, infections)"
      ],
      [
          "Air (Vayu)",
          "Breathing Issues (asthma, sinus problems, breathlessness)",
          "Restlessness (nervous energy leading to lack of concentration)",
          "Digestive Irregularity (gas, bloating, and variable appetite)",
          "Tension in Shoulders and Neck (due to stress or anxiety)"
      ],
      {
          "natural": [
              "Ginger and Honey Tea (for digestion and respiratory relief)",
              "1 tsp ginger juice, 1 tsp honey, 1 cup hot water.",
              "Add ginger juice and honey to hot water, stir well, and drink warm.",
              "Aids digestion, clears respiratory passages, soothes throat."
          ],
          "mudra": [
              "Pranayama Mudra (for better breathing)",
              [
                  "Sit in a comfortable position, with your spine straight.",
                  "Fold the index and middle fingers of both hands, and place the thumb on the right nostril, the ring and little fingers on the left nostril.",
                  "Breathe in deeply through the left nostril, close it with your thumb, and exhale through the right nostril. Alternate nostrils.",
                  "Practice for 5-10 minutes, 1-2 times daily."
              ],
              "Balances nervous energy, improves breathing, calms the mind."
          ],
          "energy": [
              "Reiki (Throat and Heart Chakras)",
              [
                  "Sit or lie down comfortably.",
                  "Focus on the throat chakra (around the neck) and the heart chakra (center of chest).",
                  "Place hands on these areas and channel soothing energy for 10-15 minutes."
              ],
              "Relieves tension in the throat, improves communication, balances nervous energy."
          ],
          "meditation": [
              "Breath-Focused Meditation (for calming the mind)",
              [
                  "Sit in a comfortable, upright position, and close the eyes.",
                  "Focus on your breath, breathing deeply and slowly.",
                  "As you inhale, count to 4. As you exhale, count to 4.",
                  "Continue this pattern for 10-15 minutes."
              ]
          ],
          "foods": [
              [
                  "Lemon water (to cleanse the digestive system)",
                  "Peppermint tea (soothes the digestive system and relieves nausea)",
                  "Bananas (easy to digest, calming for the stomach)"
              ],
              [
                  "Caffeinated drinks (increase restlessness, cause anxiety)",
                  "Spicy or fried foods (aggravate the digestive system)"
              ],
              [
                  "Drink a glass of lemon water first thing in the morning.",
                  "Consume peppermint tea after meals to ease digestion.",
                  "Include bananas as a snack to maintain energy levels and calm digestion."
              ],
              "These foods support digestion, reduce digestive discomfort, calm the nervous system, and improve overall well-being."
          ]
      }
  ],
  "Cancer": [
      [
          "Digestive Problems (bloating, indigestion)",
          "Stomach Ulcers (due to emotional stress)",
          "Breast or Chest Issues (cysts, tenderness)",
          "Fluid Retention (swelling in the abdomen or legs)",
          "Respiratory Issues (frequent colds, coughs)"
      ],
      [
          "Weak Stomach (sensitive to foods, poor digestion)",
          "Emotional Eating (leading to weight issues)",
          "Breast Health Concerns (prone to inflammation or discomfort)",
          "Weak Immune System (frequent infections)"
      ],
      [
          "Water (Jala)",
          "Stomach Weakness (acid reflux, indigestion)",
          "Excessive Fluid Retention (swollen feet, puffy face)",
          "Chest Colds (congestion, mucus buildup)",
          "Menstrual Problems (irregular cycles)"
      ],
      {
          "natural": [
              "Fennel and Cumin Tea (for digestion and gas relief)",
              "1 tsp fennel seeds, 1 tsp cumin seeds, 1 cup hot water.",
              "Boil the seeds in water for 5 minutes, then strain and drink warm.",
              "Helps with bloating, improves digestion, reduces fluid retention."
          ],
          "mudra": [
              "Apan Vayu Mudra (for digestive health)",
              [
                  "Sit comfortably with your spine straight.",
                  "Touch the tips of your middle and ring fingers to the tips of the thumb, keeping the index and little fingers straight.",
                  "Hold for 5-10 minutes daily."
              ],
              "Supports digestion, helps with detoxification and fluid retention."
          ],
          "energy": [
              "Reiki (Solar Plexus and Sacral Chakras)",
              [
                  "Sit or lie down in a comfortable position.",
                  "Focus on the solar plexus (stomach area) and sacral chakra (below the navel).",
                  "Place your hands over these areas and channel healing energy for 10-15 minutes."
              ],
              "Promotes digestion, balances water retention, and supports emotional balance."
          ],
          "meditation": [
              "Water Element Meditation",
              [
                  "Sit comfortably, close your eyes, and focus on slow breathing.",
                  "Imagine yourself surrounded by water, feeling calm and refreshed.",
                  "Visualize the water cleansing and soothing your body.",
                  "Continue for 10-15 minutes."
              ]
          ],
          "foods": [
              [
                  "Coconut water (hydrates, reduces swelling)",
                  "Melons (cooling, supports hydration)",
                  "Ginger (aids digestion)"
              ],
              [
                  "Heavy dairy (can cause bloating and mucus production)",
                  "Excessive salty foods (increases fluid retention)"
              ],
              [
                  "Drink coconut water or melon juice daily.",
                  "Include ginger in teas or meals to aid digestion."
              ],
              "These foods help with digestion, reduce water retention, and soothe the stomach."
          ]
      }
  ],
  "Leo": [
      [
          "Back and Spine Problems (lower back pain, spinal issues)",
          "Heartburn and Acid Reflux (due to fiery digestion)",
          "High Fever (prone to elevated body temperature)",
          "Digestive Issues (poor digestion, constipation)",
          "Blood Pressure Issues (either high or low)"
      ],
      [
          "Weak Heart (prone to palpitations or stress-related heart issues)",
          "Liver Imbalance (digestive issues, sluggish liver function)",
          "Increased Body Heat (heat rash, sun sensitivity)",
          "Tendency to Overeat (leading to indigestion and weight gain)"
      ],
      [
          "Fire (Agni)",
          "Acid Reflux (due to excess heat in the stomach)",
          "Blood Pressure Problems (heat can increase circulation and pressure)",
          "Heart Issues (due to heat and stress)",
          "Fever and Inflammation (prone to feverish conditions)"
      ],
      {
          "natural": [
              "Aloe Vera Juice (for cooling and digestion)",
              "2 tbsp aloe vera juice, 1 cup water.",
              "Mix aloe vera juice with water and drink on an empty stomach.",
              "Reduces internal heat, aids digestion, soothes the stomach."
          ],
          "mudra": [
              "Surya Mudra (for balancing fire energy)",
              [
                  "Sit comfortably with your back straight.",
                  "Touch the tip of your ring finger to the base of your thumb.",
                  "Hold for 10-15 minutes daily."
              ],
              "Helps cool excessive heat in the body, aids digestion."
          ],
          "energy": [
              "Reiki (Heart and Solar Plexus Chakras)",
              [
                  "Sit or lie comfortably.",
                  "Focus on the heart chakra (center of chest) and solar plexus (upper abdomen).",
                  "Place hands over these areas and channel energy for 10-15 minutes."
              ],
              "Balances heat, calms digestive and heart issues."
          ],
          "meditation": [
              "Cooling Breath Meditation",
              [
                  "Sit in a comfortable position with closed eyes.",
                  "Inhale deeply through the nose, and exhale through the mouth with a 'ha' sound.",
                  "Focus on calming the body's heat.",
                  "Continue for 10-15 minutes."
              ]
          ],
          "foods": [
              [
                  "Cucumber (cooling and hydrating)",
                  "Coconut water (natural coolant)",
                  "Leafy greens (easy on digestion, cooling)"
              ],
              [
                  "Spicy and oily foods (increase internal heat)",
                  "Caffeinated drinks (aggravate acidity)"
              ],
              [
                  "Drink coconut water and eat fresh cucumber daily.",
                  "Incorporate leafy greens into meals for cooling and digestive support."
              ],
              "These foods balance internal heat, soothe digestion, and help with hydration."
          ]
      }
  ],
  "Virgo": [
      [
          "Digestive Disorders (irregular bowel movements, constipation)",
          "Nervous Stomach (nausea, anxiety-related stomach issues)",
          "Skin Problems (acne, eczema, dry skin)",
          "Muscle Tension (tight muscles, cramping)",
          "Food Sensitivities (allergies, intolerances)"
      ],
      [
          "Weak Digestion (difficulty in digesting heavy foods)",
          "Excessive Worry (leading to digestive discomfort)",
          "Nervous System Weakness (tension headaches, anxiety)",
          "Overly Sensitive Skin (prone to rashes, allergies)"
      ],
      [
          "Earth (Prithvi) and Air (Vayu)",
          "Digestive Weakness (irregular appetite, poor absorption)",
          "Skin Sensitivities (prone to rashes, eczema)",
          "Nervous Digestive Issues (stress-related indigestion)"
      ],
      {
          "natural": [
              "Triphala Powder (for digestion and detoxification)",
              "1 tsp Triphala powder, warm water.",
              "Mix with warm water and drink before bed.",
              "Enhances digestion, relieves constipation, detoxifies the body."
          ],
          "mudra": [
              "Apan Mudra (for digestive health)",
              [
                  "Sit comfortably with your back straight.",
                  "Touch the tips of the middle and ring fingers to the tips of the thumb.",
                  "Hold for 5-10 minutes daily."
              ],
              "Promotes digestive health, helps with elimination."
          ],
          "energy": [
              "Reiki (Solar Plexus and Root Chakras)",
              [
                  "Sit or lie comfortably.",
                  "Focus on the solar plexus (digestive area) and root chakra (base of the spine).",
                  "Place hands over these areas and channel energy for 10-15 minutes."
              ],
              "Relieves digestive discomfort, balances nervous tension."
          ],
          "meditation": [
              "Grounding Meditation",
              [
                  "Sit comfortably, with your feet touching the ground.",
                  "Focus on deep, slow breathing.",
                  "Visualize roots growing from your feet into the earth.",
                  "Continue for 10-15 minutes."
              ]
          ],
          "foods": [
              [
                  "Ginger (aids digestion, reduces nausea)",
                  "Leafy greens (supports digestion, rich in fiber)",
                  "Warm soups (easy to digest, soothing)"
              ],
              [
                  "Cold, raw foods (hard to digest, can upset stomach)",
                  "Fried or greasy foods (aggravate digestion)"
              ],
              [
                  "Drink ginger tea after meals for better digestion.",
                  "Include fresh leafy greens and warm soups regularly."
              ],
              "These foods support digestion, reduce bloating, and balance the digestive system."
          ]
      }
  ],
  "Libra": [
      [
          "Kidney and Urinary Issues (prone to infections, kidney stones)",
          "Back Pain (especially in lower back)",
          "Skin Problems (acne, dryness)",
          "Hormonal Imbalance (affects skin and mood)",
          "Liver and Blood Circulation Issues (poor detoxification)"
      ],
      [
          "Weak Kidneys (susceptibility to infections)",
          "Skin Sensitivities (dryness, eczema)",
          "Digestive Problems (bloating, constipation)",
          "Fluid Retention (swelling, puffiness)"
      ],
      [
          "Air (Vayu) and Water (Jala)",
          "Kidney Weakness (susceptibility to infections)",
          "Hormonal Imbalance (affects skin and overall energy)",
          "Circulatory Problems (slow blood flow, puffiness)"
      ],
      {
          "natural": [
              "Cumin and Coriander Tea (for kidney and digestive health)",
              "1 tsp cumin, 1 tsp coriander, 1 cup hot water.",
              "Steep cumin and coriander in hot water for 5 minutes, strain, and drink warm.",
              "Improves digestion, supports kidney function, reduces fluid retention."
          ],
          "mudra": [
              "Prithvi Mudra (for balancing water element)",
              [
                  "Sit comfortably with your spine straight.",
                  "Touch the tips of your ring fingers to your thumbs.",
                  "Hold for 10-15 minutes."
              ],
              "Helps balance water retention, improves digestion, and supports kidney health."
          ],
          "energy": [
              "Reiki (Kidney and Root Chakras)",
              [
                  "Sit comfortably with your hands resting on your lap.",
                  "Focus on the kidney area and root chakra (base of spine).",
                  "Channel healing energy for 10-15 minutes."
              ],
              "Supports kidney health, balances hormonal levels, improves circulation."
          ],
          "meditation": [
              "Balancing Water Element Meditation",
              [
                  "Sit with a straight spine and close your eyes.",
                  "Focus on your breath, imagining waves of water soothing your body.",
                  "Continue for 10-15 minutes."
              ]
          ],
          "foods": [
              [
                  "Cucumber (hydrates and detoxes)",
                  "Pineapple (helps with digestion and kidney function)",
                  "Leafy greens (support kidney health)"
              ],
              [
                  "Excess salty foods (increases water retention)",
                  "Processed foods (can affect kidney and skin health)"
              ],
              [
                  "Drink cucumber and pineapple juice daily.",
                  "Eat leafy greens regularly for kidney and digestive support."
              ],
              "These foods improve hydration, support kidney health, and reduce water retention."
          ]
      }
  ],
  "Scorpio": [
      [
          "Reproductive System Issues (irregular periods, cramps)",
          "Urinary Tract Infections (prone to infections)",
          "Detoxification Problems (sluggish liver, constipation)",
          "Digestive Disorders (IBS, bloating, acidity)",
          "Skin Issues (acne, psoriasis)"
      ],
      [
          "Liver Imbalance (poor detoxification, sluggish digestion)",
          "Circulatory Issues (varicose veins, blood pressure problems)",
          "Weak Immune System (susceptible to infections)",
          "Hormonal Imbalance (affects the reproductive system)"
      ],
      [
          "Water (Jala) and Fire (Agni)",
          "Digestive Issues (acid reflux, ulcers)",
          "Hormonal Imbalance (affects reproductive organs)",
          "Detoxification Problems (sluggish liver and kidney)",
          "Heat-related Issues (inflammation, rashes)"
      ],
      {
          "natural": [
              "Triphala Powder (for detoxification and digestion)",
              "1 tsp Triphala powder, warm water.",
              "Mix Triphala powder with warm water and drink before bed.",
              "Promotes digestion, detoxifies the liver, supports the immune system."
          ],
          "mudra": [
              "Prithvi Mudra (for detoxification and grounding)",
              [
                  "Sit in a comfortable position.",
                  "Touch the tip of the ring finger to the tip of the thumb.",
                  "Hold for 10-15 minutes."
              ],
              "Aids in detoxification, helps reduce inflammation."
          ],
          "energy": [
              "Reiki (Sacral and Solar Plexus Chakras)",
              [
                  "Sit or lie comfortably.",
                  "Focus on the sacral chakra (lower abdomen) and solar plexus (upper abdomen).",
                  "Place your hands on these areas and channel energy for 10-15 minutes."
              ],
              "Helps with hormonal balance, improves digestion, and enhances detoxification."
          ],
          "meditation": [
              "Water Element Meditation",
              [
                  "Sit comfortably and focus on deep breathing.",
                  "Visualize the flow of water cleansing your body and mind.",
                  "Continue for 10-15 minutes."
              ]
          ],
          "foods": [
              [
                  "Cucumber (cooling and detoxifying)",
                  "Lemon water (cleanses and supports digestion)",
                  "Pomegranate (improves circulation and digestion)"
              ],
              [
                  "Processed foods (affect liver and digestion)",
                  "Spicy foods (aggravate acidity and inflammation)"
              ],
              [
                  "Drink lemon water and include pomegranate in meals for improved digestion.",
                  "Eat cucumber daily for detoxification."
              ],
              "These foods aid detoxification, balance digestion, and reduce inflammation."
          ]
      }
  ],
  "Sagittarius": [
      [
          "Hips and Thighs (muscle strain, joint issues)",
          "Liver Issues (overburdened, sluggish)",
          "Digestive Problems (overeating, poor digestion)",
          "Lung Problems (bronchitis, asthma, frequent coughs)",
          "Back Pain (due to overexertion)"
      ],
      [
          "Liver Imbalance (prone to overconsumption of alcohol or fatty foods)",
          "Digestive Sensitivity (irregular appetite, indigestion)",
          "Joint Pain (especially in hips, knees, and thighs)",
          "Breathing Problems (excessive coughing, shortness of breath)"
      ],
      [
          "Fire (Agni) and Air (Vayu)",
          "Overactive Digestion (prone to acidity, indigestion)",
          "Joint and Muscle Tension (strained hips, back, and thighs)",
          "Breathing Disorders (asthma, bronchitis, frequent colds)"
      ],
      {
          "natural": [
              "Ginger and Turmeric Tea (for digestion and inflammation)",
              "1 tsp fresh ginger, 1/2 tsp turmeric, 1 cup hot water.",
              "Boil the ginger and turmeric in water for 5 minutes, strain, and drink warm.",
              "Supports digestion, reduces inflammation, helps with joint pain."
          ],
          "mudra": [
              "Vayu Mudra (for balancing air element and digestion)",
              [
                  "Sit comfortably with your spine straight.",
                  "Fold your index finger towards the base of your thumb, and press the thumb gently on the index finger.",
                  "Hold for 10-15 minutes."
              ],
              "Balances air energy, improves digestion, calms nervous tension."
          ],
          "energy": [
              "Reiki (Root and Solar Plexus Chakras)",
              [
                  "Sit or lie comfortably.",
                  "Focus on the root chakra (base of spine) and solar plexus (stomach area).",
                  "Channel energy to these areas for 10-15 minutes."
              ],
              "Enhances digestion, supports joint health, and improves breathing."
          ],
          "meditation": [
              "Breathing Meditation",
              [
                  "Sit comfortably, with your spine straight.",
                  "Focus on slow, deep breaths, inhaling for 4 counts, exhaling for 4 counts.",
                  "Continue for 10-15 minutes."
              ],
              "Calms the respiratory system, improves lung capacity, and aids digestion."
          ],
          "foods": [
              [
                  "Papaya (aids digestion and reduces bloating)",
                  "Turmeric (anti-inflammatory, supports joint health)",
                  "Lentils (rich in fiber, supports digestion)"
              ],
              [
                  "Excessive alcohol (damages the liver)",
                  "Oily and fried foods (slow digestion, burden the liver)"
              ],
              [
                  "Include papaya and turmeric in your diet regularly for improved digestion and joint support.",
                  "Avoid oily and fried foods."
              ],
              "These foods reduce inflammation, support digestion, and protect the liver."
          ]
      }
  ],
  "Capricorn": [
      [
          "Bone and Joint Issues (arthritis, knee pain, fractures)",
          "Skin Problems (dry, flaky skin)",
          "Liver and Gallbladder Issues (sluggish function, indigestion)",
          "Dental Problems (tooth sensitivity, cavities)",
          "Poor Circulation (cold hands, feet)"
      ],
      [
          "Weak Bones (prone to fractures or joint pain)",
          "Liver Imbalance (difficulty detoxifying, sluggish digestion)",
          "Skin Dryness (prone to dryness, eczema)",
          "Poor Digestion (difficulty absorbing nutrients)"
      ],
      [
          "Earth (Prithvi) and Water (Jala)",
          "Bone Weakness (prone to fractures and joint pain)",
          "Skin Dryness (eczema, rough skin)",
          "Poor Circulation (prone to cold extremities)"
      ],
      {
          "natural": [
              "Ghee and Honey (for bone strength and digestion)",
              "1 tsp ghee, 1 tsp honey.",
              "Mix ghee and honey and consume daily on an empty stomach.",
              "Promotes bone health, enhances digestion, lubricates joints."
          ],
          "mudra": [
              "Prithvi Mudra (for strengthening bones and circulation)",
              [
                  "Sit comfortably with your back straight.",
                  "Touch the tip of the ring finger to the tip of the thumb.",
                  "Hold for 10-15 minutes."
              ],
              "Strengthens bones, improves circulation, reduces dryness."
          ],
          "energy": [
              "Reiki (Root Chakra and Sacral Chakra)",
              [
                  "Sit comfortably with your hands on your lap.",
                  "Focus on the root chakra (base of the spine) and sacral chakra (lower abdomen).",
                  "Channel healing energy for 10-15 minutes."
              ],
              "Improves circulation, strengthens bones, supports digestion."
          ],
          "meditation": [
              "Grounding Meditation",
              [
                  "Sit with your feet touching the ground, spine straight.",
                  "Focus on your breath, visualizing roots growing from your feet into the earth.",
                  "Continue for 10-15 minutes."
              ],
              "Improves circulation, reduces cold extremities, strengthens bones."
          ],
          "foods": [
              [
                  "Leafy greens (rich in calcium for bones)",
                  "Carrots (supports bone health)",
                  "Almonds (rich in calcium and healthy fats)"
              ],
              [
                  "Excess salt (weakens bones and affects digestion)",
                  "Dairy-heavy foods (in some children, it may cause skin dryness)"
              ],
              [
                  "Eat leafy greens and carrots regularly for bone strength.",
                  "Avoid excess salt and processed foods."
              ],
              "Supports bone health, reduces skin dryness, and improves circulation."
          ]
      }
  ],
  "Aquarius": [
      [
          "Circulatory Issues (poor blood flow, cold extremities)",
          "Ankle and Lower Leg Problems (weak circulation, prone to sprains)",
          "Neurological Issues (nervous system imbalance)",
          "Skin Sensitivity (dryness, rashes)",
          "Foot Problems (calluses, corns)"
      ],
      [
          "Weak Circulation (prone to cold hands, feet, poor blood flow)",
          "Skin Sensitivity (prone to rashes or dryness)",
          "Nervous System Imbalance (overactive or underactive nervous responses)",
          "Ankle and Foot Issues (weak circulation or strain)"
      ],
      [
          "Air (Vayu) and Ether (Akasha)",
          "Circulatory Problems (poor blood flow)",
          "Skin Sensitivity (dry or rash-prone skin)",
          "Nervous System Imbalance (inconsistent energy levels, stress-related)"
      ],
      {
          "natural": [
              "Ashwagandha and Ginger Tea (for circulation and nervous system balance)",
              "1 tsp Ashwagandha powder, 1 tsp ginger, 1 cup hot water.",
              "Boil Ashwagandha and ginger in hot water for 5 minutes, strain, and drink warm.",
              "Improves circulation, calms the nervous system, boosts energy."
          ],
          "mudra": [
              "Apana Vayu Mudra (for calming the nervous system and improving circulation)",
              [
                  "Sit comfortably with a straight spine.",
                  "Touch the tips of the middle and ring fingers to the tips of the thumb.",
                  "Hold for 10-15 minutes."
              ],
              "Improves circulation, calms the nervous system, reduces stress."
          ],
          "energy": [
              "Reiki (Heart and Root Chakras)",
              [
                  "Sit or lie comfortably.",
                  "Focus on the heart chakra (center of chest) and root chakra (base of spine).",
                  "Channel energy to these areas for 10-15 minutes."
              ],
              "Balances circulation, improves skin health, and calms nervous tension."
          ],
          "meditation": [
              "Mindful Breathing",
              [
                  "Sit comfortably and focus on slow, deep breaths.",
                  "Inhale for 4 counts, hold for 4 counts, exhale for 4 counts.",
                  "Continue for 10-15 minutes."
              ],
              "Improves circulation, reduces stress, balances nervous energy."
          ],
          "foods": [
              [
                  "Beets (supports circulation and detoxification)",
                  "Ginger (supports digestion and circulation)",
                  "Leafy greens (rich in antioxidants and improve circulation)"
              ],
              [
                  "Processed foods (affect circulation and skin)",
                  "Excess caffeine (upsets the nervous system)"
              ],
              [
                  "Eat beets and leafy greens regularly for improved circulation.",
                  "Avoid excessive caffeine and processed foods."
              ],
              "Enhances circulation, improves skin health, balances the nervous system."
          ]
      }
  ],
  "Pisces": [
    [
        "Liver and Digestive Issues (sluggish digestion, bloating)",
        "Respiratory Problems (frequent colds, coughs)",
        "Foot Issues (swollen feet, sensitivity)",
        "Hormonal Imbalance (affecting skin and mood)",
        "Immune System Weakness (prone to infections)"
    ],
    [
        "Weak Immune System (susceptible to infections)",
        "Liver Imbalance (poor detoxification)",
        "Foot and Leg Sensitivity (swelling, fatigue)",
        "Hormonal Imbalance (affects mood and skin)"
    ],
    [
        "Water (Jala) and Ether (Akasha)",
        "Weak Immune System (prone to colds and infections)",
        "Digestive Issues (slow metabolism, bloating)",
        "Respiratory Problems (frequent coughing, asthma)",
        "Fluid Retention (swollen feet, legs)"
    ],
    {
      "natural": [
          "Triphala and Turmeric Tea (for digestion and detoxification)",
          "1 tsp Triphala powder, 1/2 tsp turmeric, 1 cup hot water.",
          "Mix Triphala and turmeric with hot water, stir, and drink warm.",
          "Enhances digestion, supports liver health, detoxifies the body."
      ],
      "mudra": [
          "Apana Mudra (for detoxification and fluid balance)",
          [
              "Sit comfortably with a straight spine.",
              "Touch the tips of the middle finger and ring finger to the tip of the thumb.",
              "Hold for 10-15 minutes."
          ],
          "Supports detoxification, balances fluid retention, improves digestion."
      ],
      "energy": [
          "Reiki (Throat and Heart Chakras)",
          [
              "Sit or lie comfortably.",
              "Focus on the throat chakra (neck) and heart chakra (center of chest).",
              "Channel healing energy for 10-15 minutes."
          ],
          "Boosts the immune system, improves respiratory health."
      ],
      "meditation": [
          "Ocean Breath Meditation",
          [
              "Sit comfortably with your spine straight.",
              "Inhale deeply, then exhale with a hissing sound, like the sound of waves.",
              "Continue for 10-15 minutes."
          ],
          "Calms the mind, improves breathing, supports digestion."
      ],
      "foods": [
        [
            "Ginger (improves digestion, reduces nausea)",
            "Pineapple (supports liver detox and digestion)",
            "Coconut water (helps with fluid balance)"
        ],
        [
            "Processed sugars (weakens the immune system)",
            "Dairy-heavy foods (may aggravate mucus production)"
        ],
        [
            "Drink coconut water and eat pineapple regularly.",
            "Avoid processed sugars and excessive dairy."
        ],
        "Supports digestion, boosts immunity, helps detoxify."
      ]
    }
  ]
}

healthInsights = {
  "Aries": "Aries in the 6th house may cause health issues related to the head, eyes, or face, like headaches or sinus troubles. child may also be prone to minor injuries from being active and adventurous. Encouraging regular exercise and a balanced diet will help maintain overall health. Avoid overly spicy foods to prevent acidity or stomach discomfort. Early care and teaching caution during physical activities can keep child healthy and safe.",
  
  "Taurus": "Taurus in the 6th house suggests good physical strength and endurance. child may have a tendency to enjoy rich or heavy foods, which could lead to weight gain or digestive issues. Common health concerns may include throat, neck, or thyroid problems. Encourage regular physical activity and a diet that avoids overeating. Proper hydration and moderation in sweets or fatty foods will help maintain good health.",
  
  "Gemini": "Gemini in the 6th house points to an active mind and body but may bring issues with the lungs, shoulders, or arms. child could experience allergies, colds, or respiratory sensitivities. Encourage outdoor activities to improve lung health and ensure a stable routine to avoid stress. Consistent sleep patterns and light breathing exercises can help maintain well-being.",
  
  "Cancer": "Cancer in the 6th house indicates sensitivity in the stomach and digestive system. child may be prone to digestive discomfort or water retention. Emotional stress could also affect health. A balanced diet with warm, home-cooked meals and plenty of hydration is essential. Provide emotional support and stability to keep child in good spirits and health.",
  
  "Leo": "Leo in the 6th house suggests strong vitality but potential issues with the heart, back, or spine. child may thrive on attention and activity but should avoid overexertion. Encourage activities that promote flexibility and relaxation, like yoga. A diet rich in heart-healthy foods and regular checkups will support long-term health.",
  
  "Virgo": "Virgo in the 6th house indicates a focus on health but a tendency toward worry or stress, which can lead to digestive issues or anxiety. child may be particular about cleanliness or diet. Encourage mindfulness practices, a simple routine, and a fiber-rich diet to maintain gut health. Keeping a calm environment will benefit both mental and physical well-being.",
  
  "Libra": "Libra in the 6th house suggests a balanced approach to health but may create concerns around the kidneys, lower back, or skin. child may be sensitive to stress, which can affect digestion or skin health. Encourage relaxation techniques, such as gentle stretching or mindfulness, and a diet that supports kidney health. Regular skin care and staying hydrated are also beneficial for overall well-being.",
  
  "Scorpio": "Scorpio in the 6th house indicates intense energy but may bring health challenges related to the reproductive system, bladder, or circulatory system. child could experience issues with intense emotions affecting physical health. Encourage regular physical activity, especially activities that release tension, like swimming or cycling. A balanced diet and stress management will help maintain strong health.",
  
  "Sagittarius": "Sagittarius in the 6th house suggests a love for adventure, which could lead to injuries or overindulgence in physical activities. child may be prone to problems related to the hips, thighs, or liver. Encourage outdoor activities, but emphasize safety. A healthy diet with plenty of fruits, vegetables, and liver-supporting foods will promote overall health. Regular checkups for joint health and staying active can keep child healthy and strong.",
  
  "Capricorn": "Capricorn in the 6th house indicates a strong and disciplined nature, but health concerns may arise in the bones, joints, or knees. child could experience issues related to stiffness or slow recovery from physical strain. Encourage activities that strengthen bones and joints, like walking or gentle exercise. A diet rich in calcium and vitamin D, along with regular stretching, will help keep child in good health.",
  
  "Aquarius": "Aquarius in the 6th house suggests a unique approach to health but may bring issues with the nervous system or circulation. child may experience nervous tension or anxiety, which could affect sleep or energy levels. Encourage mental relaxation techniques, such as meditation or quiet time. A balanced diet that includes brain-boosting foods, along with regular physical activity, will help child maintain a healthy body and mind.",
  
  "Pisces": "Pisces in the 6th house indicates a sensitive health nature, with a tendency to experience issues related to the feet, immune system, or emotional well-being. child may be prone to feeling tired or overwhelmed by stress. Encourage a calm, soothing environment and regular physical activity, such as swimming or walking. A diet that supports the immune system and plenty of rest will keep child healthy and balanced."
}


carrer = {
    "Aries": [
        "The 10th house in astrology represents career, fame, and public life. If a child's 10th house is in Aries, it indicates a dynamic, energetic, and ambitious approach to career. Aries is ruled by Mars, the planet of action, courage, and assertiveness. Individuals with Aries in the 10th house are likely to seek careers that allow them to take the lead, initiate projects, and pursue their goals with passion and determination. They thrive in fast-paced environments and are often drawn to positions that require boldness and a competitive edge.",
        {
            "Entrepreneurship": "Aries individuals are natural leaders and risk-takers, making them highly suited for starting their own business or leading innovative projects.",
            "Sales and Marketing": "Careers that involve persuasion, competitive spirit, and a direct approach, such as sales or marketing, are ideal for Aries individuals.",
            "Sports and Athletics": "Aries' high energy and drive for competition can lead to success in professional sports or athletic careers.",
            "Military or Law Enforcement": "Leadership and assertiveness make Aries well-suited for military careers or roles in law enforcement, where decisiveness and courage are essential.",
            "Emergency Services": "Careers in fields like firefighting, paramedics, or other high-stress, action-driven jobs fit Aries' desire to act quickly and decisively."
        }
    ],
    "Taurus": [
        "The 10th house represents career, fame, and public life. If a child's 10th house is in Taurus, it suggests a stable, reliable, and practical approach to career. Taurus is ruled by Venus, the planet of beauty, harmony, and material success. Individuals with Taurus in the 10th house tend to seek careers that offer financial stability, long-term growth, and the ability to build something solid and enduring. They are often drawn to careers that provide comfort, security, and a sense of value.",
        {
            "Finance and Banking": "Taurus' strong financial instincts make them well-suited for careers in banking, investment, or financial planning.",
            "Real Estate": "Careers in real estate, property management, or interior design align with Taurus' appreciation for beauty and material success.",
            "Luxury Goods and Retail": "Working with luxury products, jewelry, or high-end services can bring Taurus both success and fulfillment.",
            "Agriculture and Farming": "A deep connection to the earth can lead to success in agriculture, farming, or environmental conservation.",
            "Culinary Arts": "Careers in cooking, food management, or restaurant ownership resonate with Taurus' love for comfort and sensual pleasures."
        }
    ],
    "Gemini": [
    "The 10th house in astrology represents career, fame, and public life. If a child's 10th house is in Gemini, it indicates versatility, adaptability, and a communicative approach to career. Gemini is ruled by Mercury, the planet of communication, intellect, and learning. Individuals with Gemini in the 10th house are likely to seek careers that involve intellectual stimulation, social interaction, and opportunities to express their ideas. They thrive in dynamic environments and are often drawn to professions that require quick thinking and multitasking.",
    {
        "Media and Journalism": "Gemini individuals' strong communication skills and curiosity make them highly suited for careers in writing, reporting, or broadcasting.",
        "Teaching and Education": "Their love for sharing knowledge and engaging with others makes education a natural fit for Gemini.",
        "Public Relations and Marketing": "Careers that involve networking, creativity, and persuasion, such as public relations or advertising, align well with Gemini's strengths.",
        "Travel and Tourism": "Gemini's adventurous nature and adaptability are ideal for roles in travel, tourism, or as a tour guide.",
        "Technology and IT": "With their quick learning ability and love for intellectual challenges, Gemini can excel in technology-driven careers, such as programming or digital marketing."
    }
],
    "Cancer": [
        "If a child's 10th house is in Cancer, it indicates a nurturing, empathetic, and intuitive approach to career. Cancer is ruled by the Moon, representing emotions, home, and family. Individuals with Cancer in the 10th house are often drawn to careers where they can care for others, create emotional connections, or build a secure, supportive environment. They value emotional fulfillment and a strong sense of belonging in their careers.",
        {
            "Healthcare and Nursing": "Careers in nursing, therapy, or healthcare provide an opportunity to care for others, aligning with Cancer's nurturing instincts.",
            "Teaching and Counseling": "Cancer's empathetic nature makes them great counselors, teachers, or social workers.",
            "Hospitality and Event Planning": "Organizing events, managing hotels, or working in hospitality appeals to Cancer's desire to create safe, welcoming environments.",
            "Psychology": "Counseling, therapy, or psychological research offer emotional depth and connection for Cancer.",
            "Home Management or Interior Design": "Careers that involve creating comfort, such as interior design or home organization, align with Cancer's emotional and family-centered approach."
        }
    ],
    "Leo": [
        "With the 10th house in Leo, career ambitions are driven by a desire for recognition, leadership, and creativity. Leo is ruled by the Sun, symbolizing vitality, confidence, and creativity. Individuals with Leo in the 10th house seek careers that allow them to shine, express themselves, and be in the spotlight. They excel in leadership positions and often desire to inspire or entertain others.",
        {
            "Entertainment and Performing Arts": "Leo's love for the spotlight makes them ideal for careers in acting, music, dance, or other performance-based fields.",
            "Leadership Roles": "Whether in business or politics, Leo thrives in positions of power and influence where they can lead and inspire others.",
            "Public Speaking or Media": "Leo's confidence and charisma make them well-suited for roles in media, journalism, or motivational speaking.",
            "Creative Director or Artist": "Careers in fashion, design, or visual arts provide an outlet for Leo's creativity and desire for recognition.",
            "Event Management": "Organizing and leading large-scale events or public functions offers Leo the chance to be in charge and receive recognition."
        }
    ],
    "Virgo": [
        "With Virgo in the 10th house, career success is linked to precision, practicality, and a strong work ethic. Virgo is ruled by Mercury, the planet of communication and organization. Individuals with Virgo in the 10th house are often drawn to careers that require attention to detail, problem-solving, and a methodical approach. They excel in roles that demand efficiency, organization, and service to others.",
        {
            "Healthcare and Medicine": "Careers in medicine, nursing, or allied health fields where attention to detail and care are critical are ideal for Virgo.",
            "Accounting or Finance": "Virgo's analytical skills and ability to manage finances make them well-suited for careers in accounting, auditing, or financial planning.",
            "Research or Science": "Virgo's methodical and detail-oriented nature thrives in research, laboratory work, or scientific inquiry.",
            "Education": "Teaching, tutoring, or educational administration allows Virgo to use their organizational skills while helping others.",
            "Project Management or Consulting": "Virgo excels in roles that require structure, organization, and efficiency, making them great project managers or consultants."
        }
    ],
    "Libra": [
        "With Libra in the 10th house, career success is linked to balance, harmony, and relationships. Libra is ruled by Venus, the planet of beauty, love, and diplomacy. Individuals with Libra in the 10th house are often drawn to careers that involve collaboration, fairness, and aesthetic appeal. They seek work environments that promote peace and harmony, and they are well-suited for roles where their diplomatic skills can shine.",
        {
            "Law and Mediation": "Libra's strong sense of justice and fairness makes them well-suited for careers in law, mediation, or arbitration.",
            "Diplomacy and Foreign Affairs": "Diplomatic roles or positions in international relations appeal to Libra's desire for balance and peace.",
            "Fashion and Design": "Careers in fashion, interior design, or styling tap into Libra's love for beauty and aesthetics.",
            "Public Relations": "Working in PR, marketing, or communications allows Libra to use their diplomatic and relationship-building skills.",
            "Counseling and Therapy": "Libra's desire to help others and create harmony makes them excellent counselors, therapists, or psychologists."
        }
    ],
    "Scorpio": [
        "With Scorpio in the 10th house, career success is driven by intensity, transformation, and deep passion. Scorpio is ruled by Pluto, the planet of transformation and power. Individuals with Scorpio in the 10th house are drawn to careers that involve investigation, power, and emotional depth. They excel in roles that require strategic thinking and the ability to manage crises or transformation.",
        {
            "Psychology and Counseling": "Scorpio's ability to delve into deep emotional layers makes them well-suited for careers in psychology, counseling, or therapy.",
            "Investigation and Forensics": "Roles in criminal investigation, forensic science, or detective work match Scorpio's desire to uncover hidden truths.",
            "Finance and Investment": "Careers in investment banking, stock trading, or financial management appeal to Scorpio's strategic mindset and desire for power.",
            "Medicine or Surgery": "The medical field, especially in areas requiring precision and care, like surgery, resonates with Scorpio's intense focus.",
            "Research and Science": "Careers in research, especially those involving deep analysis and uncovering new knowledge, fit Scorpio's investigative nature."
        }
    ],
    "Sagittarius": [
        "With Sagittarius in the 10th house, career success is focused on exploration, knowledge, and freedom. Sagittarius is ruled by Jupiter, the planet of expansion, optimism, and philosophy. Individuals with Sagittarius in the 10th house are drawn to careers that allow them to explore new horizons, travel, or share their knowledge and experiences with others. They are motivated by personal growth and the pursuit of truth.",
        {
            "Education and Teaching": "Sagittarius' love for knowledge and philosophy makes them great teachers, professors, or educational administrators.",
            "Travel and Tourism": "Careers in travel, tourism, or international business allow Sagittarius to explore new cultures and expand their horizons.",
            "Writing and Journalism": "Sagittarius excels in writing, especially travel journalism, or any field that involves sharing ideas and experiences.",
            "Philosophy and Religious Studies": "A career in philosophy, theology, or cultural studies appeals to Sagittarius' love for exploration of big ideas.",
            "Entrepreneurship": "With their adventurous spirit, Sagittarius is often successful in starting businesses that cater to their passions, especially those related to travel or culture."
        }
    ],
    "Capricorn": [
        "With Capricorn in the 10th house, career success is linked to structure, discipline, and long-term planning. Capricorn is ruled by Saturn, the planet of responsibility and hard work. Individuals with Capricorn in the 10th house thrive in careers that require persistence, leadership, and authority. They excel in roles where they can build a stable foundation and achieve long-term success through determination and professionalism.",
        {
            "Government or Administrative Roles": "These individuals excel in structured environments like government services, public administration, or law enforcement, where discipline and responsibility are key.",
            "Corporate Leadership": "Careers in business management, finance, or entrepreneurship can be highly successful, especially in executive positions or roles requiring long-term planning.",
            "Engineering/Architecture": "Fields that require precision, planning, and hard work, such as engineering or architecture, are ideal for Capricorn's meticulous nature.",
            "Law or Judiciary": "Legal careers, including law, judgeships, or paralegal roles, align well with Capricorn's sense of justice and order.",
            "Real Estate Development": "Real estate, especially property development or investment, can offer financial success due to Capricorn's knack for planning and building from the ground up."
        }
    ],
    "Aquarius": [
        "With Aquarius in the 10th house, career success is focused on innovation, individuality, and social progress. Aquarius is ruled by Uranus, the planet of revolution and unconventionality. Individuals with Aquarius in the 10th house are drawn to careers that challenge the status quo, innovate, and contribute to society in unique ways. They excel in roles that involve technology, social change, and forward-thinking ideas.",
        {
            "Technology and Innovation": "Careers in tech, such as software development, engineering, or IT, are ideal for Aquarius' inventive nature.",
            "Social Reform and Activism": "Aquarius' desire for social justice and equality makes them excellent candidates for roles in activism, politics, or humanitarian work.",
            "Science and Research": "Careers in scientific research, particularly in cutting-edge or experimental fields, resonate with Aquarius' love for knowledge and progress.",
            "Inventor or Entrepreneur": "Aquarius' forward-thinking mindset makes them well-suited for entrepreneurship, especially in fields related to innovation and technology.",
            "Aerospace or Engineering": "Roles in the aerospace industry or other engineering fields allow Aquarius to push boundaries and work on groundbreaking projects."
        }
    ],
    "Pisces": [
        "With Pisces in the 10th house, career success is driven by creativity, compassion, and spiritual fulfillment. Pisces is ruled by Neptune, the planet of imagination, intuition, and idealism. Individuals with Pisces in the 10th house are often drawn to careers that allow them to express their artistic abilities, connect with others on an emotional level, or work in service to humanity. They are motivated by a desire to make the world a better place through their work.",
        {
            "Arts and Entertainment": "Pisces is naturally creative and artistic, making them well-suited for careers in music, art, or film.",
            "Psychology and Counseling": "Pisces' deep empathy and intuitive nature make them excellent counselors, therapists, or social workers.",
            "Healing Professions": "Careers in alternative healing, such as acupuncture, massage therapy, or holistic health, resonate with Pisces' desire to help others.",
            "Nonprofit Work and Social Services": "Pisces' compassion makes them ideal for roles in nonprofit organizations, social work, or charity-based careers.",
            "Writing and Creative Arts": "Writing, poetry, or other forms of creative expression are ideal for Pisces' imaginative and emotionally driven nature."
        }
    ]
}

education = {
  "Aries": [
    "child, born under Aries Rashi, is energetic, ambitious, and loves challenges. child thrives in environments that offer independence and opportunities to take the lead. child enjoys subjects related to leadership, entrepreneurship, sports, or any field that requires competitive drive and determination. A dynamic and action-oriented learning environment is best for child.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Business, Entrepreneurship, Sports, Engineering, Military Studies, Leadership."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Hands-on learning, competitive challenges, and individual projects."
        },
        {
            "title": "Mode of Learning",
            "content": "Interactive learning, leadership roles, practical applications, and real-world tasks."
        }
    ],
    [
        {
            "title": "Action-Oriented",
            "content": "child prefers to learn by doing, engaging in physical activities, and solving problems through action."
        },
        {
            "title": "Leader",
            "content": "child is naturally drawn to leadership roles and enjoys being in charge of projects or teams."
        },
        {
            "title": "Competitive",
            "content": "Thrives in environments where achievements and progress are recognized and rewarded."
        }
    ],
    "Foster Leadership Skills and Competitive Spirit",
    [
        {
            "title": "Encourage Leadership Opportunities",
            "content": "Give child chances to lead group projects or participate in team-based activities."
        },
        {
            "title": "Provide Competitive Challenges",
            "content": "Set up tasks or challenges where child can compete and measure progress, such as academic competitions or sports."
        },
        {
            "title": "Support Independence",
            "content": "Allow child to take ownership of their learning process and make decisions about their academic path."
        }
    ]
],
  "Taurus": [
    "child, born under Taurus Rashi, is practical, patient, and focused on achieving long-term goals. child thrives in environments that provide stability, structure, and tangible results. child enjoys subjects related to finance, agriculture, arts, or any field that involves steady progress and real-world applications. A well-organized and methodical learning approach works best for child.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Finance, Agriculture, Architecture, Arts, Environmental Science."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Step-by-step learning, practical applications, and real-world case studies."
        },
        {
            "title": "Mode of Learning",
            "content": "Structured learning, hands-on projects, fieldwork, and internships."
        }
    ],
    [
        {
            "title": "Practical Learner",
            "content": "child excels when applying theoretical knowledge to real-life situations."
        },
        {
            "title": "Methodical",
            "content": "child prefers to take a steady, consistent approach to learning, focusing on building expertise over time."
        },
        {
            "title": "Determined",
            "content": "Shows persistence and patience in completing tasks, focusing on long-term success."
        }
    ],
    "Promote Practical Learning and Goal Setting",
    [
        {
            "title": "Encourage Steady Progress",
            "content": "Help child set long-term academic goals and break them into manageable tasks."
        },
        {
            "title": "Support Hands-On Learning",
            "content": "Provide opportunities for practical, real-world experiences, such as internships or fieldwork."
        },
        {
            "title": "Build Consistency",
            "content": "Establish a consistent study routine and ensure that child focuses on steady progress rather than rushing through tasks."
        }
    ]
],
  "Gemini": [
    "child, born under Gemini Rashi (Gemini), is naturally curious, quick-witted, and loves learning new things. child thrives in environments that encourage intellectual discussions, debates, and hands-on problem-solving. child enjoys subjects that are dynamic and allow room for creativity, such as science, technology, literature, and languages. A flexible and interactive learning approach works best for child, where exploration, questions, and practical tasks are encouraged.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Technology, Science, Engineering, Languages, Communication, Psychology, Social Sciences."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Active learning through group discussions, problem-solving, and debates."
        },
        {
            "title": "Mode of Learning",
            "content": "Online courses, interactive classes, project-based learning."
        }
    ],
    [
        {
            "title": "Curiosity-Driven",
            "content": "child enjoys exploring new topics independently, often seeking answers through various resources."
        },
        {
            "title": "Analytical",
            "content": "child excels in breaking down problems into smaller, manageable parts and solving them step by step."
        },
        {
            "title": "Social Learning",
            "content": "Collaboration with peers in group studies and discussions helps child stay engaged and motivated."
        }
    ],
    "Foster Critical Thinking Through Discussions & Projects",
    [
        {
            "title": "Set Up Regular Learning Sessions",
            "content": "Dedicate time for discussions on different topics related to child's interests. This can be done after school or on weekends."
        },
        {
            "title": "Encourage Problem-Solving",
            "content": "Provide real-life challenges that require logical thinking. For example, puzzles, coding tasks, or science experiments."
        },
        {
            "title": "Promote Group Work",
            "content": "Encourage participation in group activities or projects, where child can engage with peers, share ideas, and learn from others."
        }
    ]
],
  "Cancer": [
    "child, born under Cancer Rashi, is sensitive, intuitive, and emotionally driven in learning. child thrives in environments that offer emotional support and allow for personal connections with the subject matter. child enjoys subjects that involve creativity, helping others, or understanding human behavior, such as psychology, literature, arts, or social sciences. A calm, nurturing, and structured learning environment works best, allowing child to feel secure and confident.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Psychology, Literature, Social Sciences, Arts, Education, Healthcare."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Emotional engagement, one-on-one mentorship, small group discussions."
        },
        {
            "title": "Mode of Learning",
            "content": "A mix of traditional learning with personalized support and hands-on learning."
        }
    ],
    [
        {
            "title": "Emotionally Driven",
            "content": "child connects well with subjects that evoke emotional responses and can relate them to personal experiences."
        },
        {
            "title": "Intuitive Learner",
            "content": "Relies on gut feelings and intuition to grasp concepts and ideas."
        },
        {
            "title": "Support-Oriented",
            "content": "Needs encouragement and personalized guidance to feel confident and motivated."
        }
    ],
    "Build Emotional Connections to Learning",
    [
        {
            "title": "Create a Safe Learning Environment",
            "content": "Ensure child feels emotionally supported and safe while learning. This helps build confidence."
        },
        {
            "title": "Incorporate Emotional Aspects",
            "content": "Connect subjects with real-life stories, people, or experiences that can emotionally engage child."
        },
        {
            "title": "Encourage Creative Expression",
            "content": "Allow child to express learning through creative outlets like writing, art, or discussions."
        }
    ]
],
  "Leo": [
    "child, born under Leo Rashi, is confident, creative, and enjoys leadership roles. child thrives in environments where there is recognition for achievements and opportunities for self-expression. child is attracted to subjects like performing arts, management, leadership studies, or any field that allows for creative self-expression and the ability to inspire others. A learning environment that provides room for independence and recognition works best for child.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Performing Arts, Management, Business, Leadership Studies, Marketing, Design."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Self-directed learning, project-based work, leadership opportunities."
        },
        {
            "title": "Mode of Learning",
            "content": "Interactive classes, internships, real-world applications, creative workshops."
        }
    ],
    [
        {
            "title": "Self-Confident",
            "content": "child enjoys being in the spotlight and leads projects or group activities with ease."
        },
        {
            "title": "Creative",
            "content": "Thrives when able to express creativity in different forms, such as through design, art, or storytelling."
        },
        {
            "title": "Goal-Oriented",
            "content": "Focuses on achieving personal and academic goals and enjoys setting challenges for growth."
        }
    ],
    "Foster Leadership and Creativity",
    [
        {
            "title": "Encourage Independent Projects",
            "content": "Provide opportunities for child to lead projects or take responsibility for group work."
        },
        {
            "title": "Praise Efforts and Achievements",
            "content": "Recognize and celebrate child's academic and creative accomplishments to boost self-esteem."
        },
        {
            "title": "Incorporate Creativity",
            "content": "Encourage child to engage in creative outlets like music, drama, or design alongside academic work."
        }
    ]
],
  "Virgo": [
    "child, born under Virgo Rashi, is analytical, detail-oriented, and has a strong desire to help others. child thrives in structured environments where clear expectations are set. child enjoys subjects that require precision and critical thinking, such as mathematics, science, healthcare, or engineering. A systematic and organized approach to learning is crucial for child to excel.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Mathematics, Science, Engineering, Healthcare, Data Analysis, Accounting."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Structured, systematic learning with clear goals and detailed information."
        },
        {
            "title": "Mode of Learning",
            "content": "Lectures, research, hands-on experimentation, and data analysis."
        }
    ],
    [
        {
            "title": "Detail-Oriented",
            "content": "child excels when working through problems in a step-by-step manner, paying attention to every detail."
        },
        {
            "title": "Logical Thinker",
            "content": "Enjoys solving complex problems and applying critical thinking to find solutions."
        },
        {
            "title": "Service-Oriented",
            "content": "Finds satisfaction in work that helps others, particularly in healthcare, social services, or teaching."
        }
    ],
    "Develop Strong Organizational Skills",
    [
        {
            "title": "Set Clear Goals and Plans",
            "content": "Help child create detailed study schedules, break down tasks into manageable steps, and set academic goals."
        },
        {
            "title": "Encourage Routine Learning",
            "content": "Create a regular study schedule that allows time for consistent learning and revision."
        },
        {
            "title": "Support Practical Learning",
            "content": "Provide opportunities for hands-on learning, such as science experiments, real-world problem-solving, or internships."
        }
    ]
],
  "Libra": [
    "child, born under Libra Rashi, is balanced, diplomatic, and enjoys working in harmonious environments. child thrives in subjects that involve social interaction, fairness, and creativity, such as law, art, design, or social sciences. A cooperative, team-oriented approach to learning works best, where child can collaborate with others and discuss ideas.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Law, Social Sciences, Art, Design, Diplomacy, Psychology."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Collaborative work, group discussions, and debates."
        },
        {
            "title": "Mode of Learning",
            "content": "Interactive learning with group projects, class discussions, and real-world application."
        }
    ],
    [
        {
            "title": "Diplomatic",
            "content": "child works well in group settings, often mediating and facilitating cooperation among peers."
        },
        {
            "title": "Creative Thinker",
            "content": "Enjoys subjects that allow for creative expression and the ability to see multiple perspectives."
        },
        {
            "title": "Analytical",
            "content": "Has a strong ability to weigh different viewpoints and make balanced, fair decisions."
        }
    ],
    "Encourage Collaborative Learning & Discussions",
    [
        {
            "title": "Promote Teamwork",
            "content": "Encourage child to participate in group projects or clubs where team dynamics and shared ideas are emphasized."
        },
        {
            "title": "Foster Open Conversations",
            "content": "Set aside time for discussions on various topics, encouraging child to express ideas and consider different viewpoints."
        },
        {
            "title": "Support Creative Projects",
            "content": "Provide resources for artistic or creative work, such as art supplies or access to design platforms."
        }
    ]
],
  "Scorpio": [
    "child, born under Scorpio Rashi, is intense, focused, and driven by curiosity. child thrives in environments that challenge the intellect and allow for deep exploration of topics. child enjoys subjects that involve investigation, research, psychology, or anything that involves uncovering hidden truths. A learning approach that encourages depth, self-reflection, and transformation works best.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Psychology, Research, Medicine, Science, Criminal Justice, Forensic Studies."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Independent research, critical thinking, problem-solving, and deep analysis."
        },
        {
            "title": "Mode of Learning",
            "content": "Project-based learning, research, case studies, and experiential learning."
        }
    ],
    [
        {
            "title": "Focused and Determined",
            "content": "child works best when tackling complex subjects or problems, showing persistence and dedication."
        },
        {
            "title": "Investigative",
            "content": "Loves to dig deep into subjects, seeking to understand the underlying causes or truths."
        },
        {
            "title": "Resilient",
            "content": "child thrives in challenging academic environments that require perseverance and self-discipline."
        }
    ],
    "Cultivate Research Skills and Critical Thinking",
    [
        {
            "title": "Encourage Independent Research",
            "content": "Provide opportunities for child to explore topics in-depth through books, online resources, and research projects."
        },
        {
            "title": "Challenge with Complex Problems",
            "content": "Present problems or challenges that require critical thinking and analysis."
        },
        {
            "title": "Foster Self-Reflection",
            "content": "Encourage child to reflect on academic progress and identify areas for improvement."
        }
    ]
],
  "Sagittarius": [
    "child, born under Sagittarius Rashi, is adventurous, optimistic, and loves exploring new ideas. child thrives in environments that offer freedom, exploration, and the opportunity to engage in philosophical or broad-minded subjects. child enjoys subjects that allow for travel, global perspectives, or philosophical discussions, such as international relations, philosophy, or world history.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Philosophy, International Relations, Travel & Tourism, Literature, Anthropology."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Independent learning, exploration, broad-based knowledge, and global perspectives."
        },
        {
            "title": "Mode of Learning",
            "content": "Online learning, travel-based learning, cultural exchange, and experiential education."
        }
    ],
    [
        {
            "title": "Explorer",
            "content": "child loves exploring new ideas, cultures, and philosophies, often seeking out experiences outside the traditional classroom."
        },
        {
            "title": "Big-Picture Thinker",
            "content": "Focuses on understanding broad concepts and seeing the connections between different areas of knowledge."
        },
        {
            "title": "Optimistic",
            "content": "Approaches learning with enthusiasm, always looking for new opportunities and experiences."
        }
    ],
    "Encourage Exploration and Broad Learning",
    [
        {
            "title": "Provide Opportunities for Travel",
            "content": "Encourage experiences that expand child's worldview, such as cultural trips or exchange programs."
        },
        {
            "title": "Introduce Diverse Topics",
            "content": "Expose child to a wide range of subjects, including philosophy, world history, or global issues."
        },
        {
            "title": "Promote Independent Learning",
            "content": "Allow child to pursue self-directed projects and research that align with personal interests."
        }
    ]
]
,
  "Capricorn": [
    "child, born under Capricorn Rashi, is disciplined, practical, and highly focused on achieving long-term goals. child thrives in structured, goal-oriented environments where hard work and perseverance are emphasized. child enjoys subjects that are practical and lead to tangible results, such as business, finance, engineering, or law. A structured and goal-driven learning environment is ideal for child.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Business, Finance, Engineering, Law, Accounting, Architecture."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Structured learning with clear goals, practical applications, and real-world experiences."
        },
        {
            "title": "Mode of Learning",
            "content": "Lectures, hands-on projects, internships, and professional training programs."
        }
    ],
    [
        {
            "title": "Practical Thinker",
            "content": "child enjoys applying theoretical knowledge to real-world situations and solving practical problems."
        },
        {
            "title": "Goal-Oriented",
            "content": "Focuses on setting and achieving long-term academic and professional goals."
        },
        {
            "title": "Disciplined and Responsible",
            "content": "Works diligently, often without needing external motivation, to achieve success."
        }
    ],
    "Set Clear Goals and Provide Practical Learning Experiences",
    [
        {
            "title": "Help Set Long-Term Goals",
            "content": "Encourage child to set clear academic and career goals, breaking them down into manageable steps."
        },
        {
            "title": "Provide Practical Opportunities",
            "content": "Offer real-world learning experiences, such as internships, work experiences, or projects related to child's academic interests."
        },
        {
            "title": "Instill a Strong Work Ethic",
            "content": "Emphasize the importance of hard work, discipline, and persistence in achieving goals."
        }
    ]
],
  "Aquarius": [
    "child, born under Aquarius Rashi, is innovative, forward-thinking, and values individuality. child thrives in environments that encourage independent thinking and allow for exploration of unconventional ideas. child enjoys subjects that involve technology, science, or social change, such as robotics, environmental science, or sociology. A learning approach that encourages creativity, innovation, and social impact is ideal for child.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Technology, Robotics, Environmental Science, Sociology, Political Science, Innovation."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Independent study, brainstorming, and collaboration on innovative projects."
        },
        {
            "title": "Mode of Learning",
            "content": "Hands-on projects, online learning, group collaboration, and fieldwork."
        }
    ],
    [
        {
            "title": "Innovative Thinker",
            "content": "child excels in exploring new ideas and creating innovative solutions."
        },
        {
            "title": "Idealistic",
            "content": "Driven by a desire to make a difference in the world, child focuses on subjects that can bring about social change."
        },
        {
            "title": "Collaborative",
            "content": "Enjoys working with others on projects that have a wider impact on society."
        }
    ],
    "Foster Innovation Through Creative Exploration",
    [
        {
            "title": "Encourage Independent Learning",
            "content": "Provide resources like books, documentaries, and online courses that allow child to explore new and unconventional ideas."
        },
        {
            "title": "Support Social Impact Projects",
            "content": "Help child get involved in community projects or initiatives that focus on making a positive difference."
        },
        {
            "title": "Facilitate Brainstorming Sessions",
            "content": "Engage in regular brainstorming activities where child can share ideas and develop creative solutions."
        }
    ]
],
 "Pisces": [
    "child, born under Pisces Rashi, is intuitive, creative, and empathetic. child thrives in environments that nurture imagination and emotional expression. child enjoys subjects related to art, psychology, music, or spirituality, where they can express themselves and explore deeper meanings. A supportive, creative, and flexible learning environment works best for child.",
    [
        {
            "title": "Subjects of Interest",
            "content": "Psychology, Arts, Music, Literature, Spirituality, Philosophy."
        },
        {
            "title": "Preferred Learning Style",
            "content": "Creative exploration, introspection, and imaginative thinking."
        },
        {
            "title": "Mode of Learning",
            "content": "Art-based learning, creative writing, individual projects, and experiential learning."
        }
    ],
    [
        {
            "title": "Intuitive Learner",
            "content": "child often relies on intuition and imagination to grasp new concepts."
        },
        {
            "title": "Empathetic",
            "content": "Finds it easy to connect with others on an emotional level, making social sciences or psychology appealing."
        },
        {
            "title": "Creative Thinker",
            "content": "Loves subjects that allow for self-expression, creativity, and artistic exploration."
        }
    ],
    "Nurture Creativity and Emotional Intelligence",
    [
        {
            "title": "Provide Creative Outlets",
            "content": "Encourage activities like drawing, painting, music, or writing that allow child to express their emotions."
        },
        {
            "title": "Support Emotional Reflection",
            "content": "Help child connect academic subjects to personal experiences, fostering deeper understanding and emotional engagement."
        },
        {
            "title": "Allow Flexibility in Learning",
            "content": "Give child the freedom to explore subjects in their own way, without strict rules or rigid timelines."
        }
    ]
]
}

planetDesc = {
  "Sun" : [
    "The Sun represents strength, vitality, leadership, and self-confidence. Strengthening the Sun brings clarity, health, and a strong sense of self-worth.",
    [
      "Wake Up Early",
      "Encourage child to wake up with the Sun. Early rising fosters discipline and energy.",
      'Set an alarm for 6:00 AM. Teach child to say, "Thank you, Sun, for a new day," as they wake up.',
      "Starting the day early brings energy and helps you accomplish more."
    ],
    [
      "Take Responsibility",
      "Give child small daily tasks, like watering plants or organizing their toys, to build responsibility.",
      'Say, "You take care of your plants, just like the Sun cares for the world."',
      '"Responsibility makes you strong and dependable, like the Sun."'
    ],
    [
      'Sun Salutations (Surya Namaskar)',
      "Practice 5 rounds of Sun Salutations with child each morning. This energizes the body and connects to the Sun's power.",
      "Teach child how to do each posture, slowly and with gratitude.",
      "When you move your body and express gratitude, you invite strength and energy."
    ],
    [
      "Vitality Foods",
      "Include foods like oranges, carrots, and whole grains in the diet. These foods nourish the body with vitality.",
      "Serve orange juice or carrot sticks with a meal.",
      "Healthy foods make you strong and vibrant, just like the Sun."
    ],
    [
      "Donate on Sundays",
      "On Sundays, donate wheat, jaggery, or anything yellow.",
      "Let's give something to others today, to spread the Sun's warmth and kindness.",
      "Sharing brings warmth and light to others, just like the Sun."
    ]
  ],
  "Moon" : [
    "The Moon represents emotions, peace, intuition, and nurturing. Strengthening the Moon brings emotional balance and calmness.",
    [
      "Nighttime Calmness",
      "Establish a calm bedtime routine to help child relax and sleep well.",
      'Read a peaceful story or play soft music before bed.',
      "A calm mind at night leads to peaceful sleep, just like the Moon calms the night sky."
    ],
    [
      "Emotional Awareness",
      "Teach child to express their feelings, whether happy or sad, in a calm and gentle way.",
      'Encourage saying, "I feel happy because of the sunny day," or, "I feel sad but will talk about it."',
      "Understanding your emotions helps you feel peaceful and balanced like the Moon."
    ],
    [
      "Relaxing Night Walks",
      "Take a short walk under the moonlight to connect with the Moon's peaceful energy.",
      "Say, 'Let's walk and feel the peace the Moon gives us.'",
      "Taking time for peaceful moments brings calmness and clarity."
    ],
    [
      "Cooling Foods",
      "Include foods like milk, cucumber, and rice to cool the body.",
      "Serve a cucumber salad or warm milk at night.",
      "Cooling foods calm your body and mind, like the Moon calms the night."
    ],
    [
      "Give White Items",
      "On Mondays, donate white items such as clothes or food.",
      "Sharing white items brings peace and harmony, like the Moon.",
      "Sharing brings peace to both you and others, just like the Moon brings peace to the night."
    ]
  ],
  "Mars" : [
    "Mars represents courage, energy, and determination. Strengthening Mars encourages action, assertiveness, and bravery.",
    [
      "Exercise and Challenges",
      "Encourage child to take on physical challenges like running or climbing.",
      "Let's race to the tree or climb the slide!",
      "Physical challenges teach you to be brave and strong, like Mars."
    ],
    [
      "Bravery and Determination",
      "Teach child to face difficulties without giving up.",
      'If you fall, get up and try again. Bravery helps you grow.',
      "Facing challenges builds strength, just like Mars gives courage."
    ],
    [
      "Martial Arts or Active Games",
      "Enroll child in martial arts, yoga, or sports to channel energy positively.",
      "Every movement strengthens your body and mind, just like Mars.",
      "Physical discipline teaches you focus, strength, and perseverance."
    ],
    [
      "Strengthening Foods",
      "Include red foods like apples, lentils, and tomatoes in the diet.",
      "Serve red lentils or apple slices as snacks.",
      "These foods give you strength and vitality, just like Mars gives you energy."
    ],
    [
      "Donate Red Items",
      "On Tuesdays, donate red items such as clothes or lentils.",
      "Sharing red items boosts your courage and helps others.",
      "Giving creates strength, just like Mars makes us strong."
    ]
  ],
  "Mercury" : [
    "Mercury represents communication, intelligence, and adaptability. Strengthening Mercury enhances learning, curiosity, and mental agility.",
    [
      "Daily Learning",
      "Set aside time for daily learning through puzzles, reading, or exploring new topics.",
      "Let's read a story or solve a puzzle together.",
      "Learning helps you grow smarter and quicker, just like Mercury sharpens the mind."
    ],
    [
      "Curiosity and Communication",
      "Encourage child to ask questions and explore the world around them.",
      "What would you like to learn today? Let's find out together.",
      "Asking questions leads to learning, just like Mercury helps us understand the world."
    ],
    [
      "Mind Games and Puzzles",
      "Play memory or word games to boost cognitive abilities.",
      "Let's play a game to remember words or numbers.",
      "Training your mind makes you sharper and clever, just like Mercury."
    ],
    [
      "Brain Foods",
      "Include walnuts, almonds, and green vegetables in the diet.",
      "Serve almonds or spinach with meals.",
      "These foods make your brain sharp, like Mercury enhances intelligence."
    ],
    [
      "Donate Books",
      "On Wednesdays, donate books or educational materials.",
      "Let's donate books to spread knowledge and wisdom.",
      "Sharing knowledge brings wisdom to everyone, just like Mercury teaches us."
    ]
  ],
  "Jupiter" : [
    "Jupiter represents wisdom, spirituality, knowledge, and good fortune. Strengthening Jupiter brings higher learning, faith, and a sense of purpose.",
    [
      "Practice Gratitude",
      "Teach child to start the day by saying 'thank you' for the blessings received.",
      'Every morning, child, express one thing you are grateful for.',
      "Gratitude brings abundance and positivity, just like Jupiter blesses with wisdom."
    ],
    [
      "Seek Knowledge",
      "Encourage child to read or learn something new every day.",
      "Let's read a book about a subject you like or try a new activity together.",
      "Continuous learning brings wisdom and joy, just like Jupiter helps us grow mentally."
    ],
    [
      "Offer Water to Lord Vishnu",
      "Teach child to offer water to Lord Vishnu or chant the 'Om Namo Bhagavate Vasudevaya' mantra.",
      "Let's chant the mantra together to invite wisdom and spirituality into our lives.",
      "Chanting brings wisdom and purifies the mind, like Jupiter's blessings."
    ],
    [
      "Saffron and Yellow Foods",
      "Include saffron, yellow lentils, and pumpkin in the diet to connect with Jupiter's energy.",
      "Serve yellow foods like pumpkin curry or lentil soup.",
      "Food can nourish the body and mind, just like Jupiter nourishes our wisdom."
    ],
    [
      "Donate Yellow Items",
      "On Thursdays, donate yellow items such as bananas, saffron, or clothes.",
      "Let's donate yellow items to spread joy and wisdom.",
      "Charity brings blessings of wisdom and prosperity, like Jupiter's influence."
    ]
  ],
  "Venus" : [
    "Venus represents love, beauty, creativity, and prosperity. Strengthening Venus brings harmony, creativity, and material comforts.",
    [
      "Practice Kindness and Love",
      "Encourage child to express kindness to everyone, whether through words or actions.",
      'Say something kind to others today, like “I appreciate you!”',
      "Being kind brings harmony and joy, just like Venus spreads love and beauty."
    ],
    [
      "Appreciate Beauty in Everything",
      "Teach child to notice and appreciate beauty in nature, art, and relationships.",
      "Let's look at the flowers or clouds today and see how beautiful they are!",
      "Appreciating beauty makes life joyful and harmonious, like Venus."
    ],
    [
      "Creative Time",
      "Dedicate time each day for child to explore creative activities like painting or music.",
      "Let's paint a picture or sing a song today.",
      "Creativity brings peace and joy, just like Venus nurtures creativity."
    ],
    [
      "Sweet and Tasty Foods",
      "Include foods like sweets, dairy, and fruits to nourish the body and senses.",
      "Serve fruits like mangoes or a small piece of sweet dish.",
      "Food can be a source of pleasure and nourishment, just like Venus brings joy."
    ],
    [
      "Donate White Items",
      "On Fridays, donate white items such as clothes, sweets, or flowers.",
      "Let's donate white items to spread love and positivity.",
      "Giving brings peace and prosperity, just like Venus."
    ]
  ],
  "Saturn" : [
    "Saturn represents discipline, hard work, patience, and responsibility. Strengthening Saturn brings perseverance, wisdom, and a sense of duty.",
    [
      "Daily Routine",
      "Establish a fixed routine for child, including time for work, rest, and play.",
      "Let's follow a schedule each day to be responsible.",
      "A disciplined routine helps you succeed, just like Saturn teaches us responsibility."
    ],
    [
      "Patience and Hard Work",
      "Teach child that success comes with consistent effort and patience.",
      'If you want to achieve something, keep trying every day.',
      "Hard work and patience lead to success, just like Saturn teaches us."
    ],
    [
      "Service and Duty",
      "Encourage child to take on responsibilities at home, like organizing or helping with chores.",
      "Let's clean up the room together as part of our routine.",
      "Doing your duty brings strength and wisdom, like Saturn's influence."
    ],
    [
      "Nourishing Foods for the Body",
      "Include dark-colored foods like black sesame seeds, grains, and root vegetables in the diet.",
      "Serve dishes made from dark-colored grains or root vegetables.",
      "These foods give you the strength and stamina to face challenges, just like Saturn."
    ],
    [
      "Donate Black Items",
      "On Saturdays, donate items like black clothes, sesame seeds, or oil.",
      "Let's donate black items to help others and earn Saturn's blessings.",
      "Giving brings strength and stability, just like Saturn."
    ]
  ],
  "Rahu" : [
    "Rahu represents illusion, desire, and ambition. It can bring rapid growth but also challenges. Strengthening Rahu brings clarity, focus, and breaking free from illusions.",
    [
      "Focus on Goals",
      "Encourage child to set one clear goal and work towards it daily.",
      "Let's set a goal for the day and take small steps towards it.",
      "Focused effort helps you achieve your dreams, just like Rahu pushes us towards growth."
    ],
    [
      "Overcome Illusions",
      "Teach child to see things clearly and not get distracted by false promises.",
      'If something sounds too good to be true, it might be an illusion.',
      "Understanding what is real and what is not brings true success."
    ],
    [
      "Meditation and Mindfulness",
      "Introduce child to basic meditation techniques to calm the mind and increase focus.",
      "Let's sit quietly and focus on your breath for 5 minutes every day.",
      "Meditation helps clear the mind and focus on true desires."
    ],
    [
      "Avoid Overindulgence",
      "Encourage simple, balanced meals without excessive spices or sweets.",
      "Serve healthy, balanced meals and limit processed food.",
      "Moderation in food helps clear the mind, just like Rahu helps us find clarity."
    ],
    [
      "Donate Items for Growth",
      "On Saturdays, donate items related to ambition, like books or educational materials.",
      "Let's donate books or useful items to help others grow.",
      "Helping others grow brings growth to yourself, just like Rahu's influence."
    ]
  ],
  "Ketu" : [
    "Ketu represents spiritual growth, liberation, and detachment. It helps in breaking free from material attachments and focusing on higher consciousness. Strengthening Ketu brings peace, spiritual enlightenment, and the ability to let go of attachments.",
    [
      "Simplify Life",
      "Teach child to focus on essentials and detach from unnecessary distractions.",
      "Let's organize your space and only keep the things you truly need.",
      "Simplicity in life brings peace and clarity, just like Ketu teaches detachment."
    ],
    [
      "Let Go of Attachments",
      "Teach child that true happiness comes from within and not from material possessions.",
      "Sometimes, giving away things we don't need makes space for new opportunities.",
      "Detaching from unnecessary things helps us grow spiritually, just like Ketu shows the way to liberation."
    ],
    [
      "Spiritual Practices",
      "Introduce child to daily prayer or reflection as a way to connect with higher consciousness.",
      "Let's sit together for 5 minutes every morning and reflect on the day ahead.",
      "Spiritual practices bring peace and liberation, just like Ketu helps us connect to our higher self."
    ],
    [
      "Simple and Light Foods",
      "Encourage a diet focused on simplicity, like fruits, vegetables, and light meals that nourish the body without overloading it.",
      "Let's eat simple meals today, like fruits or vegetable soup, to feel light and clear.",
      "Simple foods support clarity and peace, just like Ketu's energy helps us let go of distractions."
    ],
    [
      "Donate Spiritual Materials",
      "On Sundays, donate spiritual books or items related to meditation and learning.",
      "Let's donate books, clothes, or spiritual items to help others grow.",
      "Sharing spiritual knowledge helps you grow, just like Ketu's influence brings enlightenment."
    ]
  ]
}

subContent = {
    "Aries" : [
        "child's subconscious mind may be driven by strong desires to act decisively and independently. With an 8th house in Aries, there may be an instinct to face challenges head-on, but this impulsiveness can also bring about subconscious fears or resistance, particularly around being in control of situations. When feeling threatened or challenged, child might struggle with the urge to react too quickly or resist vulnerability. These subconscious patterns can sometimes hinder child's growth by creating internal conflict, especially when it comes to trusting others or handling emotional situations with patience.",
        [ 
            {"title" : "Impulsiveness",
            "content" : "A tendency to act quickly without fully considering the consequences, which can sometimes lead to regret or missed opportunities."},
            {"title": "Fear of Losing Control", "content": "A deep-seated need to maintain control over situations, leading to difficulty in trusting others or letting go."},
            {"title":"Emotional Reactivity","content": "Strong emotional reactions (anger, frustration) can arise quickly, affecting relationships and inner peace."},
            {"title" : "Resistance to Vulnerability","content" : "A subconscious fear of showing weakness or being hurt, which may prevent emotional growth."},
            {"title" : "Difficulty Embracing Change", "content" : "Fearing the unknown, child may resist transformation or growth due to a subconscious attachment to the status quo."}
        ],
        {
            "manifestation" : [
                "Affirmations for Patience and Trust",
                "Repeating positive affirmations to help child embrace patience, self-control, and trust.",
                [
                    "I trust myself and others to navigate change with patience.",
                    "I release fear and allow myself to grow through challenges."
                ],
                "Repeat these affirmations 5 times in the morning with intention.",
                "Affirmations create new thought patterns, helping to overcome fear and impulsive behavior."
            ],
            "quantum" : [
                "Shifting Energy for Emotional Balance",
                "Visualizing emotional energy as vibrations that can be altered to promote calmness and positivity.",
                [
                    "child should sit quietly and focus on breathing.",
                    "Imagine emotions as waves or energy, with negative emotions represented as dark, heavy energy.",
                    "Visualize this energy shifting into light, peaceful vibrations."   
                ],
                "Practice for 3-5 minutes twice a day, after waking and before bed.",
                "Visualizing energy transformation can help release emotional blocks, raising vibrational energy to a positive state."
            ],
            "healing" : [
                "Breathing for Emotional Release",
                "Use deep breathing to release intense emotions like anger or frustration.",
                [
                    "child should sit comfortably and focus on their breath.",
                    "Inhale deeply for 4 counts, imagining calm energy filling the body.",
                    "Hold the breath for 4 counts and exhale slowly for 6 counts."
                ],
                "Repeat for 5-10 minutes whenever feeling overwhelmed.",
                "Deep breathing reduces stress and calms emotional responses, aiding in emotional release."
            ],
            "mudra" : [
                "The Surya Mudra for Empowerment",
                "This mudra enhances personal power, calmness, and emotional control.",
                [
                    "child should sit straight, palms facing upwards.",
                    "Place the ring finger at the base of the thumb, keeping the other fingers extended.",
                    "Hold this position while focusing on deep breathing."
                ],
                "Hold for 5-10 minutes daily.",
                "The Surya Mudra helps calm emotional reactions and supports inner strength."
            ]
        }
    ],
    "Taurus": [
    "child's subconscious mind with an 8th house in Taurus may be deeply connected to emotional security and the need for stability. However, this can also create subconscious blocks when it comes to change or unexpected events. child may have a strong desire for material or emotional stability and could feel threatened by any shifts that challenge this sense of security. These deep-rooted fears may create resistance to change or cause stubbornness in adapting to new situations, potentially hindering emotional growth and personal transformation.",
    [
        {
            "title": "Fear of Change",
            "content": "Subconscious resistance to change due to a need for security and stability."
        },
        {
            "title": "Stubbornness",
            "content": "A tendency to hold onto old beliefs or routines, making it difficult to adapt or let go of the past."
        },
        {
            "title": "Attachment to Comfort",
            "content": "A deep attachment to physical or emotional comfort, which may prevent embracing new challenges."
        },
        {
            "title": "Materialism",
            "content": "A subconscious focus on possessions or external validation, which can cloud inner peace."
        },
        {
            "title": "Avoidance of Emotional Risk",
            "content": "Fear of emotional loss or vulnerability, leading to avoiding new emotional experiences."
        }
    ],
    {
        "manifestation": [
            "Affirmations for Growth and Adaptability",
            "Repeating affirmations to help child embrace change and let go of past attachments.",
            [
                "I am open to change and trust that it brings growth.",
                "I release my attachment to comfort and embrace new opportunities."
            ],
            "Say these affirmations 5 times every morning.",
            "Affirmations create new subconscious patterns, helping to reduce fear of change and enhance adaptability."
        ],
        "quantum": [
            "Transforming Fearful Energy",
            "Use the concept of energy transformation to release fear and anxiety related to change.",
            [
                "child should sit comfortably and focus on breathing.",
                "Imagine fear or resistance as a dark, heavy cloud surrounding the body.",
                "Visualize this cloud dissipating and being replaced by a warm, bright light of peace and trust."
            ],
            "Practice this for 3-5 minutes each morning.",
            "This practice helps shift subconscious fear into positive energy, promoting emotional healing."
        ],
        "healing": [
            "Grounding Breathwork for Stability",
            "Focus on grounding and calming breathwork to help let go of fear and find inner peace.",
            [
                "child should sit comfortably with feet flat on the floor.",
                "Inhale deeply through the nose for 4 counts.",
                "Hold for 4 counts, then slowly exhale through the mouth for 6 counts."
            ],
            "Do this for 5-10 minutes each day, focusing on grounding energy.",
            "This breathing practice helps create a sense of stability and reduces anxiety."
        ],
        "mudra": [
            "The Prithvi Mudra for Grounding",
            "This mudra promotes stability, grounding, and emotional balance.",
            [
                "child should sit with a straight back, palms facing upwards.",
                "Touch the tip of the ring finger to the tip of the thumb, keeping other fingers extended.",
                "Focus on deep breathing and grounding energy into the body."
            ],
            "Hold for 5-10 minutes daily.",
            "The Prithvi Mudra enhances stability and emotional calmness, helping release fear and attachment."
        ]
    }
],
    "Gemini": [
    "child's subconscious mind with an 8th house in Gemini may be constantly seeking knowledge and understanding. There may be a subconscious need for communication, mental stimulation, and new ideas. However, this mental restlessness can sometimes lead to difficulty focusing or forming deep emotional connections. child might subconsciously avoid emotional depth, preferring intellectual pursuits, which can block personal growth in emotional or transformative areas of life.",
    [
        {
            "title": "Mental Restlessness",
            "content": "Difficulty focusing on one thing or staying emotionally grounded due to a constant flow of thoughts."
        },
        {
            "title": "Avoiding Emotional Depth",
            "content": "A tendency to intellectualize emotions rather than connect with them on a deeper level."
        },
        {
            "title": "Difficulty with Commitment",
            "content": "A subconscious fear of being tied down or restricted in relationships or life choices."
        },
        {
            "title": "Shifting Attention",
            "content": "Constantly changing interests or goals, making it hard to follow through with deep personal growth."
        },
        {
            "title": "Superficial Connections",
            "content": "Tendency to form shallow relationships or avoid meaningful emotional bonds."
        }
    ],
    {
        "manifestation": [
            "Affirmations for Focus and Emotional Depth",
            "Use affirmations to enhance emotional connection and mental clarity.",
            [
                "I focus my energy on meaningful emotional connections.",
                "I embrace the depth of my feelings and allow myself to experience emotional growth."
            ],
            "Repeat these affirmations 5 times in the morning.",
            "Affirmations help focus the mind and encourage deeper emotional connections."
        ],
        "quantum": [
            "Focusing Energy for Emotional Clarity",
            "Use visualization to focus and direct energy towards emotional clarity.",
            [
                "child should sit comfortably and breathe deeply.",
                "Visualize energy flowing to the heart, clearing away any confusion or distractions.",
                "See this energy expanding, bringing emotional clarity and deep connections."
            ],
            "Practice for 5 minutes twice a day.",
            "This technique uses the mind's power to direct energy for emotional clarity and deeper connections."
        ],
        "healing": [
            "Deep Breathing for Grounding",
            "Use deep breathing to ground the mind and bring emotional focus.",
            [
                "child should sit comfortably with feet on the ground.",
                "Inhale slowly for 4 counts, hold for 4, and exhale slowly for 6 counts."
            ],
            "Repeat for 5-10 minutes to calm the mind.",
            "Deep breathing helps bring focus and reduces mental restlessness."
        ],
        "mudra": [
            "The Gyan Mudra for Clarity",
            "This mudra enhances mental clarity and emotional connection.",
            [
                "child should sit with a straight back.",
                "Touch the tips of the index fingers and thumbs together, keeping other fingers extended.",
                "Focus on calming the mind and deepening emotional awareness."
            ],
            "Hold this position for 5-10 minutes daily.",
            "The Gyan Mudra helps clear mental clutter, improving emotional depth and clarity."
        ]
    }
],
    "Cancer": [
    "child's subconscious mind, with the 8th house in Cancer, may be deeply connected to emotional security, family, and the need to protect loved ones. However, this can create subconscious fears and attachments related to vulnerability, emotional loss, and abandonment. child may subconsciously suppress their emotions or avoid confronting deeper feelings to maintain a sense of safety. There may be an intense desire to shield oneself and others from emotional pain, which could hinder growth and emotional freedom. This emotional armor can also make it challenging for child to fully trust and open up in relationships.",
    [
        {
            "title": "Fear of Abandonment",
            "content": "Subconscious fears of being left behind or not being loved can create emotional blocks."
        },
        {
            "title": "Emotional Suppression",
            "content": "A tendency to hide emotions, making it hard to process feelings and express vulnerability."
        },
        {
            "title": "Overprotectiveness",
            "content": "A subconscious need to control and protect, which can create tension in relationships."
        },
        {
            "title": "Fear of Emotional Pain",
            "content": "Avoiding emotional depth due to the fear of being hurt or experiencing loss."
        },
        {
            "title": "Difficulty Letting Go",
            "content": "Subconsciously holding onto past emotional wounds or relationships, making it hard to move forward."
        }
    ],
    {
        "manifestation": [
            "Affirmations for Emotional Freedom and Trust",
            "Use affirmations to encourage trust, emotional expression, and letting go of past pain.",
            [
                "I trust myself to open my heart and embrace my emotions.",
                "I release fear and trust that I am safe to express my feelings."
            ],
            "Repeat these affirmations 5 times in the morning and evening.",
            "Affirmations reprogram the subconscious mind, creating space for emotional release and trust."
        ],
        "quantum": [
            "Energy Transformation for Emotional Healing",
            "Visualize emotional energy shifting from fear to calm and peace.",
            [
                "child should sit quietly and focus on breathing.",
                "Visualize fear or emotional pain as dark energy around the chest area.",
                "See this dark energy transforming into warm, golden light, filling the body with peace and emotional freedom."
            ],
            "Practice this visualization for 3-5 minutes each morning.",
            "Visualization transforms negative emotional energy into positive vibrations, helping to release fear and past pain."
        ],
        "healing": [
            "Healing Through Heart-Centered Breathing",
            "Use deep heart-centered breathing to calm emotional reactions and release stress.",
            [
                "child should sit comfortably, place hands on the heart, and focus on deep breathing.",
                "Inhale deeply through the nose for 4 counts, imagining light entering the heart.",
                "Hold for 4 counts and exhale slowly for 6 counts, releasing tension."
            ],
            "Repeat for 5-10 minutes, especially when feeling overwhelmed or emotionally triggered.",
            "Heart-centered breathing calms the nervous system, promoting emotional healing and peace."
        ],
        "mudra": [
            "The Apan Vayu Mudra for Emotional Balance",
            "This mudra helps release emotional tension and encourages inner peace.",
            [
                "child should sit comfortably with their hands resting on the knees, palms facing upward.",
                "Touch the tips of the index and middle fingers to the tips of the thumb, while keeping the other fingers extended.",
                "Focus on deep, calm breathing and visualize emotional healing."
            ],
            "Hold the mudra for 5-10 minutes daily.",
            "The Apan Vayu Mudra promotes emotional balance, reducing fear and promoting calmness."
        ]
    }
],
  "Leo": [
    "child's subconscious mind with the 8th house in Leo may carry a deep need for recognition, attention, and validation. There could be subconscious fears about not being appreciated or seen, leading to emotional blocks around expressing their true selves. child may subconsciously seek to control how they are perceived by others, which can create resistance to vulnerability. Fear of being judged or criticized might also prevent child from fully embracing emotional depth or change, causing them to hide their true feelings behind a façade of confidence.",
    [
        {
            "title": "Fear of Rejection",
            "content": "Subconscious fear of not being accepted or seen for who they truly are."
        },
        {
            "title": "Overcompensation",
            "content": "A tendency to seek constant validation or attention to feel emotionally secure."
        },
        {
            "title": "Emotional Pride",
            "content": "A subconscious need to protect pride, which may prevent child from admitting vulnerability or emotional pain."
        },
        {
            "title": "Need for Control",
            "content": "A tendency to control situations to ensure recognition and validation."
        },
        {
            "title": "Avoiding Vulnerability",
            "content": "Subconsciously avoiding emotional depth or honesty due to fear of being judged or misunderstood."
        }
    ],
    {
        "manifestation": [
            "Affirmations for Self-Acceptance and Emotional Honesty",
            "Repeat affirmations to encourage self-love, emotional expression, and acceptance.",
            [
                "I am worthy of love and acceptance just as I am.",
                "I embrace my vulnerability and trust that it strengthens me."
            ],
            "Repeat these affirmations 5 times each morning.",
            "Affirmations help shift subconscious beliefs, fostering self-love and emotional openness."
        ],
        "quantum": [
            "Transforming Emotional Energy for Authenticity",
            "Use energy visualization to shift from fear of rejection to personal authenticity.",
            [
                "child should sit in a quiet space and breathe deeply.",
                "Visualize a dark cloud of self-doubt or fear of rejection surrounding the body.",
                "See this cloud dissolving, and replace it with golden, radiant energy that represents authenticity and confidence."
            ],
            "Practice for 3-5 minutes daily.",
            "Visualization can help transform negative emotional patterns, allowing for greater authenticity and emotional freedom."
        ],
        "healing": [
            "Breathwork for Emotional Release",
            "Deep breathing to release emotional blockages and restore inner calm.",
            [
                "child should sit comfortably, focusing on their breath.",
                "Inhale deeply for 4 counts, imagining positive energy entering the body.",
                "Hold the breath for 4 counts, then slowly exhale for 6 counts, releasing tension."
            ],
            "Repeat for 5-10 minutes, especially when feeling emotionally stuck or tense.",
            "Breathwork clears emotional tension, promoting healing and emotional freedom."
        ],
        "mudra": [
            "The Surya Mudra for Confidence",
            "This mudra enhances self-confidence and emotional balance.",
            [
                "child should sit with their back straight, palms facing upward.",
                "Touch the ring finger to the base of the thumb while keeping the other fingers extended.",
                "Focus on deep breathing and visualize feelings of self-assurance and inner strength."
            ],
            "Hold the mudra for 5-10 minutes daily.",
            "The Surya Mudra promotes confidence and emotional balance, helping to release fear of rejection and insecurity."
        ]
    }
],
  "Virgo": [
    "child's subconscious mind with the 8th house in Virgo may be highly analytical and detail-oriented, but this can sometimes lead to subconscious worry and overthinking. There might be a tendency to focus on perfectionism, which can create emotional barriers or resistance to change. child may subconsciously feel the need to control every detail of life to feel safe, leading to anxiety when things are out of order or when they are unable to meet high standards. These deep-seated concerns can cause them to resist transformation or emotional depth, as they focus too much on fixing external situations rather than allowing internal growth.",
    [
        {
            "title": "Perfectionism",
            "content": "A subconscious drive to make everything perfect, which can lead to frustration or avoidance of emotional expression."
        },
        {
            "title": "Worry and Overthinking",
            "content": "A tendency to overanalyze, creating mental and emotional stress."
        },
        {
            "title": "Fear of Imperfection",
            "content": "Subconscious fears of making mistakes or being judged for not being 'good enough.'"
        },
        {
            "title": "Difficulty Letting Go",
            "content": "A tendency to hold on to minor details or past events, preventing emotional healing."
        },
        {
            "title": "Resistance to Vulnerability",
            "content": "Fear of being imperfect or judged may lead child to avoid emotional depth or change."
        }
    ],
    {
        "manifestation": [
            "Affirmations for Self-Acceptance and Relaxation",
            "Use affirmations to release the need for perfectionism and embrace emotional growth.",
            [
                "I am enough just as I am, without needing to be perfect.",
                "I release worry and trust the process of growth."
            ],
            "Repeat these affirmations 5 times in the morning and evening.",
            "Affirmations can help child shift from perfectionism to self-acceptance and emotional openness."
        ],
        "quantum": [
            "Energy Release for Emotional Freedom",
            "Visualize releasing control over minor details and shifting to emotional freedom.",
            [
                "child should sit quietly and focus on deep breathing.",
                "Visualize holding tightly to mental clutter or perfectionist tendencies.",
                "See these tensions dissolving and being replaced with a feeling of peace and calm."
            ],
            "Practice for 5 minutes daily.",
            "Visualization helps release the need for perfection and fosters emotional freedom."
        ],
        "healing": [
            "Guided Breathing for Letting Go",
            "Focused breathing to release emotional tension and let go of control.",
            [
                "child should sit comfortably with hands on the belly.",
                "Inhale deeply through the nose for 4 counts, expanding the belly.",
                "Exhale through the mouth for 6 counts, releasing tension in the body."
            ],
            "Repeat for 5-10 minutes to promote relaxation and release anxiety.",
            "Breathing helps reduce mental chatter and fosters emotional healing."
        ],
        "mudra": [
            "The Apana Mudra for Emotional Release",
            "This mudra helps let go of control and release emotional tension.",
            [
                "child should sit with their back straight and palms facing upward.",
                "Touch the tips of the middle and ring fingers to the tips of the thumb.",
                "Focus on breathing and releasing any emotional tension."
            ],
            "Hold for 5-10 minutes each day.",
            "The Apana Mudra helps release deep-seated emotions and brings emotional calm."
        ]
    }
],
  "Libra": [
    "child's subconscious mind with the 8th house in Libra may have a deep-seated need for balance, harmony, and justice, which could cause them to avoid confronting difficult emotions. child might fear conflict and might subconsciously suppress their own needs or emotions in favor of keeping peace or seeking approval from others. This can create challenges in standing up for themselves and expressing personal boundaries, as they might fear alienating others or being seen as confrontational. The desire for balanced relationships may sometimes create unconscious emotional imbalances, where child struggles to deal with personal conflicts.",
    [
        {
            "title": "Fear of Conflict",
            "content": "Subconscious fear of disagreements or being judged can lead to emotional avoidance."
        },
        {
            "title": "Lack of Self-Assertion",
            "content": "Difficulty expressing personal boundaries or asserting their own needs."
        },
        {
            "title": "People-Pleasing",
            "content": "A tendency to prioritize others' needs over their own, creating internal resentment."
        },
        {
            "title": "Over-Reliance on Relationships",
            "content": "Subconscious belief that their worth is tied to how well they relate to others."
        },
        {
            "title": "Avoidance of Emotional Depth",
            "content": "Fear of deep emotional confrontations or conflicts, leading to emotional detachment."
        }
    ],
    {
        "manifestation": [
            "Affirmations for Healthy Boundaries and Confidence",
            "Use affirmations to encourage emotional independence and self-assertion.",
            [
                "I honor my emotions and express my needs confidently.",
                "I create healthy boundaries with others and respect my personal space."
            ],
            "Repeat these affirmations 5 times each morning.",
            "Affirmations help shift subconscious beliefs towards healthy self-expression and boundaries."
        ],
        "quantum": [
            "Energy Release for Emotional Independence",
            "Visualize emotional energy being released to create independence from others' expectations.",
            [
                "child should sit comfortably and close their eyes.",
                "Visualize energetic cords connecting them to others, draining their emotional energy.",
                "See these cords dissolving, and feel the energy returning to them as an aura of confidence and independence."
            ],
            "Practice this visualization for 5 minutes daily.",
            "Visualization helps child disconnect from emotional reliance on others and strengthens their personal energy."
        ],
        "healing": [
            "Heart-Centered Breathing for Inner Balance",
            "Use deep breathing to calm emotions and restore balance within the heart.",
            [
                "child should sit comfortably and place hands on the heart.",
                "Inhale deeply for 4 counts, imagining love and balance flowing into the heart.",
                "Exhale slowly for 6 counts, releasing any emotional tension or conflict."
            ],
            "Repeat for 5-10 minutes to calm the mind and restore emotional balance.",
            "Heart-centered breathing promotes emotional calm, helping to manage anxiety and maintain balance."
        ],
        "mudra": [
            "The Apan Vayu Mudra for Emotional Clarity",
            "This mudra helps release emotional tension and encourages clarity in relationships.",
            [
                "child should sit comfortably with palms facing upward.",
                "Touch the tips of the index and middle fingers to the tips of the thumb, keeping the other fingers extended.",
                "Focus on breathing deeply, allowing clarity and emotional healing."
            ],
            "Hold for 5-10 minutes daily.",
            "The Apan Vayu Mudra promotes emotional clarity and balance, helping to reduce conflicts."
        ]
    }
],
  "Sagittarius": [
    "child's subconscious mind with the 8th house in Sagittarius could have a deep desire for freedom, expansion, and exploration. However, this can lead to subconscious resistance to emotional depth or change, as child may be more focused on seeking external adventure rather than confronting internal emotions. The fear of being confined or restricted may cause them to suppress deeper feelings or avoid situations that require emotional intimacy. This desire for freedom and exploration can sometimes manifest as emotional detachment or avoidance of personal transformation.",
    [
        {
            "title": "Fear of Emotional Confinement",
            "content": "Subconscious fear of being restricted emotionally or mentally."
        },
        {
            "title": "Avoidance of Deep Connections",
            "content": "A tendency to avoid emotional depth or commitment in relationships."
        },
        {
            "title": "Restlessness and Escapism",
            "content": "A tendency to escape difficult emotions by seeking constant change or adventure."
        },
        {
            "title": "Difficulty Confronting the Past",
            "content": "Subconscious avoidance of unresolved issues or emotional wounds."
        },
        {
            "title": "Fear of Limitation",
            "content": "Fear that emotional depth might limit their freedom or personal growth."
        }
    ],
    {
        "manifestation": [
            "Affirmations for Emotional Freedom and Deep Connection",
            "Use affirmations to encourage emotional depth and openness.",
            [
                "I embrace emotional depth and trust in the process of personal transformation.",
                "I am free to explore both my inner world and the world around me."
            ],
            "Repeat these affirmations 5 times each morning.",
            "Affirmations promote the integration of emotional depth with the need for freedom and exploration."
        ],
        "quantum": [
            "Energy Transformation for Emotional Liberation",
            "Visualize the release of emotional confinement and the expansion of inner freedom.",
            [
                "child should sit comfortably and breathe deeply.",
                "Visualize a ball of restrictive energy surrounding their heart area.",
                "See this energy dissolving into light, allowing freedom and emotional openness to fill the space."
            ],
            "Practice for 3-5 minutes daily.",
            "Visualization helps child release emotional blockages and integrate the need for freedom with emotional depth."
        ],
        "healing": [
            "Breathwork for Grounding and Emotional Release",
            "Focused breathing to ground and release any restlessness or emotional avoidance.",
            [
                "child should sit with feet firmly planted on the ground.",
                "Inhale deeply for 4 counts, imagining stability and grounding energy flowing into the body.",
                "Exhale slowly for 6 counts, releasing any emotional restlessness or escapism."
            ],
            "Repeat for 5-10 minutes to calm the mind and restore emotional balance.",
            "Breathwork helps anchor the mind, fostering emotional release and stability."
        ],
        "mudra": [
            "The Apan Mudra for Emotional Release and Balance",
            "This mudra helps release emotional blocks and brings balance to the mind.",
            [
                "child should sit with their back straight and palms facing upward.",
                "Touch the tips of the middle and ring fingers to the tips of the thumb.",
                "Focus on deep breathing, releasing emotional tension and seeking balance."
            ],
            "Hold for 5-10 minutes daily.",
            "The Apan Mudra encourages emotional release and brings balance to both the body and mind."
        ]
    }
],
  "Capricorn": [
    "child's subconscious mind with the 8th house in Capricorn might be heavily focused on responsibility, discipline, and achievement. There could be a subconscious fear of failure, which might make them overly cautious or resistant to emotional vulnerability. The need for control and structure may cause them to suppress their deeper feelings, as they fear that emotional instability will interfere with their sense of control. This can create emotional barriers, as child may subconsciously believe that feelings of vulnerability or emotional expression will hinder their goals or success.",
    [
        {
            "title": "Fear of Failure",
            "content": "Subconscious fear of not meeting their own or others' expectations, leading to emotional avoidance."
        },
        {
            "title": "Emotional Suppression",
            "content": "A tendency to suppress emotions in favor of maintaining control or achieving goals."
        },
        {
            "title": "Over-Responsibility",
            "content": "Taking on too much responsibility subconsciously, leading to emotional exhaustion."
        },
        {
            "title": "Fear of Vulnerability",
            "content": "A subconscious belief that showing vulnerability will weaken their emotional strength."
        },
        {
            "title": "Difficulty Trusting Others",
            "content": "Fear that relying on others emotionally might hinder their personal growth or success."
        }
    ],
    {
        "manifestation": [
            "Affirmations for Emotional Release and Trust",
            "Use affirmations to promote emotional vulnerability and self-acceptance.",
            [
                "I trust myself and allow emotions to flow freely without fear.",
                "I embrace vulnerability as a source of strength."
            ],
            "Repeat these affirmations 5 times each morning.",
            "Affirmations help shift the subconscious mind from fear to emotional trust and openness."
        ],
        "quantum": [
            "Energy Clearing for Emotional Freedom",
            "Visualize clearing emotional blocks that hinder vulnerability and trust.",
            [
                "child should sit with eyes closed and take a deep breath.",
                "Visualize a cloud of emotional tension surrounding their heart, holding them back.",
                "See the cloud dissolving, replaced with light and emotional freedom."
            ],
            "Practice for 3-5 minutes daily.",
            "Visualization helps child release emotional blockages and embrace emotional freedom."
        ],
        "healing": [
            "Heart-Centered Breathing for Emotional Vulnerability",
            "Focused breathing to open the heart and release emotional barriers.",
            [
                "child should sit with hands on their heart, eyes closed.",
                "Inhale deeply for 4 counts, imagining warmth and openness filling the heart.",
                "Exhale slowly for 6 counts, releasing any fear or tension around vulnerability."
            ],
            "Repeat for 5-10 minutes daily.",
            "This practice helps dissolve fears around emotional vulnerability and fosters trust."
        ],
        "mudra": [
            "The Prithvi Mudra for Emotional Grounding",
            "This mudra encourages emotional grounding and stability.",
            [
                "child should sit comfortably with palms facing upward.",
                "Touch the tips of the ring finger and thumb together.",
                "Focus on deep, calming breaths, allowing the earth's energy to ground and stabilize emotions."
            ],
            "Hold for 5-10 minutes daily.",
            "The Prithvi Mudra promotes grounding and stability, helping child manage emotional suppression."
        ]
    }
],
    "Aquarius": [
    "child's subconscious mind with the 8th house in Aquarius could be influenced by a need for freedom and independence in both thoughts and emotions. However, this desire for detachment and non-conformity might make them unconsciously avoid emotional connection or vulnerability. They might fear being too emotionally invested or dependent on others, and this could create barriers to true intimacy. child may also have an unconscious belief that deep emotions are irrational or disruptive to their sense of independence.",
    [
        {
            "title": "Fear of Emotional Dependency",
            "content": "Subconscious fear of being too emotionally attached to others."
        },
        {
            "title": "Emotional Detachment",
            "content": "Tendency to detach from emotional experiences in favor of intellectual reasoning."
        },
        {
            "title": "Avoidance of Intimacy",
            "content": "Difficulty forming deep emotional connections due to fear of loss of independence."
        },
        {
            "title": "Fear of Being Misunderstood",
            "content": "Feeling that others cannot understand or accept their unique emotional world."
        },
        {
            "title": "Over-Intellectualization",
            "content": "Tendency to intellectualize emotions rather than experiencing them."
        }
    ],
    {
        "manifestation": [
            "Affirmations for Emotional Openness and Connection",
            "Use affirmations to foster emotional connection and openness.",
            [
                "I am open to forming deep emotional connections with others.",
                "I trust in the value of emotional intimacy and sharing my feelings."
            ],
            "Repeat these affirmations 5 times in the morning.",
            "Affirmations help shift child's mindset towards emotional openness and trust."
        ],
        "quantum": [
            "Energy Release for Emotional Freedom",
            "Visualize releasing emotional barriers and fostering openness.",
            [
                "child should sit with eyes closed and take a few deep breaths.",
                "Visualize an emotional barrier around the heart area dissolving into light.",
                "See themselves opening up emotionally and feeling free to connect with others."
            ],
            "Practice for 5 minutes daily.",
            "Visualization helps child let go of emotional detachment and open up to connection."
        ],
        "healing": [
            "Breathwork for Emotional Release and Openness",
            "Use deep breathing to release emotional blockages and encourage openness.",
            [
                "child should sit with hands on their chest, focusing on the breath.",
                "Inhale deeply for 4 counts, filling the chest with air.",
                "Exhale for 6 counts, imagining emotional blockages dissolving."
            ],
            "Repeat for 5-10 minutes.",
            "Deep breathing can help dissolve emotional detachment and foster openness."
        ],
        "mudra": [
            "The Shunya Mudra for Emotional Awareness",
            "This mudra helps enhance emotional awareness and openness.",
            [
                "child should sit comfortably with palms facing upwards.",
                "Touch the tips of the middle finger and thumb together.",
                "Focus on emotional awareness, breathing deeply and calmly."
            ],
            "Hold for 5-10 minutes daily.",
            "The Shunya Mudra helps increase emotional awareness and encourages emotional connection."
        ]
    }
],
    "Pisces": [
    "child's subconscious mind with the 8th house in Pisces may experience deep emotional sensitivity and a tendency to merge with others. However, this intense emotional nature can sometimes lead to subconscious confusion or lack of boundaries. child might struggle with distinguishing their own feelings from those of others, leading to emotional overwhelm or escapism. This can manifest as difficulty processing emotions in a healthy way, as well as a tendency to avoid confronting painful truths.",
    [
        {
            "title": "Emotional Overwhelm",
            "content": "Difficulty distinguishing personal emotions from those of others."
        },
        {
            "title": "Escapism",
            "content": "Subconscious avoidance of painful emotions through daydreaming or fantasy."
        },
        {
            "title": "Lack of Boundaries",
            "content": "Difficulty maintaining healthy emotional boundaries with others."
        },
        {
            "title": "Fear of Emotional Depth",
            "content": "Subconscious fear of facing the full intensity of emotions."
        },
        {
            "title": "Sensitivity to Criticism",
            "content": "Fear of being emotionally hurt by others' judgment or criticism."
        }
    ],
    {
        "manifestation": [
            "Affirmations for Emotional Clarity and Boundaries",
            "Use affirmations to promote emotional clarity and boundary-setting.",
            [
                "I honor my own emotions and maintain healthy boundaries.",
                "I trust myself to navigate emotional experiences with clarity and strength."
            ],
            "Repeat these affirmations 5 times each morning.",
            "Affirmations help create clarity and emotional resilience."
        ],
        "quantum": [
            "Energy Clearing for Emotional Boundaries",
            "Visualize clearing emotional confusion and strengthening personal boundaries.",
            [
                "child should sit comfortably and focus on their breath.",
                "Visualize a protective shield surrounding their aura, keeping others' emotions separate.",
                "See any emotional confusion dissolving, allowing clarity and peace to fill their mind."
            ],
            "Practice for 5 minutes daily.",
            "Visualization helps create stronger emotional boundaries and reduces overwhelm."
        ],
        "healing": [
            "Guided Breathing for Grounding and Emotional Clarity",
            "Grounding breathwork to enhance emotional clarity and release overwhelm.",
            [
                "child should sit with feet firmly on the ground.",
                "Inhale deeply for 4 counts, grounding their energy into the earth.",
                "Exhale slowly for 6 counts, releasing emotional tension and confusion."
            ],
            "Repeat for 5-10 minutes.",
            "This practice calms the mind, helping child release emotional overwhelm and find clarity."
        ],
        "mudra": [
            "The Prana Mudra for Emotional Strength",
            "This mudra promotes emotional strength and clarity.",
            [
                "child should sit comfortably with palms facing upwards.",
                "Touch the tips of the thumb, ring, and little fingers together.",
                "Focus on deep, calming breaths, allowing emotional clarity to emerge."
            ],
            "Hold for 5-10 minutes daily.",
            "The Prana Mudra helps enhance emotional clarity, strength, and stability."
        ]
    }
],
    "Scorpio": [
        "child's subconscious mind might be shaped by deep, powerful emotions and intense experiences. With a Scorpio influence, there could be a strong desire to control situations or emotions to avoid feeling vulnerable. This may lead to a tendency to hide emotions or resist change, especially when feeling threatened. Fear of betrayal or being hurt could create subconscious blocks, affecting trust in others and making it difficult to embrace growth. These hidden feelings may sometimes prevent child from fully expressing themselves or opening up to new possibilities.",
        [
            {
                "title": "Fear of Vulnerability",
                "content": "child might subconsciously guard emotions and resist expressing feelings due to a fear of being hurt or betrayed."
            },
            {
                "title": "Trust Issues",
                "content": "There may be difficulty trusting others, particularly due to past experiences or fear of betrayal."
            },
            {
                "title": "Intense Emotions",
                "content": "Strong emotional reactions, such as jealousy or anger, could arise unexpectedly, creating inner turmoil."
            },
            {
                "title": "Resistance to Change",
                "content": "Subconscious fear of change or the unknown can create emotional blockages that prevent growth."
            },
            {
                "title": "Holding onto the Past",
                "content": "child may struggle to let go of past emotional wounds, keeping them stuck in unresolved feelings or memories."
            }
        ],
        {
            "manifestation": [
                "Affirmations for Trust and Transformation",
                "Use daily affirmations to help child embrace trust, change, and emotional openness.",
                [
                    "I trust myself and others to create positive connections.",
                    "I embrace change and allow transformation to happen with ease.",
                    "I release past fears and open my heart to new possibilities."
                ],
                "Repeat each affirmation 5 times each morning, feeling the meaning of each word.",
                "Affirmations can reprogram the subconscious mind, helping to shift negative beliefs and promote trust and transformation."
            ],
            "quantum": [
                "Thought & Emotion Formatting for Positive Vibrations",
                "Visualize thoughts and emotions as energy patterns that can be changed to raise vibrations and attract positive outcomes.",
                [
                    "child should sit comfortably, close their eyes, and focus on their breath.",
                    "Visualize thoughts as colors: negative thoughts could be gray or dark, while positive thoughts are bright and vibrant.",
                    "See the gray thoughts slowly transforming into bright colors, feeling the emotional shift as the energy becomes lighter and more positive."
                ],
                "Practice for 3-5 minutes, twice a day, ideally after waking up and before bed.",
                "This visualization technique helps change the emotional frequency of the body, shifting negative energy into positive vibrations, improving overall mood and well-being."
            ],
            "healing": [
                "Releasing Emotional Blockages with Deep Breathing",
                "Deep breathing can help release stored emotional tension, especially from past experiences.",
                [
                    "child should sit comfortably and close their eyes.",
                    "Inhale deeply through the nose for a count of 4, imagining positive energy filling the body.",
                    "Hold the breath for 4 counts, letting the energy settle.",
                    "Exhale slowly for 6 counts, imagining all negative emotions leaving the body."
                ],
                "Repeat this breathing pattern for 5-10 minutes daily, especially when feeling overwhelmed or tense.",
                "Deep breathing promotes relaxation and helps release repressed emotions, bringing emotional clarity and peace."
            ],
            "mudra": [
                "The Prana Mudra for Emotional Healing",
                "This mudra helps to restore balance, increase energy, and promote emotional healing.",
                [
                    "child should sit with a straight back, either in a chair or on the floor.",
                    "Place the tips of the ring and little fingers to the tip of the thumb, while keeping the index and middle fingers extended.",
                    "Rest the hands on the knees with the palms facing upward.",
                    "Focus on breathing deeply, keeping the mind calm and focused on the sensation in the hands."
                ],
                "Hold this mudra for 5-10 minutes daily, ideally before bedtime.",
                "The Prana Mudra increases the flow of life energy (prana), helping to heal emotional wounds and balance the body's energy system."
            ]
        }
    ]
}

nakshatraContent = {
    'Ashwini': [
    {
        "name": "Prince Charles",
        "famous": "Heir to the British throne, philanthropy, charity",
        "nakshatra": "Attractive personality, gives hope to others, charity, religious."
    },
    {
        "name": "Sania Mirza",
        "famous": "Tennis player",
        "nakshatra": "Attractive personality"
    },
    {
        "name": "Yukta Mookhey",
        "famous": "Miss World",
        "nakshatra": "Beautiful, attractive personality"
    },
    {
        "name": "Jacqueline Kennedy Onassis",
        "famous": "Wife of US President John.F.Kennedy, fashion icon",
        "nakshatra": "Attractive personality"
    },
    {
        "name": "Jerry Lewis",
        "famous": "American Comedian",
        "nakshatra": "Interest in acting, music, charity"
    },
    {
        "name": "Alfred Adler",
        "famous": "Austrian Psychotherapist",
        "nakshatra": "Healing"
    },
    {
        "name": "Bruce Lee",
        "famous": "Actor",
        "nakshatra": "Interest in acting"
    },
    {
        "name": "Richard Tamas",
        "famous": "Cultural Historian and Astrologer",
        "nakshatra": "Intelligent, bright, interest in spirituality"
    },
    {
        "name": "Aldous Huxley",
        "famous": "Writer and Philosopher",
        "nakshatra": "Intelligent, interest in philosophy"
    },
    {
        "name": "Ingrid Bergman",
        "famous": "Swedish actress",
        "nakshatra": "Beautiful, interest in acting"
    },
    {
        "name": "Geena Davis",
        "famous": "American actress",
        "nakshatra": "Beautiful, interest in acting"
    },
    {
        "name": "Pamela Anderson",
        "famous": "American actress",
        "nakshatra": "Beautiful, interest in acting"
    },
    {
        "name": "Selena Gomez",
        "famous": "Singer",
        "nakshatra": "Beautiful. interest in music"
    }
], 
    'Bharani': [
    {
        "name": "C.G.Jung",
        "famous": "Psychiatrist",
        "nakshatra": "Investigative mind."
    },
    {
        "name": "Karl Marx",
        "famous": "Philosopher",
        "nakshatra": "Leadership, public life."
    },
    {
        "name": "Elton John",
        "famous": "Singer",
        "nakshatra": "Charismatic, public life."
    },
    {
        "name": "Oliver Stone",
        "famous": "Filmmaker",
        "nakshatra": "Public life, literary skills."
    },
    {
        "name": "Edgar Cayce",
        "famous": "Clairvoyant",
        "nakshatra": "Occult."
    },
    {
        "name": "James Braha",
        "famous": "Writer",
        "nakshatra": "Literary skills."
    },
    {
        "name": "Carlos Castaneda",
        "famous": "Writer",
        "nakshatra": "Literary skills."
    },
    {
        "name": "Tonya Harding",
        "famous": "Skater",
        "nakshatra": "Attractive, public life."
    },
    {
        "name": "Sir Ashutosh Mukherjee",
        "famous": "Jurist, educationist",
        "nakshatra": "Public life, leadership"
    },
    {
        "name": "Swami Shivananda",
        "famous": "Spiritual Guru",
        "nakshatra": "Charismatic, public life, healthy."
    },
    {
        "name": "Mahboob Ali Khan - the Nizam of Hyderabad",
        "famous": "Ruler",
        "nakshatra": "Poetic skills."
    }
],
    'Krittika': [
    {
        "name": "Guru Nanak",
        "famous": "Spiritual Guru",      
        "nakshatra": "Famous, preceptor."
    },
    {
        "name": "Bill Clinton",
        "famous": "US President",        
        "nakshatra": "Attractive personality, famous."
    },
    {
        "name": "Ronald Reagan",
        "famous": "US President",
        "nakshatra": "Intelligent, unstable decisions."
    },
    {
        "name": "Bob Dylan",
        "famous": "Musician",
        "nakshatra": "Peaceful, good in advising."
    },
    {
        "name": "Frida Kahlo",
        "famous": "Painter",
        "nakshatra": "Engaged in arts."
    },
    {
        "name": "Mick Jagger",
        "famous": "Singer",
        "nakshatra": "Living away from the place of birth."
    },
    {
        "name": "Gregory Peck",
        "famous": "Actor",
        "nakshatra": "Good periods - 25 to 35 years, 50 to 55 years."
    },
    {
        "name": "Peter Sellers",
        "famous": "Actor",
        "nakshatra": "Attached to mother."
    },
    {
        "name": "Jimmy Hoffa",
        "famous": "Labor leader",
        "nakshatra": "Combative."
    }
],
    'Rohini': [
    {
        "name": "Lord Krishna",
        "famous": "Avatara of Vishnu",
        "nakshatra": "Brilliant, attractive eyes."
    },
    {
        "name": "Werner Erhard",
        "famous": "Author",
        "nakshatra": "Leadership, wealthy."
    },
    {
        "name": "Queen Victoria",
        "famous": "Legacy,'Empire",
        "nakshatra": "Power, popularity."
    },
    {
        "name": "Michelle Pfeiffer",
        "famous": "Actress",
        "nakshatra": "Attractive, popular."
    },
    {
        "name": "Burt Reynolds",
        "famous": "Actor",
        "nakshatra": "Attractive, popular."
    },
    {
        "name": "General Franco",
        "famous": "Military General",
        "nakshatra": "Power."
    },
    {
        "name": "John Milton",
        "famous": "Poet",
        "nakshatra": "Poetic skills."
    },
    {
        "name": "Bernard Shaw",
        "famous": "Playwright",
        "nakshatra": "Literature."
    }
],
    'Mrigashira': [
    {
        "name": "Dr. Rajendra Prasad", 
        "famous": "Indian President",  
        "nakshatra": "Political power" 
    },
    {
        "name": "Dr. B.V.Raman",       
        "famous": "Astrologer, Author",
        "nakshatra": "Intelligent, writing skills."
    },
    {
        "name": "Walter Mondale",
        "famous": "US Vice President",
        "nakshatra": "Political power, wealth."
    },
    {
        "name": "Shirley Temple",
        "famous": "Ambassador",
        "nakshatra": "Religious."
    },
    {
        "name": "Brooke Shields",
        "famous": "Actress",
        "nakshatra": "Attractive, popular, bold."
    },
    {
        "name": "Doris Day",
        "famous": "Actress",
        "nakshatra": "Attractive, popular"
    }
],
    'Ardra': [
    {
        "name": "Adi Shankaracharya",
        "famous": "Spiritual leader",
        "nakshatra": "Knowledge."    
    },
    {
        "name": "Ramanujacharya",    
        "famous": "Spiritual leader",
        "nakshatra": "Knowledge."
    },
    {
        "name": "Swami Kriyananda",
        "famous": "Spiritual leader",
        "nakshatra": "Writing skills."
    },
    {
        "name": "Albert Einstein",
        "famous": "Scientist",
        "nakshatra": "Intelligent."
    },
    {
        "name": "Hilary Clinton",
        "famous": "Politician",
        "nakshatra": "Communication skills."
    },
    {
        "name": "Ross Perot",
        "famous": "Businessman",
        "nakshatra": "Indecisiveness."
    },
    {
        "name": "Babe Ruth",
        "famous": "Baseball player",
        "nakshatra": "Athletic, skillful."
    },
    {
        "name": "Marie Antoinette",
        "famous": "French Queen",
        "nakshatra": "Ungrateful."
    }
],
    'Punarvasu':[
    {
        "name": "Ramana Maharshi",
        "famous": "Spiritual leader",
        "nakshatra": "Knowledge, self-control."
    },
    {
        "name": "Bob Hope",
        "famous": "Comedian",
        "nakshatra": "Happy, contented."
    },
    {
        "name": "Jerry Brown",
        "famous": "Governor of California",
        "nakshatra": "Communication skills, self-control."
    },
    {
        "name": "Paul Simon",
        "famous": "Singer",
        "nakshatra": "Troubled marriage."
    },
    {
        "name": "Ira Progoff",
        "famous": "Psychotherapist",
        "nakshatra": "Writing skills."
    }
],
    'Pushya': [
    {
        "name": "Thyagaraja",
        "famous": "Carnatic music composer",
        "nakshatra": "Short-tempered."      
    },
    {
        "name": "Arnold Schwarzenegger",    
        "famous": "Actor",
        "nakshatra": "Wealthy, successful."
    },
    {
        "name": "Maxfield Parrish",
        "famous": "Painter",
        "nakshatra": "Artistic, sensitive."
    },
    {
        "name": "Janet Reno",
        "famous": "US Attorney General",
        "nakshatra": "Systematic."
    },
    {
        "name": "Mussolini",
        "famous": "Dictator",
        "nakshatra": "Arrogance."
    }
],
    'Ashlesha': [
    {
        "name": "Mahatma Gandhi",
        "famous": "Nonviolence",
        "nakshatra": "Leadership, political success."
    },
    {
        "name": "Jawaharlal Nehru",
        "famous": "Indian Prime Minister",
        "nakshatra": "Leadership, political success."
    },
    {
        "name": "Paul McCartney",
        "famous": "Singer",
        "nakshatra": "Mystical."
    },
    {
        "name": "Bepin Bihari",
        "famous": "Astrologer, author",
        "nakshatra": "Skill in the occult, literary skills."
    },
    {
        "name": "Robert Bly",
        "famous": "Poet",
        "nakshatra": "Literary skills."
    },
    {
        "name": "Dennis Harness",
        "famous": "Astrologer",
        "nakshatra": "Skill in the occult."
    },
    {
        "name": "Marc Edmund Jones",
        "famous": "Writer",
        "nakshatra": "Literary skills."
    },
    {
        "name": "Barbara Streisand",
        "famous": "Singer",
        "nakshatra": "Troubled marriage."
    },
    {
        "name": "Oscar Wilde",
        "famous": "Poet",
        "nakshatra": "Literary skills."
    }
],
    'Magha': [
    {
        "name": "Paramahansa Yogananda",     
        "famous": "Spiritual leader",        
        "nakshatra": "Honored and respected."
    },
    {
        "name": "Maharshi Mahesh Yogi",      
        "famous": "Spiritual leader",        
        "nakshatra": "Honored and respected."
    },
    {
        "name": "Winston Churchill",
        "famous": "British Prime Minister",
        "nakshatra": "Public relations, popularity."
    },
    {
        "name": "Dennis Flaherty",
        "famous": "Astrologer",
        "nakshatra": "Skill in the occult.."
    },
    {
        "name": "Walt Whitman",
        "famous": "Poet",
        "nakshatra": "Enjoys life."
    },
    {
        "name": "Joseph Stalin",
        "famous": "Russian Premier",
        "nakshatra": "Short-tempered."
    }
],
    'Purva Phalguni': [
    {
        "name": "Chaitanya Mahaprabhu",       
        "famous": "Spiritual leader",
        "nakshatra": "Attractive personality."
    },
    {
        "name": "Dustin Hoffman",
        "famous": "Actor",
        "nakshatra": "Creative, intelligent."
    },
    {
        "name": "John F Kennedy",
        "famous": "US President",
        "nakshatra": "Leadership qualities."
    },
    {
        "name": "John Travolta",
        "famous": "Actor",
        "nakshatra": "Fond of traveling."
    },
    {
        "name": "Robert Redford",
        "famous": "Actor",
        "nakshatra": "Handsome, sweet talking."
    },
    {
        "name": "Shirley McLaine",
        "famous": "Actress",
        "nakshatra": "`Mystical, teaching skills."
    },
    {
        "name": "Madonna",
        "famous": "Singer",
        "nakshatra": "Troubled mind."
    }
], 'Uttara Phalguni': [
    {
        "name": "Shuddhananda Bharati",
        "famous": "Philosopher",       
        "nakshatra": "Learned, noble." 
    },
    {
        "name": "Sean Connery",        
        "famous": "Actor",
        "nakshatra": "Popular, wealthy."
    },
    {
        "name": "Jack Nicholson",
        "famous": "Actor",
        "nakshatra": "Respected, luxury in life."
    },
    {
        "name": "Alexander Graham Bell",
        "famous": "Inventor",
        "nakshatra": "Intelligent."
    },
    {
        "name": "Jonathan Winters",
        "famous": "Comedian",
        "nakshatra": "Happy, winters."
    },
    {
        "name": "Mel Gibson",
        "famous": "Actor",
        "nakshatra": "Good period 38 to 62 years."
    },
    {
        "name": "Agatha Christie",
        "famous": "Writer",
        "nakshatra": "Clean-hearted, independent."
    }
], 'Hasta': [
    {
        "name": "Swami Vivekananda",
        "famous": "Spiritual leader",
        "nakshatra": "Knowledgeable, attractive character, self-discipline."
    },
    {
        "name": "Jagdish Chandra Bose",
        "famous": "Physicist",
        "nakshatra": "Knowledgeable, inquisitive."
    },
    {
        "name": "Jimmy Carter",
        "famous": "US President",
        "nakshatra": "Wealth late in life, leadership qualities."
    },
    {
        "name": "Rudolph Valentino",
        "famous": "Actor",
        "nakshatra": "Attractive, sweet smile."
    },
    {
        "name": "Burt Reynolds",
        "famous": "Actor",
        "nakshatra": "Friendly."
    },
    {
        "name": "Robert Duvall",
        "famous": "Actor",
        "nakshatra": "Moody nature."
    },
    {
        "name": "Richard Burton",
        "famous": "Actor",
        "nakshatra": "Cunning nature."
    }
],'Chitra': [
    {
        "name": "Chhatrapati Shivaji Maharaj",
        "famous": "Ruler",
        "nakshatra": "Visionary, fearless."   
    },
    {
        "name": "Krishnaraja Wadiyar IV",     
        "famous": "Ruler",
        "nakshatra": "Interest in music and arts."
    },
    {
        "name": "Richard Chamberlain",
        "famous": "Actor",
        "nakshatra": "Handsome, artistic."
    },
    {
        "name": "George Bush",
        "famous": "US President",
        "nakshatra": "Popular, leadership qualities."
    },
    {
        "name": "Nicholas cage",
        "famous": "Actor",
        "nakshatra": "Popular."
    },
    {
        "name": "Dwight Eisenhower",
        "famous": "US President",
        "nakshatra": "Popular, leadership qualities."
    },
    {
        "name": "Marie Antoinette",
        "famous": "Queen of France",
        "nakshatra": "Troubled marriage."
    }
], 'Swati': [
    {
        "name": "Meher Baba",
        "famous": "Spiritual leader",
        "nakshatra": "Righteous, compassionate."
    },
    {
        "name": "Charlie Chaplin",
        "famous": "Comedian",
        "nakshatra": "Intelligent, famous."
    },
    {
        "name": "Harry Truman",
        "famous": "US President",
        "nakshatra": "Adamant, short-tempered."
    },
    {
        "name": "James Dean",
        "famous": "Actor",
        "nakshatra": "Troubled marriage."
    },
    {
        "name": "Nelson Rockefeller",
        "famous": "US Vice President",
        "nakshatra": "Wealthy."
    },
    {
        "name": "Edith Hathaway",
        "famous": "Author",
        "nakshatra": "Charitable."
    }
], 'Vishakha':[
    {
        "name": "Gautam Buddha",
        "famous": "Spiritual leader",
        "nakshatra": "Kindness, sweet talking, intelligence."
    },
    {
        "name": "Swami Muktananda",
        "famous": "Spiritual leader",
        "nakshatra": "Intelligent."
    },
    {
        "name": "Robert Handerson",
        "famous": "Author",
        "nakshatra": "Writing skills, ability to convince."
    },
    {
        "name": "Warren Beatty",
        "famous": "Actor",
        "nakshatra": "Attractive, popular."
    },
    {
        "name": "Alexander",
        "famous": "Ruler",
        "nakshatra": "Lives away from family, leadership qualities."
    },
    {
        "name": "Mario Cuomo",
        "famous": "NY Governor",
        "nakshatra": "Humanitarian."
    }
], 'Anuradha': [
    {
        "name": "Alex Haley",
        "famous": "Writer",
        "nakshatra": "Wise, honest, kind."
    },
    {
        "name": "Kevin Costner",
        "famous": "Actor",
        "nakshatra": "Charismatic, hardworking, brave."
    },
    {
        "name": "Steve Allen",
        "famous": "T.V. personality",
        "nakshatra": "Troubled marriage."
    },
    {
        "name": "Saddam Hussein",
        "famous": "Ruler",
        "nakshatra": "Determined."
    },
    {
        "name": "Gerard Depardieu",
        "famous": "Actor",
        "nakshatra": "Determined."
    }
], 'Jyeshtha': [
    {
        "name": "Friedrich Nietzche",   
        "famous": "Philosopher",        
        "nakshatra": "Noble, irritable."
    },
    {
        "name": "Mozart",
        "famous": "Composer",
        "nakshatra": "Talent in music."
    },
    {
        "name": "Beethoven",
        "famous": "Composer",
        "nakshatra": "Talent in music."
    },
    {
        "name": "Al Pacino",
        "famous": "Actor",
        "nakshatra": "Physical strength."
    },
    {
        "name": "Vincent Van Gogh",
        "famous": "Painter",
        "nakshatra": "Trouble in early life."
    },
    {
        "name": "Howard Hughes",
        "famous": "Businessman",
        "nakshatra": "Wealthy."
    }
], 'Mula': [
    {
        "name": "Sri Aurobindo",
        "famous": "Spiritual leader",
        "nakshatra": "Spiritually oriented, charitable."
    },
    {
        "name": "Ramakrishna Dalmia",
        "famous": "Businessman",
        "nakshatra": "Wealthy, charitable."
    },
    {
        "name": "Dalai Lama",
        "famous": "Spiritual leader",
        "nakshatra": "Peace-loving, spiritually oriented."
    },
    {
        "name": "Al Gore",
        "famous": "US Vice President",
        "nakshatra": "Proud, attractive."
    },
    {
        "name": "Billy Graham",
        "famous": "Evangelist",
        "nakshatra": "Communication skills. success in foreign lands."
    },
    {
        "name": "Judy Garland",
        "famous": "Actress",
        "nakshatra": "Wealthy, spendthrift."
    }
],'Purva Ashadha': [
    {
        "name": "Osho",
        "famous": "Spiritual leader",
        "nakshatra": "Attractive, charismatic."
    },
    {
        "name": "Adolf Hitler",
        "famous": "Dictator",
        "nakshatra": "Power to convince, obstinate."
    },
    {
        "name": "Johnny Carson",
        "famous": "T.V.Personality",
        "nakshatra": "Communication skills, intelligent."
    },
    {
        "name": "William James",
        "famous": "Philosopher",
        "nakshatra": "Writing skills."
    },
    {
        "name": "Donna Summer",
        "famous": "Singer",
        "nakshatra": "Attachment to friends."
    }
], 'Uttara Ashadha': [
    {
        "name": "Deepak Chopra",
        "famous": "Author",
        "nakshatra": "Charming, graceful."
    },
    {
        "name": "Abraham Lincoln",        
        "famous": "US President",
        "nakshatra": "Virtuous, charitable, intelligent."
    },
    {
        "name": "Napolean",
        "famous": "Ruler",
        "nakshatra": "Power, leadership qualities."
    },
    {
        "name": "Cary Grant",
        "famous": "Actor",
        "nakshatra": "Popular, many friends."
    },
    {
        "name": "Cat Stevens",
        "famous": "Singer",
        "nakshatra": "Grateful, straightforward."
    },
    {
        "name": "John Lennon",
        "famous": "Singer",
        "nakshatra": "Troubled marriage."
    }
], 'Shravana': [
    {
        "name": "Narasimha Bharati Mahaswamiji",
        "famous": "Spiritual leader",
        "nakshatra": "Religious, sweet talking."
    },
    {
        "name": "David Frawley",
        "famous": "Author",
        "nakshatra": "Intelligent, famous."
    },
    {
        "name": "Henry Ford",
        "famous": "Businessman",
        "nakshatra": "Wealthy, creative."
    },
    {
        "name": "Muhammad Ali",
        "famous": "Boxer",
        "nakshatra": "Principled, charitable."
    },
    {
        "name": "Bruce Willis",
        "famous": "Actor",
        "nakshatra": "Religious, good marriage."
    },
    {
        "name": "Jessica Lange",
        "famous": "Actress",
        "nakshatra": "Foodie, perfectionist."
    }
], 'Dhanishta': [
    {
        "name": "Princess Diana",
        "famous": "British royal family",  
        "nakshatra": "Wealthy, charitable."
    },
    {
        "name": "Timothy Leary",
        "famous": "Psychologist",
        "nakshatra": "Daring, controversial."
    },
    {
        "name": "R Maria Rilke",
        "famous": "Poet",
        "nakshatra": "Mystical, liking for music and poetry."
    },
    {
        "name": "Orson Welles",
        "famous": "Director",
        "nakshatra": "Difficult to convince."
    },
    {
        "name": "Marilyn Monroe",
        "famous": "Actress",
        "nakshatra": "Trouble in marriage."
    }
], 'Shatabhisha': [
    {
        "name": "Paul Newman",
        "famous": "Actor",
        "nakshatra": "Principled, charitable."
    },
    {
        "name": "Michelangelo",
        "famous": "Painter",
        "nakshatra": "Truthful, principled."
    },
    {
        "name": "Goethe",
        "famous": "Poet",
        "nakshatra": "Writing skills, good memory."
    },
    {
        "name": "Ronnie Gale Dreyer",
        "famous": "Author",
        "nakshatra": "Interest in astrology."
    },
    {
        "name": "Robin Williams",
        "famous": "Actor",
        "nakshatra": "Daring, adamant."
    },
    {
        "name": "J Edgar Hoover",
        "famous": "Director, FBI",
        "nakshatra": "Strong opinions, defeat of rivals."
    },
    {
        "name": "Paul Klee",
        "famous": "Artist",
        "nakshatra": "Interest in arts, independent."
    }
], 'Purva Bhadrapada': [
    {
        "name": "Sri Ramakrishna Paramahamsa",
        "famous": "Spiritual leader",
        "nakshatra": "Deeply spiritual, teaching skill."
    },
    {
        "name": "Aleister Crowley",
        "famous": "Occultist",
        "nakshatra": "Interest in the occult."
    },
    {
        "name": "Hugh Hefner",
        "famous": "Publisher",
        "nakshatra": "Skillful at work, wealthy."
    },
    {
        "name": "Robert De Niro",
        "famous": "Actor",
        "nakshatra": "Wealthy, good at work."
    },
    {
        "name": "Madame Curie",
        "famous": "Physicist",
        "nakshatra": "Intelligent,"
    },
    {
        "name": "Groucho Marx",
        "famous": "Comedian",
        "nakshatra": "Cynical, witty,"
    }
], 'Uttara Bhadrapada': [
    {
        "name": "Indira Gandhi",        
        "famous": "Indian PM",
        "nakshatra": "Attractive."      
    },
    {
        "name": "Robert Kennedy",       
        "famous": "US Attorney General",
        "nakshatra": "Virtuous."
    },
    {
        "name": "Cary Grant",
        "famous": "Actor",
        "nakshatra": "Self-control, defeats rivals."
    },
    {
        "name": "Christina Collins Hills",
        "famous": "Astrologer",
        "nakshatra": "Good marriage."
    }
], 'Revati': [
    {
        "name": "Rabindranath Tagore",
        "famous": "Writer",
        "nakshatra": "Interest in traditions, writing skills."
    },
    {
        "name": "Marlon Brando",
        "famous": "Actor",
        "nakshatra": "Popular, independent, ambitious."
    },
    {
        "name": "James Taylor",
        "famous": "Cricketer",
        "nakshatra": "Ambitious, wealthy."
    },
    {
        "name": "Joe Pesci",
        "famous": "Actor",
        "nakshatra": "Wisdom."
    },
    {
        "name": "Jim Jones",
        "famous": "Preacher",
        "nakshatra": "Interest in religion."
    },
    {
        "name": "Whitney Houston",
        "famous": "Singer",
        "nakshatra": "Magnetic personality."
    }
]}

