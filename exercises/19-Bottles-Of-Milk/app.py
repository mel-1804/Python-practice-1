# ✅↓ Write your code here ↓✅
def number_of_bottles():
    for i in range(99,2,-1):
        if i == 1:
            print (str(i) + 'bottles of milk on the wall, ' + str(i) + 'bottles of milk.' + 'Take one down and pass it around, no more bottles of milk on the wall.' + 'No more bottles of milk on the wall, no more bottles of milk.Go to the store and buy some more,, 99 bottles of milk on the wall.')
        else:
            print(str(i) + 'bottles of milk on the wall, ' + str(i) + 'bottles of milk.' + 'Take one down and pass it around, ' + str(i-1) + 'bottles of milk on the wall.')

number_of_bottles()
