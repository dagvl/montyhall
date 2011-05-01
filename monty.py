import random

def main():
    run_n(1000000, False)
    run_n(1000000, True)
def run_n(n, change):
    
    random.seed() #FIXME
    acc = {}
    acc[True] = 0
    acc[False] = 0
    for i in xrange(0, n):
        result = one_round(change=change)
        acc[result] += 1
        
        
    print "------"
    print "Change?:   ", repr(change)
    print "Correct:   ", acc[True]
    print "Wrong:     ", acc[False]
    print "Percentage:", (acc[True] / (acc[True] + acc[False] + 0.0))


def one_round(change):
    car = random.randint(0, 2)
    selection = random.randint(0, 2)
    
    door = ["g", "g", "g"]
    door[car] = "C"
    selection_out = [" ", " ", " "]
    
    if change:
        selection_out[selection] = "i"
        new_choice = [0, 1, 2]
        new_choice.remove(selection)
        if(door[new_choice[0]] == "g"):
            new_choice.remove(new_choice[0])
        else:
            new_choice.remove(new_choice[1])
        
        if len(new_choice) != 1:
            raise Exception("Too many doors!? " + str(len(new_choice)))
        selection = new_choice[0]       
       
    
    selection_out[selection] = "X"
    
    #print "".join(door), "", 
    #print "".join(selection_out)
    
    return car == selection
     
    
    
    
if __name__ == '__main__':
    main()
    
    