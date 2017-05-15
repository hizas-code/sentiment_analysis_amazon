from preprocess import tokenizing
from feature_extraction import feature_extraction
from file_handler import *
from nltk import NaiveBayesClassifier
from scraper import search_spider
from scrapy.crawler import CrawlerProcess
from feature_extraction import get_adjective

import pickle
import nltk

def learning():
    reviews = get_data('Electronics_5.json', 'reviewText')
    ratings = get_data('Electronics_5.json', 'overall')

    labels = []
    i1 = 0
    i2 = 0
    i3 = 0
    i4 = 0
    i5 = 0
    for rating in ratings :
        '''
        if(rating <= 1) : i1 += 1
        if(rating <= 2) : i2 += 1
        if(rating <= 3) : i3 += 1
        if(rating <= 4) : i4 += 1
        if(rating <= 5) : i5 += 1
        if rating >= 4 : labels.append('positive')
        else : labels.append('negative')
        '''
        labels.append(str(rating))
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
    '''
    classifier_file = open('classifier.pickle','rb')
    classifier = pickle.load(classifier_file)
    classifier_file.close()
    '''
    classifier = learning()
    classifier_file = open('classifier.pickle','wb')
    pickle.dump(classifier,classifier_file)
    classifier_file.close()

    prob = classifier.prob_classify(feature_extraction('i hate this product, it is really bad'))
    label = prob.samples()
    print(prob.prob('5.0'))
    '''
    id_review = get_review('Electronics_5.json')
    id_product = get_product('meta_Electronics.json')
    asd = get_data('Electronics_5.json','asin')
    print(asd)
    target = input("Product Name : ")
    for key, value in id_product.items() :
        if target.lower() in key.lower() :
            names = key.lower()
            id = value.lower()
            break
    reviews = []
    print(id)
    print(names)
    i = 0
    for key, value in id_review.items() :
        if id == key :
            reviews.append(value)
            break
    print(reviews)
    
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/53.0.2 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl(search_spider.SearchSpider)
    a = process.start()
    #prob = classifier.classify(feature_extraction(testing_string))
    '''

main()

