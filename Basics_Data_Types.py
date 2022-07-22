# Basics Data Types:
'''
Các kiểu dữ liệu cơ bản trong Python: bool, None, int, float, str
'''
'''
Topic #0: bool & None
'''
# [] bool: True & Fales
var_bool = True

# [] type(): Dynamically typed

# print(type(var_bool))

# Numerically, they're evaluated as integers with value 1 (True), 0 (False)
a = 4 + True
#print(a)
b = False
#if b == 0:
#   print("B is 0")

# [] None: Phan tu khong
var_none = None
#print(type(var_none))
# None is often used as a placeholer for optional or missing value.
# It evaluates as False conditionals.
#email_address = None
# email_address = "luan@code.vn"

# if email_address:
#     print(f"Email address is {email_address}")
# else:
#     print(f"Email address is empty or {email_address}")

'''
Topic #1: Number (int & float)
'''
# [] Numbers: int (Interer = So Nguyen) & float (Floating point numbers = So thu)
# print(type(1)) #int
# print(type(0))
# print(type(-10))

# print(type(0.0)) #float
# print(type(2.3))
# print(type(4E2), 4E2) #4*10(^2)

# [] Arithmetic: Cac phep toan:+ - * / ** // %
# print(10+3) #13
# print(10*3) #30
# print(10-3) #7
# print(10/3) #3.3333333
# print(10//3) #3
# print(10**3) #1000
# print(10%3) # chia lay phan du 10 chia 3 bang 3 du 1 

# [] basics Function (Ham co ban)
print(pow(10,3)) #10**3 = 1000 (ham mu)
print(abs(-6.9)) #6.9 (ham tri tuyet doi la ham lay so duong cua mot so)
print(round(6.69)) #7 lam tron thanh so nguyen
print(round(5.47939, 4)) #5.4794 (round to nth dight)
print(bin(512)) # '0b1000000000' --> binary format chuyen sang ham nhi phan
print(hex(512)) # '0x200' --> hexadecimal format chuyen sang ham thap luc phan