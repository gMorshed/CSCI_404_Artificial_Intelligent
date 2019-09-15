'''
Author: Gazi Mahbub Morshed
'''
import sys
from bayesian_network import Bayesian_network

def main(command_line_arguments):
    if(len(command_line_arguments) < 2 or len(command_line_arguments) > 7  ):
        #python included the running file name as an argument, so I just increases the bound by one on both sides
        print("The number of arguments should be between 1 to 6 inclusive")
        exit(-1)
    bayesian_network_obj = Bayesian_network() #instantiate the Bayesian Network class
    bayesian_network_obj.loading_input_values()
    is_given = False
    del command_line_arguments[0] #deleting the file name from command_line_arguments
    for word in command_line_arguments:
        if word == "given":
            is_given = True 
            continue
        if is_given:
            bayesian_network_obj.given_values[word[0]] = word[1]
        else:
            bayesian_network_obj.conditions[word[0]] = word[1] #first character is the variable name and the second character is the truth value
    
    #print(bayesian_network_obj.conditions,"------",bayesian_network_obj.given_values)
    if(is_given and len(bayesian_network_obj.given_values.keys()) < 1 or len(bayesian_network_obj.given_values.keys()) > 4): #if a event is given for c2, it has to less or equal to four event
        print("Given event c2 has to be in between 1-4")
        exit(-1)
    if( len(bayesian_network_obj.conditions.keys()) < 1 or len(bayesian_network_obj.conditions.keys()) > 5) : #validating the c1 events as well 
        print("Number of conditions has to be inbetween 1-5")
        exit(-1)
        
    #update the conditions with the given events
    bayesian_network_obj.conditions.update(bayesian_network_obj.given_values)
    #generating rest of the truth values 
    bayesian_network_obj.conditions.update(bayesian_network_obj.remaining_possible_values(bayesian_network_obj.conditions))
    bayesian_network_obj.given_values.update(bayesian_network_obj.remaining_possible_values(bayesian_network_obj.given_values))
    #print(bayesian_network_obj.conditions,"------",bayesian_network_obj.given_values)
    c1_events_prob, c2_events_prob,final_prob = 0.0,0.0,0.0
    #calculate c1 events probabilty
    for b in range(len(bayesian_network_obj.conditions["B"])):
        for e in range(len(bayesian_network_obj.conditions["E"])):
            for a in range(len(bayesian_network_obj.conditions["A"])):
                for j in range(len(bayesian_network_obj.conditions["J"])):
                    for m in range(len(bayesian_network_obj.conditions["M"])):
                        c1_events_prob += bayesian_network_obj.computeProbability(bayesian_network_obj.conditions["B"][b],\
                        bayesian_network_obj.conditions["E"][e],\
                        bayesian_network_obj.conditions["A"][a],\
                        bayesian_network_obj.conditions["J"][j],\
                        bayesian_network_obj.conditions["M"][m] )
    final_prob = c1_events_prob            
    #calculate c2 events
    if(is_given):
        for b in range(len(bayesian_network_obj.given_values["B"])):
            for e in range(len(bayesian_network_obj.given_values["E"])):
                for a in range(len(bayesian_network_obj.given_values["A"])):
                    for j in range(len(bayesian_network_obj.given_values["J"])):
                        for m in range(len(bayesian_network_obj.given_values["M"])):
                            c2_events_prob += bayesian_network_obj.computeProbability(bayesian_network_obj.given_values["B"][b],\
                            bayesian_network_obj.given_values["E"][e],\
                            bayesian_network_obj.given_values["A"][a],\
                            bayesian_network_obj.given_values["J"][j],\
                            bayesian_network_obj.given_values["M"][m] )
    
        final_prob = c1_events_prob/c2_events_prob
    s=""
    for word in command_line_arguments:
        if(word == "given"):
            s = s[:-4]
            s+="| "
        else:
            s+= word + " and "
    s = s[:-4]
    print("The probabilty of the statement ",s)
    print("{0:.10f}".format(final_prob)) #rounding up to 10 decimal places
    
if __name__ == '__main__':
    main(sys.argv)  
