# Advent of Code 2020

It's advent of code time so I decided to upload my solutions to github. Not entirely sure how far I am going to get but hopefully I'll have the time to make it all the way through. A quick word of notice that although I try to solve things in a nice way sometimes things get messy trying to solve and if it works I'm not gonna go back and optimize stuff for these daily challenges.  

Every day is stored in its own folder with the input for that day. Both problems are solved in the same program, some integrated together cleaner than others. I've decided to write things in Python because it is fun and quick.  

Throughout Advent of Code I have been using the map function to do basic input parsing. I have though been aware of the more standard pythonic way of list creation. I decided to do a quick test to see which is really faster in `listManip.py` and sadly my was was a tiny bit slower. Running it with 10000000 repetitions it took the map version 38.2305561 seconds to finish and the standard python list version 37.2890668 seconds to finish. I am absolutely crushed my way was slightly slower. Ignorance truly was bliss.  
