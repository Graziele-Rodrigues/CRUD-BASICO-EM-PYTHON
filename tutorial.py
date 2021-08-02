import sqlite3,os,time,winsound

class Manager:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""
    
    def add(self):
        running = True
        while running:
            os.system("cls") #limpando tela
            print("----------ADICIONE UM NOVO CONTATO----------")
            print("Precione a tecla SHIFT + Q para cancelar")
            print()
            temp_name = input('Name: ')
            if len(temp_name) != 0 and temp_name != "q".upper():
                db = sqlite3.connect("connection")
                cursor = db.cursor()
                cursor.execute("SELECT Name FROM contacts")
                results = cursor.fetchall()
                for i in results:
                    if temp_name in i:
                        print('ESTE CONTATO JA EXISTE') 
                        time.sleep(2)
                        self.add()
                self.name=temp_name
                temp_name= ' '
                time.sleep(0.20)
                self.phone = input("Phone: ")
                time.sleep(0.20)
                self.address = input("Address: ")
                time.sleep(0.20)
                cursor.execute("""INSERT INTO contacts\
                                (Name, Phone, Address)VALUES(?,?,?)""",\
                                (self.name, self.phone, self.address))
                db.commit()
                add_more = input("Deseja adicionar mais outro contato? (Y/N): ")
                if add_more == 'y'.lower():
                    continue
                else:
                    db.close()
                    running = False
                    print("MENU ENCERRADO")
                    time.sleep(2)
                    self.menu()
            elif temp_name == "q".upper():
                print('Saindo do menu...')
                time.sleep(2)
                self.menu()
            else:
                print('Campo vazio, tente novamente')
                time.sleep(1)
                self.add()



    def remove(self):
        print()
        print("DELETAR CADASTROS")
        name = input("Digite o nome do cliente: ")
        confirm = input("Tem certeza? (Y/N) ").upper()
        if confirm == "Y":
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            cursor.execute("DELETE FROM contacts WHERE Name = ?",(name,))
            db.commit()
            print("DELETADO COM SUCESSO")
            time.sleep(2)
            self.menu()
        else:
            print("Saindo...")
            time.sleep(2)
            self.menu()
            
    def update(self):
        print()
        print("ATUALIZAR CADASTROS")
        name = input("Digite o nome do cliente: ")
        confirm = input("Tem certeza? (Y/N) ").upper()
        if confirm == "Y":
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            phone_update = input("Atualizar telefone? (Y/N) ").upper()
            if phone_update == "Y":
                phone = input("Digite o novo telefone: ")
                cursor.execute("UPDATE contacts SET Phone = ? Where Name=?", (phone, name))
                db.commit()
                print("ATUALIZADO COM SUCESSO")
                time.sleep(2)
            else:
                print("Saindo...")
                time.sleep(2)
            address_update = input("Atualizar o Address? (Y/N) ").upper()
            if address_update == "Y":
                address = input("Digite o novo address: ")
                cursor.execute("UPDATE contacts SET Address = ? Where Name=?", (address, name))
                db.commit()
                print("ATUALIZADO COM SUCESSO")
                time.sleep(2)
                self.menu()
            else:
                print("Saindo...")
                time.sleep(2)
                self.menu()
        else:
            print("Saindo...")
            time.sleep(2)
            self.menu()

    def list(self):
        count = 0 
        count_2 = 0
        db = sqlite3.connect("connection")
        cursor = db.cursor()
        os.system("cls")
        print("-------------CONTATOS-------------")
        time.sleep(0.5)
        cursor.execute("SELECT Name, Phone, Address FROM contacts")
        results = cursor.fetchall()
        for row in results:
            time.sleep(0.5)
            count += 1
            count_2 += 1
            print(count_2, row)
            print()
            if count == 5:
                input("Precione Qualquer Tecla para continuar: ")
                count = 0
                print()
        print("FIM DOS RESULTADOS")
        print()
        option = input("Aperte (A) para atualizar, (D) para deletar e (M) para menu: ")
        if option == 'a'.lower():
            self.update()
        elif option == 'd'.lower():
            self.remove()
        elif option == 'm'.lower():
            self.menu()
        else:
            print("opcao invalida")

    def terminate(self):
        confirm = input("DESEJA REALMENTE SAIR DO SISTEMA? (Y/N) ").upper()
        if confirm=="Y":
            print("Saindo do sistema")
            winsound.Beep(3000,50)
            print("...........")
            time.sleep(0.5)
            print(".......")
            time.sleep(0.5)
            print("....")
            time.sleep(0.5)
            print("..")
            time.sleep(0.5)
            print(".")
            exit()
        else:
            self.menu()
            

    def menu(self):
        winsound.Beep(2000,50)
        print('-----------MENU-----------')
        time.sleep(0.05)
        print('1 :) Add')
        time.sleep(0.05)
        print('2 :) Remove')
        time.sleep(0.05)
        print('3 :) Update')
        time.sleep(0.05)
        print('4 :) List')
        time.sleep(0.05)
        print('5 :) Terminate')
        print()
        opcao = input('SELECIONE UMA OPÇÃO: ')
        if opcao == "1":
            self.add()
        elif opcao == "2":
            self.remove()
        elif opcao == "3":
            self.update()
        elif opcao == "4":
            self.list()
        elif opcao == "5":
            self.terminate()
        else:
            valido = False
            winsound.Beep(2500, 1000)
            print('ERROR! TENTE NOVAMENTE AS OPCOES DE 1 A 5' )
            
    def main(self):
        if os.path.isfile("connection"):
            db=sqlite3.connect("connection")
            time.sleep(2)
            print("CONECTADO AO BANCO DE DADOS")
            time.sleep(2)
            self.menu()
        else:
            print("CONEXAO NAO EXISTE")
            time.sleep(2)
            print("CRIANDO NOVA CONEXÃO COM BANCO DE DADOS")
            time.sleep(2)
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            cursor.execute("""CREATE TABLE 
                            contacts(Name TEXT, Phone TEXT, Address TEXT)""")
            print("CONEXÃO CRIADO COM SUCESSO")
            time.sleep(2)
            self.menu()
        
        self.menu()

contacts = Manager()
contacts.main()

