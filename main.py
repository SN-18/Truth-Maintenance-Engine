import propositional


#driver code
if __name__ =="__main__":

    f = open("LogicFile.txt")
    # print("hi")

    kb = []
    li_statements=[]

    TMS=propositional.TMS(kb)
    # print(TMS.kb)

    final_state=[]
    index=0

    for line in f:

        print(line)
        # print(line.strip('\n'))
        index+=1
        state=[]

        if "ASSERT" in line:
            # print("assert")
            state.append(index)
            statement=line[9:].strip('\n').strip(' ').strip(' ').strip('(').strip(')')
            state.extend(statement.split(', '))

            final_state=[]
            # final_state.append(index)

            for i in range(len(state)):
                final_state.append(state[i]) #idea is to append final_state[i+1]=state[i]

            #debugging print statement commented out
            # print("final state is", final_state)

            # if not kb:

            ret_val=TMS.assert_s(final_state)

            #conflict has occurred, do not continue
            if ret_val==-1:
                break

            # elif kb:
            #     TMS.resolution(kb, state)

            # print(statement)

        elif "RETRACT" in line:
            index+=1
            # state.append(index)
            # print("retract")
            statement = line[10:].strip('\n').strip(' ').strip('(').strip(')')

            # print(statement)
            state.extend(statement)
            #debugging print statements commented out
            # print("retract state is", state)
            # print("retract statement is",state)
            TMS.retract_s(state)
            # print("I've returned from retract")




    print("The kb is:")
    for i in range(len(TMS.kb)):
        print(TMS.kb[i])
