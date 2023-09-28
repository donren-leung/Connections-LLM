<h1>
    <font size="6">Connections-LLM </font>
</h1>
<font size="4">
    <em>Synthesising <a href="https://www.nytimes.com/games/connections">the popular NY Times puzzle</a> with an LLM</em>
</font>

### About Connections
If you didn't know, NY Times has a new daily puzzle called "Connections" which they ripped off of BBC's Only Connect. To be fair, they have made the categories and answers more casual and doable. You have a 4x4 grid of 16 words, and they can be divided evenly into 4 secret categories. The goal is to guess 4 words at a time to see if you've uncovered a category, and you get 4 lives.

### Why Connections
Applying LLMs to Connections is a passion project to get more than the daily puzzle, while learning more about LLMs along the way. Along the way if it's easy, interesting or a prerequisite, I'll probably try other things like *solving* a Connections puzzle, rating the difficulty of a category, or creating region- or domain- themed puzzles. See the below [roadmap](#roadmapgoalsideas).

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

### Category-first approach
You couldn't fathomly list all the categories a word could belong to. Even if you made a semantic connection graph of words from a dictionary, and another from all the idioms and rhymes ever known, and one for all the characters in all the famous books in the world, you wouldn't be able to associate "Hatter" to *all* of these categories:
1. Fictional Character in Alice in Wonderland 2. Occupation 3. Mad as a ___ 4. Fictional Character Frozen in Time

Notably 4. which I arbitrarily extended from 1. because I don't just superficially know of the Mad Hatter!

### Extrapolating from past Connections puzzles
The best way I see to do it is, you want to think of a category first, then see what words you can think of to go in that category. I want to test out <ins>my hypothesis that Generative AI, once trained on existing Connections puzzles</ins> either with fine tuning or in-context instruction, will be <ins>creative enough to generate a diverse range categories.</ins> From Car Rental Companies and Harry Potter Spells to Travel Souvenir Ideas and Nvidia Architecture Codenames.

You pretty much need to have lived as a human, in the physical world seeing things, doing things, hearing and learning about things to make interesting connections between things. The next best thing IMO is a generative pre-trained model that has trawled through the internet and has read and trained on everything we have ever talked about. Basically a talking wikipedia. It also might not hurt to perform RAG using sources like wiki to keep up to date.

## Roadmap/goals/ideas
There is so much more potential than just parroting the NY Times! And there are so many interesting side-quests along the way!!
- Synthesising the entire puzzle
    - Synthesising individual categories + generating words from an input category
        - Domain- themed categories -> categories for Australians, Star Wars fans, people in the legal field etc.
            - Try prompting LLM. Maybe GPT4 is good enough if it isn't too niche, else wait for GPT5
            - Fine tuning/RAG for super niche domain knowledge
            - Wiki/google
        - Categories and answers in different languages at the same or different time. Puzzles for 👩‍🎓 people learning languages or 🧠 multilinguists!!

    - BFS/DFS graph-based generation to explore and randomly choose from possibilities \
        Figuring out the best way to interlace categories and words for maximum number of red herrings for an extra challenge.
        - Using a programming language with an LLM-integrated framework like Microsoft guidance, LMQL, Langchain: \
            Use the programming language for the execution logic and flow. \
            🔎 LLM results can be extracted into arrays. \
            🔎 Chain of thought prompting is only good for linear processes

- Solving the puzzle
    - Classifying the category based on 4 words
    - Graph-based traversal; solving a 4 categories before submitting an answer.

    - Classifying the regionality/domain given a category and its 4 words \
        🔎 Scrape historic puzzles from BBC and NY Times, to use as training for regionality.
    - Classifying the difficulty of a category \
        NY Times has a colour system for difficulty


### Hi! I'm still working on documenting everything I've worked on so far. If you are interested to know more about something I haven't written about yet, I'd be happy to discuss this further!

