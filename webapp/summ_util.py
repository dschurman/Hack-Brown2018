from gensim.summarization import summarize
from gensim.summarization import keywords
import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()

# Heart of Darkness, Gutenberg
my_string = """
The Nellie, a cruising yawl, swung to her anchor without a flutter of the sails, and was at rest. The flood had made, the wind was nearly calm, and being bound down the river, the only thing for it was to come to and wait for the turn of the tide. The sea-reach of the Thames stretched before us like the beginning of an interminable waterway. In the offing the sea and the sky were welded together without a joint, and in the luminous space the tanned sails of the barges drifting up with the tide seemed to stand still in red clusters of canvas sharply peaked, with gleams of varnished sprits. A haze rested on the low shores that ran out to sea in vanishing flatness. The air was dark above Gravesend, and farther back still seemed condensed into a mournful gloom, brooding motionless over the biggest, and the greatest, town on earth.
The Director of Companies was our captain and our host. We four affectionately watched his back as he stood in the bows looking to seaward. On the whole river there was nothing that looked half so nautical. He resembled a pilot, which to a seaman is trustworthiness personified. It was difficult to realize his work was not out there in the luminous estuary, but behind him, within the brooding gloom.
"""


# Every One of the World's Big Economies Is Now Growing
nytimes_economy = """
A decade after the world descended into a devastating economic crisis, a key marker of revival has finally been achieved. Every major economy on earth is expanding at once, a synchronous wave of growth that is creating jobs, lifting fortunes and tempering fears of popular discontent.
No tidy, all-encompassing narrative explains how the world has finally escaped the global downturn. The United States has been propelled by government spending unleashed during the previous administration, plus a recent $1.5 trillion shot of tax cuts. Europe has finally felt the effects of cheap money pumped out by its central bank.
In general terms, improvement owes less to some newfound wellspring of wealth than the simple fact that many of the destructive forces that felled growth have finally exhausted their potency. The long convalescence has yielded a global recovery that is far from blistering in pace, and geopolitical risks threaten its demise. Many economists are skeptical that the benefits of growth will reach beyond the educated, affluent, politically connected class that has captured most of the spoils in many countries and left behind working people whose wages have stagnated even as jobless rates have plunged.
And still the fact that every major swath of the globe is expanding is a source of optimism. There is no guarantee that this expansion will prove more equitable. Yet if growth were to evolve, bolstering wages while adding to the security of middle-class lives, the beginning would probably feel something like now.
"""

badline = "aa aaa aaaaaa"

#clean up the string first!! make a function
# remove non ascii? or specify encoding to prevent errors
# remove newline characters?


def summarize_text(input_string, word_count, ratio=0.1):
    try:
        summary = summarize(input_string, word_count=word_count)
        if len(summary) == 0:
            summary = summarize(input_string, ratio = ratio)
    except:
        summary = input_string
    return summary

def get_keywords(input_string, words):
    try:
        stopwords_list = nltk.corpus.stopwords.words('english')
        all_words = input_string.split(" ")
        cleaned_words = [porter_stemmer.stem(word.lower()) for word in all_words if
                         word not in stopwords_list and len(word) > 1 and word.isalpha()]
        yes = " ".join(cleaned_words)
        keys = keywords(yes, words=words)
    except:
        keys = ""
    return keys


# print("************START************")
# print(summarize_text(nytimes_economy, word_count=30))
# print(get_keywords(nytimes_economy))
# print("*************END*************")
