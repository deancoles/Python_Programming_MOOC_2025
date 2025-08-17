"""
Please write a program which calculates the correct amount of tax for a gift from a close relative.

Value of gift	        	Tax at the lower limit	        Tax rate for the exceeding part (%)
5 000 — 25 000	                100	                                    	8
25 000 — 55 000	                1 700	                                10
55 000 — 200 000	            	4 700	                                12
200 000 — 1 000 000	        22 100	                                15
1 000 000 —	                    	142 100	                                17

"""

value = float(input("Enter the value of your gift: "))

low_limit = 0
tax_rate = 0

if value < 5000:
    print("No tax!")
elif value >= 5000 and value < 25000:
    low_limit = 100
    tax_rate = 0.08
    print(f"Amount of tax: {(low_limit + (value - 5000) * tax_rate)} euros")
elif value >= 25000 and value < 55000:
    low_limit = 1700
    tax_rate = 0.10
    print(f"Amount of tax: {(low_limit + (value - 25000) * tax_rate)} euros")
elif value >= 55000 and value < 200000:
    low_limit = 4700
    tax_rate = 0.12
    print(f"Amount of tax: {(low_limit + (value - 55000) * tax_rate)} euros")
elif value >= 200000 and value < 1000000:
    low_limit = 22100
    tax_rate = 0.15
    print(f"Amount of tax: {(low_limit + (value - 200000) * tax_rate)} euros")
else:
    low_limit = 142100
    tax_rate = 0.17
    print(f"Amount of tax: {(low_limit + (value - 1000000) * tax_rate)} euros")