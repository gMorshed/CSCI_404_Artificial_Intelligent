#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        logical_expression
# Purpose:     Contains logical_expression class, inference engine,
#              and assorted functions
#
# Created:     09/25/2011
# Last Edited: 07/22/2013  
# Notes:       *This contains code ported by Christopher Conly from C++ code
#               provided by Dr. Vassilis Athitsos
#              *Several integer and string variables are put into lists. This is
#               to make them mutable so each recursive call to a function can
#               alter the same variable instead of a copy. Python won't let us
#               pass the address of the variables, so put it in a list which is
#               passed by reference. We can also now pass just one variable in
#               the class and the function will modify the class instead of a
#               copy of that variable. So, be sure to pass the entire list to a
#               function (i.e. if we have an instance of logical_expression
#               called le, we'd call foo(le.symbol,...). If foo needs to modify
#               le.symbol, it will need to index it (i.e. le.symbol[0]) so that
#               the change will persist.
#              *Written to be Python 2.4 compliant for omega.uta.edu
#-------------------------------------------------------------------------------

import sys
from copy import copy

#-------------------------------------------------------------------------------
# Begin code that is ported from code provided by Dr. Athitsos
class logical_expression:
    """A logical statement/sentence/expression class"""
    # All types need to be mutable, so we don't have to pass in the whole class.
    # We can just pass, for example, the symbol variable to a function, and the
    # function's changes will actually alter the class variable. Thus, lists.
    def __init__(self):
        self.symbol = ['']
        self.connective = ['']
        self.subexpressions = []

def print_expression(expression, separator):
    """Prints the given expression using the given separator"""
    if expression == 0 or expression == None or expression == '':
        print('\nINVALID\n')

    elif expression.symbol[0]: # If it is a base case (symbol)
        sys.stdout.write('%s' % expression.symbol[0])

    else: # Otherwise it is a subexpression
        sys.stdout.write('(%s' % expression.connective[0])
        for subexpression in expression.subexpressions:
            sys.stdout.write(' ')
            print_expression(subexpression, '')
            sys.stdout.write('%s' % separator)
        sys.stdout.write(')')


def read_expression(input_string, counter=[0]):
    """Reads the next logical expression in input_string"""
    # Note: counter is a list because it needs to be a mutable object so the
    # recursive calls can change it, since we can't pass the address in Python.
    result = logical_expression()
    length = len(input_string)
    while True:
        if counter[0] >= length:
            break

        if input_string[counter[0]] == ' ':    # Skip whitespace
            counter[0] += 1
            continue

        elif input_string[counter[0]] == '(':  # It's the beginning of a connective
            counter[0] += 1
            read_word(input_string, counter, result.connective)
            read_subexpressions(input_string, counter, result.subexpressions)
            break

        else:  # It is a word
            read_word(input_string, counter, result.symbol)
            break
    return result


def read_subexpressions(input_string, counter, subexpressions):
    """Reads a subexpression from input_string"""
    length = len(input_string)
    while True:
        if counter[0] >= length:
            print('\nUnexpected end of input.\n')
            return 0

        if input_string[counter[0]] == ' ':     # Skip whitespace
            counter[0] += 1
            continue

        if input_string[counter[0]] == ')':     # We are done
            counter[0] += 1
            return 1

        else:
            expression = read_expression(input_string, counter)
            subexpressions.append(expression)


def read_word(input_string, counter, target):
    """Reads the next word of an input string and stores it in target"""
    word = ''
    while True:
        if counter[0] >= len(input_string):
            break

        if input_string[counter[0]].isalnum() or input_string[counter[0]] == '_':
            target[0] += input_string[counter[0]]
            counter[0] += 1

        elif input_string[counter[0]] == ')' or input_string[counter[0]] == ' ':
            break

        else:
            print(('Unexpected character %s.' % input_string[counter[0]]))
            sys.exit(1)


