# Import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def encodeGenres(genres):
    g = []
    gn = []
    for genre in genres:
        gl = genre.split('|')
        gn.append(np.array(gl))
        for i in gl:
            if i not in g:
                g.append(i)

    gen = np.zeros((len(gn),len(g)))
    for i in range(len(gn)):
        for j in gn[i]:
            gen[i][g.index(j)] = 1

    return gen   

def encodePlot(plot):
    import re
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    corpus = []
    for i in range(0, plot.shape[0]):
        review = re.sub('[^a-zA-Z]', ' ', plot[i])
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        corpus.append(review)

    # Creating the Bag of Words model
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(max_features = 500)
    plot_X = cv.fit_transform(corpus).toarray()    
    
    return plot_X
    
