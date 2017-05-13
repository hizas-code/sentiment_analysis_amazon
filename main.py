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
    data_train = ([(review, label) for review,label in zip(reviews,labels)])
    feature_sets = [(feature_extraction(data), label) for (data,label) in data_train]
    classifier = NaiveBayesClassifier.train(feature_sets)
    return classifier

def main():
    classifier = learning()
    testing_string = 'I really like this'
    prob = classifier.classify(feature_extraction(testing_string))
    print(prob)

if __name__ == '__main__':
    main()