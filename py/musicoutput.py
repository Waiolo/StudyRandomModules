VERSES = [
'and a Partridge in a Pear Tree.',
'two Turtle Doves',
'three French Hens',
'four Calling Birds',
'five Gold Rings',
'six Geese-a-Laying',
'seven Swans-a-Swimming',
'eight Maids-a-Milking',
'nine Ladies Dancing',
'ten Lords-a-Leaping',
'eleven Pipers Piping',
]

POSITIONS = [
'first',
'second',
'third',
'fourth',
'fifth',
'sixth',
'seventh',
'eighth',
'ninth',
'tenth',
'eleventh',
'twelfth'
]
def recite(start_verse, end_verse):
    verses = VERSES[start_verse-1:end_verse]
    full_verses = []

    for verse in verses:
        build_verses = VERSES[1:VERSES.index(verse)+1]
        build_verses.reverse()

        if VERSES.index(verse) == 0:
            build_verses.append(VERSES[0])
        else:
            build_verses.append(f'and {VERSES[0]}')

        build_verses = ','.join(build_verses)

        position = POSITIONS[VERSES.index(verse)]

        full_verses.append(f'On the {position} day of Christmas my true love gave to me: {build_verses}')

    return full_verses