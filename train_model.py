import pandas as pd 
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer 
import string 
import nltk
from nltk.corpus import stopwords 
import fitz
import pickle


#? Initialize the vectorizer
vectorizer = CountVectorizer()

def pre_process_df():
    """
    Function to read the dataset into a pandas dataframe
    """
    f_df = pd.DataFrame(columns=['Text','Label'])
    df = pd.read_csv('dataset.csv')
    f_df['Text'] = df['Text']
    f_df['Label'] = df['Label']
    return f_df

def input_process(text):
    """
    Function to preprocess the input text by translating the punctuations and removing the stop words
    Parameters:
    text: Input text
    """
    translator = str.maketrans('','',string.punctuation)
    # translating punctuations to empty space
    nopunc = text.translate(translator)
    #* removing stop words using list comprehension
    words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    # return bu joining the words from list to a text
    return ' '.join(words)

def remove_stop_words(ip):
    """
    Function to remove the stop words from the input text by processing each line of the text 
    Parameters:
    ip: Input text
    """
    final_ip = [] 
    for line in ip:
        line = input_process(line)
        final_ip.append(line)
    return final_ip



def train_model(df):
    """
    Function to train the model using Multinomial Naive Bayes
    Parameters:
    df: Dataframe containing the text and label
    """
    # X is the input and y is the label
    X = df['Text']
    y = df['Label']
    # remove stop words from input text
    X = remove_stop_words(X)
    df['Text'] = X
    # fit the vectorizer to the input text
    X = vectorizer.fit_transform(X)
    # ? Initialize Multinomial Naive Bayes model
    nb = MultinomialNB()
    # fit the model to the input data
    nb.fit(X,y)
    print("Model Training Done")
    return nb



if __name__ == "__main__":
    #? download the stopwords from the nltk library
    nltk.download('stopwords')
    df = pre_process_df()
    model = train_model(df)
    # save the model to a file
    pickle.dump(model,open('classifier.model','wb'))
    # save the vectorizer to a file
    pickle.dump(vectorizer,open('vectorizer.pickle','wb'))

    