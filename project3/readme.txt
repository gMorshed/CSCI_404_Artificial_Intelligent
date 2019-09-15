Name: Gazi Mahbub Morshed
CSM ID: 10726727
Programming language : Python 3.6.5
Code structure: I used the starter code given by the project description. CheckTrueFalse.py contains the function checkTrueFalse which
                calls the inference algorithm and writes the output to the result.txt according to the program description.
                It uses a helper function called Negation right undernearth it. 
                logical_expression.py contains most of my code. TT_ENTAILS is the inference algorithm that is called from checkTrueFalse
                and rest of the code are helper function for the truth table entailment.
                
How to run the code: Assuming the grader have the above python version installed,  root into the main directory of the project and 
                        type from the command line "python check_true_false.py wumpus_rules.txt [additional_knowledge_file] [statement_file]"
                        The result will be stored in result.txt as required. 
Reference: I researched and adapted idea's from the source's sited below
    http://vlm1.uta.edu/~athitsos/courses/cse4308_fall2015/lectures/03a_tt_entails.pdf
    https://github.com/miteshree/Artificial-Intelligence

 
Note: I couldn't figure out how to find the negation of a statement properly, so my implimentation result will work for 
        mostly "definite true" and "definite false". But the inference algorithm finds the correct answer.
                         
