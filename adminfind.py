import requests, pyfiglet

rs = pyfiglet.figlet_format("adminfind")
print(rs)

url = input("URL(ex: www.example.com):")
sublink = input("https(y/t):")

wordlist = open("wordlist.txt", "r")

if sublink == "y":
      link = "https://"
      check = requests.get(link+url)

      if check.status_code == 200:
         try:
             print("Status Code:" ,check)   
             print("Start Scanning...")
             print("Tekan ctrl + c untuk berhenti")

             for word in wordlist:
                 k = word.strip()
                 m = requests.get(link+url+"/"+k)

                 if m.status_code == 200:
                   print("Ditemukan:" ,link+url+"/"+k, m.status_code)
                 elif m.status_code == 301:
                   print(url+"/"+k, m.status_code)
         except KeyboardInterrupt:
               print("Stop")
         except:
               print("error")
      elif check.status_code == 404:
           print("Link:" ,url, "Tidak Ditemukan")
           print("Status Code:" ,check)
elif sublink == "t":
      link = "http://"
      check = requests.get(link+url)

      if check.status_code == 200:
         try:
             print("Status Code:" ,check)   
             print("Start Scanning...")
             print("Tekan ctrl + c untuk berhenti")

             for word in wordlist:
                 k = word.strip()
                 m = requests.get(link+url+"/"+k)

                 if m.status_code == 200:
                   print("Ditemukan:" ,link+url+"/"+k, m.status_code)
                 elif m.status_code == 301:
                   print(url+"/"+k, m.status_code)
         except KeyboardInterrupt:
               print("Stop")
         except:
               print("error")
      elif check.status_code == 404:
           print("Link:" ,url, "Tidak Ditemukan")
           print("Status Code:" ,check)
   
print("finish")
       
