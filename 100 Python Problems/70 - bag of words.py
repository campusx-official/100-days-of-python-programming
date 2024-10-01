# Write a function that accepts a list of strings, performs Bag of Words, and converts it to numerical vectors.

# https://en.wikipedia.org/wiki/Bag-of-words_model

def bow(sentences):
    vocab = []
    for i in sentences:
        vocab.extend(i.split()) 
    vocab = list(set(vocab))

    vector2d = []
    for sentence in sentences:
        vector = []
        for word in vocab:
            vector.append(sentence.count(word))
        vector2d.append(vector)
    
    return vector2d

sentences = [
    'Hello how are you',
    'I was waiting for your call',
    'where do you work',
    'Lets meet someday',
    'Hope you are fine'
]

bow(sentences)