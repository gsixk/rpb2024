def main():
    print("Let's implement division. Type two numbers for x and y")
    
    x = int(input("x > "))
    y = int(input("y > "))
    if y !=0:
        print("%d/%d=%d" % (x, y, divide(x,y)))
    else:  
        print("Error: cannot divide by zero.")


def add(a, b):
    result = x+y

    return result
    
    
# TODO:  divide() 함수 정의

def divide(x,y):
    if y==0:
         print("Error: cannot divide by zero.") 
    else:
        return x/y      

if __name__ == "__main__":
    main()
