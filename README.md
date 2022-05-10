# Catalan-Numbers-Music-Generator

The Catalan numbers are a sequence of numbers that occur frequently in many counting problems. For example, the nth Catalan number, C_n, counts the number of expressions containing n pairs of parentheses which are correctly matched: ((())) ()(()) ()()() (())() (()()).

This script creates a midi file based on the sequence of catalan numbers. 
It chooses notes in E major based on the catalan numbers' value mod 8. 
0=Eb, 1=F, 2=G ... 7=D. 
It also chooses the duration of that note taking the catalan numbers' value mod 5 
and using that as an index into an array containing [sixteenth, eighth, quarter, half, whole] note durations. 
You can adjust the below parameters to adjust the number of notes generated, the tonic note, and major or minor.
You can play the generated midi file using musescore or another program.
