
# -*- coding: utf-8 -*-

import random


##
# Based on u/GanjhisKhan's  post on r/Jordan_Peterson_Memes 2019.02.05 (he's trapped in an archetypical story of profound significance, please send help)
# www.reddit.com/r/Jordan_Peterson_Memes/comments/anmawh/jp_conspiracy_theory_starterpack
#

# code originated: u/superfluous_umlaut
#
# License : Code is free to use and modify. Give credit where credit's due.
#
##
 
""" Jordan B. Peterson Conspiracy Theory Genarator"""


villians = ['Postmodern Noemarxists', \
            'Feminists (who secretly crave domination', \
            'Leftist academics', \
            'Dangerous idealogues', \
            'Derrida and Foucault', \
            'Indoctrinated students', \
            'Social justice types', \
            'Radical trans activists', \
            'Politically-correct HR departments', \
            'Actual communists', \
            'The Left', \
            'Millienials with a victimhood mentality']

spicy_verbs = ['are totally corrupting', \
               'have zero respect for', \
               'want to annihilate', \
               'assault the archetype of', \
               "don't bloody believe in", \
               'will quickly infect', \
               'unleash the Chaos Dragon of', \
               'dismiss and transgress', \
               'must be stopped from attacking', \
               'will make Gulags out of', \
               'feminize and weaken']

jbp_favs = ['the dominance hierarchy', \
            'the metaphorical substrate', \
            'Western values', \
            'the classical humanities', \
            'the individual', \
            "the Hero's journey", \
            'the fabric of Being', \
            "Solzhenitsyn's genius", \
            "Carl Jung's legacy", \
            "IQ testing's ability to determine achievement", \
            'the divine Logos', \
            'the inescapable tragedy and suffering of life', \
            "the humble lobster's quest"]

conn_ = 'because of their'

evil_weapons = ['murderous equity doctrine', \
                'dangerous egalitarian utopia', \
                'hatrd of Objective Truth', \
                'compelled speach', \
                'group identity', \
                'Maoist pronouns', \
                'propaganda from Frozen', \
                'radical collectivism', \
                'lens of power for everything', \
                'disdain for Being', \
                'ideological bill C-16', \
                'low serotonin levels and poor posture', \
                "totalitarian ideology which I've been studying for decades"]

ominous_conclusions = ["and we can't even have a conversation about it!", \
                       "so just ask the Kulaks how that worked out.", \
                       'and no one is talking about it!', \
                       'as you can bloody well imagine', \
                       'just like Nietzsche prophesized.', \
                       'so you should sign up for the Self-Authoring Suite.', \
                       '[while still ignoring original question] so let me ask you this...', \
                       'and you can be damn sure about that!', \
                       "and that's that!"]

def join_phrase(data):
    ele = [data['villians'], data['verbs'], data['favorites'], conn_, data['weapons'], data['conclusions'] ]

    return " ".join(ele)

def main():
    data = {'villians': villians, \
            'verbs': spicy_verbs, \
            'favorites': jbp_favs, \
            'weapons': evil_weapons, \
            'conclusions': ominous_conclusions }
    
    out = {}

    for k, v in data.items():        
        out[k] = random.choice(v)
    
    phrase = join_phrase(out)

    print(phrase)    

if __name__ == '__main__':
    main()


