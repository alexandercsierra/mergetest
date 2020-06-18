'''
Bitwise Operations
-----------------------

Boolean:
    and or  True False
    &&  ||  numbers

octet == byte

A  B  A BITWISE-AND B
---------------------
0  0     0
0  1     0
1  0     0
1  1     1

Bitwise operators:
and: &
or:  |
not: ~
xor: ^

bitwise operations can be carried out on multibit numbers, column by column

  10100100
& 10110111
-----------
  10100100

bottom number acted as a stencil. Everywhere there is a zero, it 'masks' out other numbers, and leaves a zero. The series of ones, lets the top number come through. AND Mask

255.255.255.0 subnet mask
11111111.11111111.11111111.00000000
uses bitwise and to determine if network traffic should go out into the internet or stay in your LAN

In general:
you can use AND to clear (set to 0) bits
you can use OR to set (set to 1) bits


Shifting
--------------

moving all bits in a number left or right

to the right
111001
011100

011100
001110

  vv
12345678
shift left by two right by 6
34567800
00000034

more commonly:
(doesn't actually exist in decimal but for example)
  12345678
& 00990000
----------
  00340000
  then shift right
  00000034

In ls8 check first two bits of a command to see how many arguments it should take
  increment pc as num of arguments plus 1

ex:
  10000010
& 11000000
--------
  10000000
  shift
  00000010

right shift by 6
>> 6

num_operands = (ir & 0b11000000) >> 6
how_far_to_move_pc = num_operands + 1
pc += how_far_to_move_pc

moving of the pc is the job of the CPU and not the instruction
'''

'''
Assembling (asm.py - takes assembly and turns into numbers)

Load program from txt file
--------------------------

int() is okay with spaces around a number
'''

#MY program
3 #SAVE_REG
1
99



with open('prog1') as f:
  for line in f:
    line = line.split('#')
    v = int(line[0])
    
sys.exit(0)


with open('prog1') as f:
  address = 0
  for line in f:
    line = line.split('#')
    try:
      v = int(line[0])
    except ValueError:
      continue
    
    memory[address] = v
    address +=1

sys.exit(0)


with open(sys.argv[1]) as f:

  for address, line in enumerate(f):
    line = line.split('#')
    try:
      #remember that int takes a base as a second argument
      v = int(line[0], 2)
    except ValueError:
      continue
    
    memory[address] = v

sys.exit(0)

# sys.argv is a list of things passed in after python
#should do some error checking, to see that a filename exists, and that a filename was passed in

'''
Branch Tables (aka dispatch tables)
-----------------------------------
In this example, it takes longer to run function 4 than it does to run function 1. O(n)

'''

def fun1():
  print('fun1')

def fun2():
  print('fun2')

def fun3():
  print('fun3')

def fun4():
  print('fun4')


def call_fun(n):
  if n == 1:
    fun1(x ,y)
  elif n == 2:
    fun2(x ,y)
  elif n == 3:
    fun3(x ,y)
  elif n == 4:
    fun4(x ,y)

#Branch table will map functions to numbers O(1)
#move the branch table outside of the function to stop it from being reconstructed each time

def call_fun(n, x=None, y=None):
  branch_table = {
    1: fun1,
    2: fun2,
    3: fun3,
    4: fun4,
    5: lambda x, y: print(f'lambda {x} {y}')
  }
  f = branch_table[n]
  f(x,y)


  ir = memory[pc]
  f = branch_table[ir]
  f()

  if ir not in branch_table:
      print('error')
  branch_table[ir]()


  '''
  Bitwise Operations
  -------------------

  '''

  if x < 10 and x > 2:
    print('foo')

  x = 5

  if True and True:
    print('foo')