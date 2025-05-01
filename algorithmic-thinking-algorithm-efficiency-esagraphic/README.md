# Python-algorithmic_thinking-algorithm_efficiency

Python has several built-in functions to search for words in a larger text (substrings in a string). **Without using any of these** can you make the ``find`` function in ``find.py`` be more efficient and scale better?

**Overview of files**
====

``find.py`` - This file contains the search algorithm. The length of the `word`
that is being looked for is stored in `word_length`. As a next step, the
algorithm then tries to find the word in the `text` by starting in a random
place within the `text` and comparing with the following letters from there.
These steps are repeated as often as necessary until the correct index number is
located. You should modify this file to make the algorithm look more
systematically through the `text`, to return a value of `-1` if the word is not
present at all. Furtheron the algorithm itself should be tailored to work more
efficiently with larger file sizes.

Run the ``app.py`` both without any modifications and with modifications. It should run at least 5 times faster with your modifications.

``sample.txt`` - This is a sample text file. For this exercise we use it as the main text within which we are searching for a word.

``app.py`` - This file contains the main app. Run it to load the app. It tries to run the find algorithm 1000 looking for a random word each time to see whether it returns a correct index value each time and it measures how long it takes to perform the search. You do not need to modify this file.

**Bonus:**
====

Read about the [Knuth-Morris-Pratt algorithm](https://johnlekberg.com/blog/2020-11-15-string-search.html). Create a ``find_kmp.py`` file with a find function uses that this algorithm. Try running ``app.py`` on your own algorithm in ``find.py`` and on the KMP algorithm in ``find_kmp.py``. How do the timings compare? Under what circumstances is the KMP algorithm faster? 
