#list with the names of all the files
nameList = ["pal_seq1.txt","pal_seq2.txt","pal_seq3.txt","pal_seq4.txt","pal_seq5.txt","pal_seq6.txt","pal_seq7.txt","pal_seq8.txt",]

#for loop that runs the code for every file
for item in nameList:
    dataFile = open(item,"r")
    data = dataFile.read()

    # function that finds the reverse sequence   
    def reverse(seq):
        # creates an empty empty variable
        reverse = ""
        # sets a counter to 0
        c = 0
        for item in seq:
            # increases counter by one
            c += 1 
            # adds the item that is the length of the seq - the counter using indexing to reverse
            reverse += seq[len(seq)-c]
        return reverse  

    #function that finds the compliment
    def comp(seq):
        # creates an empty variable 
        compliment = ""    
        for item in seq:
            # finds the compliment of each individual item and adds it to compliment
            if item == "A":
                compliment += "T"
            elif item == "T":
                compliment +="A"
            elif item == "G":
                compliment+="C"
            elif item == "C":
                compliment+="G"
        # returns compliment
        return compliment 
 
    #print(reverse(comp(data)))
    #print(data)

    # compares the reverse compliment to the original sequence
    if comp(reverse(data)) == data:
        print("Yay, it's a palindrome")
    else:
        print("Sadness, it's not.")