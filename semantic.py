import spacy

# Load the larger language model
nlp = spacy.load('en_core_web_md')

# Similarity between words: cat, monkey, and banana
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print("Similarity between 'cat' and 'monkey':", word1.similarity(word2))
print("Similarity between 'banana' and 'monkey':", word3.similarity(word2))
print("Similarity between 'banana' and 'cat':", word3.similarity(word1))

# Similarity between words: cat, monkey, banana, and zoo (example of our own)
word_zoo = nlp("zoo")
print("Similarity between 'zoo' and 'cat':", word_zoo.similarity(word1))
print("Similarity between 'zoo' and 'monkey':", word_zoo.similarity(word2))
print("Similarity between 'zoo' and 'banana':", word_zoo.similarity(word3))

# Working with vectors for words comparison
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Working with sentences
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
