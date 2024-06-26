
def exercise2():
    word = input()
    character_dic = {}

    for characters in word:
        if characters in character_dic:
            character_dic[characters] += 1
        else: 
            character_dic[characters] = 1

    print(character_dic)

if __name__ == "__main__":
    exercise2()
    
