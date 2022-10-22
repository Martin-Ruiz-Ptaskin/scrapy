# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:47:36 2022

@author: mruizpta
"""

import time
import mysql.connector
from mysql.connector import Error
from selenium import webdriver 
from threading import Thread, Barrier
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

mycursor.execute("SELECT * FROM ethereum")
cachelist=[]
myresult = mycursor.fetchall()


for rest in myresult:
    resultados= cartera(rest[0],rest[1])
    cachelist.append(resultados)
"""----------------------FIN CONECCION----------------------------"""

def func(threads,url):
 driver = webdriver.Chrome(executable_path=r'C:\\Users\\mruizpta\\chromedriver_win32\\chromedriver.exe')

 for u in url:     
   driver.get("https://blockchair.com/es/ethereum/address/"+u)
   autos = driver.find_elements_by_xpath('//div[@class="account-hash-wrap d-flex p-relative br-8 bgc-bright shadow-block"]')
   
   for auto in autos:
            # Por cada anuncio hallo el preico
    precio = auto.find_element_by_xpath('.//span[@class="wb-ba"]').text
    wallet = auto.find_element_by_xpath('.//div[@class="account-hash__hash__value mt-5 d-flex ai-center font-mono medium lh-100 c-txt-main wb-ba fs-18"]').text
    print(precio,wallet)
    wllet=cartera(wallet,precio)
    amount.append(wllet)
 driver.close()
 
 
	

url =['0xf977814e90da44bfa03b6295a0616a897441acec','0xda9dfa130df4de4673b89022ee50ff26f6ea73cf','0x0716a17fbaee714f1e6ab0f9d59edbc5f09815c0','0xbe0eb53f46cd790cd13851d5eff43d12404d33e8','0x742d35cc6634c0532925a3b844bc454e4438f44e','0xa7efae728d2936e78bda97dc267687568dd593f3','0xe92d1a43df510f82c66382592a047d288f85226f','0x1b3cb81e51011b549d78bf720b0d924ac763a7c2','0xca8fa8f0b631ecdb18cda619c4fc9d197c8affca','0xdf9eb223bafbe5c5271415c75aecd68c21fe3d7f','0xb29380ffc20696729b7ab8d093fa1e2ec14dfe2b','0x8103683202aa8da10536036edef04cdd865c225e','0x176f3dab24a159341c0509bb36b833e7fdd0a132','0x0a4c79ce84202b03e95b7a692e5d728d83c44c76','0x5a52e96bacdabb82fd05763e25335261b270efcb','0x2b6ed29a95753c3ad948348e3e7b1a251080ffb9','0x189b9cbd4aff470af2c0102f365fc1823d857965','0x9acb5ce4878144a74eeededa54c675aa59e0d3d2','0x9845e1909dca337944a0272f1f9f7249833d2d19','0x9bec8d9d62c68792cea3123a231fb8c31f140f3d','0xb7b9526e61738032cefaaaea37164e279ab87c76','0x99c9fc46f92e8a1c0dec1b1747d010903e884be1','0x59448fe20378357f206880c58068f095ae63d5a5','0x558553d54183a8542f7832742e7b4ba9c33aa1e6','0x98ec059dc3adfbdd63429454aeb0c990fba4a128','0xcdbf58a9a9b54a2c43800c50c7192946de858321','0xbf3aeb96e164ae67e763d9e050ff124e7c3fdd28','0xc882b111a75c0c657fc507c04fbfcd2cc984f071','0x36a85757645e8e8aec062a1dee289c7d615901ca','0x550cd530bc893fc6d2b4df6bea587f17142ab64e','0xdc1487e092caba080c6badafaa75a58ce7a2ec34','0x9cf36e93a8e2b1eaaa779d9965f46c90b820048c','0xa7e4fecddc20d83f36971b67e13f1abc98dfcfa6','0xa0efb63be0db8fc11681a598bf351a42a6ff50e0','0x8b83b9c4683aa4ec897c569010f09c6d04608163','0x5b5b69f4e0add2df5d2176d7dbd20b4897bc7ec4','0x18709e89bd403f470088abdacebe86cc60dda12e','0x4756eeebf378046f8dd3cb6fa908d93bfd45f139','0x554f4476825293d4ad20e02b54aca13956acc40a','0x2f2d854c1d6d5bb8936bb85bc07c28ebb42c9b10','0xd6216fc19db775df9774a6e33526131da7d19a2c','0xa8dcc0373822b94d7f57326be24ca67bafcaad6b','0x0548f59fee79f8832c299e01dca5c76f034f558e','0x203520f4ec42ea39b03f62b20e20cf17db5fdfa7','0xb9711550ec6dc977f26b73809a2d6791c0f0e9c8','0xfd898a0f677e97a9031654fc79a27cb5e31da34a','0xfe01a216234f79cfc3bea7513e457c6a9e50250d','0xb8cda067fabedd1bb6c11c626862d7255a2414fe','0x701c484bfb40ac628afa487b6082f084b14af0bd','0x4b4a011c420b91260a272afd91e54accdafdfc1d','0xc4cf565a5d25ee2803c9b8e91fc3d7c62e79fe69','0xb20411c403687d1036e05c8a7310a0f218429503','0xd05e6bf1a00b5b4c9df909309f19e29af792422b','0x19d599012788b991ff542f31208bab21ea38403e','0x77afe94859163abf0b90725d69e904ea91446c7b','0xca582d9655a50e6512045740deb0de3a7ee5281f','0x0f00294c6e4c30d9ffc0557fec6c586e6f8c3935','0xeb2b00042ce4522ce2d1aacee6f312d26c4eb9d6','0x7ae92148e79d60a0749fd6de374c8e81dfddf792','0x091933ee1088cdf5daace8baec0997a4e93f0dd6','0x828103b231b39fffce028562412b3c04a4640e64','0x9a1ed80ebc9936cee2d3db944ee6bd8d407e7f9f','0xb9fa6e54025b4f0829d8e1b42e8b846914659632','0xba18ded5e0d604a86428282964ae0bb249ceb9d0','0x0c05ec4db907cfb91b2a1a29e7b86688b7568a6d','0xe04cf52e9fafa3d9bf14c407afff94165ef835f7','0x9c2fc4fc75fa2d7eb5ba9147fa7430756654faa9','0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98','0x8d95842b0bca501446683be598e12f1c616770c1','0x35aeed3aa9657abf8b847038bb591b51e1e4c69f','0xb93d8596ac840816bd366dc0561e8140afd0d1cb','0xb5ab08d153218c1a6a5318b14eeb92df0fb168d6','0xdb3c617cdd2fbf0bb4309c325f47678e37f096d9','0x7ead3a4361bd26a20deb89c9470be368ee9cb6f1','0x5f397b62502e255f68382791947d54c4b2d37f09','0xd5268a476aadd1a6729df5b3e5e8f2c1004139af','0xf481b7fab9f5d0e74f21ae595a749634fb053619','0xf203f6ce087e91c88881d0390f54c3dcb30fcd76','0x3c68e2be148cfa3da533d7bbceb4973deebc0df3','0x595faf77e533a5cd30ab5859c9a0116de8bad8db','0x1bd3fc5ac794e7af8e834a8a4d25b08acd9266ce','0xd47b4a4c6207b1ee0eb1dd4e5c46a19b50fec00b','0xd65fb7d4cb595833e84c3c094bd4779bab0d4c62','0xa1a45e91164cdab8fa596809a9b24f8d4fdbe0f3','0x368d43c23843ca9b49dc861d80251bda6a090367','0x6d9d2b30df394f17a5058aceb9a4d3446f1bc042','0x84bf16e7675cee22d0e0302913ccf58b45333ddf','0xb4f4317b7885de16305d1303570879c21f378255','0xf443864ba5d5361bbc54298551067194f980a635','0xbed96d0840201011df1467379a5d311e0040073a','0x4eac9ce57af61a6fb1f61f0bf1d8586412be30bc','0x2d1566722288be5525b548a642c98b546f116aa0','0x76ae5632ae65d95dd704218920f7d8ac4daef9cc','0x5657e633be5912c6bab132315609b51aadd01f95','0x67f706db3bbd04a250eed049386c5d09c4ee31f0','0x5f0cc098cfef729a0c1072268945d1a5fd57b45d','0x40f50e8352d64af0ddda6ad6c94b5774884687c3','0x2d89034424db22c9c555f14692a181b22b17e42c','0x469f1ea76d13d4b4ea20a233eac8ce6ac74d5087','0x539c92186f7c6cc4cbf443f26ef84c595babbca1','0xbfbbfaccd1126a11b8f84c60b09859f80f3bd10f','0x868dab0b8e21ec0a48b726a1ccf25826c78c6d7f','0x999e77c988c4c1451d3b1c104a6cca7813a9946e']





cantidad=round(len(url)/25)
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
 if(1==2): 

  print("entra aca")
  query="INSERT INTO `ethereum`(`wallet`, `amount`) VALUES ('"+ tag.wallet +"','"+amount+"')"
  execute_query(connection, query)
  
  
  """ con este actualizo """
 if(1==1):
  for cache in cachelist:
            
            
            if cache.wallet==tag.wallet:
                
                previo=float(cache.amount)
                neto=(previo-float(amount))
                print(previo-float(amount))
                query="UPDATE `ethereum` SET `amount`='"+amount+"' WHERE `wallet`='"+ tag.wallet +"'"
                
                execute_query(connection, query)
                if neto>=3:
                   print( "se debe accionar tiene menos",cache.wallet)
                elif neto <=-3 :
                    print("se debe aacionar tiene mas",cache.wallet)

   