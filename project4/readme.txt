Name and CSM ID: Gazi Mahbub Morshed (10726727)

Programming language: Python 3.7.2

Code structure: I have a calculate_probability function where all the code resites and I call this 
                function to do the posterior probability calculation. In the beginning of this function
                all the given values are hardcoded. Then I calculate lime probabilty. Then I handle 
                the cases of incorrect argument and no observation. Then I calculate the sum of the 
                probability using sum rule. Then I go through each and every observation sequence and 
                calculate the probabilty of the hyposthesis of the five bags using product rule. 
                Then I calculate the probabilty of next observation of being a specific type.
                Then I write the results to the file. 

Compilation instruction: Through your command line, go the root of the submitted directory where you 
                        can see the main.py . Then run "python main.py [observation_sequence]" and the
                        result will be stored in "result.txt"
