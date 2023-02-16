print("L1 is a set of strings starting and ending with alphabet alpha_one")#first alphabet to be input
print("L2 is a set of strings starting with substring alpha_one alpha_two alpha one eg 101")
print("pick language L1 OR L2?",end="")
language = input().upper()

print(f"You have chosen {language}")


class wrongLanguageError(ValueError):
   pass

# class invalidAlphabet(ValueError):
#     pass

def pickLanguage(choice):
    #choice=choice.upper()
    if choice == "L1":
        language_one()
    elif choice == "L2":
        language_two()
    else:
        print("wrong language")
        raise wrongLanguageError(choice)

def language_one():
    print("Executing language 1")
    print("Enter the first alphabet ", end="")
    alpha_one = input()#was a
    print("Enter the second alphabet ", end="")
    alpha_two = input()
    states = ["A","B","C","D"]
    alphabets = [alpha_one,alpha_two]
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
        return response
    def processString(string_input):

        if string_input =="q":
            print("END OF PROGRAM")
        else:
            current = start_state
            for i in string_input:
                if i == alpha_one or i == alpha_two:
                    pass
                else:
                    raise KeyError("entered invalid alphabet")
                current = transition_function[(current, i)]


            if (current == final_state):
                print("string is correct")

            else:
                print("string is incorrect")
            processString(getResponse())
    processString(getResponse())


#language_one()
def language_two():
    print("Executing language 2")
    print("Enter the first alphabet ", end="")
    alpha_one = input()#was 1
    print("Enter the second alphabet ", end="")
    alpha_two = input()
    states = ["q0","q1","q2","q3","q4"]
    alphabets = [alpha_one,alpha_two]
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
        return response
    def processString(string_input):

        if string_input =="q":
            print("END OF PROGRAM")
        else:
            current = start_state
            for i in string_input:
                if i == alpha_one or i == alpha_two:
                    pass
                else:
                    raise KeyError("entered invalid alphabet")
                current = transition_function[(current, i)]


            if (current == final_state):
                print("string is correct")

            else:
                print("string is incorrect")
            processString(getResponse())
    processString(getResponse())


#language_two()
pickLanguage(language)