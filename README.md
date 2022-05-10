# Catalan-Numbers-Music-Generator

The Catalan numbers are a sequence of numbers that occur frequently in many counting problems. For example, the nth Catalan number, C_n, counts the number of expressions containing n pairs of parentheses which are correctly matched: ((())) ()(()) ()()() (())() (()()). The first Catalan numbers for n=0, 1, 2, 3, ... are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, ...

This script creates a midi file based on the sequence of catalan numbers. It chooses notes in E major based on the catalan numbers mod 8. 0=Eb, 1=F, 2=G ... 7=D. It also chooses note duration using the catalan numbers mod 5 
and using that as an index into an array containing [sixteenth, eighth, quarter, half, whole] note durations. 

The script is also adjustable to the number of notes generated, the tonic note, and to the use of a major or minor scale.
