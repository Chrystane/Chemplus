nrg_broken = 0
nrg_formed = 0

choice = ''

print("BOND ENERGY T01/S01 SOLVER ::: version 1.0\n")

print("### INSTRUCTIONS ###")
print("Input values as directed for bonds BROKEN during the reaction.")
print("These appear on the left-hand side of the chemical equation!")
print("\n")

while choice.lower() != "n":

    coeff = int(input("number of bonds broken: "))
    bond_nrg = float(input("energy of each of these bonds: "))

    nrg_broken += coeff*bond_nrg

    print("total nrg in broken bonds = " + str(nrg_broken))

    choice = input("input more broken bonds? y/n: ")

while choice.lower() != 'e':

    coeff = int(input("number of bonds formed: "))
    bond_nrg = float(input("energy of each of these bonds: "))

    nrg_formed += coeff*bond_nrg

    print("total nrg in broken bonds = " + str(nrg_formed))

    choice = input("[e]xit?: ")


result = str((nrg_broken - nrg_formed))
print("The total energy change is " + result)

