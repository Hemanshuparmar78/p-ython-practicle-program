#functions
name="hemanshu"
print(len(name)) #length
print(name.endswith("shu"))
print(name.startswith("he"))
print(name.capitalize())

#new line escape
a="hemanshu\nparmar"
b="hemanshu\tparmar"
print(a)
print(b)

nameshort=name[0:3]
print(nameshort)

#string slicing 
ch1=name[1]
print(ch1)
print(name[-4:-1])
print(name[:4])
print(name[0:])

#skiping
a="abcdefghijklmnopqrstuvwxyz"
print(a[1:7:2])
print(a[1::5])