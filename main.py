import constant
import helper

def main():

	a = float(input("Enter your annual salary: "))
	p = float(input("Enter the percent of your salary to save, as a decimal: "))
	t = float(input("Enter the cost of your dream home: "))

	helper.months_to_pay_for_house(a, p, t)

	# helper.months_to_pay_for_house(50000, 0.25, 250000)

# Entry point into the program
if __name__ == "__main__":
	main()