import nltk
def pos():
    teststr=str(raw_input("Enter a string:"))
    text=nltk.word_tokenize(teststr)
    list1=nltk.pos_tag(text)
    plc=[]
    for i in range(0,len(list1)):
        if list1[i][1]=='NNP' or list1[i][1]=='NN':
            if list1[i+1][1]=='NNP' or list1[i+1][1]=='NN':
                

        elif dict1[i]=='NN' or dict1[i]=='NNP':
            plc.append(i)
    print plc

    for i in plc:
        teststr=teststr.replace(i,'place')

    print teststr   
    
    
