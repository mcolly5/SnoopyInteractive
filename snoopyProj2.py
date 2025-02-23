import streamlit as st
import requests
import random
import pandas as pd
import theTea
baseurl = "https://raw.githubusercontent.com/ajzbc/kanye.rest/master/quotes.json"
r = requests.get(baseurl)
if r.status_code == 200:
    quotes = r.json()

def get_name():
    global name
    name = st.text_input("Name? ")#NEW
    if not name:
        st.title("Welcome...?")
    else:
        st.title("Welcome, " + name + "!")
    st.write("---")
get_name()
##OPENER######################################################
def welcome():
    st.image("images/openSnoopy.jpg", use_column_width = True)#NEW
    st.write("You've won a special day with Joe Cool. Let's see what you get up to!")
    st.write("---")
welcome()
#########BREAKFAST###########################################
def breakfast():
    st.header("First, let's eat.")
    uno = "Eggs and toast"
    dos = "Pancakes"
    tres = "Just some coffee is fine."
    quat = "Woodstock"
    breaky = st.selectbox("What'll we have? ", [uno, dos, tres, quat])
    if breaky == uno:
        st.write("A classic choice. Shall we indulge?")
        st.image("images/toast.jpg", width = 200)
    if breaky == dos:
        st.write("Always up for some nines!")
        st.image("images/pancakes.jpg", width = 200)
    if breaky == tres:
        st.write("Fair enough.")
        st.image("images/coolSnoopy.jpg", width = 200)
    if breaky == quat:
        st.write("**NO!!!!!!!!!!!!!!!!!!!!!!!**")
        st.image("images/scared.jpg", width = 200)
    st.write("---")
breakfast()
###VISITING DIALOGUES############################################
def charlieVisit():
    st.image("images/charlie.jpg", use_column_width=True)
    st.subheader("Snoopy's always down to see his best friend!")
    st.write("_You follow him to their house and knock on the door._")
    st.write("_'Snoop? Is that you?' A boyish voice calls._")
    st.write("_'Hello! I was wondering where you'd gone off to. Who's your friend?'_")
    st.write("_*Snoopy whispers something to Charlie.* '" + name + "_? Well, nice to meet you.'")
    st.write("_'Hey snoop, how about some fetch, huh?'_")
    st.write("_Snoopy looks offended and scowls at Charlie Brown. 'What's the deal? You are literally a dog! Fine. Man's best friend... right.'_")
    st.write("_Charlie Brown dejectedly closes the door while snoopy puts his snout in the air in distaste. Dang._")

def linusVisit():
    st.image("images/linus.jpg", use_column_width=True)
    st.subheader("_Snoopy beckons you to follow him. You join him on an adventure through some offside part of the neighborhood._")
    st.write("_You arrive at Linus's house, where he's engrossed in tending to his pumpkin patch._")

    st.write("_Linus looks up, momentarily startled, then breaks into a wide smile. Snoopy does a jig to express excitement(because he's nonverbal)._")
    st.write("_'Snoopy! And a new friend? This is fantastic! We could use all the help we can get.'_")

    st.write("_You, Snoopy, and Linus spend the day silently working on the pumpkin patch, sharing stories through gestures and expressions._")
    st.write("_Linus passionately explains the Great Pumpkin legend, and Snoopy stops you from breaking the truth to him because he's been through enough already._")

    st.write("_As evening falls, you gather around Linus's crusty blanket, waiting for the Great Pumpkin. The air is filled with excitement and camaraderie._")
    st.write("_Even if the Great Pumpkin doesn't make an appearance, the friendship and shared moments make this quiet quest unforgettable...:)_")
    
def lucyVisit():
    st.image("images/lucy.jpg", use_column_width=True)
    st.subheader("_You know a girlboss when you see one._")
    st.write("_There was only one place Lucy could be: at her therapy stand._")
    st.write("_'It's ok to not be okay! The Doctor is in! Lay your burdens on me!' She cried like a true businesswoman._")
    st.write("_Snoopy(noneverbally) suggets that you get consoled on your latest situationship. Before you can protest, Lucy's superhuman hearing compels her to bascially teleport to your side for a nice discussion._")


    st.write("_'What's your name?' She asks for taxing purposes. You answer. 'Well, _" + name + "_,' she sighs, you really should have cut that person off months ago. Why are you fighting for someone's attention? Respect yourself. Couldn't be me.'_")
    st.write("_You hate that she's right, but it just be like that sometimes. You thank her for her consolation and she hands you a 900 dollar invoice. When you say you don't have that kind of money, she says it's a skill issue. You can't argue with her because she teleports away to go help Zayn Malik get over the way he was treated by Yolanda Hadid which... is honestly more important._")
def schroVisit():
    st.image("images/schroeder.jpg", use_column_width=True)
    st.subheader("_Snoopy knew you a music enthusiast._")
    st.write("_You find Schroeder on the street corner, approaching every stranger he can asking to compare 'Spotify Wrapped' lists. He insists that no one has as niche results as him, and Snoopy(nonverbally) insists that you put him in his place._")
    st.write("_'I bet you've never heard of Cody Fry, huh?' Schroeder says while looking you up and down.'_")

    st.write("_Before another word, you reveal that your top songs were the entire Interstellar soundtrack(and one Michael Cera song). Someone gags behind you._")
    st.write("_Schroeder is speechless and then stutters, 'W-w-what is your name?' in a mix of shock, fear, and awe. You tell him it's too underground, he wouldn't understand._")
    st.write("_'Well whoever you are... I ask that you spare me..' He stumbles back into the Music and Arts store he came from and everyone claps._")
    st.write("**Just kidding. He was playing piano and ya'll stayed for like 10 minutes.**")


