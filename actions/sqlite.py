import sqlite3

def init_data():
    conn = sqlite3.connect('demo.db') 
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")
    sql = "drop table if exists Register;"
    cursor.execute(sql)
    sql=""" CREATE TABLE if not exists Register( section text, grp VARCHAR, name VARCHAR, room VARCHAR, time VARCHAR ); """
    cursor.execute(sql)
    sql = "drop table if exists Teacher;"
    cursor.execute(sql)
    sql=""" CREATE TABLE if not exists Teacher( name text,  contact VARCHAR ); """
    cursor.execute(sql)
   
    sql = "drop table if exists Course;"
    cursor.execute(sql)
    sql=""" CREATE TABLE if not exists Course( name text,  teacher_id int,  foreign key (teacher_id) references Teacher(rowid), unique (teacher_id, name) ); """
    cursor.execute(sql) 
    
    sql = "drop table if exists Message;"
    cursor.execute(sql)
    sql=""" CREATE TABLE if not exists Message( message text,  teacher_id integer,  foreign key (teacher_id) references Teacher(rowid)); """


    #sql=""" CREATE TABLE if not exists Room_state( section text, grp VARCHAR, name VARCHAR, room VARCHAR, time VARCHAR ); """
    cursor.execute(sql)

    cursor.execute('''INSERT INTO Register(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("Master 1","alternant","Robotique","Salle 2","11:00"))
    cursor.execute('''INSERT INTO Register(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("Master 1","alternant","infra","Salle 3","13:00"))
    cursor.execute('''INSERT INTO Register(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("Master 1","classique","sécurité","Salle 2","11:00"))
    cursor.execute('''INSERT INTO Register(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("Master 1","classique","web","Salle 8","13:00"))
    cursor.execute('''INSERT INTO Register(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("Master 2","alternant","IA","Salle 5","11:00"))
    cursor.execute('''INSERT INTO Register(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("Master 2","alternant","VoIP","Salle 7","13:00"))
    cursor.execute('''INSERT INTO Register(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("Master 2","classique","anglais","Salle 4","11:30"))
    cursor.execute('''INSERT INTO Register(section,grp,name,room,time) VALUES (?, ?, ?, ?, ?)''', ("Master 2","classique","ecom","Salle 6","13:30"))

    cursor.execute('''INSERT INTO Teacher(name, contact) VALUES (?, ?)''', ("Fabrice Lefevre","lefevre.fabrice@alumni.univ-avignon.fr"))
    cursor.execute('''INSERT INTO Teacher(name, contact) VALUES (?, ?)''', ("Abderrahim Benslimane","abderrahim.benslimane@alumni.univ-avignon.fr"))
    cursor.execute('''INSERT INTO Teacher(name, contact) VALUES (?, ?)''', ("Philippe Gozlan","gozlan.philippe@alumni.univ-avignon.fr"))
    cursor.execute('''INSERT INTO Teacher(name, contact) VALUES (?, ?)''', ("Lilian Rondin","rondin.lilian@alumni.univ-avignon.fr"))


    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("Innovation", 1 ))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("VeilleTechnologique",1))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("Robotique", 1))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("IA", 1))

    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("Multimédia", 2))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("VoIP", 2))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("Architecture", 2))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ( "Reseaux", 2))

    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("Robotique", 3))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("Codesign", 3))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("Electronique",3 ))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("Cryptographie",3 ))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("Cybercriminalité",3 ))


    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("AnglaisEntreprise", 4))
    cursor.execute('''INSERT INTO Course(name, teacher_id) VALUES (?, ?)''', ("AnglaisProfessionnel", 4))



    sql = "drop table if exists Room;"
    cursor.execute(sql)
    sql=""" CREATE TABLE if not exists Room( nom_salles VARCHAR, description VARCHAR); """

    #sql=""" CREATE TABLE if not exists Room_state( section text, grp VARCHAR, name VARCHAR, room VARCHAR, time VARCHAR ); """
    cursor.execute(sql)


    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("amphi ada"," à gauche lors de l'entrée dans le hall"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle electronique"," à l'etage au fond du couloir à droite"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle robotique","à l'etage au fond du couloir à gauche"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle un","Juste en avançant un peu à votre droite"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle deux bis","en prenant le long du hall à votre gauche"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle quatre","au bout du couloir à droite en face de la salle deux"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle sept","se situe dans le hall en avancant de 20 mètres"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle huit","juste dans le hall en face de la salle quatre"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle informatique deux","a l'etage au fond du couloir à droite"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle informatique quatre","a l'etage au fond du couloir à gauche"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle informatique trois","Juste en avancant un peu à votre droite"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle stat six","en prenant le long du hall à votre gauche"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle windows stat sept","se situe dans le hall en avancant de 20 mètres"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle windows stat huit ","juste dans le hall en face de la salle stat sept"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("salle informatique stat neuf ","juste dans le hall en face de la salle stat huit"))
    cursor.execute('''INSERT INTO Room(nom_salles,description) VALUES (?, ?)''', ("amphi blaise","gauche sur le même alignement que amphi ada lors de l'entrée dans le hall"))
    

    sql = "drop table if exists Salles;"
    cursor.execute(sql)
    sql1 = """ CREATE TABLE if not exists Salles( site text, salle VARCHAR, time VARCHAR ); """
    cursor.execute(sql1)
    cursor.execute('''INSERT INTO Salles(site,salle,time) VALUES (?, ?, ?)''',
                   ("ceri",  "La salle S2 est libre à :", "11:00"))
    cursor.execute('''INSERT INTO Salles(site,salle,time)  VALUES (?, ?, ?)''',
                   ("ceri",  "La salle Stat2 est libre de :", "13:00 à 16:00"))
    cursor.execute('''INSERT INTO Salles(site,salle,time)  VALUES (?, ?, ?)''',
                   ("ceri",  "La salle S3 est libre de :", "09:00 à 13:00"))
    cursor.execute('''INSERT INTO Salles(site,salle,time)  VALUES ( ?, ?, ?)''',
                   ("ceri",  "La salle Stat1 est libre de :", "11:00 à 13:00"))
    cursor.execute('''INSERT INTO Salles(site,salle,time)  VALUES (?, ?, ?)''',
                   ("ceri",  "La salle Stat5 est libre de :", "11:00 à 12:00"))
    cursor.execute('''INSERT INTO Salles(site,salle,time)  VALUES ( ?, ?, ?)''',
                   ("ceri",  "La salle S5 est libre de :", "16:00 à 17:30"))
    cursor.execute('''INSERT INTO Salles(site,salle,time)  VALUES (?, ?, ?)''',
                   ("ceri",  "La salle S3 est libre de :", "13:00 à 17:30"))
    cursor.execute('''INSERT INTO Salles(site,salle,time)  VALUES (?, ?, ?)''',
                   ("ceri",  "La salle Stat3 est libre de :", "17:00 à 19:00"))
    cursor.execute('''INSERT INTO Salles(site,salle,time)  VALUES (?, ?, ?)''',
                   ("ceri", "La salle amphi blaise est libre de :", "17:00 à 19:00"))
    cursor.execute('''INSERT INTO Salles(site,salle,time)  VALUES (?, ?, ?)''',
                   ("ceri", "La salle amphi ada est libre de :", "14:00 à 16:00"))



    print("Table created successfully........")

    # Commit your changes in the database
    conn.commit()

    #Closing the connection
    conn.close()


def select_schedule(section,grp):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  #cursor.execute('''SELECT * FROM Register WHERE section=? AND grp=?''',(section,grp,))
  cursor.execute('''SELECT * FROM register ''')

  rows = cursor.fetchall()

  text =""
  for row in rows:
    print(row)
    text = row[2]+" en "+row[3]+" à "+row[4]
    break

  #Closing the connection
  conn.close()
  
  return text




def select_description(nom_salles):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  cursor.execute('SELECT description FROM Room WHERE nom_salles="'+str(nom_salles)+'";')
  
  rows = cursor.fetchall()

  text =""

  print(rows[0])
  text = rows[0][0]
    
  #Closing the connection
  conn.close()
  
  return text

def select_salle():
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  cursor.execute('SELECT nom_salles FROM Room ')
  
  rows = cursor.fetchall()

  texts = list()
  texts.append("Les salles du ceri sont  ")

  for row in rows:
    print(row)
    texts.append(row[0]+",")
    

  #Closing the connection
  conn.close()
  
  return texts



def select_free_room(site, time):
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    cursor.execute('''SELECT * FROM Salles WHERE site=? AND time=?''', (site, time))

    rows = cursor.fetchall()

    texts = list()
    for row in rows:
        print(row)
        texts.append("Sur le site : " +row[0]+" "+row[1]+" "+row[2])
        break

    # Closing the connection
    conn.close()

    return texts


def select_data(section,grp):
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  #cursor.execute('''SELECT * FROM Register WHERE section=? AND grp=?''',(section,grp,))
  cursor.execute('''SELECT * FROM Teacher ''')

  rows = cursor.fetchall()

  text =""
  for row in rows:
    print(row)
    #text = row[2]+" in "+row[3]+" at "+row[4]
    break

  #Closing the connection
  conn.close()
  
  return text

def send_message(message):
  """
  docstring
  """
  pass
def select_by_course(course):
  """
  docstring
  """
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  cursor.execute("SELECT teacher.name, teacher.rowid, course.name, course.teacher_id FROM Teacher inner join Course on teacher.rowid = Course.teacher_id WHERE Course.name like '%{}%' ".format(course))
  
  rows = cursor.fetchall()

  texts = list()
  #texts.append( "Les reusltats sont ")
  for row in rows:
    print(row)
    texts.append( "Nom  "+str(row[0])+" Course  "+str(row[2]))

  #Closing the connection
  conn.close()
  
  return texts

def select_by_name(name):
  """
  docstring
  """
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  cursor.execute("SELECT teacher.name, teacher.rowid, course.name, course.teacher_id FROM Teacher inner join Course on teacher.rowid = Course.teacher_id WHERE Teacher.name like '%{}%' ".format(name))
  
  rows = cursor.fetchall()
  texts = list()
  texts.append( "Les cours enseignés par "+name+" sont  ")
  for row in rows:
    print(row)
    texts.append( str(row[2]) )
  

  #Closing the connection
  conn.close()
  
  return texts
def print_data():
  conn = sqlite3.connect('demo.db') 
  cursor = conn.cursor()
  print("Database created and Successfully Connected to SQLite")
 
  cursor.execute('''SELECT teacher.name, teacher.rowid, course.name, course.teacher_id FROM Teacher inner join Course on teacher.rowid = Course.teacher_id ''')
  
  rows = cursor.fetchall()

  for row in rows:
    print(row)

  #Closing the connection
  conn.close()

if __name__ == "__main__":
 init_data()
 #print("All data:")
 #print_data()
 #print("Select classique")
 print(select_salle())
 
