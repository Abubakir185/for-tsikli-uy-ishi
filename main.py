son = int(input("son kiritng: "))
sum = 0
for i in range(1, son + 1):
    sum = sum + i

print(sum)




text = input("Jumla kiriting: ")  
bosh_h = "" 
kichik_h = ""

for char in text:
    if char.isupper():
        bosh_h = bosh_h + char
    if char.islower():
        kichik_h = kichik_h + char

print(bosh_h, kichik_h)




text = input("Jumla kiriting: ")  
bosh_h = "" 
kichik_h = ""

for char in text:
    if char.isupper():
        bosh_h = bosh_h + char
    if char.islower():
        kichik_h = kichik_h + char

print(f"{bosh_h} => {len(bosh_h)} ta, {kichik_h} => {len(kichik_h)} ta.")





text = input("Jumla kiriting (raqmlar ham mukin): ")  
bosh_h = "" 
kichik_h = ""
num = ""

for char in text:
    if char.isupper():
        bosh_h = bosh_h + char
    if char.islower():
        kichik_h = kichik_h + char
    if char .isdigit() :
        num = num + char   
    


print(f"{bosh_h} => {len(bosh_h)}ta, {kichik_h} => {len(kichik_h)}ta, {num} => {len(num)}ta ")