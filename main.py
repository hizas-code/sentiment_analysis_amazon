from preprocess import tokenizing
from feature_extraction import feature_extraction
from file_handler import get_data
from nltk import NaiveBayesClassifier
import nltk

def learning():
    reviews = get_data('Electronics_5.json','reviewText')
    ratings = get_data('Electronics_5.json','overall')
    labels = []
    for rating in ratings :
        if rating >= 2.5 : labels.append('positive')
        else : labels.append('negative')
    data_train = ([(label, review) for label,review in zip(labels,reviews)])
    data_train = nltk.classify.apply_features(feature_extraction, data_train)
    classifier = NaiveBayesClassifier.train(data_train)
    return classifier

def main():
    classifier = learning()
    testing_string = 'I really like this'

    data = tokenizing(testing_string)
    feature = feature_extraction(('positive',data))

    prob = classifier.prob_classify(feature)
    print(prob)
    labels = prob.samples()
    print(labels)

if __name__ == '__main__':
    main()