import time
import mysql.connector
from mysql.connector import Error
from selenium import webdriver 
from threading import Thread, Barrier
from datetime import date,datetime

amount=[]
class cartera:
    def __init__(self,wallet,amount):
        self.wallet=wallet
        self.amount = amount
        
"""---------------------------------------------------"""
        
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

"""---------------------------------------------------"""

connection = create_db_connection("localhost", "root", "", "scrapy")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
"""---------------------------------------------------"""
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="scrapy"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM bitcoin")
cachelist=[]
myresult = mycursor.fetchall()


for rest in myresult:
    resultados= cartera(rest[0],rest[1])
    cachelist.append(resultados)
"""----------------------FIN CONECCION----------------------------"""

def func(threads,url):
   try: 
     driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')
    
     for u in url:     
       driver.get("https://blockchair.com/es/bitcoin/address/"+u)
       autos = driver.find_elements_by_xpath('//div[@class="account-hash-content w-100"]')
       for auto in autos:
                # Por cada anuncio hallo el preico
        precio = auto.find_element_by_xpath('.//span[@class="wb-ba"]').text
        wallet = auto.find_element_by_xpath('.//div[@class="account-hash__hash__value mt-5 d-flex ai-center font-mono medium lh-100 c-txt-main wb-ba fs-20"]').text
        wllet=cartera(wallet,precio)
        amount.append(wllet)
     driver.close()
   except:
       print ("error")
 
	

