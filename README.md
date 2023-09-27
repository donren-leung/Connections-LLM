<h1>
    <font size="6">Connections-LLM </font>
</h1>
<font size="4">
    <em>Synthesising <a href="https://www.nytimes.com/games/connections">the popular NY Times puzzle</a> with an LLM</em>
</font>

<br>

If you didn't know, NY Times has a new daily puzzle called "Connections" which they ripped off of BBC's Only Connect. To be fair, they have made the categories and answers more casual and doable. You have a 4x4 grid of 16 words, and they can be divided evenly into 4 secret categories. The goal is to guess 4 words at a time to see if you've uncovered a category, and you get 4 lives.

## Why LLMs?
The categories are diverse and can be very creative and out-of-the-box. Here are some examples I compiled in just 10 minutes (ALLCAPS: NY Times, Capitalcase: BBC).

Literal dictionary meaning:
- WET WEATHER                   (HAIL, RAIN, SLEET, SNOW)
- MAR                           (CHIP, DING, NICK, SCRATCH)

Association with something:
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

Even from this small corpus, you can see how wide the gamut of categories is. This is the beauty I see in this game.

You couldn't fathomly list all the categories a word could belong to. Even if you made a semantic connection graph of words from a dictionary, and another from all the idioms and rhymes ever known, and one for boy names in the world, you still wouldn't be able to list 4 Car Rental Companies, or 4 Harry Potter Spells or 4 Travel Souvenir Ideas, or 4 Nvidia Architecture Codenames.

You pretty much need to have lived as a human, in the physical world seeing things, doing things, hearing and learning about things. The next best thing IMO is a generative pre-trained model that has trawled through the internet and has read and trained on everything we have ever talked about. Basically a talking wikipedia.

## Roadmap
TODO

### Hi! I'm still working on documenting everything I've worked on so far. If you are interested to know more about something I haven't written about yet, I'd be happy to discuss this further!
Soz, I've been too busy with hunting for a rtx 3090 lately

