# Nick Weisberg


#########################################################################################
class State(object):
    """The Problem State objects record data needed to solve the search problem.
    """
    def __init__(self, object):

        self.action = 'Initial state'
        """ I split up each line into index, rows, columns, values,
        and goal. I store each value or set of values in an array """
        self.index = object[0]
        self.rows = object[1]
        self.columns = object[2]
        self.values = object[3:3+(int(object[1])*int(object[2]))]
        self.goal = object[3+(int(object[1])*int(object[2])):len(object)]
        

    


    def __str__(self):
        """ I walk through each row of the values,
        creating a 2D array for output on the console """

        display = "Current State            Goal State \n"
        display = display + "\n"
        for i in range(0, int(self.rows)):
            displayArr = self.values[i*(int(self.columns)):(i+1)*(int(self.columns))]
            displayArrGoal = self.goal[i*(int(self.columns)):(i+1)*(int(self.columns))]
            for i in displayArr:
                display = display + str(i) + "  "
            display = display + "           "
            for i in displayArrGoal:
                display = display + str(i) + "  "
            display = display + "\n"
            display = display + "\n"
        return display

    def __eq__(self, other):
        """ Allows states to be compared by comparing their data """
        return False

#########################################################################################
class InformedState(State):
    """We add a place to
       store the estimated path cost to the goal state.  
    """
    def __init__(self, puzzle, hval=0):
        """
           The hval attribute estimates the path cost to the goal state from the current state
        """
        super().__init__(puzzle)
        self.hval = hval


#########################################################################################
class Problem(object):
    """The Problem class defines aspects of the problem such as is_goal(), 
    actions(), result()
    """

    def __init__(self, object):
        self._stuff = 'might add initializations'


    def is_goal(self, a_state:State):
        """Returns true if the given state is a goal state"""
        if a_state.values == a_state.goal:
            return True
        return False


    def actions(self, a_state:State):
        """ I create an array of actions consisting of an up and down
        action for every column, and a right and left action for every row
        """
        global actionList
        actionList = []
        for i in range(0, int(a_state.rows)):
            actionList.append("shiftRow" + str(i) + "Left")
            actionList.append("shiftRow" + str(i) + "Right")
        for i in range(0, int(a_state.columns)):
            actionList.append("shiftColumn" + str(i) + "Up")
            actionList.append("shiftColumn" + str(i) + "Down")
        
        return actionList

    def result(self, a_state:State, an_action):
        """Given a state and an action, return the resulting state.
        """
        index = a_state.index
        rows = a_state.rows
        columns = a_state.columns
        values = a_state.values
        goal = a_state.goal
        
        if an_action not in actionList:
            print("That action is not an option. Please select from list above.")
            return None
        action = an_action.replace("shift","")
        
        #I search the string for keywords to determine what action to use, then store the row/column number
        
        if "Row" in action:
            action = action.replace("Row","")
            if "Left" in action:
                action = action.replace("Left","")
                indexNumber = int(action)
                
                # I determine where in the array of values the row being shifted starts and ends
                # then create a new array to store the values of the current row
                
                startOfEdit = indexNumber * int(columns)
                endOfEdit = startOfEdit + int(columns)
                rowOrg = values[startOfEdit:endOfEdit]
                
                # I then create another array to store the edited row, 
                # and walk through the original row, shifting each element by 1
                
                editedRow = []
                for i in range(0, len(rowOrg)-1):
                    editedRow.append(rowOrg[i+1])
                editedRow.append(rowOrg[0])
                
                # I then create a new array to store the new values, putting my edited row in its place
                
                newValues = []
                newValues = newValues + values[0:startOfEdit]
                newValues = newValues + editedRow
                newValues = newValues + values[endOfEdit:len(values)]
                
                # I then create a new state with my new values
                
                newState = []
                newState.append(index)
                newState.append(rows)
                newState.append(columns)
                newState = newState + newValues
                newState = newState + goal
                newState = State(newState)
                return newState
                
                
            elif "Right" in action:
            
                # All steps here are identical to the ones above,
                # its just if the row is being shifted right instead of left
            
                action = action.replace("Right","")
                indexNumber = int(action)
                startOfEdit = indexNumber * int(columns)
                endOfEdit = startOfEdit + int(columns)
                rowOrg = values[startOfEdit:endOfEdit]
                editedRow = []
                editedRow.append(rowOrg[len(rowOrg)-1])
                for i in range(1, len(rowOrg)):
                    editedRow.append(rowOrg[i-1])  
                newValues = []
                newValues = newValues + values[0:startOfEdit]
                newValues = newValues + editedRow
                newValues = newValues + values[endOfEdit:len(values)]
                newState = []
                newState.append(index)
                newState.append(rows)
                newState.append(columns)
                newState = newState + newValues
                newState = newState + goal
                newState = State(newState)
                return newState
              
              
        # I search the string for keywords to determine what action to use, then store the row/column number
                
        elif "Column" in action:
            action = action.replace("Column","")
            if "Up" in action:
                action = action.replace("Up","")
                indexNumber = int(action)
                
                # I create an array consisting of the column to be edited
                
                columnOrg = []
                for i in range(0, int(rows)):
                    columnOrg.append(values[indexNumber + i*int(columns)])
                
                editedColumn = []
                
                # I edit the column by shifting all values up or down
                
                for i in range(0, len(columnOrg)-1):
                    editedColumn.append(columnOrg[i+1])
                editedColumn.append(columnOrg[0])
                
                # I then create a new array to store the new values, putting my edited row in its place
                
                newValues = []
                for i in range(0, int(rows)):
                    newValues = newValues + values[i*int(columns):i*int(columns)+indexNumber]
                    newValues.append(editedColumn[i])
                    newValues = newValues + values[i*int(columns)+indexNumber+1:(i+1)*int(columns)]
                 
                 # I then create a new state with my new values
                 
                newState = []
                newState.append(index)
                newState.append(rows)
                newState.append(columns)
                newState = newState + newValues
                newState = newState + goal
                newState = State(newState)
                return newState
                
            # All steps here are identical to shifting up, I just shift down instead
            
            elif "Down" in action:
                action = action.replace("Down","")
                indexNumber = int(action)
                columnOrg = []
                for i in range(0, int(rows)):
                    columnOrg.append(values[indexNumber + i*int(columns)])
                editedColumn = []
                editedColumn.append(columnOrg[len(columnOrg)-1])
                for i in range(1, len(columnOrg)):
                    editedColumn.append(columnOrg[i-1])
                newValues = []
                for i in range(0, int(rows)):
                    newValues = newValues + values[i*int(columns):i*int(columns)+indexNumber]
                    newValues.append(editedColumn[i])
                    newValues = newValues + values[i*int(columns)+indexNumber+1:(i+1)*int(columns)]
                 
                newState = []
                newState.append(index)
                newState.append(rows)
                newState.append(columns)
                newState = newState + newValues
                newState = newState + goal
                newState = State(newState)
                return newState
    
        return None



