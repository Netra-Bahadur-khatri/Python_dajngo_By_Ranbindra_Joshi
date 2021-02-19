# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

# x = list(map(int, input("Enter an numbers: ").split()))
# print(x)

def fibonnaci_numbers():
    # series = []
    len_fibonnaci_series = int(input("Enter length for the fibonnaci series : "))
    # x,y = input("Enter first two number to generate an fibonnaci series: ").split()
    # x,y = int(x),int(y)
    # series.extend([x,y])

    series = [1,1]
    while(len(series) < len_fibonnaci_series):
        a = series[-1] + series[-2]
        series.append(a)
    return series


if __name__ == "__main__":
    c = fibonnaci_numbers()
    print(c)
