#! /usr/bin/env python3

import sys
import math

with open(sys.argv[1], "r") as f_in:
	A = int(f_in.readline().strip().split(": ")[1])
	B = int(f_in.readline().strip().split(": ")[1])
	C = int(f_in.readline().strip().split(": ")[1])
	f_in.readline()
	program = list(map(int, f_in.readline().strip().split(": ")[1].split(",")))

def run(program, A, B, C, quine=False):
	def combo(operand):
		if operand <= 3:
			return operand
		if operand == 4:
			return A
		if operand == 5:
			return B
		if operand == 6:
			return C
		raise RuntimeError("reserved combo operand")
	out = []
	#anyprint = False
	pc = 0
	while pc < len(program):
		opcode, operand = program[pc], program[pc+1]
		if   opcode == 0: # adv -- A // combo -> A
			op = combo(operand)
			res = A // 2**op
			if not quine: print(f"adv A={A} // 2**(combo={op})={2**op} -> A={res}")
			A = res
		elif opcode == 1: # bxl -- B XOR literal -> B
			if not quine: print(f"bxl B={B} XOR lit={operand} -> B={B^operand}")
			B = B ^ operand
		elif opcode == 2: # bst -- combo%8 -> B
			op = combo(operand)
			res = op % 8
			if not quine: print(f"bst combo={op} % 8 -> B={res}")
			B = res
		elif opcode == 3: # jnz -- if A not zero, jump to literal
			if A != 0:
				if not quine: print(f"jnz A={A} pc={operand}")
				pc = operand
				continue # skip += 2
			if not quine: print(f"jnz A=0 nop")
		elif opcode == 4: # bxc -- B XOR C -> B (ignore operand)
			res = B ^ C
			if not quine: print(f"bxc B={B} xor C={C} -> B={res}")
			B = res
		elif opcode == 5: # out -- print combo%8
			op = combo(operand)
			#if not anyprint:
			#	anyprint = True
			#	print(",", end="")
			#print(op  % 8, end="")
			#sys.stdout.flush()
			res = op % 8
			if quine:
				if len(out) > len(program) or res != program[len(out)-1]:
					return []
			else: print(f"out combo={op} % 8 -> {res}")
			out.append(res)
		elif opcode == 6: # bdv -- A // combo -> B
			op = combo(operand)
			res = A // 2**op
			if not quine: print(f"bdv A={A} // 2**(combo={op})={2**op} -> B={res}")
			B = res
		elif opcode == 7: # cdv -- A // combo -> C
			op = combo(operand)
			res = A // 2**op
			if not quine: print(f"cdv A={A} // 2**(combo={op})={2**op} -> C={res}")
			C = res
		pc += 2
	return out
	#print()

out = run(program, A, B, C)
print(",".join(map(str, out)))

A = 0
while True:
	if A %100000 == 0:
		print(A, end="\r")
	out = run(program, A, B, C, True)
	if len(out) == len(program):
		for x, y in zip(out, program):
			if x != y:
				break
		else:
			print(A)
			break
	A += 1