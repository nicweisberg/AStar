# Nick Weisberg



import a1q2_UninformedSearch as BlindSearch
import Problem as P

print()
print()
print()
print("/////////////   Basic Search Algorithms ////////////")
print("//////////// Shows time, nodes & space ////////////")
print("///////////      Nick Weisberg        ///////////")
print()
print()
inputFile = input("Which input file would you like to read from? (easy, moderate, hard, veryhard, puremadness) ")
print()
print("Reading files from "+inputFile+".txt: ")
print()



testProblems = []
file = open(inputFile + ".txt", "r")
lines = file.readlines()
for line in lines:
    print(line)
    line = line.strip()
    line = line.replace("   ", " ")
    line = line.split(" ")
    testProblems.append(line)

timeLimit = int(input("Enter a time limit for the searches (in seconds): "))

print()
print()
print("Performing Breadth First Search: ")
print()



avTime = 0
avNodes = 0
avSpace = 0
counter = 0

for i in range (0,len(testProblems)):

    testProblem = testProblems[i]
    state = P.State(testProblem)


    problem = P.Problem(state)
    

    searcher = BlindSearch.Search(problem,timelimit=timeLimit)

    answer = searcher.BreadthFirstSearch(state)
    if answer.success == True:
        avTime = avTime + answer.time
        avNodes = avNodes + answer.nodes
        avSpace = avSpace + answer.space
        counter = counter + 1
    

    print(str(answer))
print()
if counter>=1:
    print("The average time BreadthFirstSearch took was " + str(avTime/counter) + " seconds")
    print("The average number of nodes BreadthFirstSearch searched was " + str(avNodes/counter) + " nodes")
    print("The average maximum size of the frontier for BreadthFirstSearch was " + str(avSpace/counter))
    print()


print()
print()
print("Performing Depth Limited Search: ")
print()
avTime = 0
avNodes = 0
avSpace = 0
counter = 0
depth = int(input("What is the maximum depth you would like Depth Limited Search to search to? "))

for i in range (0,19):

    testProblem = testProblems[i]
    state = P.State(testProblem)


    problem = P.Problem(state)

    searcher = BlindSearch.Search(problem,timelimit=timeLimit)

    answer = searcher.DepthLimitedSearch(state, depth)
    if answer.success == True:
        avTime = avTime + answer.time
        avNodes = avNodes + answer.nodes
        avSpace = avSpace + answer.space
        counter = counter + 1
    

    print(str(answer))
print()
if counter>=1:
    print("The average time DepthLimitedSearch took was " + str(avTime/counter) + " seconds")
    print("The average number of nodes DepthLimitedSearch searched was " + str(avNodes/counter) + " nodes")
    print("The average maximum size of the frontier for DepthLimitedSearch was " + str(avSpace/counter))
    print()

print()
print()
print("Performing Iterative Deepening Search: ")
print()
avTime = 0
avNodes = 0
avSpace = 0
counter = 0

for i in range (0,19):

    testProblem = testProblems[i]
    state = P.State(testProblem)


    problem = P.Problem(state)
    

    searcher = BlindSearch.Search(problem,timelimit=timeLimit)
   
    answer = searcher.IDS(state)
    if answer.success == True:
        avTime = avTime + answer.time
        avNodes = avNodes + answer.nodes
        avSpace = avSpace + answer.space
        counter = counter + 1
    

    print(str(answer))
print()
if counter>=1:
    print("The average time IterativeDeepingSearch took was " + str(avTime/counter) + " seconds")
    print("The average number of nodes IterativeDeepingSearch searched was " + str(avNodes/counter) + " nodes")
    print("The average maximum size of the frontier for IterativeDeepingSearch was " + str(avSpace/counter))
    print()
    
print()
print()
print("Performing Depth First Search: ")
print()
avTime = 0
avNodes = 0
avSpace = 0
counter = 0

for i in range (0,19):

    testProblem = testProblems[i]
    state = P.State(testProblem)

    
    problem = P.Problem(state)
    
   
    searcher = BlindSearch.Search(problem,timelimit=timeLimit)
 
    answer = searcher.DepthFirstSearch(state)
    if answer.success == True:
        avTime = avTime + answer.time
        avNodes = avNodes + answer.nodes
        avSpace = avSpace + answer.space
        counter = counter + 1
    

    print(str(answer))
print()
if counter>=1:
    print("The average time DepthFirstSearch took was " + str(avTime/counter) + " seconds")
    print("The average number of nodes DepthFirstSearch searched was " + str(avNodes/counter) + " nodes")
    print("The average maximum size of the frontier for DepthFirstSearch was " + str(avSpace/counter))
    print()