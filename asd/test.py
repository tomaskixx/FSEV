def input_error():
	print("Dvere sú zatvorené! Skúste prosím znovu!")

def input_switches():
	a = int(input("Spínač A: (1 - zapnutý; 0 - vypnutý) "))
	b = int(input("Spínač B: (1 - zapnutý; 0 - vypnutý) "))
	return a, b

print("Dvere sa otvoria iba vtedy, ak je jeden zo spínačov aktívny, ale nie oba.")
switchA, switchB = input_switches()
while switchA == switchB:
	input_error()
	switchA, switchB = input_switches()
print("Otvorili ste štvrté dvere. Gratulujem! Týmto ste prešli ste všetkými úrovňami!")