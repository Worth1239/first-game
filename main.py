name = ""
while len(name) == 0:
    name = input("Hello, what is your name?")
print("Hello" + name)
age = input("How old are you" + name)
while age == 0:
    age = input("How old are you" + name)
print("'You" + name + " are" + age + " years old'")
age = (int(age))
if 0 < age <= 16:
    print("'Go get a job lil bro'")
elif age < 0:
    print("'talk to me once you've been born lil bro'")
elif 30 > age > 16:
    print("'go back to your 9-5 lil bro'")
elif age >= 30:
    print("'go back to the retirement home you old mf'")
feelers = input("'I'm sorry did that hurt your feelings?'")
feelers = str(feelers)
if feelers == ("no" or "nope" or "nah" or " no" or " nope" or " nah" or "no " or "nope " or "nah "):
    print("'alr lil bro you aint tough'")
    print("*gets up in your face*")
elif not feelers == ("no" or "nope" or "nah" or " no" or " nope" or " nah" or "no " or "nope " or "nah "):
    print("'I dont care'")
cos = input("'whatchu you gonna do now?'"" A.swing"" B.walk away" " C.keep smack talking" " D.kiss")
if cos == ("A" or "a" or " A" or " a"):
    print("He dodges and throws a jab to your stomach")
    x = input("How do you respond? A:Block B:Dodge C:Go for a punch to his face")
    if x == ("A" or "a" or " A" or " a"):
        print("You block his punch and he leaves an opening to his face")
        poo = input("How do you respond?" "A:Punch him in the face" "B: Rizz him up")
        if poo == ("A" or "a"):
            print("he wasn't expecting it and you knock him out")
        elif poo == ("B" or "b"):
            print("He gets flustered by your W rizz and he runs away.")
    elif x == ("B" or "b" or " b" or " b"):
        print("He reacts to your dodge and hits you in the face. You pass out")
    elif x == ("c" or "C" or " c" or " C"):
        print("You knock him out in one punch")
elif cos == ("B" or " B" or "b" " b"):
    print("He keeps smack talking while you are turned around")
    y = input("How do you respond? A: Turn around and smack him B:walk away peacefully C:Say smthn about his mom")
    if y == ("A" or "a" or " a" or " A"):
        print("your punch is so strong you knock him out")
    elif y == ("B" or "b" or " b" or " B"):
        print("You walk away peacfully and go about your day")
    elif y == ("C" or "c" or " C" or " c"):
        print("He gets mad and punches you. You cannot react and pass out.")
    elif cos == ("C" or "c" or " C" or " c"):
        print("He punches you in the jaw and you pass out")
elif cos == ("D" or "d" or " D" or " d"):
    print("He kisses you back and you make out intensely")
    z = input("How do you respond? A:Pull his body closer to yours B: Kiss his neck C:Grab his 🤫 D: Sucker punch him")
    if z == ("A" or "a" or " a" or " A"):
        print("You guys makeout and go back to his splace ;)")
    elif z == ("B" or "b" or " b" or " B"):
        print("You bite his neck too hard and he dies")
    elif z == ("C" or "c" or " c" or " C"):
        print("You guys go back to his place and get freaky")
    elif z == ("D" or "d" or " d" or " D"):
        print("He expected your punch, catches it and knocks you out in one punch")
