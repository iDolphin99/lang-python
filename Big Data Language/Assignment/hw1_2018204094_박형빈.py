def nCake() :
    while (True) :
        print("\nN단 케이크의 N입력")
        n = int(input("(1이상 10이하의 N입력) : "))
        
        if n<1 or n>10 :
            print("다시 입력하세요\n")
            continue
        elif n==1 : 
            for x in range(2) :
                print(" " * 2, end='')
                print("*" * 2)
            return
        else :  
            for x in range(1, n+1) :
                for y in range (2) : 
                    print(" " * (4*(n-x)), end='')
                    print("*" * (8*x - 6))
            return


def nThunder() : 
    while (True) : 
        print("\n번개의 밑변 길이")
        n = int(input("(3이상 10이하의 길이 입력) : "))
        
        if n<3 or n>10 :
            print("다시 입력하세요\n")
            continue
        else :
            for y in range(2) :
                for x in range(1, n) :
                    print(" " * (n-x), end='')
                    print("*" * n)
                if y==0 : 
                    print("*" * (2*n))
            return
                    

    

while (True) :
    print("도형을 선택하세요")
    print("1. N단 케이크")
    print("2. 번개")
    print("3. 종료")
    op = int(input())
    if op ==3 :
        print("종료합니다.")
        break
    elif op == 1: 
        nCake()
    elif op == 2 : 
        nThunder() 
    else : 
        print("잘못된 입력입니다. 다시 입력하세요 \n\n")
    print("\n\n")
 

                                    
