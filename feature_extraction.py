from nltk import pos_tag
from preprocess import tokenizing

def feature_extraction(words):
	features = {}
	tokens = tokenizing(words)
	adjectives = get_adjective(tokens)
	adjectives = set(adjectives)
	for adjective in adjectives :
		features[adjective] = adjective in adjectives
	return features

def negate_sequence(tokens):
	binerNegation = False
	delims = '?.,!:;'
	result = []
	words = tokens
	for word in words:
		stripped = word.strip(delims).lower()
		negated = "not_" +stripped if binerNegation else stripped
		result.append(negated)
		if word in negation:
			binerNegation = not binerNegation
		if any(c in word for c in delims):
			binerNegation = False
	return result

def get_adjective(tokens):
	tagger = pos_tag(tokens)
	adjectives = []
	negated_word = negate_sequence(tokens)
	for (word,tag),negate_word in zip(tagger,negated_word) :
		if tag in adjective_tag : adjectives.append(negate_word)
	return adjectives

adjective_tag = [
	"JJ",
	"JJS",
	"JJR"
]

negation = [
	'no',
	'not',
	'don\'t',
	'didn\'t',
	'ain\'t',
	'isn\'t',
	'aren\'t',
	'haven\'t',
	'hasn\'t',
]