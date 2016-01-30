# markovinator
Markov chain string generation module for Python.

# Adding this module to your project
Add the markovinator.py file to the same directory your project is located in. Then import:

    from markovinator import Markovinator
    
# How to use this module

Simply create an instance of the Markovinator class, 
passing the sample string as input. Then call on the object's 
*generate_sentence()* method or *generate_paragraph()* method to 
generate a pseudo-random string based on that input.

Example program:

    markov = Markovinator("The quick brown fox jumps over the lazy dog.")
    print markov.generate_sentence()
    
You can control how many sentences to generate using the 
*generate_paragraph()* method by passing it as an input parameter, e.g.:
    
    print markov.generate_paragraph(6) # prints a paragraph 6 sentences long

You can add to and change the sample input as well:

    markov.add_input("This input will add to the previous input.")
    
The *add_input()* add to the previously existing input. Alternatively, you can replace the current input with a new set of input text using the *refresh_input()* method.

    markov.refresh_input("This input will replace the previous input.")