#########################################################################################
class InformedProblem(Problem):
    """I add the ability to calculate an estimate to the goal state.
    """
    def __init__(self, object):
        super().__init__(object)


    def calc_h(self, a_state, ad, far):
        """This function computes the heuristic function h(n)
        """
        hVal = 0
        
        for value in a_state.values:
            adjacent = []
            row = []
            column = []
            indexCurr = a_state.values.index(value)
            
            # I fetch the row that the value is in and store it in an array
            
            rowNumber = indexCurr//int(a_state.columns)
            row = row + a_state.goal[int(a_state.columns)*rowNumber : int(a_state.columns)*(rowNumber+1)]
        
            # I fetch the column that the value is in and store it in an array
        
            columnNumber = indexCurr%int(a_state.columns)
            for i in range(0, int(a_state.rows)):
                column.append(a_state.goal[columnNumber + i*int(a_state.columns)])
            
            # I create an array of 4 value, each being a directly adjacent value (one shift vertical or horizontal) 
            
            if columnNumber==0:
                adjacent.append(row[1])
                adjacent.append(row[int(a_state.columns)-1])
            elif columnNumber==int(a_state.columns)-1:
                adjacent.append(row[0])
                adjacent.append(row[int(a_state.columns)-2])
            else:
                adjacent.append(row[columnNumber-1])
                adjacent.append(row[columnNumber+1])
                
            if rowNumber==0:
                adjacent.append(column[1])
                adjacent.append(column[int(a_state.rows)-1])
            elif rowNumber==int(a_state.rows)-1:
                adjacent.append(column[0])
                adjacent.append(column[int(a_state.rows)-2])
            else:
                adjacent.append(column[rowNumber-1])
                adjacent.append(column[rowNumber+1])    
            
            
            # If the value is the same as the value in the goal state,
            # I add 10, if it can be reached by 1 shift, add 20, if farther, I add 40
            
            if value == a_state.goal[a_state.values.index(value)]:
                hVal = hVal + 10
            elif value in adjacent:
                hVal = hVal + ad
            else:
                hVal = hVal + far
        return hVal

    def result(self, a_state, an_action, ad, far):
        """Given a state and an action, return the resulting state.
        """
        astate = super().result(a_state, an_action)
        astate.hval = self.calc_h(astate, ad, far)
        return astate

