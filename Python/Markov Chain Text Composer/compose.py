
import os, re
import string, random
from graph import Graph, Vertex


def get_words(text_path):
    with open(text_path, 'r') as file:
        text = file.read()
        
        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        
    words = text.split()
    words = words[:1000]
    return words


def make_graph(words):
    g = Graph()
    prev_word = None
    
    for word in words:
        word_vertex = g.get_vertex(word)
        if prev_word:
            prev_word.increment_edge(word_vertex)
        
        prev_word = word_vertex
        
    g.generate_probability_mapping()
    return g


def compose(g: Graph, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
        
    return composition


if __name__ == '__main__':
    words = get_words('Markov Chain Text Composer\hp_sorcerer_stone.txt')
    g = make_graph(words)
    composition = compose(g, words, 100)
    print(' '.join(composition))
