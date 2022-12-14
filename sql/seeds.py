import random

def get_personas():
    return personas


def get_aeronaves():
    return aeronaves


def get_vuelos():
    return vuelos


def get_relacion_persona_aeronave():
    return relacion_persona_aeronave


vuelos = [('Lake Nicoleburgh', 'East Justin', 3396, '2022-01-15', '2022-01-16', 6535.21),
          ('Davisburgh', 'South Monicafort', 4328, '2022-01-15', '2022-01-16', 1871.77),
          ('Huntborough', 'Ortegaton', 13780, '2022-01-15', '2022-01-16', 3106.04),
          ('New Sandrashire', 'North Jennifertown', 10198, '2022-01-15', '2022-01-16', 845.54),
          ('Karenburgh', 'Pottsborough', 13694, '2022-01-15', '2022-01-16', 6222.31),
          ('Bellmouth', 'Mooretown', 9693, '2022-01-15', '2022-01-16', 3805.25),
          ('Eugeneville', 'Port Jamieshire', 11558, '2022-01-15', '2022-01-16', 251.5),
          ('Nguyenton', 'Lake Nicole', 1227, '2022-01-15', '2022-01-16', 5373.82),
          ('Christopherstad', 'Ericside', 8964, '2022-01-15', '2022-01-16', 333.27),
          ('Martinville', 'West Amy', 9897, '2022-01-15', '2022-01-16', 4923.64),
          ('North Erinmouth', 'Mitchellborough', 13710, '2022-01-15', '2022-01-16', 2113.71),
          ('Darrellport', 'Davidborough', 4025, '2022-01-15', '2022-01-16', 3858.74),
          ('Port Susanmouth', 'Lake Jessica', 11036, '2022-01-15', '2022-01-16', 4063.66),
          ('Annaburgh', 'Jonesmouth', 5530, '2022-01-15', '2022-01-16', 1307.73),
          ('Hectorstad', 'North David', 5795, '2022-01-15', '2022-01-16', 3440.61),
          ('North Luismouth', 'Mccluretown', 5093, '2022-01-15', '2022-01-16', 4784.18),
          ('Kylechester', 'Lake Stephaniefort', 4934, '2022-01-15', '2022-01-16', 404.11),
          ('Carlside', 'Shannonburgh', 1161, '2022-01-15', '2022-01-16', 1329.2),
          ('Peggyport', 'Kingland', 10071, '2022-01-15', '2022-01-16', 2328.79),
          ('Reginaldborough', 'Lindabury', 13426, '2022-01-15', '2022-01-16', 5293.77),
          ('Port Emilyfort', 'North Jamiechester', 13115, '2022-01-15', '2022-01-16', 7741.5),
          ('Smithberg', 'East Ryanhaven', 13990, '2022-01-15', '2022-01-16', 1214.29),
          ('Lake Alison', 'Kristenchester', 13223, '2022-01-15', '2022-01-16', 1904.56),
          ('Barrettborough', 'Port Mallory', 13133, '2022-01-15', '2022-01-16', 3107.27),
          ('West Sarah', 'Smithfort', 4954, '2022-01-15', '2022-01-16', 560.44),
          ('East Nataliefort', 'New Jessicaton', 1097, '2022-01-15', '2022-01-16', 332.94),
          ('Torresstad', 'South Bryan', 7711, '2022-01-15', '2022-01-16', 1931.76),
          ('Evanschester', 'East Christinatown', 2968, '2022-01-15', '2022-01-16', 146.74),
          ('Englishstad', 'Byrdfort', 13158, '2022-01-15', '2022-01-16', 4162.6),
          ('Nicholasburgh', 'Rodriguezton', 12735, '2022-01-15', '2022-01-16', 468.35),
          ('Vincentborough', 'New Amy', 4478, '2022-01-15', '2022-01-16', 146.42),
          ('West Michealview', 'Russellville', 4465, '2022-01-15', '2022-01-16', 1599.52),
          ('West Christine', 'Cynthiashire', 5708, '2022-01-15', '2022-01-16', 4037.08),
          ('Andrewbury', 'Myersshire', 381, '2022-01-15', '2022-01-16', 3035.52),
          ('East Chaseborough', 'Lake Charlesstad', 14209, '2022-01-15', '2022-01-16', 4055.34),
          ('New Chadmouth', 'Juantown', 10958, '2022-01-15', '2022-01-16', 6469.02),
          ('Heidiside', 'Lake Melissa', 4282, '2022-01-15', '2022-01-16', 747.72),
          ('Woodsberg', 'Paulborough', 13327, '2022-01-15', '2022-01-16', 7445.82),
          ('Clarencebury', 'East Michele', 655, '2022-01-15', '2022-01-16', 3395.94),
          ('Lake Anthonyport', 'North Jennaborough', 1185, '2022-01-15', '2022-01-16', 464.53),
          ('South Derrickmouth', 'Port Sarahchester', 8157, '2022-01-15', '2022-01-16', 4614.53),
          ('North Christina', 'North Christopherport', 1012, '2022-01-15', '2022-01-16', 2957.35),
          ('Port John', 'East Kelseyshire', 11445, '2022-01-15', '2022-01-16', 7272.8),
          ('New Carolville', 'Grayton', 2561, '2022-01-15', '2022-01-16', 6342.33),
          ('Garnertown', 'Port Kayla', 590, '2022-01-15', '2022-01-16', 7670.31),
          ('Michaelport', 'East Nicholas', 8268, '2022-01-15', '2022-01-16', 5915.38),
          ('Monicafurt', 'Johnsonhaven', 13443, '2022-01-15', '2022-01-16', 5558.57),
          ('New Richard', 'Port Kristenville', 1508, '2022-01-15', '2022-01-16', 4220.13),
          ('New Frank', 'Heatherland', 2004, '2022-01-15', '2022-01-16', 6414.53),
          ('New Meghantown', 'North Janice', 6568, '2022-01-15', '2022-01-16', 243.27),
          ('North Theodoreside', 'West David', 9884, '2022-01-15', '2022-01-16', 1825.02),
          ('Franklinshire', 'South Keithview', 9895, '2022-01-15', '2022-01-16', 546.91),
          ('Baileymouth', 'Jacksonfort', 7120, '2022-01-15', '2022-01-16', 1391.47),
          ('East Elizabeth', 'South Michaelmouth', 7774, '2022-01-15', '2022-01-16', 3554.85),
          ('Russellborough', 'North Tara', 13245, '2022-01-15', '2022-01-16', 4689.85),
          ('Ericside', 'West Edwardberg', 14527, '2022-01-15', '2022-01-16', 3825.41),
          ('Ericaton', 'Lyonsshire', 13038, '2022-01-15', '2022-01-16', 7997.5),
          ('East Josephland', 'North Shawn', 620, '2022-01-15', '2022-01-16', 472.98),
          ('Kramershire', 'Gregorystad', 8134, '2022-01-15', '2022-01-16', 7944.13),
          ('Lake Rita', 'East Francis', 5033, '2022-01-15', '2022-01-16', 4051.29),
          ('Saraland', 'Zacharyfurt', 13428, '2022-01-15', '2022-01-16', 3416.18),
          ('New Juan', 'West Brian', 13947, '2022-01-15', '2022-01-16', 5290.89),
          ('Angelaland', 'Justinton', 14644, '2022-01-15', '2022-01-16', 4925.94),
          ('Wrightmouth', 'North Johnnymouth', 12200, '2022-01-15', '2022-01-16', 215.92),
          ('North Shawn', 'Phillipsmouth', 7255, '2022-01-15', '2022-01-16', 755.51),
          ('Cherylborough', 'Ruizton', 14632, '2022-01-15', '2022-01-16', 4435.34),
          ('Martinmouth', 'Sarastad', 6911, '2022-01-15', '2022-01-16', 1792.34),
          ('Alexisburgh', 'Rojasland', 6778, '2022-01-15', '2022-01-16', 5298.82),
          ('Port Christinachester', 'Staceyshire', 13336, '2022-01-15', '2022-01-16', 2817.94),
          ('Antoniofurt', 'West Nancy', 4153, '2022-01-15', '2022-01-16', 4247.37),
          ('East Sherry', 'Port Eugene', 13988, '2022-01-15', '2022-01-16', 4711.86),
          ('Nicoleview', 'Troyside', 3510, '2022-01-15', '2022-01-16', 4903.44),
          ('New Carly', 'West Donald', 3445, '2022-01-15', '2022-01-16', 7170.53),
          ('Port Wanda', 'Priceshire', 12499, '2022-01-15', '2022-01-16', 2539.36),
          ('Leefort', 'East Brianland', 3853, '2022-01-15', '2022-01-16', 3358.31),
          ('West Crystal', 'Rossfort', 12318, '2022-01-15', '2022-01-16', 2174.2),
          ('East Whitneymouth', 'Owensfort', 7834, '2022-01-15', '2022-01-16', 7119.46),
          ('Lake Jenniferfort', 'Cynthiaport', 11348, '2022-01-15', '2022-01-16', 6058.28),
          ('East Sarastad', 'East Bridgetstad', 13127, '2022-01-15', '2022-01-16', 3798.78),
          ('Nicoleport', 'North Kelly', 11577, '2022-01-15', '2022-01-16', 1162.12),
          ('Lake Sonya', 'Jacksonborough', 7061, '2022-01-15', '2022-01-16', 2145.69),
          ('Mclaughlinstad', 'Brittneymouth', 9712, '2022-01-15', '2022-01-16', 7973.76),
          ('Port Lawrence', 'Lake Michaelmouth', 14019, '2022-01-15', '2022-01-16', 814.26),
          ('Hollowayville', 'Mcdanielmouth', 105, '2022-01-15', '2022-01-16', 5818.57),
          ('New Scottville', 'Shawnport', 10024, '2022-01-15', '2022-01-16', 2883.03),
          ('Jessicabury', 'Barnettshire', 10654, '2022-01-15', '2022-01-16', 567.86),
          ('North Julie', 'New Joycemouth', 3471, '2022-01-15', '2022-01-16', 577.03),
          ('Angelaborough', 'West Cynthia', 3973, '2022-01-15', '2022-01-16', 6426.28),
          ('Wilsonhaven', 'Brittneyborough', 8880, '2022-01-15', '2022-01-16', 2111.09),
          ('Josephport', 'Lake Mary', 6782, '2022-01-15', '2022-01-16', 683.64),
          ('Peterhaven', 'Hallfurt', 14984, '2022-01-15', '2022-01-16', 3738.21),
          ('East Lukeside', 'Thomasside', 7047, '2022-01-15', '2022-01-16', 2764.45),
          ('New Karen', 'North Julie', 10288, '2022-01-15', '2022-01-16', 5835.13),
          ('Lake Mary', 'Danielston', 6789, '2022-01-15', '2022-01-16', 3333.04),
          ('South Brianland', 'Deborahville', 5840, '2022-01-15', '2022-01-16', 6940.36),
          ('Mckeemouth', 'Jimmyfort', 1647, '2022-01-15', '2022-01-16', 7869.6),
          ('Briannaport', 'Port Caseyview', 6343, '2022-01-15', '2022-01-16', 582.55),
          ('Stephensonshire', 'North Andrew', 6950, '2022-01-15', '2022-01-16', 2088.9),
          ('East Victoriafurt', 'Clarkbury', 14336, '2022-01-15', '2022-01-16', 5155.4),
          ('Maryfurt', 'New Paulmouth', 4587, '2022-01-15', '2022-01-16', 1933.44)
          ]

