import os
from gensim import corpora, models, similarities

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]


from pprint import pprint  # pretty-printer
from collections import defaultdict

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]

# remove words that appear only once
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

pprint(texts)


dictionary = corpora.Dictionary(texts)
dictionary.save('C:\\Projects\\nlp\\src\\test\\deerwester.dict')  # store the dictionary, for future reference
print(dictionary)


corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('C:\\Projects\\nlp\\src\\test\\deerwester.mm', corpus)

lsi = models.LsiModel(corpus, num_topics=2)

print("print_topics")
print(lsi.print_topics(2))

print("show_topic")
print(lsi.show_topic(0))
print(lsi.show_topic(1))

print("print_debug")
print(lsi.print_debug())

print("lsi")
print(lsi)