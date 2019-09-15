#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        check_true_false
# Purpose:     Main entry into logic program. Reads input files, creates 
#              base, tests statement, and generates result file.
#
# Created:     09/25/2011
# Last Edited: 07/22/2013     
# Notes:       *Ported by Christopher Conly from C++ code supplied by Dr. 
#               Vassilis Athitsos.
#              *Several integer and string variables are put into lists. This is
#               to make them mutable so each recursive call to a function can
#               alter the same variable instead of a copy. Python won't let us
#               pass the address of the variables, so I put it in a list, which
#               is passed by reference.
#              *Written to be Python 2.4 compliant for omega.uta.edu
#-------------------------------------------------------------------------------

import sys
from logical_expression import *





def main(argv):

    model={}
    if len(argv) != 4:
        print(('Usage: %s [wumpus-rules-file] [additional-knowledge-file] [input_file]' % argv[0]))
        sys.exit(0)

    # Read wumpus rules file
    try:
        input_file = open(argv[1], 'r')
    except:
        print(('failed to open file %s' % argv[1]))
        sys.exit(0)

    # Create the knowledge base with wumpus rules
    print('\nLoading wumpus rules...')
    knowledge_base = logical_expression()
    knowledge_base.connective = ['and']
    for line in input_file:
        # Skip comments and blank lines. Consider all line ending types.
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  # A mutable counter so recursive calls don't just make a copy
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    # Read additional knowledge base information file
    try:
        input_file = open(argv[2], 'r')
    except:
        print(('failed to open file %s' % argv[2]))
        sys.exit(0)

    # Add expressions to knowledge base
    print('Loading additional knowledge...')
    for line in input_file:
        # Skip comments and blank lines. Consider all line ending types.
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  # a mutable counter
        value=line.split() #including the additonal knowledge to the model
        for i,item in enumerate(value):
            if(item[0]=="("):
                a=item.replace("(","")
                value[i]=a
            elif(item[-1]==")"):
                a=item.replace(")","")
                value[i]=a
            
        if(value[0]=='not'):
            model[value[1]]=False
        else:
            model[value[0]]=True
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    # Verify it is a valid logical expression
    if not valid_expression(knowledge_base):
        sys.exit('invalid knowledge base')

    # I had left this line out of the original code. If things break, comment out.
    print_expression(knowledge_base, '\n')

    # Read statement whose entailment we want to determine
    try:
        input_file = open(argv[3], 'r')
    except:
        print(('failed to open file %s' % argv[3]))
        sys.exit(0)
    print('Loading statement...')
    statement = input_file.readline().rstrip('\r\n')
    input_file.close()
    
    # Convert statement into a logical expression and verify it is valid
    statement = read_expression(statement)
    
    
    if not valid_expression(statement):
        sys.exit('invalid statement')

    # Show us what the statement is
    print('\nChecking statement: ', end=' ')
    print_expression(statement, '')
    print()

    # Run the statement through the inference engine
    #check_true_false(knowledge_base, statement)
    check_true_false(knowledge_base,statement,model) 
    sys.exit(1)
    
def check_true_false(knowledge_base,statement,model):
    f = open("result.txt", "w")
    negation_statement = Negation(knowledge_base,statement,model)
    
    if(TT_ENTAILS(knowledge_base,statement,model) and ( not negation_statement )) :
        f.write("definitely true")
    elif(negation_statement and ( not TT_ENTAILS(knowledge_base,statement,model) ) ):
        f.write("definitely false")
    elif not (TT_ENTAILS(knowledge_base,statement,model) and negation_statement ):
        f.write("possibly true, possibly false")
    elif(TT_ENTAILS(knowledge_base,statement,model) and negation_statement ):
        f.write("both true and false")
    f.close()
    
def Negation(knowledge_base,statement,model):
    return not (TT_ENTAILS(knowledge_base,statement,model))


if __name__ == '__main__':
    main(sys.argv)
