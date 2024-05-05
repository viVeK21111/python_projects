''' Next word prediction using nlp and deep learning '''

# 1) Data cleaning and preprocessing

import string
import numpy as np
# import nltk
# nltk.download('punkt')
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from nltk.tokenize import sent_tokenize


file=open('C:\\Users\\Asus\\Documents\\pg5200.txt','r',encoding='utf8') 

lines=[]
for i in file:
    lines.append(i)

data=""
for i in lines:
    data=' '.join(lines)
    
data=data.replace('\n','').replace('\r','').replace('\ufeff','')

trs=str.maketrans(string.punctuation, ' '*len(string.punctuation))
new_data=data.translate(trs)

z=[]
for i in new_data.split():
    if i not in z:
        z.append(i)
data=' '.join(z)

l=[]

for i in data:
    l.append(sent_tokenize(i))


tokenizer=Tokenizer(num_words=len(data))  # tokenizer object
tokenizer.fit_on_texts([data])
sequence_data=tokenizer.texts_to_sequences([data])[0]
# print(len(data.split()))
# print(len(sequence_data))

# print(sequence_data) 

total_words=len(tokenizer.word_index)+1 
input_sequence=[]
for i in range(1,len(sequence_data)):
    input_sequence.append(sequence_data[:i+1]) 

# print(l1)
# padding the lists

# print(input_sequence)
max_sequence_len=max([len(x) for x in input_sequence])
from keras.utils import pad_sequences
input_sequence=np.array(pad_sequences(input_sequence,maxlen=max_sequence_len,padding='pre'))

x=input_sequence[:,:-1]
y=input_sequence[:,-1]
    
X=np.array(x)
Y=keras.utils.to_categorical(y,num_classes=total_words)


# 2) model
model=keras.Sequential() 
model.add(keras.layers.Embedding(total_words,240,input_length=max_sequence_len-1)) # input_dim=total_words 
# output_dim=240 
model.add(keras.layers.LSTM(1000,return_sequences=True))
model.add(keras.layers.LSTM(1000)) # return_sequence is False by default 
model.add(keras.layers.Dense(1000,activation='relu'))
model.add(keras.layers.Dense(total_words,activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
# model.summary()

model.fit(X,Y)
    
