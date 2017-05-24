from BayesianNetwork import *

##Implement all of the following functions

## Do not modify any of the objects passed in as parameters!
## Create a new Factor object to return when performing factor operations



'''
multiply_factors(factors)

Parameters :
              factors : a list of factors to multiply
Return:
              a new factor that is the product of the factors in "factors"
'''
def multiply_factors(factors):

    name = 'product of'
    new_scope = []
    assignment = []
    assigned = []
    for f in factors:
        scope = f.get_scope()
        name = name + f.name
        for v in scope:
            if not v in new_scope:
                new_scope.append(v)
                assigned.append(False)
    new_factor = Factor(name, new_scope)
    len_factor = len(new_factor)
    
    new_ass = list(new_factor.get_assignment_iterator())
    for a in new_ass:
        a.append(-1)
    
    for f in factors:
        n = 0;
        indexes = []
        while n < len(f):
            indexes.append(new_factor.index(f[n]))
            n = n + 1
        for n_ass in new_ass:
            old_ass = f.get_assignment_iterator()
            find_match = False
            o_ass = old_ass.next()
            while (find_match != True) and (o_ass != NULL):
                same = True
                i = 0
                while (same == True) and (i < len(f)):
                    if o_ass[i] != n_ass[indexes[i]]:
                        same = False
                    else:
                        i = i + 1
                if same == True:
                    if n_ass[-1] == -1:
                        n_ass[-1] = f.get_value(o_ass)
                    else:
                        n_ass[-1] = n_ass[-1] * f.get_value(o_ass)
                    find_match = True
                o_ass = old_ass.next()
            if n_ass[-1] == -1:
                print("cannot find the probability for the assignment\n")
                
    new_factor.add_values(new_ass)
    
    return new_factor



'''
restrict_factor(factor, variable, value):

Parameters :
              factor : the factor to restrict
              variable : the variable to restrict "factor" on
              value : the value to restrict to
Return:
              A new factor that is the restriction of "factor" by
              "variable"="value"
      
              If "factor" has only one variable its restriction yields a 
              constant factor
'''
def restrict_factor(factor, variable, value):
    i = factor.get_scope().index(variable)
    itr = factor.get_assignment_iterator()
    assignments = []
    ass = itr.next()
    while ass != NULL:
        if ass[i] == value:
            ass_with_value = list(ass[i])
            ass_with_value.append(factor.get_value(ass[i]))
            assignments.append(oass_with_value)
        ass = itr.next()
    #should I change variable.evidence_index?    
    
    new_factor = Factor(factor.name + 'restrict' + variable.name + 'to' + value, factor.get_scope())
    #res_index = new_factor.get_scope().index(variable)
    #new_factor.scope[res_index].set_evidence(value)

    new_factor.add_values(assignments)
    return new_factor
    
'''    
sum_out_variable(factor, variable)

Parameters :
              factor : the factor to sum out "variable" on
              variable : the variable to sum out
Return:
              A new factor that is "factor" summed out over "variable"
'''
def sum_out_variable(factor, variable):
    old_scope = factor.get_scope()
    new_scope = old_scope.remove(variable)
    new_factor = Factor(factor.name + 'sum out' + variable.name, new_scope)
    old_ass = list(factor.get_assignment_iterator())
    new_ass = list(new_factor.get_assignment_iterator())
    indexes = []
    for v in new_scope:
        indexes.append(old_scope.index(v))
    
    for o_ass in old_ass:
        #find the correspond new_ass, add the value to that new_ass
        found = False
        n = 0
        while (found == False) and (n < len(new_ass)):
            i = 0
            match = True
            while (i < len(new_scope)) and (match == True):
                if (new_ass[n][i] != o_ass[indexes[i]]):
                    match = False
                else:
                    i = i + 1
            if match = True:
                found = True
                if len(new_ass[n]) == len(new_scope):
                    new_ass[n].append(factor.get_value(o_ass))
                elif len(new_ass[n]) == len(new_scope)+1:
                    new.ass[n][-1] = new.ass[n][-1]+factor.get_value(o_ass)
                else:
                    print("error happen in sum_out_variable, the length of the neww_ass is not correct\n")
            n = n + 1
    new_factor.add_values(new_ass)
    return new_factor

    
'''
VariableElimination(net, queryVar, evidenceVars)

 Parameters :
              net: a BayesianNetwork object
              queryVar: a Variable object
                        (the variable whose distribution we want to compute)
              evidenceVars: a list of Variable objects.
                            Each of these variables should have evidence set
                            to a particular value from its domain using
                            the set_evidence function. 

 Return:
         A distribution over the values of QueryVar
 Format:  A list of numbers, one for each value in QueryVar's Domain
         -The distribution should be normalized.
         -The i'th number is the probability that QueryVar is equal to its
          i'th value given the setting of the evidence
 Example:

 QueryVar = A with Dom[A] = ['a', 'b', 'c'], EvidenceVars = [B, C]
 prior function calls: B.set_evidence(1) and C.set_evidence('c')

 VE returns:  a list of three numbers. E.g. [0.5, 0.24, 0.26]

 These numbers would mean that Pr(A='a'|B=1, C='c') = 0.5
                               Pr(A='a'|B=1, C='c') = 0.24
                               Pr(A='a'|B=1, C='c') = 0.26
'''       
'''
multiply_factors(factors)

Parameters :
              factors : a list of factors to multiply
Return:
              a new factor that is the product of the factors in "factors"
              
restrict_factor(factor, variable, value):

Parameters :
              factor : the factor to restrict
              variable : the variable to restrict "factor" on
              value : the value to restrict to
Return:
              A new factor that is the restriction of "factor" by
              "variable"="value"

              If "factor" has only one variable its restriction yields a 
              constant factor
              
sum_out_variable(factor, variable)

Parameters :
              factor : the factor to sum out "variable" on
              variable : the variable to sum out
Return:
              A new factor that is "factor" summed out over "variable"
'''
def VariableElimination(net, queryVar, evidenceVars):
    
    min_fill = min_fill_ordering(net.factors(), queryVar)
    for var in min_fill:
        factors = []
        for f in net.factors():
            if var in f.get_scope():
                factors.append(f)
        mult_factors = multiply_factors(factors)
        for v in mult_factors.get_scope():
            mult_factors = restrict_factor(mult_factors, v, v.get_evidence())
    
        
