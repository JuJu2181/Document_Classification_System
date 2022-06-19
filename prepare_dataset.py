# * Originally the dataset will have 2 different types of documents for AI and WEB. Running this Script will arrange the data in 2 different folders for AI and WEB.
import os 
import shutil 
# Change directory to enter dataset folder 
os.chdir('dataset')
# Make 2 new directories: AI and WEB
os.mkdir('AI')
os.mkdir('WEB')
# To copy the files to respective folders
for file in os.listdir(os.getcwd()):
    if file.endswith("_AI.pdf"):
        shutil.copy(file,'AI/'+file)
    elif file.endswith('_WEB.pdf'):
        shutil.copy(file,'WEB/'+file)
# To delete the original files after copying to the respective folders
for file in os.listdir(os.getcwd()):
    if file.endswith(".pdf"):
        os.remove(file)