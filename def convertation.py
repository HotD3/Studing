COEF = 0.62137
miles = int(input('Enter miles:'))
def convert(miles):
    print('Convertation miles to km')
    km = (miles / COEF)
    print('Converted miles to km = ' +str(km))
    print('Miles = ' + str(miles))
convert(miles)
