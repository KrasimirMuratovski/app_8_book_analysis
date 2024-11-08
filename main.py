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

###### Regex examples
pattern = re.compile("Chapter [a-z]+")## returns an object; '+' could have more than one digit after the space
pattern = re.compile("Chapter [0-9]+")## returns an object; '+' could have more than one digit after the space

res = re.findall(pattern, book)
 ### OR
res = pattern.findall(book)


# pattern = re.compile("[^.]* love [a-zA-Z]*")
pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
# print(len(pattern.findall(book)))
###### Regex examples


##### Dict sorting
d={
	'would':575,
	'said':56,
	'could':662,
	'like':36,
	'hate':50
}

# srt = sorted(d.items(), key=lambda x: x[1], reverse=True)
# d_list = [(value, key) for (key, value) in d.items()]
# res = sorted(d_list, reverse=True)
##### Dict sorting


#### English STOPWPRDS
english_stopwords = nltk.download('stopwords')
english_stopwords = stopwords.words('english')
filtered_words = []
for word, count in d.items():
	if word not in english_stopwords:
		filtered_words.append((word, count))
#### English STOPWPRDS

### Splitting the book by chapers with re
pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)
### Splitting the book by chapers with re


chapters = chapters[1:]

for nr, chapter in enumerate(chapters):
	scores = analyzer.polarity_scores(chapter)
	print(nr, scores)


