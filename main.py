# Zone 1 ## zone pour les fonctions
# exercice 00 (la fonction est definie dans cette zone)
def exempleHello (msg):
    return "bonjour {}, comment allez-vous ?".format(msg)


###### exercice 01
def makeDico_H6(name, sep):
  dico={}
  nbLines=0
  file = open(name, "r")
  for line in file:
    nbLines +=1
    dico[line.split(sep)[0]] = line.split(sep)[1]
  print ("Création d'un dictionnaire à partir du fichier {} avec {} entrées\n".format(name,nbLines))
  return dico

###### exercice 02
def verifUrl_D7(url):
  if len(url.split(".")) == 2 :
    if len(url.split(".")[1])<=3:
      return True
    else:
      return False
  else : 
      return False


###### exercice 03
def getTLD_Q3(url):
  if verifUrl_D7(url):
    return url.split(".")[1]
  else:
    print("TLD mal formée")
    return False

###### exercice 04
def VerifTLD_S6(tldOk,tld):
  result = False
  for x in tldOk:
    if tld == x:
      result = True
  if result == False:
    print("TFL absente")
  return result

###### exercice 05
def ipVerifFormat_M5(adresseIp):
  result = True
  if adresseIp.count(".") == 3:
    for x in range(0,len(adresseIp.split("."))) :
      if int(adresseIp.split(".")[x]) < 0 or int(adresseIp.split(".")[x]) > 255:
        print("nombre de champs incorrect")
        result = False 
  else:
    print("nombre de champs incorrect")
    result = False
  return result
###### exercice 06
def makeTLD_C7(dico):
  listTLD= []
  nbTLD = 0
  for elem in dico:
      if  listTLD.count(elem.split(".")[1]) == 0:
        listTLD.append(elem.split(".")[1])
        nbTLD +=1
  print ("Creation d'une liste de TLD comprenant {} entrees".format(nbTLD))
  return listTLD

# Zone 2 ## zone pour les classes
###### exercice 07
class serveurDns_O7:
  __dns =""
  def __init__(self,resolDNS):
    self.__dns = resolDNS

###### exercice 08
  #Erreur :AttributeError: 'str' object has no attribute 'items'
  #Je n'arrive pas à comprendre pourquoi

  # def resolDNS_W1(self, url):
  #   if verifUrl_D7(url):
  #     for lien, ip in self.__dns.items():
  #       if lien == url:
  #         return ip
  #     print("url introuvable")
  #     return False
  #   else:
  #     print("erreur de format de l’url")
  #     return False
###### exercice 09


###### exercice 10
    

# Zone 3 ## zone pour les tests des fonctions

def main() :
  from re import split
  ###### exercice 00 (la fonction est appelee dans cette zone afin de confirmer son fonctionnement)
  print("exercice 00 #######################")
  salutations = exempleHello("Michel")
  print(salutations)
  print(salutations.split(sep=" "))

	###### exercice 01
  print("exercice 01 #######################")
  dns=makeDico_H6("dns.txt", ",")

	###### exercice 02
  print("exercice 02 #######################")
  print(str(verifUrl_D7("reddit.com")) + "\n")

	###### exercice 03
  print("exercice 03 #######################")
  print(str(getTLD_Q3("reddit.com"))+ "\n")

	###### exercice 04
  print("exercice 04 #######################")
  print(str(VerifTLD_S6(["fr","com","eu","uk"],"fr")) +"\n")

	###### exercice 05
  print("exercice 05 #######################")
  print(str(ipVerifFormat_M5("192.125.3.5"))+"\n")

	###### exercice 06
  print("exercice 06 #######################")
  print(str(makeTLD_C7(dns)) + "\n")
	# Zone 4 ## zone pour les tests de la classe

	###### exercice 07
  print("exercice 07 #######################")
  test = serveurDns_O7("reddit.com, 192.120.3.2")

	###### exercice 08
  print("exercice 08 #######################")
  #print(str(test.resolDNS_W1("Leboncoin.fr"))+"\n")

	###### exercice 09
  print("exercice 09 #######################")
	
	###### exercice 10
  print("exercice 10 #######################")

if __name__=="__main__":
  print("main()")
  main()