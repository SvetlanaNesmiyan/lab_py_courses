def multiply_digits(number):

  while number > 9:
    product = 1
    while number > 0:
      digit = number % 10
      product *= digit
      number //= 10
    number = product
  return number

num = int(input("Введіть ціле число:"))

result = multiply_digits(num)

print(result)