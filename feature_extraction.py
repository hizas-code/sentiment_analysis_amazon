
def feature_extraction(data):
	features = {}
	topic =  data[0]
	words = data[1]
	features['topic'] = topic
	words = negate_sequence(words)
	words = set(words)
	for word in words :
		features[word] = word in words
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