# Create a product and price for three items
p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

# create a company name and information
company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

# declare ending message
message = "Thanks for shopping with us today!"

# Create a top border
print("*" * 50)
 # print company information first, using format
print( '\t\t{}'.format( company_name.title( ) ))
print( '\t\t{}'.format(company_address) )
print( '\t\t{}'.format(company_city) )
print("*" * 50)
print("\tProduct Name\tProduct Price")
print( "\t{}\t\t\t${}".format(p1_name.title( ), p1_price) )
print( "\t{}\t\t${}".format(p2_name.title( ), p2_price) )
print( "\t{}\t\t\t${}".format(p3_name.title( ), p3_price) )
# print out header for section of total
print("\t\t\tTotal")
# calculate total price and print out
total = p1_price + p2_price + p3_price
print("\t\t\t\t\t{}".format( total))
print( "=" * 50)
print( "\n\t{}\n".format(message) )
print( "*" * 50 )