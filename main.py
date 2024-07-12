import random def
compareNumber (c, u):if
  u == c
:
  print ("\nYou guessed correctly")
	print ("\nComputer Generate number is ", c)
  else
:
  if u
  >c:
	print ("\nYour number is larger than the computer number")
	else
  :
	print ("\nYour number is smaller than the computer number")
	  compNumber = random.randint (1, 100) userNumber = 0 while userNumber
	!=compNumber:
	 userNumber =
	   int (input ("\nEnter a number which is near the guessed number: "))
  compareNumber (compNumber, userNumber)
