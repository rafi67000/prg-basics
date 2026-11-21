# dictionary
mobile = {
    "OS": "Android",           # system operacyjny (str)
    "manufacturer": "Samsung", # producent (str)
    "model": "Galaxy S23",     # model (str)
    "ram_GB": 8,               # pamięć RAM w GB (int)
    "storage_GB": 256,         # pamięć wbudowana w GB (int)
    "screen_inches": 6.1,      # przekątna ekranu w calach (float)
}

for key, value in mobile.items(): # iterowanie po  parach w słowniku
    print(f"{key} : {value}")
