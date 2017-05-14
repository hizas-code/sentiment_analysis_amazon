from preprocess import tokenizing
from feature_extraction import feature_extraction
from file_handler import get_data
from file_handler import get_data_2
from nltk import NaiveBayesClassifier
import nltk

def learning():
    reviews = get_data('Electronics_5.json', 'reviewText')
    ratings = get_data('Electronics_5.json', 'overall')

    labels = []
    for rating in ratings :
        if rating >= 2.5 : labels.append('positive')
        else : labels.append('negative')
    data_train = ([(review, label) for review,label in zip(reviews,labels)])
    feature_sets = [(feature_extraction(data), label) for (data,label) in data_train]
    classifier = NaiveBayesClassifier.train(feature_sets)
    return classifier

def get_id():
    target = input("Enter a product name to search for : ")
    products = get_data_2('meta_Electronics.json')
    product_id = get_data('Electronics_5.json', 'asin')
    product_review = get_data('Electronics_5.json', 'reviewText')
    target_id = products[target]
    data = ([idProduct,reviewProduct] for idProduct,reviewProduct in zip(product_id,product_review))
    pos = 0
    found = False
    while pos < len(product_id) and not found:
        if product_id[pos] == target_id:
            found = True
            result_id = product_id[pos]
        else:
            pos = pos+1

    while pos < len(data) and not found:
        if result_id == data[pos][0]:
            found = True
            result_review = data[pos][1]
        else:
            pos = pos+1

    return result_review

def main():
    classifier = learning()
    testing_string = 'I really like this'
    prob = classifier.classify(feature_extraction(testing_string))
    print(prob)

if __name__ == '__main__':
    main()