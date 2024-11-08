import nltk
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
import re

### Sentiment analysis
analyzer = SentimentIntensityAnalyzer() ## instantiating the class
## dictionary with polarity scores
# scores = analyzer.polarity_scores("Hey, look now how beautiful the trees are. I love them.")
# if scores["pos"]>scores["neg"]:
# 	print("Positive text")
# else:
# 	print("Negative text")
# #######


with open("miracle-in-the-andes.txt", 'r', encoding="utf8") as f:
	book = f.read()


### Splitting the book by chapers with re
pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)

chapters = chapters[1:]

for nr, chapter in enumerate(chapters):
	scores = analyzer.polarity_scores(chapter)
	print(nr, scores)