def valid_expression(expression):
    """Determines if the given expression is valid according to our rules"""
    if expression.symbol[0]:
        return valid_symbol(expression.symbol[0])

    if expression.connective[0].lower() == 'if' or expression.connective[0].lower() == 'iff':
        if len(expression.subexpressions) != 2:
            print(('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions))))
            return 0

    elif expression.connective[0].lower() == 'not':
        if len(expression.subexpressions) != 1:
            print(('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions))))
            return 0

    elif expression.connective[0].lower() != 'and' and \
         expression.connective[0].lower() != 'or' and \
         expression.connective[0].lower() != 'xor':
        print(('Error: unknown connective %s.' % expression.connective[0]))
        return 0

    for subexpression in expression.subexpressions:
        if not valid_expression(subexpression):
            return 0
    return 1


def valid_symbol(symbol):
    """Returns whether the given symbol is valid according to our rules."""
    if not symbol:
        return 0

    for s in symbol:
        if not s.isalnum() and s != '_':
            return 0
    return 1

#extract Synbol function as required by the project description
def ExtractUniqueSymbol(sentence):
    result_set = set()
    if(len(sentence.subexpressions) == 0): #base case,,if there are no subexpression to this expression,, 
        #return the unique symbols
        for i in sentence.symbol:
            result_set.add(i)
    else:
        for elem in sentence.subexpressions:
            result_set.update(ExtractUniqueSymbol(elem))
    return result_set

#to increase effciency, this function removes the symbols from the symbol list for which we already have values
def Efficiency(symbols,model):
    all_keys=list(model.keys())
    shortened_symbol_list=[]
    for item in symbols:
        if not (item in all_keys):
            shortened_symbol_list.append(item)
    return shortened_symbol_list

#this is the inference algorithm using truth table
def TT_ENTAILS(KB,alpha,model):
    symbols= ExtractUniqueSymbol(KB)
    symbols.update(ExtractUniqueSymbol(alpha))
    symbols = Efficiency(list(symbols), model)
    return TT_CHECK_ALL(KB,alpha,symbols,model)
    
def TT_CHECK_ALL(KB,alpha,symbols,model):
    if(len(symbols) == 0):
        if(PL_True(KB,model)):
            return PL_True(alpha,model)
        else:
            return True       
    else:
        P=symbols[0]
        rest=symbols[1:]
        return TT_CHECK_ALL(KB,alpha,rest,Extend(P,True,model)) and TT_CHECK_ALL(KB,alpha,rest,Extend(P,False,model))

#extending  the model to accomodate for the new symbols values
def Extend(P,bool_value,model):
    model[P]=bool_value
    return model

#PL_TRUE according to the homework assignment
def PL_True(statement,model):
    if(statement.connective[0]==''):
        return model[statement.symbol[0]]
    elif(statement.connective[0] == 'and'):
        if(len(statement.subexpressions) == 0):
            return True
        else:
            result_list=[]
            for item in statement.subexpressions:
                result_list.append(PL_True(item,model))
            if False in result_list:
                return False
            else:
                return True
    elif(statement.connective[0] == 'or'):
        if(len(statement.subexpressions) == 0): 
            return False
        else:
            result_list=[]
            for item in statement.subexpressions:
                result_list.append(PL_True(item,model))
            if True in result_list:
                return True
            else:
                return False
    elif(statement.connective[0] == 'xor'):
        if(len(statement.subexpressions) == 0): 
            return False
        else:
            result_list=[]
            for item in statement.subexpressions:
                result_list.append(PL_True(item,model))
            if(result_list.count(True) ==1):
                return True
            else:
                return False
    elif(statement.connective[0]=='not'):
        if(len(statement.subexpressions) ==0):
            sys.exit("Problem in 'not' connective")
        else:
            return not PL_True(statement.subexpressions[0],model)
    elif(statement.connective[0] =='if'):
        if(len(statement.subexpressions) != 2):
            sys.exit("Problem in 'if' connective")
        else:
            left = PL_True(statement.subexpressions[0],model)
            right = PL_True(statement.subexpressions[1],model)
            if(left ==True and right ==False):
                return False
            else:
                return True
    elif(statement.connective[0] =='iff'):
        if(len(statement.subexpressions) != 2): 
            sys.exit("Problem in 'iff' connective")
        else:
            result1 = PL_True(statement.subexpressions[0],model)
            result2 = PL_True(statement.subexpressions[1],model)
            return result1 == result2
    else:
        return True
# End of ported code
#-------------------------------------------------------------------------------

# Add all your functions here
