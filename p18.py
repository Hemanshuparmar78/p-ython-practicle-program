a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))

average=(a+b+c)/3
print(average)

#function defintion 
def avg():
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    c=int(input("enter a number:"))

    average=(a+b+c)/3
    print(average)

#functon call
avg()
avg()

#function with arguments
def hello(name):
    print("hello ",name)
    return "ok"# return statement

a=hello("hemanshu")
print(a)