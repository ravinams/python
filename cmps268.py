from csv import reader
# open file in read mode


class Person:
    def __init__(self, first_name, last_name, address, email, dob, ethnicity, education):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.dob = dob
        self.ethnicity = ethnicity
        self.education = education

    def __str__(self) -> str:
       return self.first_name+" | "+self.last_name+" | "+self.address+" | " + self.email+" | "+self.dob+" | "+self.ethnicity+" | "+self.education
       
    def display(self):
        print(self.first_name+" | "+self.last_name+" | "+self.address+" | " +
              self.email+" | "+self.dob+" | "+self.ethnicity+" | "+self.education)
  

people = []

with open('New_Raw_Data.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    header = next(csv_reader)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        # print(row)
        people.append(Person(row[0], row[1], row[2],
                             row[3], row[4], row[5], row[6]))

for person in people:
    #person.display()
    print(person)
