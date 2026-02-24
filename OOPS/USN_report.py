# -------------------------------------------
# Student Score Card Program using OOP
# -------------------------------------------

# Create a class named Student (blueprint for student objects)
class Student:

    # Constructor method
    # Automatically runs when object is created
    def __init__(self):

        # Take student basic details from user
        self.name = input("Enter student name: ")
        self.usn = input("Enter student USN: ")

        # List to store marks of 3 subjects
        self.marksList = []

        # List to store total marks (not really needed, but kept as per question)
        self.totalList = []

        # Variable to store sum of marks
        self.totalMarks = 0

        # Variable to store percentage
        self.percentage = 0.0


    # Method to read marks and calculate total + percentage
    def getMarks(self):

        print("\nEnter marks for 3 subjects:")

        # Loop runs 3 times (for 3 subjects)
        for i in range(1, 4):

            # Take mark input and convert to float
            mark = float(input("Enter mark for subject " + str(i) + ": "))

            # Add mark into marks list
            self.marksList.append(mark)

        # Calculate total using sum() function
        self.totalMarks = sum(self.marksList)

        # Store total inside totalList
        self.totalList.append(self.totalMarks)

        # Calculate percentage
        # total / number of subjects
        self.percentage = self.totalMarks / 3


    # Method to display score card
    def display(self):

        print("\n------ STUDENT SCORE CARD ------")

        # Print student details
        print("Name:", self.name)
        print("USN:", self.usn)

        # Print marks list
        print("Marks in 3 subjects:", self.marksList)

        # Print total marks
        print("Total Marks:", self.totalList[0])

        # Print percentage rounded to 2 decimal places
        print("Percentage:", round(self.percentage, 2), "%")

        print("--------------------------------")


# -------------------------------------------
# Main Program
# -------------------------------------------

# Create an object of Student class
student1 = Student()

# Call method to take marks and calculate results
student1.getMarks()

# Call method to display score card
student1.display()