def franklinVisit():
    st.image("images/franklin 1.jpg", use_column_width=True)
    st.subheader("Okay, there's no adventure here. I just want everyone to see how nice this kid looks. Like seriously, how did we sleep on him?")

    st.image("images/franky22.jpg", use_column_width=True)
    st.subheader("**LOOK AT HIM!!SO FRIENDLY!!!**")
    st.subheader("Goodness.")

    st.image("images/franklin 3.jpg", use_column_width=True)             
    st.subheader("Anyways...")

def iceSpiceVisit():
    st.image("images/ice spice.jpg", use_column_width=True)
    st.subheader("Snoopy loves Ice Spice! She was his #1 on Spotify Wrapped with 300,000 minutes.")
    st.write("_You fly on his doghouse to New York, listening to 'Like..?' All the way there._")
    st.write("_Snoopy was too nervous to ring the doorbell at her secret deli location you guys tracked down, so you do it._")
    st.write("_'Like grra, who's there?' Someone says. You push Snoopy in front of you so he can meet his idol._")
    st.write("_When Ice Spice opens the door, you both take a step back. 'Let's keep it a stack, how did you find me?' she asks delightedly. 'No one has ever found my Deli™.'")
    st.write("_Snoopy points at his map, covered in red circles, arrows, and glitter. 'You guys must be true fans, like graa,' she says. 'Want to be in my music video?'_")
    st.write("_Snoopy is so excited he can hardly speak. He jumps up and down and begs you to do it with him. You say sure(even though you prefer Flo Milli)._")
    st.write("_Ice Spice smiles.'Awesome! Like grra. Let me tell my producer. Hey [redacted], " + name + " and Snoopy are my friends and they're going to be in the video! Like grra.'_")
    st.write("_Snoopy takes out his ice spice wig and runs to the back, you trailing behind him._")
#####################VISIT COMMAND###########################################
def visit(neighborhood):
    st.header("Now that we're full, Snoopy is ready to make some rounds? Who should we visit?")
    people = pd.DataFrame(neighborhood)
    st.dataframe(neighborhood, column_config={
        "Name": "Names",
        "Age": "Ages",
        "Lives in": "Lives inn",
        "Favorite pas": "Favorite pastime"},
        hide_index=True,
        )
    answr = st.text_input("Who are we seeing? ")
    if answr == "Charlie Brown":
        charlieVisit()
    elif answr == "Linus":
        linusVisit()
    elif answr == "Lucy":
        lucyVisit()
    elif answr == "Schroeder":
        schroVisit()
    elif answr == "Franklin":
        franklinVisit()
    elif answr == "Ice Spice":
        iceSpiceVisit()
    elif not answr:
        pass
    else:
        st.write("_So that's actually not someone on the list..._")
    st.write("---")
visit(theTea.Neighborhood)
#############################ROCK PAPER SCISSORS###################
def rPS():
    st.subheader("On the way home, Snoopy wants to play Rock Paper Scissors. You best indulge him.")
    hand = st.radio("Your move.", ['Rock', 'Paper', 'Scissors'])#NEW
    
    snoopy_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    st.write(f"You chose: {hand}")
    st.write(f"Snoopy chose: {snoopy_choice}")

    if hand == snoopy_choice:
        st.write("Go again. There can only be one winner.")
    elif(
        (hand == 'Rock' and snoopy_choice == 'Scissors') or
        (hand == 'Paper' and snoopy_choice == 'Rock') or
        (hand == 'Scissors' and snoopy_choice == 'Paper')):
        st.write("**You win! Snoopy is mad.**")
        st.image("images/angry snoop.jpg", use_column_width=True)
    else:
        st.write("**Snoopy wins! He dances in victory instead of flying the doghouse..**")
        st.image("images/celebrationsnoop.jpg", use_column_width=True)
    st.write("---")
rPS()        
############ENDING###########################################
def snoopyQuote():
    st.image("images/wise.jpg", use_column_width=True)
    bad_words = [
        "One day I'm gon' marry a porn star", 
        "Shut the fuck up I will fucking laser you with alien fucking eyes and explode your fucking head",
        "I care. I care about everything. Sometimes not giving a f#%k is caring the most.",          
        "I feel like me and Taylor might still have sex",
        ]
    st.header("You arrive back at GT. This could be the last time you ever see Snoopy! You turn and ask:")
    ask = st.button("Any final words of wisdom (that are totally not Kanye quotes)?")#NEW
    if ask:
        snoopWords = random.choice(quotes)
        if snoopWords in bad_words:
            st.write("He responds: " + theTea.Kendrick)
            st.write("(this is not kanye)")
        else:
            st.write("He reponds: " + snoopWords)
        st.write("---")
        st.subheader("And with that, he went off to battle in a scrappy 1940s airplane battle, or renovate his house, or discover Obama's last name... we don't know. Get home safe now!")
        st.subheader("_THE END_")
        st.image("images/bye.jpg", use_column_width=True)
snoopyQuote()
############################################################
   


