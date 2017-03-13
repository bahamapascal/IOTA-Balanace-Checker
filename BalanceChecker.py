from iota import Iota

# The amount of addresses the user wants to generate
numberOfAddresses = 5
# The seeds from which the addresses will get generated
seeds = ["POCTEST", "TGAT"]



def seedSelector ():
	x = len(seeds) - 1
	i = 0
	while i <= x:
		seed = seeds[i]
		print("Seed " + seed + " contains following addresses:")
		addressGenerator(seed)
		i += 1
	else:
		print ("Finished!!!")



def addressGenerator(seed):
		api = Iota('http://148.251.233.147:14265', seed)
		gna_result = api.get_new_addresses(count=numberOfAddresses)
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

def addressBalance(address):
	api = Iota('http://148.251.233.147:14265')
	gna_result = api.get_balances(address)
	balance = gna_result['balances']
	return (balance[0])
	

print ( "Checking balance on the first " + str(numberOfAddresses) + " addresses for " + str(len(seeds)) + " seeds!")
print ("This can take a while...")		
seedSelector()