url =['34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo','bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97','3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6','1LQoWist8KkaUXSPKZHNvEyfrEkPHzSsCd','3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb',      'bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt','37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs','1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF','bc1qa5wkgaew2dkv56kfvj49j0av5nml45x9ek9hz6','3Kzh9qAqVWQhEsfQz7zEQL1EuSx5tyNLNS','bc1qd4ysezhmypwty5dnw7c8nqy5h5nxg0xqsvaefd0qn5kq32vwnwqqgv4rzr','1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC','1AC4fMwgY8j9onSbXEWeH6Zan8QGMSdmtA','35PPdr9CSZuqwi2S7vj9ResHQCVTsYuB3z','bc1qmxjefnuy06v345v6vhwpwt05dztztmx4g3y7wp','1LruNZjwamWJXThX2Y8C2d47QqhAkkc5os','3LCGsSmfr24demGvriN4e3ft8wEcDuHFqh','3LQUu4v9z6KNch71j7kbj8GPeAGUo1FW6a','bc1q7ydrtdn8z62xhslqyqtyt38mm4e2c4h3mxjkug','38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67','bc1qjasf9z3h7w3jspkhtgatgpyvvzgpa2wwd2lr0eh5tx44reyn2k7sfc27a4','bc1qjysjfd9t9aspttpjqzv68k0ydpe7pvyd5vlyn37868473lell5tqkz456m','bc1qcdeadk07jkthules0yw9u9ue9pklvr608ez94jgwcf7h2ldzcg6qwxp9er','12XqeqZRVkBDgmPLVY4ZC6Y4ruUUEug8Fx','bc1qx9t2l3pyny2spqpqlye8svce70nppwtaxwdrp4','3FHNBLobJnbCTFTVakh5TXmEneyf5PT61B','12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr','bc1qr4dl5wa7kl8yu792dceg9z5knl2gkn220lk7a9','12tkqA9xSoowkzoERHMWNKsTey55YEBqkv','385cR5DM96n1HvBDMzLHPYcw89fZAXULJP','bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h','3FpYfDGJSdkMAvZvCrwPHDqdmGqUkTsJys','17MWdxfjPYP2PYhdy885QtihfbW181r1rn','1aXzEKiDJKzkPxTZy9zGc3y1nCDwDPub2','19D5J8c59P2bAkWKvxSYw8scD3KUNWoZ1C','3FupZp77ySr7jwoLYEJ9mwzJpvoNBXsBnE','bc1q4jchcr7nla277su5lpjzttxp3xg5j8wds5lcwg','1932eKraQ3Ad9MeNBHb14WFQbNrLaKeEpT','143gLvWYUojXaWZRrxquRKpVNTkhmr415B','18B1dqmRiMVt6mwUrqMUvkT14mChTwdXGT','bc1qtw30nantkrh7y5ue73gm4mmy0zezfqxug3psr94sd967qwg7f76scfmr9p','17rm2dvb439dZqyMe2d4D6AQJSgg6yeNRn','1PeizMg76Cf96nUQrYg8xuoZWLQozU5zGW','bc1qkz55x35wlnrkrn5n0nq4wwsme9vszrwavu5qf4','39gUvGynQ7Re3i15G3J2gp9DEB9LnLFPMN','15pqaBHFwFEphRqmXAPbs3QRLLPB7e2uMb','3H5JTt42K7RmZtromfTSefcMEFMMe18pMD','31k2z8HocUWMCMXBkXREPiXNgK2fB3iLwo','15cHRgVrGKz7qp2JL2N5mkB2MCFGLcnHxv','3JZq4atUahhuA9rLhXLMhhTo133J9rF97j','34HpHYiyQwg69gFmCq2BGHjF1DZnZnBeBP','bc1q080rkmk3kj86pxvf5nkxecdrw6nrx3zzy9xl7q','1GR9qNz7zgtaW5HwwVpEJWMnGWhsbsieCG','bc1qw0pswznckx7s6tjmd2f5hrx4q6kc5nyrdxku50','3Qrx7c1f2SmubFMJvKJnFW37YwacQmxDqq','1KUr81aewyTFUfnq4ZrpePZqXixd59ToNn','3BMEXqGpG4FxBA1KWhRFufXfSTRgzfDBhJ','3EMVdMehEq5SFipQ5UfbsfMsH223sSz9A9','1MDq7zyLw6oKichbFiDDZ3aaK59byc6CT8','3BHXygmhNMaCcNn76S8DLdnZ5ucPtNtWGb','1FZy7CPFA2UqqQJYUA1cG9KvdDFbSMBJYG','1KVpuCfhftkzJ67ZUegaMuaYey7qni7pPj','1BZaYtmXka1y3Byi2yvXCDG92Tjz7ecwYj','bc1quhruqrghgcca950rvhtrg7cpd7u8k6svpzgzmrjy8xyukacl5lkq0r8l2d','36rPiyFi4pZmnAyYbDTABqLN3WcWP6yJXS','bc1q4vxn43l44h30nkluqfxd9eckf45vr2awz38lwa','12qTdZHx6f77aQ74CPCZGSY47VaRwYjVD8','1DNUjpHPNKMoKYBHxJz2Sh1uQQdJkGsXj5','3HSMPBUuAPQf6CU5B3qa6fALrrZXswHaF1','12Gjyd3MMR7Dj2KwCxw71wwzZXVp2xy8nK','17SAATrqavNbzmqBwqxzZc7rK6u9Rmi9hE','1C7u4Zqu6ZZRsiKsFMYVDvNLfCwsGrbeTq','14KzHoS5dXbhy2kBevNKLz2ZMtjaqHkKWZ','1Cr7EjvS8C7gfarREHCvFhd9gT3r46pfLb','15ZQJagAa2iUCwpQXUUCZ4BfzFW5TAVyJj','1F34duy2eeMz5mSrvFepVzy7Y1rBsnAyWC','35pgGeez3ou6ofrpjt8T7bvC9t6RrUK4p6','bc1qhd0r5kh3u9mhac7de58qd2rdfx4kkv84kpx302','bc1qx2x5cqhymfcnjtg902ky6u5t5htmt7fvqztdsm028hkrvxcl4t2sjtpd9l','1f1miYFQWTzdLiCBxtHHnNiW7WAWPUccr','bc1qsxdxm0exqdsmnl9ejrz250xqxrxpxkgf5nhhtq','bc1qtef0p08lputg4qazhx2md43ynhc9kp20pn297qnz68068d9z48asmemanj','1BAFWQhH9pNkz3mZDQ1tWrtKkSHVCkc3fV','bc1qe75775tzuvspl59cw77ycc472jl0sgue69x3up','14YK4mzJGo5NKkNnmVJeuEAQftLt795Gec','1Ki3WTEEqTLPNsN5cGTsMkL2sJ4m5mdCXT','35WHp4Hid61peyH4tuhNunwRj2gtNB41Lo','1KbrSKrT3GeEruTuuYYUSQ35JwKbrAWJYm','1P1iThxBH542Gmk1kZNXyji4E4iwpvSbrt','12tLs9c9RsALt4ockxa1hB4iTCTSmxj2me','1ucXXZQSEf4zny2HRwAQKtVpkLPTUKRtt','1CPaziTqeEixPoSFtJxu74uDGbpEAotZom','1LfV1tSt3KNyHpFJnAzrqsLFdeD2EvU1MK','bc1q5nfww5jn5k4ghg7dpa4gy85x7uu3l4g0m0re76','3EEDeu13ex19AqQBTZStVsAFy6j1gRwgWc','bc1q4srun4yspqem2pqgk47eq9jspcht3fmyrmfdeu','bc1qe39l9l84sa44r9j2jjkgdc7p4ltj3sracd932k','bc1qvy0sp8cdj3cv2wwh05scucxw6vxqpdlhfjvqn8','bc1qm6q8tgml3cr9gpx63a5jqtj2dxlsyz4q3ghjlf','bc1qdhvtwg0eealy5d2spua2a89sq05ydvtgjy4uau']




