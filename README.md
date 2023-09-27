<h1>
    <font size="6">Connections-LLM </font>
</h1>
<font size="4">
    <em>Synthesising <a href="https://www.nytimes.com/games/connections">the popular NY Times puzzle</a> with an LLM</em>
</font>

If you didn't know, NY Times has a new daily puzzle called "Connections" which they ripped off of BBC's Only Connect. To be fair, they have made the categories and answers more casual and doable. You have a 4x4 grid of 16 words, and they can be divided evenly into 4 secret categories. The goal is to guess 4 words at a time to see if you've uncovered a category, and you get 4 lives.

### Why LLMs?
The categories are diverse and can be very creative and out-of-the-box. Here are some examples I compiled in just 10 minutes (ALLCAPS: NY Times, Capitalcase BBC).

Literal dictionary meaning:
- WET WEATHER                   (HAIL, RAIN, SLEET, SNOW)
- MAR                           (CHIP, DING, NICK, SCRATCH)

Association with something
- Things you can 'fire'         (Question, Pot, Gun, Employee)
- Things that can be spread     (Germs, Rumours, Butter, Wings)
- COMMON MERCH ITEMS            (MUG, TEE, PEN, TOTE)
- BOWLING                       (BALL, PIN, LANE, ALLEY)
- WEB BROWSER-RELATED           (WINDOW, TAB, HISTORY, BOOKMARK)

Pop culture references:
- Gas laws                      (Boyle, Henry, Avogadro, Gay-Lussac)
- NBA TEAMS                     (BUCKS, HEAT, JAZZ, NETS)
- JACKS                         (MA, BLACK, FROST, SPARROW)
- SOCIAL MEDIA APP ENDINGS      (GRAM, BOOK, TUBE, IN)
- Philip Marlowes               (Mitchum, Gould, Powell, Montgomery)

Prefixes/suffixes in words, or phrases/idioms:
- ___JACK                       (APPLE, CRACKER, FLAP, LUMBER)
- End in boys' names            (Gluttony, Earmark, Crackerjack, Trumpeter)
- DIRTY ___                     (LAUNDRY, MARTINI, JOKE, DOZEN)
- Hold your ___                 (Serve, Tongue, Breath, Horses)

More word play:
- Homophones of boys' names     (Kneel, Dug, Fill, Gym)
- NUMBER HOMOPHONES             (WON, TOO, ATE, FOR)
- PALINDROMES                   (KAYAK, LEVEL, MOM, RACE CAR)

Even from this small corpus, you can see how wide the gamut of categories is. You couldn't fathomly list all the categories a word could belong to - even if you had a dictionary and a list of all the idioms and rhymes and boy names in the world, you still wouldn't be able to list 4 Car Rental Companies, or 4 Harry Potter Spells or 4 Travel Souvenir Ideas.


### If you are here because I sent a link to you, then please come back in a day! I've been too busy with hunting for a rtx 3090 so all my thoughts are still in my head

TODO list:
randomise category word seeds
Clean up conditional tone in bonus combo
Capitalise Category Names

Branch off the same category twice
Strategic placement of quotation marks around brainstorm words, instead of CAPITAL CASE?

Review chatgpt log and copy paste into here

- Just list category pairs and the red herrings between them - way easier than finding good puzzle set.

BBC is good for individual categories
Get list of good examples, lsit of bad (celebrities, british tv shows etc.)
Then ask chat gpt to filter out the rest.
