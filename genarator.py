print('''
       #***********************************#
       #      Generator Program            #
       #***********************************#''')
print('''
1-Binary  to Decimal
2-Decimal To Binary
3-exit
press the key ''')
while(True):
 işlem=int(input("\nEnter the number of the transaction you want to do:"))
 if işlem == 1 :
  x = input("Binary code enter: ")
  decimal=0
  if(len(x) > 8):
     print("too many numbers input, please try again")

  if (len(x) == 8):
      a=list(x)
      if (a [0] > '1' or a [0] > '1' or a [1] > '1' or a [2] > '1' or a [3] > '1' or a [4] > '1' or a [5] > '1' or a [6] > '1' or a [7] > '1' ):
          print("You entered wrong binary code, please check your code")
      else:
          for i in range(len(x)):
            decimal += int(x[i]) * 2 ** abs((i - (len(x) - 1)))
          print("Decimal code:",decimal)
  else:
      print("please write 8 digits")
 elif işlem == 2 :
      x =int(input("number:"))
      dec= [int(i) for i in list('{0:0b}'.format(x))]
      print("Binary code:")
      while len(dec) < 8:
        dec.insert(0,0)
      for i in dec :
       print(i,end="")
 elif işlem == 3:
     break

 else:
     print("You entered the wrong transaction number, please try again")