relacion_persona_aeronave = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3),
                             (4, 6)]
aeronaves = [
    ("Airbus 319", 2000),
    ("Airbus 330", 3000),
    ("Boeing 737", 6000),
    ("Boeing 747", 7000),
    ("Airbus 319", 2000),
    ("Airbus 330", 5500),
    ("Boeing 737", 2000),
    ("Boeing 747", 3000),
    ("Airbus 319", 1500)
]

personas = [
    ('Amanda Warren', 39922.59), ('Amy Bennett MD', 6474),
    ('Carrie Wood', 46420.74), ('Melissa Foster', 84733.58),
    ('Tiffany Rice', 84996.9), ('Marissa Callahan', 97981.8),
    ('Amanda Arias', 42719.50), ('James Solis', 82213.12),
    ('Dylan Simon', 74186.56), ('Brandy Williams', 73452.9),
    ('Kevin Bates', 61115.849), ('Alan Jackson', 87710.91),
    ('Gerald Graham', 33678.35), ('Brian Dominguez', 63160.630),
    ('Donald Boone', 13110.59), ('Charles Taylor', 86805.96),
    ('Karen Hunt', 19774.115), ('Laura Donovan', 14063.17),
    ('Felicia Smith', 80788.81), ('Laurie Wright', 78693.59),
    ('Beth Ball', 68796.10), ('Brian Cunningham', 31026.203),
    ('Angela Miller', 49987.19), ('Joel Horn', 46860.329),
    ('Mary Jackson', 36929.98), ('Kimberly Rojas', 62555.61),
    ('Brenda Davis', 46358.63), ('Brandy Ashley', 13657.388),
    ('Audrey Nguyen', 12750.11), ('Tara Haynes', 41827.462),
    ('Michael Taylor', 72850.56), ('Jackie Blair', 30747.483),
    ('Gail Little', 77874.2), ('Joseph Whitaker', 64974.097),
    ('James Ross', 40742.191), ('Dennis Obrien', 72545.81),
    ('Brittany Richards', 18773.37), ('Ralph Spencer', 52745.247),
    ('Teresa Delacruz', 26731.308), ('Jessica Schneider', 60677.37),
    ('Richard Stewart', 57199.71), ('Alexis Franco', 60466.10),
    ('Alexis Roberts', 92947.85), ('Alex Cook', 95547.3),
    ('Crystal Smith', 46268.61), ('Reginald Carter', 40577.790),
    ('Mindy Clark', 94196.2), ('Michael Cunningham', 22866.437),
    ('Laura Marshall', 46839.874), ('Dr. Karla Johnson', 76057.49),
    ('Barbara Norton', 76377.70), ('Laura Cross', 25532.36),
    ('Pamela Wright', 55990.20), ('William Le', 34778.40),
    ('Karen Russo', 27711.664), ('Krystal Hopkins', 99277.49),
    ('Melissa Mayer', 39303.40), ('Jason King', 74414.0),
    ('Zachary Taylor', 74956.0), ('Jesus Hurst', 34681.51),
    ('Austin Harmon', 60609.82), ('Dr. Robert Wilson', 90705.23),
    ('Stephen Morrow', 23121.751), ('Amy Anderson', 30795.208),
    ('Stephanie Logan', 37483.91), ('Sharon Rowland', 74640.40),
    ('Daniel Meza', 10143.247), ('Gerald White', 35076.47),
    ('Jennifer Bennett', 32336.20), ('Samuel Gonzalez', 33178.835),
    ('Kimberly Taylor', 18307.639), ('Andrew Oliver', 58189.17),
    ('Lisa Price', 56114.44), ('Margaret Duncan', 90168.13),
    ('Susan Barnes', 71429.32), ('Jeremy Peters', 99140.00),
    ('Anthony Powers', 81295.65), ('Carl Weaver', 49533.7),
    ('Micheal Kelly', 18670.33), ('Jordan Stewart', 23754.000),
    ('Calvin Simmons', 90555.82), ('Laura Lambert', 34868.57),
    ('John Mueller', 78473.55), ('Joshua Anderson', 70314.92),
    ('Sara Lee', 78044.87), ('David Allen', 16187.031),
    ('Anthony Cooper', 28278.055), ('Douglas Flores', 58057.99),
    ('Steve Hill', 31593.498), ('Natalie Campbell', 27302.16),
    ('Lori Brown', 27904.650), ('Dr. Rhonda Becker', 49542.86),
    ('Claire Brown', 78628.83), ('Angela Gregory', 77703.82),
    ('Mrs. Margaret Davis', 19246.577), ('Heather Wilson', 13780.388),
    ('Zachary Short', 12441.94), ('Anna Wilson', 47147.71),
    ('Julie Ortiz', 78746.29), ('John Wolf', 96298.19)
]
