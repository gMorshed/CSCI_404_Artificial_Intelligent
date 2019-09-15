import sys
def calculate_probability():
    number_of_bags=5
    prior_prob_of_bags = [0.1,0.2,0.4,0.2,0.1]
    cherry_prob=[1.0,0.75,0.5,0.25,0.0]
    lime_prob=[]
    file_object = open("result.txt", 'w')
    for item in cherry_prob:
        lime_prob.append(1.0-item)
    if(len(sys.argv) > 2 ): #more than one command line argument is not supported including the filename to run
        print("Can't accept more than one command line argument")
        exit(-1)
    elif(len(sys.argv) == 1):
        file_object.write("Observation sequence Q: \n")
        file_object.write("Length of Q: "+str(0)+"\n\n")
        for i in range(number_of_bags):
            file_object.write("P(h"+str(i+1)+" | Q) = {0:.10f}\n".format(prior_prob_of_bags[i]))    
        file_object.write("\nProbability that the next candy we pick will be C, given Q: {0:.10f}\n".format(0.5))
        file_object.write("Probability that the next candy we pick will be L, given Q: {0:.10f}\n".format(0.5))
        file_object.close()
        exit(0)
    Q = sys.argv[1]
    Q_length = len(Q)
    file_object.write("Observation sequence Q: "+Q+"\n")
    file_object.write("Length of Q: "+str(Q_length)+"\n\n")
    #handle no observation case
    sum_cherry_prob = 0.0
    sum_lime_prob = 0.0
    for i in range(number_of_bags):
        sum_cherry_prob += prior_prob_of_bags[i] * cherry_prob[i] #sum rule
        sum_lime_prob += prior_prob_of_bags[i] * lime_prob[i]
    for i in range(Q_length): #go through all the observation and calculate the product rule
        if(Q[i] == 'C'): #when it's cherry
            for j in range(number_of_bags): #product rule on every bag
                prior_prob_of_bags[j] = (prior_prob_of_bags[j] * cherry_prob[j]) / sum_cherry_prob
                #file_object.write("P(h"+str((i+1))+" | Q) = "+str(prior_prob_of_bags[j])) #observation index start from 0, that's why adding 1 to it
        elif(Q[i] == 'L'):
            for j in range(number_of_bags):
                prior_prob_of_bags[j] = (prior_prob_of_bags[j] * lime_prob[j]) / sum_lime_prob
                #file_object.write("P(h"+str((i+1))+" | Q) = "+str(prior_prob_of_bags[j]))
        else:
            print("INVALID OBSERVATION")
            exit(0)
        #resetting the sum_prob variables as we calculate new sum probabilty based on the new observation
        sum_cherry_prob, sum_lime_prob=0.0,0.0
        for i in range(number_of_bags):
            sum_cherry_prob += prior_prob_of_bags[i] * cherry_prob[i]
            sum_lime_prob += prior_prob_of_bags[i] * lime_prob[i]
    #done calculating the posterior probabilty based on the observation, now writing result
    for i in range(number_of_bags):
        file_object.write("P(h"+str(i+1)+" | Q) = {0:.10f}\n".format(prior_prob_of_bags[i]))        
    file_object.write("\nProbability that the next candy we pick will be C, given Q: {0:.10f}\n".format(sum_cherry_prob))
    file_object.write("Probability that the next candy we pick will be L, given Q: {0:.10f}\n".format(sum_lime_prob))
    file_object.close()


calculate_probability()
