"""
Markovinator for Python
Version 0.1

Generates text based on a Markov chain given sample input.
To use, simply create an instance of the Markovinator class, 
passing the sample text as input. Then call on the object's 
generate_sentence() method or generate_paragraph() method to 
generate pseudo-random text based on that input.

Example program:

    from markovinator import Markovinator
    m = Markovinator("The quick brown fox jumps over the lazy dog.")
    print m.generate_sentence()
    
You can control how many sentences to generate using the 
generate_paragraph() method by passing it as an input parameter, e.g.:
    
    print m.generate_paragraph(6) # prints a paragraph 6 sentences long
    
"""

import re
import random

class Markovinator:
    def __init__(self, input):
        self.sentence = ""
        self.input = self._process_input(input) 
        """ 
        Two Markov corpuses to be generated on instantiation:
        The regular pool and the starting pool.
        The starting pool is used to select natural starting points
        for Markov chains
            
        """
        self.pool = {}
        self.starting_pool = {}
        self._generate_pools()

    def _generate_pools(self):
        # Return type: void
        for sentence in self.input:
            for j in xrange(2, len(sentence)):
                key = (sentence[j - 2], sentence[j - 1])
                if key in self.pool:
                    self.pool[key].append(sentence[j])
                else:
                    self.pool[key] = [sentence[j]]    
            if len(sentence) > 2:
                if sentence[0] in self.starting_pool:
                    self.starting_pool[sentence[0]].append(sentence[1])
                else:
                    self.starting_pool[sentence[0]] = [sentence[1]]
            
    def _process_input(self, input):
        # Input type: str
        # Return type: 2D list
        # Splits the input into sentences, then words.
        sentence_list = re.split('([\n\.?])', input)
        sentence_list = [s for s in sentence_list if s is not '']
        sentence_enders = [".", "!", "?", "\n"]
        
        """ Note: This is kind of a cruddy hack to add split delimiters back
            onto the words they were originally attached to """
        for i, s in enumerate(sentence_list):
            if s in sentence_enders:
                sentence_list[i - 1] = sentence_list[i - 1] + s
        for i, sentence in enumerate(sentence_list):
            sentence_list[i] = sentence.split(" ")
            for j in xrange(sentence_list[i].count('')):
                sentence_list[i].remove('')
        return sentence_list
    
    def _get_starting_point(self):
        # Return type: Tuple
        start = random.choice(self.starting_pool.keys())
        starting_point = (start, self.starting_pool[start][random.randint(0, len(self.starting_pool[start]) - 1)])
        return starting_point
    
    def _is_sentence_end(self, word):
        # Input: str
        # Return type: Bool
        return word.endswith(".") or word.endswith("!") or word.endswith("?") or word.endswith("?")
   
    def generate_sentence(self, start=None):
        # Return type: str
        if not start: 
            self.sentence = ""
            start = self._get_starting_point()
            self.sentence += start[0] + " " + start[1]
        next_word = self.pool[start][random.randint(0, len(self.pool[start]) - 1)]
        self.sentence += " " + next_word
        try: 
            self.pool[(start[1], next_word)]
            if not self._is_sentence_end(next_word):
                self.generate_sentence((start[1], next_word))
        except:
            pass
        return self.sentence + " "
        
    def generate_paragraph(self, limit=5):
        # Input: int (optional)
        # Return type: str
        output = ""
        while limit > 0:
            output += self.generate_sentence()
            limit -= 1
        return output
        
    def add_input(self, new_input):
        # Input: str
        # Return type: void
        self.input = self._process_input(new_input)
        self._generate_pools()
        
    def refresh_input(self, new_input=""):
        # Input: str
        # Return type: void
        self.input = self._process_input(new_input)
        self.pool = {}
        self.starting_pool = {}
        self._generate_pools()

