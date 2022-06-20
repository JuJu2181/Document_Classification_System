import nltk 
import pickle 
import fitz 
from sklearn.feature_extraction.text import CountVectorizer
from train_model import input_process

def load_model_and_vectorizer():
    """
    Function to load the model and vectorizer

    Returns:
        None
    """    
    # ? Load the model and vectorizer from pickle file
    model = pickle.load(open("classifier.model",'rb'))
    vectorizer = pickle.load(open("vectorizer.pickle","rb"))
    return model, vectorizer

if __name__ == "__main__":
    model, vectorizer = load_model_and_vectorizer()
    print("Model Loaded Sucessfully")
    #* read the input text from the user
    path = input("Enter the path of the file: ")
    # ? read the input text from the file
    doc = fitz.open(path)
    content = ""
    # ? read the content of the file
    for page in range(len(doc)):
        content += doc[page].get_text()
    # ? preprocess the input text
    content = input_process(content)
    # ? transform the input text to vector
    content = vectorizer.transform([content])
    # ? predict the label of the input text
    pred = model.predict(content)
    if pred[0] == 1:
        print("The document is about AI")
    else:
        print("The document is about WEB") 
    