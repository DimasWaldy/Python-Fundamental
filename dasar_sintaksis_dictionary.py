users = {
     "id": 1,
     "name" : "Dimas",
     "username" : "dimas1",
     "email" : "dimas1@gmail.com",
    "address" : {
        "street" : "Cut Mutia",
        "suite" : "Blok A4",
        "city" : "Bekasi",
        "zipcode": "17113",
        "geo" : {
            "lat" : "-23.111",
            "lng" : "12.142"
        }
    }
}
print(users)
print(users['id'])
print(users['name'])
print(users['username'])
print(users['email'])
print(users['address']['geo']) #mengakses dictionary di dalam dictionary


#mengubah dictionary python menjadi json
print("\nUbah dict ke JSON")
import json
result = json.dumps(users)
print(result)

#buat file dictionary python menjadi json , setelah dirunnging akan muncul file result.json di project
with open('result.json', 'w') as file:
    json.dump(users, file)