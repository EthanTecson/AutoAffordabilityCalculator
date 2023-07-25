"""
Created on Sun Nov 20 14:12:34 2022

@author: ethantecson
"""
"""
     Author/copyright: Ethan Tecson.  All rights reserved.
     Used with permission and modified by: WhoeverModifiesIt
     Date: 20 November 2022
"""
#######################################################################
def average_salary(total, down_payment, maintenance, insurace):
     # 10% markup
     total = total * 1.10 
     # 7% tax rate
     taxed_total = total * 1.07 

     # 10% down payment
     down_payment = taxed_total * .1 

     # Total leftover after down payment
     post_down_payment_total = taxed_total - down_payment

     # 5 year term
     pre_monthly_total = post_down_payment_total / 40

     # Monthly maintenance cost 
     maintenance = maintenance / 12

     # Monthly insurance cost 
     insurace = insurace / 12

     final_monthly_total = pre_monthly_total + maintenance + insurace

     # 10% of monthly gross income
     final_monthly_total *= 10 

     # yearly gross income
     answer = final_monthly_total * 12

     return '$' + str(round(answer))
     
######################################################################
def main():
     """
     """
     auto_cost = int(input('Total Cost of Car: '))
     down_payment = int(input('Down Payment (In Percentage): %'))
     maintenance = int(input('Average Maintenance Cost (Yearly): '))
     insurance = int(input('Average Insurance Cost (Yearly): '))

     print('Average Salary:', average_salary(auto_cost, down_payment, maintenance, insurance))
######################################################################
main()
