Author: Gazi Mahbub Morshed
CSM ID: 10726727
Programming language: Java and compiler version 'java version "1.8.0_191" '
Code structure: I used the starter code given from the project writeup. In one-move mode, the indicated player at the end of the input_file acts as an 
                    Maximization player as stated and in interactive mode computer is the maximization player. 

maxconnect4.java: I added the interactive implimentation of the game. It has two parts. Computer part and the human part. I followed the instructions
                    given on how to impliment computer and human's interaction based on the project writeup. 

GameBoard.java : I added two functions called getThreeCount and getTwoCount for the use of the evaluation function. getThreeCount basically counts
                    how many opprtunities are there to convert a three in a row into a score (four in a row) and getTwoCount counts how many        
                    twos can be converted into a score ( 1100 or 0101 or 1010 or 0011 to 1111). See next section for reference

AiPlayer.java :  I have a MINIMAX function that is being called  by the findbestPlay function. MINIMAX function impliments the minimax algorithm with 
                alpha beta pruning as described in the
                lecture and book. MINIMAX calls MAX-VALUE AND MIN-VALUE which are undernearth MINIMAX. Moreover, there are utility-function 
                and evaluation function towards the end of this file. evaluation-function is currently being used for the alpha-beta pruning 
                with depth limit. The evaluation-function has been adapted some from the research paper included in the project write up and 
                the rest from http://web.media.mit.edu/~msaveski/projects/2009_connect-four.html
                Th weights for different scores and possible scores (100,10,4) are the results of educated guess and trail & error.
                I used the utility funtion before I introduced depth limit. 
                
How to run the code: The compilation of the code follows exactly the given direction for java sample code. After unzipping and coming inside the main directory
                        First run : javac maxconnect4.java GameBoard.java AiPlayer.java
                        Then : java maxconnect4 one-move [input_file] [output_file] [depth] (for one-move)
                            or java maxconnect4 interactive [input_file] [computer-next/human-next] [depth] (for interactive mode)
                        if anything else written instead of [computer-next/human-next], the program will terminate
                    The value of the depth of course has an affect on how long will it take to complete the search and the search time 
                    also increases if the board is nearly empty and thus decreases when the board is nearly full. 
                    So, on a nearly empty board, I suggest using a smaller depth limit if you want to computer to make a fast decision.
                        