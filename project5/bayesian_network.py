'''
author: Gazi Mahbub Morshed
this is the Baysian network class. It has instance variable for all the variables and the conditions events c1 and the given events c2
It poses the compute probabilty function which takes in all the truth value for the variables and compute the joint probabilty based on that. 
The implimentation is pretty straight forward
It also has a function that populated the inputs that is given by the project writeup. It also has a function called
"remaining possible values which generates both Truth value for the hidden variables
'''
class Bayesian_network:
    def __init__(self):
        self.burglary_truth_values={}
        self.earthquake_truth_values={}
        self.alarm_truth_values={}
        self.mary_called_truth_values={}
        self.john_called_truth_values={}
        self.conditions={}
        self.given_values={}
        
    def computeProbability(self,b_TV, e_TV, a_TV, j_TV, m_TV): #finding joint probabilty
        result_prob=0.0 
        #accessing the value for the given event according to their Truth Value
        burglary_value = self.burglary_truth_values["Bt"]
        earthquake_value = self.earthquake_truth_values["Et"]
        alarm_value = self.alarm_truth_values["At|B"+b_TV+",E"+e_TV]
        john_value = self.john_called_truth_values["Jt|A"+a_TV]
        mary_value = self.mary_called_truth_values["Mt|A"+a_TV]
        #we substract the probabilty from 1 to find the value for when the event is false
        if(b_TV == "f"):
            burglary_value = 1.0 - burglary_value
        if(e_TV == "f"):
            earthquake_value = 1.0 - earthquake_value
        if(a_TV == "f"):
            alarm_value = 1.0 - alarm_value
        if(j_TV == "f"):
            john_value = 1.0 - john_value
        if(m_TV == "f"):
            mary_value = 1.0 - mary_value
        result_prob = burglary_value * earthquake_value * alarm_value * john_value * mary_value
        return result_prob
       
    def loading_input_values(self): #given vales by the problem itself.
        self.burglary_truth_values["Bt"] = 0.001
        self.earthquake_truth_values["Et"] = 0.002
        self.alarm_truth_values["At|Bt,Et"] = 0.95
        self.alarm_truth_values["At|Bt,Ef"]=0.94
        self.alarm_truth_values["At|Bf,Et"]=0.29
        self.alarm_truth_values["At|Bf,Ef"]=0.001
        self.mary_called_truth_values["Mt|At"] = 0.70
        self.mary_called_truth_values["Mt|Af"] = 0.01
        self.john_called_truth_values["Jt|At"] = 0.90
        self.john_called_truth_values["Jt|Af"] = 0.05
        
    def remaining_possible_values(self,given_dict): #genrates both truth value for the hidden variables
        result_dict={}
        if(not "B" in given_dict):
            l=["t","f"]
            result_dict["B"]=l
        if(not "E" in given_dict):
            l=["t","f"]
            result_dict["E"]=l
        if(not "A" in given_dict):
            l=["t","f"]
            result_dict["A"]=l
        if(not "M" in given_dict):
            l=["t","f"]
            result_dict["M"]=l
        if(not "J" in given_dict):
            l=["t","f"]
            result_dict["J"]=l
        return result_dict