Name: Gazi Mahbub Morshed
CSM ID: 10726727
Programming language: Python 3.6.5
Code structure: I have Bayesian Network class in bayesian_network.py. It has instance variable for all the variables and conditions and given events
                It also has the compute_probabilty function which computes the joint probabilty given the Truth values for all the events.
                It also has a function which loads up all the given values by the project and another function called remainning possible values 
                which generates all the truth values for the hidden variables.
                Main reads in the command line arguments and populates the appropiate values for the Bayesian Network class. 
                It also checks to make sure command line arugments are correct. Then it goes through c1 and c2 events and computes their probabilty.
                I have rounded up the result to 10 decimal places.
To run the code: In your command line, go to the root of the submitted directory and 
                 run "python main.py [the events to find the probability for]"
