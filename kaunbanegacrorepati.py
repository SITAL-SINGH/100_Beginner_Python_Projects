# kaun banega crorepati hosted by sital singh 


def question_no_1(qsn_list,ans_list,valid_inputs1):
    # for index, item in enumerate(qsn_list,start=1):
    #     f"{index}.  {item}"
    # print(len(ans_list))
    user_input1=input("\nAre you ready for the game (y/n): ")
    print("\n")
    if user_input1.lower.strip() in valid_inputs1:
        print("..Game Starts Now..".center(65))
        print("\n")
        print("...Remember, This is first question and if you give the correct answer you can take 10 Lakh Rupees to home...\n")
        print(f"Q.1--> {qsn_list[0]}\n")
        print(f'''options:    a. {ans_list[0] }       b. {ans_list[1]} 
            c. {ans_list[2]}         d. {ans_list[3]}''')
        print("\n")
        answer1=input("Enter the answer (a,b,c,d): ")
        if answer1.lower().strip()=="b" or answer1.lower().strip()==ans_list[1]:
              print(f"---> Answer is b.{ans_list[1]}")
              print("Cogratulation!!! Your answer is correct and won 10 lakh rupees\n")
              total_won_money=1000000

        else:
               print(f"---> Answer is b.{ans_list[1]}")
               print("Bad Luck!!! Your answer is incorrect and you cannot continue the game..\n")
               total_won_money=0
               print("you didnt any money prize")
               exit()


def question_no_2(qsn_list,ans_list,valid_inputs1):  
    print("\n")
    print("...Remember, This is second question and if you give the correct answer another 50 lakhs will be added and you will go home empty handed once you looses the game...\n")

    user_input_2=input("Do you want to continue or leave the game with prize pool of 10 lakhs(y/n): ")

    if user_input_2.lower().strip() in valid_inputs1:
    
        print(f"Q.2--> {qsn_list[1]}\n")
        print(f'''options:    a. {ans_list[4] }        b. {ans_list[6]} 
            c. {ans_list[5]}          d. {ans_list[7]}''')
        print("\n")
        answer=input("Enter the answer (a,b,c,d): ")
        if answer.lower().strip()=="c" or answer.lower().strip()==ans_list[5]:
              print(f"---> Answer is c.{ans_list[5]}")
              print("Cogratulation!!! Your answer is correct and won 50 lakh rupees\n")
              total_won_money=1000000+5000000
              print(f"your total won money is {total_won_money}")

        else:
               print(f"---> Answer is c.{ans_list[5]}")
               print("Bad Luck!!! Your answer is incorrect and you cannot continue the game..\n")
               total_won_money=0
               print("you didnt any money prize")
               exit()

def question_no_3(qsn_list,ans_list,valid_inputs1):  
    print("\n")
    print("...Remember, This is third question and if you give the correct answer another 1 crore will be added and you will go home empty handed once you looses the game...\n")

    user_input_3=input("Do you want to continue or leave the game with prize pool of 60 lakhs(y/n): ")

    if user_input_3.lower().strip() in valid_inputs1:
    
        print(f"Q.3--> {qsn_list[2]}\n")
        print(f'''options:    a. {ans_list[8] }        b. {ans_list[9]} 
            c. {ans_list[10]}          d. {ans_list[11]}''')
        print("\n")
        answer=input("Enter the answer (a,b,c,d): ")
        if answer.lower().strip()=="b" or answer.lower().strip()==ans_list[9]:
              print(f"---> Answer is b.{ans_list[9]}")
              print("Cogratulation!!! Your answer is correct and won 1 crore rupees\n")
              total_won_money=1000000+5000000+10000000
              print(f"your total won money is {total_won_money}")

        else:
               print(f"---> Answer is b.{ans_list[9]}")
               print("Bad Luck!!! Your answer is incorrect and you cannot continue the game..\n")
               total_won_money=0
               print("you didnt any money prize")
               exit()

