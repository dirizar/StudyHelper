import random
import pickle
import os


class TestMaker:
    def __init__(self, num_question):
        self.num_question = num_question



    def creating_test(self):
        print(" copy and paste your multi line input")       #instructions
        print(" type '?' to finish your input")

        test_dic = {}
        for i in range(self.num_question):          #creating a multy line input system
            print("\n", i + 1)

            question = " "
            question_join = []
            x = ''

            while x != "?":
                x = input()
                question_join.append(x)     #if ? is in a new line stop asking


            question = question.join(question_join)
            print(question)
            answer = input("write the coorect answwer \n")
            test_dic.setdefault(question, answer)            #corverting dic to a list of tuple

        list = test_dic.items()
        return list



    def do_test(self, test_list):            #creating a test

       os.system("cls")

       point = 0
       enumerate = 0


       for num in test_list :

           answer = input(str(num[0]) + "\n")


           if answer in num[1]:             #cheking answers correct
               point += 1
               enumerate +=1
               os.system("cls")


           else:
               print("FALSE \n")
               print("correct answer is: " + num[1] + "\n")
               point += 0
               enumerate += 1
               v = input("type enter to continue")
               os.system("cls")


       return point


    def calculate(self, points):            #calculating score
        step1 = points / self.num_question
        step2 = step1 * 100
        print("Your test score is {} %".format(round(step2)))

        if step2 <= 70.0:
            bad = input("bad human")

        if step2 >= 70:
            print("You can do better")

        if step2 >= 80.0:
            good = input("good human")


    def lode_data(self):                        #pickle loding saved data
        pickle_name = input("Lode a file in here \n")

        while True:
            try:
                pickle_in = open(pickle_name, "rb")



            except (NameError, FileNotFoundError):
                print("I did't find your file \n\n ")
                break

            else:
                pickle_list = pickle.load(pickle_in)
                self.show_load_data(pickle_list)




    def safe_data(self, data):          #the saving data system using pickle

        safe_question = input("Save the file for another try. Type 'y' to save file. \
Else press enter")

        if safe_question == "y":

            name_file = input("Save as ?\n")
            pickle_out = open(name_file, "wb")
            pickle.dump(data, pickle_out)
            pickle_out.close()
            stop = input("finish type enter to continue")

        else:
            pass

    def show(self, list_test):              #the runing function
        self.safe_data(list(list_test))
        test = self.do_test(list_test)
        self.calculate(test)
        self.safe_data(self.creating_test())

    def show_load_data(self, data):     #runing wen def load data is True
        test = self.do_test(data)
        self.calculate(test)




########################################################################################################################





while True:
    try:
        total_question = int(input("how many question you want? type int number \n \
!if you have a safed file type 100!\n"))

    except ValueError:
        print("\n you need to put numbers")

    else:
        break


test_maker = TestMaker(total_question)

if total_question == 100:
    test_maker.lode_data()

test_questions = test_maker.creating_test()
test_maker.show(test_questions)