cantidad=round(len(url)/10)
barrier = Barrier(cantidad)
def get_sublists(original_list, number_of_sub_list_wanted):
 sublists = list()
 for sub_list_count in range(number_of_sub_list_wanted): 
  sublists.append(original_list[sub_list_count::number_of_sub_list_wanted])
 return sublists
url=get_sublists(url, cantidad)
threads = []

for a in url:
 i = Thread(target=func, args=(barrier,a,))
 i.start()
 threads.append(i)

for i in threads:
 i.join()



        

print(len(amount))
for tag in amount:
    

 amount= tag.amount.replace(',','')
   
 amount= amount.replace(',','.')
 """ con este cargo nuevos con borrado previo """
 try:
     if(1==2): 
    
      print("entra aca")
      query="INSERT INTO `bitcoin`(`wallet`, `amount`) VALUES ('"+ tag.wallet +"','"+amount+"')"
      execute_query(connection, query)
      
      
      """ con este actualizo """
     if(1==1):
    
      for cache in cachelist:
                
                
                if cache.wallet==tag.wallet:
                    
                    previo=float(cache.amount)
                    neto=(previo-float(amount))
                    print(previo-float(amount))
                    query="UPDATE `bitcoin` SET `amount`='"+amount+"' WHERE `wallet`='"+ tag.wallet +"'"
                    print(query)
                    execute_query(connection, query)
                    if neto ==0:
                        print( "nada que hacer")
                    if neto>=3:
                       print( "se debe accionar tiene menos")
                       query="INSERT INTO `hist_cripto_changes`(`wallet`, `amount`,`date`, `cripto`) VALUES ('"+ tag.wallet +"','"+amount+"',"+date.today().strftime("%m/%d/%Y")+",'BTC')"
    
                    elif neto <=-3 :
                        print("se debe aacionar tiene mas",cache.wallet)
                        query="INSERT INTO `hist_cripto_changes`(`wallet`, `amount`,`date`, `cripto`) VALUES ('"+ tag.wallet +"','"+amount+"',"+date.today().strftime("%m/%d/%Y")+",'BTC')"
 except:
   print ("error")   

   