def question_no_4(qsn_list,ans_list,valid_inputs1):  
    print("\n")
    print("...Remember, This is fourth question and if you give the correct answer another 10 Crore will be added and you will go home empty handed once you looses the game...\n")

    user_input_4=input("Do you want to continue or leave the game with prize pool of 1 Crore and 51 lakhs(y/n): ")

    if user_input_4.lower().strip() in valid_inputs1:
    
        print(f"Q.4--> {qsn_list[3]}\n")
        print(f'''options:    a. {ans_list[12] }        b. {ans_list[13]} 
            c. {ans_list[14]}          d. {ans_list[15]}''')
        print("\n")
        answer=input("Enter the answer (a,b,c,d): ")
        if answer.lower().strip()=="c" or answer.lower().strip()==ans_list[14]:
              print(f"---> Answer is c.{ans_list[14]}")
              print("Cogratulation!!! Your answer is correct and won 10 Crore rupees\n")
              total_won_money=1000000+5000000+100000000+10000000
              print(f"your total won money {total_won_money}")

        else:
               print(f"---> Answer is c.{ans_list[14]}")
               print("Bad Luck!!! Your answer is incorrect and you cannot continue the game..\n")
               total_won_money=0
               print("you didnt any money prize")
               exit()

def question_no_5(qsn_list,ans_list,valid_inputs1):  
    print("\n")
    print("...Remember, This is last question and if you give the correct answer another 50 Crore will be added and you will go home empty handed once you looses the game...\n")

    user_input_5=input("Do you want to continue or leave the game with prize pool of 11crore and 50 lakhs(y/n): ")

    if user_input_5.lower().strip() in valid_inputs1:
    
        print(f"Q.5--> {qsn_list[4]}\n")
        print(f'''options:    a. {ans_list[17] }        b. {ans_list[16]} 
            c. {ans_list[18]}          d. {ans_list[19]}''')
        print("\n")
        answer=input("Enter the answer (a,b,c,d): ")
        if answer.lower().strip()=="a" or answer.lower().strip()==ans_list[17]:
              print(f"---> Answer is c.{ans_list[17]}")
              print("Cogratulation!!! Your answer is correct and won 50 lakh rupees\n")
              total_won_money=1000000+5000000+100000000+10000000+500000000
              print(f"your total won money {total_won_money}")

        else:
               print(f"---> Answer is a.{ans_list[17]}")
               print("Bad Luck!!! Your answer is incorrect and you cannot continue the game..\n")
               total_won_money=0
               print("you didnt any money prize")
               exit()











def crore_pati_sys():
    print(" 'Welcome To Kaun Banega CrorePati' ".center(65))

    qsn_list=["Who was the first Prime Minister of India?",
              "The Quit India Movement was launched in which year?",
             "Which is the largest river in India by volume of water?",
              "Who won the Nobel Peace Prize in 2023?",
             "Which planet is known as the ‘Red Planet’?",
            "Which Bollywood actor is known as the ‘King of Bollywood’?",
            "Who was the father of Lord Rama in the epic Ramayana?",
            "In which year did India win its first Cricket World Cup?",
            "Who wrote the famous novel Godan?",
            "If 5 pens cost ₹100, how much will 8 pens cost?"]
    
    ans_list=["Mahatma Gandhi","Jawaharlal Nehru","Sardar Patel","Dr. Rajendra Prasad","1930","1942","1947"," 1950"," Ganga","Brahmaputra"," Godavari","Yamuna"," Maria Ressa"," Volodymyr Zelensky","Narges Mohammadi","UNHCR","Venus"," Mars"," Jupiter"," Saturn","Salman Khan","Aamir Khan"," Shahrukh Khan","Amitabh Bachchan","Dasharatha","Ravana","Janaka"," Bharata","1975","1983","1987"," 1992","Munshi Premchand","Rabindranath Tagore"," R. K. Narayan"," Sarat Chandra Chattopadhyay","₹120","₹140"," ₹160","₹180"]
    valid_inputs1=["yes","YES","y","ye"]
    
    question_no_1(qsn_list,ans_list,valid_inputs1)
    print("\n")
    question_no_2(qsn_list,ans_list,valid_inputs1)
    print("\n")
    question_no_3(qsn_list,ans_list,valid_inputs1)
    print("\n")
    question_no_4(qsn_list,ans_list,valid_inputs1)
    print("\n")
    question_no_5(qsn_list,ans_list,valid_inputs1)
    print("\n")











crore_pati_sys()