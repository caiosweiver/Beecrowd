PEC1, NUMPEC1, UNIPEC1 = input().split()

PEC1 = int(PEC1)
NUMPEC1 = int(NUMPEC1)
UNIPEC1 = float(UNIPEC1)

PEC2, NUMPEC2, UNIPEC2 = input().split()

PEC2 = int(PEC2)
NUMPEC2 = int(NUMPEC2)
UNIPEC2 = float(UNIPEC2)

VALOR = NUMPEC1 * UNIPEC1 + NUMPEC2 * UNIPEC2

print("VALOR A PAGAR: R$ %0.2f" % VALOR)