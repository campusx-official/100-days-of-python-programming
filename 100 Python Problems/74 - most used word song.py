# Write a program that can find the most used word in a song.

lyrics = '''I got room
In my fumes (yeah)
She fill my mind up with ideas
I'm the highest in the room (it's lit)
Hope I make it outta here (let's go)
She saw my eyes, she know I'm gone (ah)
I see some things that you might fear
I'm doin' a show, I'll be back soon (soon)
That ain't what she wanna hear (nah)
Now I got her in my room (ah)
Legs wrapped around my beard
Got the fastest car, it zoom (skrrt)
Hope we make it outta here (ah)
When I'm with you, I feel alive
You say you love me, don't you lie (yeah)
Won't cross my heart, don't wanna die
Keep the pistol on my side (yeah)
Case it's fumes (smoke)
She fill my mind up with ideas (straight up)
I'm the highest in the room (it's lit)
Hope I make it outta here (let's go, yeah)
We ain't stressin' 'bout the loot (yeah)
My block made of queseria
This not the Molly, this the boot
Ain't no comin' back from here
Live the life of La Familia
It's so much gang that I can't see ya (yeah)
Turn it up 'til they can't hear (we can't)
Runnin', runnin' 'round for the thrill
Yeah, dawg, dawg, 'round my real (gang)
Raw, raw, I been pourin' to the real (drank)
Nah, nah, nah, they not back of the VIP (in the VIP)
Gorgeous, baby, keep me hard as steel
Ah, this my life, I did not choose
Uh, been on this since we was kids
We gon' stay on top and break the rules
Uh, I fill my mind up with ideas
Case it's fumes
She fill my mind up with ideas (straight up)
I'm the highest in the room (I'm the highest, it's lit)
Hope I make it outta here
I'm the highest, you might got the Midas touch
What the vibe is? And my bitch the vibiest, yeah
Everyone excited, everyone too excited, yeah now
Play with the giants, little bit too extravagant, yeah now
Night, everyone feel my vibe, yeah
In the broad day, everyone hypnotizing, yeah
I'm okay and I take the cake, yeah'''

D = {}

for word in lyrics.split():
    if word in D:
        D[word] = D[word] + 1
    else:
        D[word] = 1
        
max_val = max(D.values())

for i in D:
    if D[i] == max_val:
        print(i, max_val)
        break