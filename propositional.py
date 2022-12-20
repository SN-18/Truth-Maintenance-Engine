import copy
import queue
import collections


class TMS:
    def __init__(self,kb,state=""):
        self.kb=kb
        self.state=state
        self.resolved_count=-1



    #assert_s asserts statement
    def assert_s(self, current_state):
        #initialization, empty kb, no need of resolution
        if len(self.kb)==0:
            self.kb.append(current_state)
            print("Justification: Initializing KB by adding statement: ",current_state)
            return 0

        # conflict, eg, asserting 'a' when '-a' is in kb
        #eg of current state would be [1,'-a']
        if len(current_state)==2:
            negation_flag=False

            #in above eg, atomic state would be '-a'
            for element in current_state[1:]:
                atomic_statement = str(element)
                if '-' in atomic_statement:
                    atomic_state_negated = atomic_statement[1:]
                else:
                    atomic_state_negated = '-' + atomic_statement[0]

                if '-' in atomic_statement:
                #for eg, '-a'
                    negation_flag=True

                for i in range(len(self.kb)):
                    if len(self.kb[i])==2:  #for eg, kb[i] could be [2,'a']
                        atomic_list=atomic_statement.split('-')
                        atomic_statement_non_negated=atomic_list[-1]
                        if negation_flag and ('-' + self.kb[i][1])==atomic_statement:
                        # if negation_flag and atomic_statement_non_negated in self.kb[i]:
                            #eg, -a is atomic_statement and a is kb[i][1]
                            # and because a and -a are not consistent
                            print("Justification: A conflict has occurred between states",atomic_statement,\
                                "and",self.kb[i][1])
                            return -1

                        elif not negation_flag and (('-'+ atomic_statement)==self.kb[i][1]):
                            #eg atomic_statement='a' and kb[i][1]=='-a'
                            print("Justification: A conflict has occurred between states",atomic_statement,\
                                  "and",self.kb[i][1])
                            return -1

        #End of conflict edge case

        #Iterate through all the atomic statements in current state
        #if current_state=[5,'a','b','-c','d']
        #then atomic statements would be 'a','b','-c','d'
        for i in range(1,len(current_state)):
            atomic_statement=str(current_state[i])

            #iterate over all the smaller lists representing statements
            #in knowledge base, and make a deep copy of each of these statements
            #since one does not want to modify the original kb's lists or
            #statements

            for j in range(0,len(self.kb)):
                kb_copy_j=copy.deepcopy(self.kb[j])


                #for ex, atomic statement is '-a'
                if '-' in atomic_statement:
                    atomic_li=atomic_statement.split('-')
                    atomic_statement_non_negated=atomic_li[1]
                    if atomic_statement_non_negated in kb_copy_j:

                        self.resolution(current_state, kb_copy_j)



                elif ('-' + atomic_statement) in kb_copy_j:
                    self.resolution(current_state, kb_copy_j)



                        #call resolution only when say, 'a' or other atomic
                        # statement; or their negation, such as '-a'
                        # for eg, is in j'th list of kb


        #resolution has either occurred, or it wasn't required, but now
        #I add the current state

        # for x in range(1,len(current_state)):
        #     current_state_string=current_state_string +" " + current_state[x]

        print("Justification: Adding statement",current_state)
        self.kb.append(current_state)
        return










    def retract_s(self, current_state):
        index=current_state[0]


        #if index is not negative, then it means that it's a
        #simple statement from kb, and not one after resolving two statements

        de=collections.deque(current_state)

        q = queue.Queue()
        q.put(current_state)



        while(de):
            current_state_temp=de[0]

            index = current_state[0]


            i=0
            while (i<len(self.kb)):


                if not self.kb[i]:
                    print(self.kb[i])
                    i=i+1
                    continue


                if int(self.kb[i][0])==int(index):

                    #simply remove, as this is the statement

                    print("Justification: Removing statement:",self.kb[i][0],"due to RETRACT:",index)
                    # de.append(self.kb[i])
                    self.kb.remove(self.kb[i])
                    break

                #remove statements that have this statement as a parent

                elif self.kb[i][len(self.kb[i])-1]==int(index) or \
                self.kb[i][len(self.kb[i])-2]==int(index):

                    de.append(self.kb[i])
                    print("Justification: Removing statement at the index",index,"according", \
                    "to logic.txt, due to RETRACT:",index,"as this statement"
                    "is it's parent")

                    self.kb.remove(self.kb[i])
                    #put in dequeue so one can unwind it and remove other statements
                    #which have this as parents

                i=i+1


            de.pop()



        print("return")
        return



    def resolution(self, current_state, kb_state_j):
        # print("I am in resolution")
        current_state_copy = copy.deepcopy(current_state)
        kb_state_j_copy=copy.deepcopy(kb_state_j)
        resolution_flag = False
        new_statement=[]

        for atomic_state in current_state_copy[1:]:
            # if atomic_state in kb_state_j_copy[1:]:
            #     current_state_copy.remove(atomic_state)


            if '-' in atomic_state:
                atomic_state_negated=atomic_state[1:]
            else:
                atomic_state_negated='-'+atomic_state[0]
            # print("atomic_state_negated:",atomic_state_negated)

            if atomic_state_negated in kb_state_j_copy:
                # print("I am here")
                current_state_copy.remove(atomic_state)
                kb_state_j_copy.remove(atomic_state_negated)

        new_statement.append(self.resolved_count)
        self.resolved_count = self.resolved_count - 1
            # new_statement.append(len(self.kb))
        small_li = []
        small_li.extend(current_state_copy[1:])
        small_li.extend(kb_state_j_copy[1:])
        new_statement.append(small_li)

        new_statement.append(current_state_copy[0])
        new_statement.append(kb_state_j_copy[0])

        new_statement_string = ""
        # print("this is the new_statement variable's value",new_statement)
        new_statement_list = new_statement[1:-2]

        # print("new_Statement_list is", new_statement_list)

        for i in range(len(new_statement_list)):
            new_statement_string = new_statement_string + " " + str(new_statement_list[i])
            print("Adding statement", new_statement_string, "to the knowledge base after resolution")
            self.kb.append(new_statement)








































