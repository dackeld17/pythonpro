print('\n\t\t\tTrust Fund Buddy\n')

print('Totals your monthly spending so that your trust fund doesn"t run out')
print('<and you"re focred to get a real job>.')
print('\nPleas enter the requested, monthly costs. Since you"re rich, ignore pennies\nand use only dollar amounts.\n\n')

car = int(input("Lamborghini Tune-ups: "))
apt = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Gifts: "))
din = int(input("Dinning Out: "))
sta = int(input("Staff <butlers, chef, driver, assistant>: "))
per = int(input("Personal Guru and Coach: "))
game = int(input("Computer Games: "))

total = car+apt+jet+gifts+din+sta+per+game

print("\nGrand Total: ",total)
