import codecs
from six import moves

# Imports the PyOTA library
from iota import Iota


numberOfAddresses = int(moves.input("How many addresses should be generated and checked for balance on each seed? "))
iotaNode = moves.input("""
To use this script you must connect to a IOTA node. You can use your local node address "http://localhost:14265"
if you have a full node running or you can connect to a remote node. You can finde remote nodes to connect to on
http://iotasupport.com/lightwallet.shtml

Please enter a node address to connect to: """)


with codecs.open("inputSeeds.txt", "r", 'ascii') as seedFile:
	seeds = seedFile.read().splitlines()

# Will take a list of seeds and calls the addressGenerator function for each seed
def seedSelector ():
	x = len(seeds) - 1
	i = 0
	while i <= x:
		seed = seeds[i].strip()
		if seed:
			print("Checking seed " + seed + " for balance...")
			addressGenerator(seed.encode('ascii'))
		i += 1
	else:
		print ("Finished!!!")


# Generates addresses of a given seed using the "get_new_addresses()" function
def addressGenerator(seed):
	api = Iota(iotaNode, seed) # The iota nodes IP address must always be supplied, even if it actually isn't used in this case.
	gna_result = api.get_new_addresses(count=numberOfAddresses) # This is the actual function to generate the address.
	addresses = gna_result['addresses']
	total = 0
	i = 0
	while i < numberOfAddresses:
		address = [addresses[i]]
		balance = addressBalance(address)
		print ("Address " + str(address[0]) + " has a balance of: " + str(balance))
		total += balance
		i += 1
	if total > 0:
		print ("The above addresses have a total balance of " + str(total) + " Iota tokens!!!")
	else:
		print ("No balance on those addresses!")

# Sends a request to the IOTA node and gets the current confirmed balance
def addressBalance(address):
	api = Iota(iotaNode)
	gb_result = api.get_balances(address)
	balance = gb_result['balances']
	return (balance[0])


print ( "Checking balance on the first " + str(numberOfAddresses) + " addresses for " + str(len(seeds)) + " seeds!")
print ("This can take a while...")
seedSelector()
