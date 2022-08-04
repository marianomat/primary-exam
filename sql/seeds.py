import random

from faker import Faker

faker = Faker()

personas = []

for i in range(100):
    personas.append((faker.name(), random.uniform(10000.00, 100000.00)))




def get_personas():
    return personas


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
