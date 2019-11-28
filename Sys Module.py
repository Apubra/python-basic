import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')
print(sys.argv)
def main(arg):
    print(arg)

main(sys.argv[1])

# //////////////////////////////////////////////
import sys

while True:
  # output to stdout:
  print ("Yet another iteration ...")
  try:
    # reading from sys.stdin (stop with Ctrl-D):
    number = input("Enter a number: ")
  except EOFError:
    print ("\nciao")
    break
  else:
    number = int(number)
    if number == 0:
      print (sys.stderr, "0 has no inverse")
    else:
      print ("inverse of %d is %f" % (number, 1.0/number) )

# we can execute that code using command line and text file
# python urllib\ module.py < Test.txt
# we can execute that code using command line and text file and output will save by creating a file.
# python urllib\ module.py < Test.txt > output.txt
