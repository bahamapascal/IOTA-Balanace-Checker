from iota import Iota


numberOfAddresses = 5
seeds = ["POCTEST", "TGAT"]


api = Iota('http://148.251.233.147:14265', b'SEED9GOES9HERE')



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


# Generate 5 addresses, starting with index 0.
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
	
addresses = ["MII9DNFOSWEJUQAMZPMFKHVWKEERZLOQGBPVLCJWWTJPOBCAVOWNABUJLBJXQSNGOEZQKTCXAVHBDZCIKDLMZYSPWW"]
print ( "Checking balance on the first " + str(numberOfAddresses) + " addresses for " + str(len(seeds)) + " seeds!")
print ("This can take a while...")		
seedSelector()



def nodeInfo():
	rawInfo = (api.get_node_info())
	info = rawInfo['latestMilestoneIndex']
	
		
	return info

