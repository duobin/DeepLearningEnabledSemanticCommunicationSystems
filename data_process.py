import pickle

import numpy
from nltk import word_tokenize
from torch.utils.data import Dataset



class CorpusData(Dataset):
    def __init__(self):
        with open('data/corpus_10w_train.txt', 'r') as file:  # attention the way of file is opened
            start = ""
            end = ""
            self.text = [start + line.strip() + end for line in file]

        with open('data/id_dic_10w.pkl', 'rb') as file:
            self.id_dic = pickle.load(file)

    def __len__(self):
        return len(self.text)

    def __getitem__(self, index):
        sen = self.text[index]  # get sentence at index position
        sen_split = word_tokenize(sen)  # get a list consist of single word in the sentence
        input = numpy.zeros((1, 30))  # used to pad sentence
        num = 0
        for word in sen_split:
            input[0, num] = self.id_dic[word]
            num += 1
            if(num >= 30):  # at most store 30 words
                break

        return input, num
