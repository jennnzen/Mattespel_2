import turtle
import time
import explain
scores = {"koordinater":0,"kvadrant":0, "givengraf":0, "potensiell":0, "x_for_y":0, "funktion_tabell":0, "expo": 0}

def minigames(user_choise):
    global scores
    if user_choise==0:
        explain.kordinat_explain() #fixa return i förklaring först
        import kordinater
        kordinater.padda(scores)
    elif user_choise==1:
        explain.kvadrant_explain()
        import kvadrant
        kvadrant.game(scores)
    elif user_choise==2:
        explain.givenGraf_explain()
        import givenGraf
        givenGraf.grid(scores)
    elif user_choise==3:
        explain.funktio_tabell_explain()
        import funktio_tabell
        funktio_tabell.game(scores)
    elif user_choise==4:
        explain.x_for_y_explain()
        import x_for_y
        x_for_y.grid(scores)
    elif user_choise==5:
        explain.potensiell_explain()
        #fixa så den inte skriver ut i terminalen
        import potensiell
        potensiell.grid(scores)
    elif user_choise==6:
        explain.expo_explain()
        #fixa så den inte skriver ut i terminalen
        import expo
        expo.grid(scores)
    elif user_choise==7:
        #fixa så den inte skriver ut i terminalen
        import easteregg
        easteregg.easteregg(scores)
    else:
        #run funny program
        print(user_choise)

def flytt(trtl, length):
    trtl.pu()
    trtl.fd(length)
    trtl.pd

def pos(trtl, x, y):
    trtl.pu()
    trtl.setpos(x, y)
    trtl.pd
    return

def game_hub():
    window = turtle.Screen()
    window.colormode(255)
    window.bgcolor(231, 228, 237)
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)
    trtl = turtle.Turtle()

    trtl.speed(0)
    trtl.ht()
    trtl.pu()

    pos(trtl, -320, 230) 
    trtl.write("Välkommen till ett mattespel mannen!", font=("Time New Roman", 22, "bold"), align="left")

    pos(trtl, -300, 170) 

    minispel=["Bestämning av x och y-kordinat av en punkt","Bestämning av kvadrant en punkt befinner sig i","Räta linjens ekvation (Y=kx+m)","Värdetabelövning för räta linjer","Att ge funktionsvärde på spesifika x värden i y=kx+m","Potensialfunktioner","Exponnsialfunktioner"]
    temp = 0

    for n in (minispel):
        trtl.write(str(minispel.index(n)) + " - " + n, font=("Time New Roman", 15, "normal"), align="left")

        temp += 1
        x_kord = (170 - temp*30)
        pos(trtl, -300, x_kord)

    pos(trtl, -320, -90)
    trtl.write("Du tar dig tillbaka genom att skriva return i rutan som", font=("Time New Roman", 15, "bold"), align="left")

    pos(trtl, -320, -120)
    trtl.write("kommer upp när du är i minispelen!!!!", font=("Time New Roman", 15, "bold"), align="left")

    pos(trtl, -320, -150)
    trtl.write("Lycka till!", font=("Time New Roman", 15, "normal"), align="left")


    trtl.ht()
    # window.exitonclick()

    time.sleep(1)

    #ta in user input oc se till att de är en intiger mellan 0 0ch (6+1) hehe annars få dem att skriva in igen
    sc = turtle.Screen()
    user_input=0
    while user_input != None:
        try:
            user_input = int(sc.numinput("vart vill du 0-7","Ditt val:"))
            if not 0 <= user_input <= 7:
                raise ValueError
        except (TypeError, OverflowError, ValueError):
            time.sleep(1)
            continue
        break

    turtle.clearscreen()
    
    minigames(user_input)
    turtle.clear()
    game_hub()

game_hub()

#undantagshantering så man inte kan trycka cancle

#import funktio_tabell
#import givenGraf
#import kordinater
#import kvadrant
#import tabellGraf
