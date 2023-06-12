list_of_cloud = ["aws","azure","gcp","oracle"]
list_of_env = ["dev","test","prod"]
#list_of_num = []
#list_of_num.append(1)
#list_of_num.append(2)
#list_of_num.append("Rachana")
#print(list_of_cloud[3])
#for i in range(10):
    #print(i)
    #print("BOOM!")
#for cloud in list_of_cloud:
    #print(cloud)

#List iteration
for cloud in list_of_cloud:
    if cloud == "aws":
        print("aws is the best!")
# dictionary
dict_of_cloud ={
    "aws":"Amazon Web Services",
    "azure":"Microsoft Azure",
    "gcp":"Google Cloud Platform"
}

print (dict_of_cloud["aws"])
print(dict_of_cloud.get("azure","Not found!"))
print(dict_of_cloud.get("Linode","Not found!"))
dict_of_cloud.update({"Linode":"Linode Cloud"})
print(dict_of_cloud["Linode"])
print(dict_of_cloud)