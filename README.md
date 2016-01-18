# markovinator
Markov chain generator for Python.


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
