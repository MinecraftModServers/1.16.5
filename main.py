import os, time


print("**script**: starting server")
os.system('nohup java -Xmx1G -jar forge-1.16.5-36.2.39.jar > nohup.out &')

while True:
    time.sleep(10)
    result = open('nohup.out', 'r').read().find('Done')
    if result > -1:
        break

print("**script**: server has started!")
time.sleep(10)
print("**script**: starting ngrok tcp")
os.system('ngrok tcp -region us 8080 &')
time.sleep(10)



