# #CONTINUATION ON OPERATORS IN QUIZ TWO
# #ASSIGNMENT OPERATORS
# sum=6
# sum+=6
# sum+=5
# print(sum)

#Given that we have two products ,a laptop and a mouse such that the price of a laptop is 300000
#and the price of a mouse is 500000.use a for loop to find the total sum of the products.
laptop=300000
mouse=50000
sum=0
prices=[300000 ,50000]
Product_prices=[laptop,mouse]
for price in Product_prices:
    sum+=price
    print(f"The total sum of the products is:{sum:,}")