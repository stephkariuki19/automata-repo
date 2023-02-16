print("L1 is a set of strings starting and ending with alphabet alpha_one")#first alphabet to be input
print("L2 is a set of strings starting with substring alpha_one alpha_two alpha one eg 101")
print("pick language L1 OR L2?",end="")
language = input().upper()

class wrongLanguageError(ValueError):
   pass


def pickLanguage(choice):

    if choice == "L1":
        language_one()
    elif choice == "L2":
        language_two()
    else:
        print("wrong language")
        raise wrongLanguageError(choice)
def checkAlphabets(letter_one,letter_two,b):
    if b== letter_one or b == letter_two:
        pass
    else:
        raise KeyError(" string has a wrong alphabet")
def checkIfEmpty(test_string):
    if test_string == "":
        raise ValueError("cannot enter empty string")

def language_one():
    print("Executing language 1")
    print("Enter the first alphabet ", end="")
    alpha_one = input()#was a
    print("Enter the second alphabet ", end="")
    alpha_two = input()
    start_state = "A"
    final_state = "B"
    transition_function = {
        ("A",alpha_one):"B",
        ("A", alpha_two): "D",
        ("B", alpha_one): "B",
        ("B", alpha_two): "C",
        ("C", alpha_one): "B",
        ("C", alpha_two): "C",
        ("D", alpha_one): "D",
        ("D", alpha_two): "D"
    }
    #shd run until user puts q

    def getResponse():
        print("Enter the string  ", end="")
        response = input()
        checkIfEmpty(response)
        return response
    def processString(string_input):

        if string_input =="q":
            print("END OF PROGRAM")
        else:
            current = start_state
            for i in string_input:
                checkAlphabets(alpha_one,alpha_two,i)
                current = transition_function[(current, i)]


            if (current == final_state):
                print("string is correct")

            else:
                print("string is incorrect")
            processString(getResponse())
    processString(getResponse())

def language_two():
    print("Executing language 2")
    print("Enter the first alphabet ", end="")
    alpha_one = input()#was 1
    print("Enter the second alphabet ", end="")
    alpha_two = input()
    start_state = "q0"
    final_state = "q3"
    transition_function = {
        ("q0",alpha_two):"q4",
        ("q0", alpha_one): "q1",
        ("q1", alpha_two): "q2",
        ("q1", alpha_one): "q4",
        ("q2", alpha_two): "q4",
        ("q2", alpha_one): "q3",
        ("q3", alpha_two): "q3",
        ("q3", alpha_one): "q3",
        ("q4", alpha_two): "q4",
        ("q4", alpha_one): "q4"

    }
    #put string_input as input

    def getResponse():
        print("Enter the string  ", end="")
        response = input()
        checkIfEmpty(response)
        return response
    def processString(string_input):

        if string_input =="q":
            print("END OF PROGRAM")
        else:
            current = start_state
            for i in string_input:
                checkAlphabets(alpha_one, alpha_two, i)
                current = transition_function[(current, i)]


            if (current == final_state):
                print("string is correct")

            else:
                print("string is incorrect")
            processString(getResponse())
    processString(getResponse())


pickLanguage(language)


