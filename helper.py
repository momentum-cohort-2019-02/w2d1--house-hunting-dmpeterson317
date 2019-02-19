import constant as c

def months_to_pay_for_house(annual_salary, portion_saved, total_cost):

	current_savings = 0
	month = 0

	while current_savings < (total_cost * c.PORTION_DOWN_PAYMENT):
		current_savings += portion_saved * annual_salary / c.MONTHS + current_savings * c.R / c.MONTHS
		month += 1
	else:
		print("Number of months:" + str(month))
