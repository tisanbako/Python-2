l = [{"name":["jerry", "bako", "zack"], "age":12, "address":"lagos"}, "a","b",
     "c", {"name2":"tisan", "hobbies":["travel", "dance", "sing"]},"d"]
print(l[0]["name"][0]) #jerry first [0] is for everything in the dict 
print(l[2])   #b
print(l[4]["hobbies"][0])  #travel
print(l[5])     #d


m = {"name":["jerry", "bako", "zack"], "age":12, "address":"lagos", 
"hobbies":["travel", "dance", "sing"]}
print(m["name"][2])    #Zack
print(m["hobbies"][1])    #dance

a = [{"name":["jerry", "bako", "zack"],}, {"name":[12, "address" ]}, {"name":["tisan", "misa", "sassy"]}]
for b in a:
    print(b["name"][0])
    #print(b["name"][2]) will be out of range as second name index ends at 1