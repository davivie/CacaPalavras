

import re
from email.mime.text import MIMEText
import random
import smtplib
import random



def email_enviar(remetente,corpo,destinatario,assunto,senha):

        #corpo da mensagem
        msg = MIMEText(corpo)
        msg['From'] = remetente # quem envia
        msg['To'] = destinatario # quem recebe
        msg['Subject'] = assunto #o assunto


    ###
        conector = smtplib.SMTP("smtp.gmail.com",587)
        conector.starttls()

        conector.login(msg['From'], senha)

        conector.sendmail(msg['From'], [msg['To']], 
        msg.as_string()
        .encode('utf-8'))

        print('Email enviado')

while True:
        opcao=input("Gostaria de Jogar ou enviar um email? digite: Jogar / Email ").upper()


        if opcao == "EMAIL":
                remetente=input("digite o remetente")

                regex_emailr= r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$'

                if re.search(regex_emailr, remetente):

                    senha=input("digite a senha do remetente")

                    assunto= input("Digite o assunto do seu texto")

                    corpo=input("Digite o corpo do seu email")

                    
                    alteraC= input("deseja alterar o corpo ou assunto, diga SIM ou aperte enter para continuar").upper()

                    while True: 
                        if alteraC =="SIM":

                            alteraD=input("qual deseja alterar corpo ou assunto? ").upper()
                            
                            
                            if alteraD =="CORPO":
                                corpo=input("digite o novo corpo")
                                

                            elif alteraD =="ASSUNTO":
                                assunto=input("digite o novo assunto")
                
                                
                                break

                            elif alteraD!= "CORPO" or "ASSUNTO":
                                print("opcão invalida")
                                    

                        elif alteraC != "SIM":
                        
                            break
            

                    while True:
                        
                            destinatario=input("digite o email do destinatario ")

                            regex_email= r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$'
                            
                            if re.search(regex_email, destinatario):

                                    email_enviar(remetente,corpo,destinatario,assunto,senha)
                                    break
                            else:
                                print("email invalido")
                else:
                    print("remetente invalido")

        elif opcao != "EMAIL":
            print("Email invalido")
                
        elif opcao =="JOGAR":

            def escolher_palavra():
                palavra= ['LIMAO','ABACAXI','JABUTICABA','UVA','MELANCIA','ABACATE','MORANGO','ABACATE','PEQUI']
                return random.choice(palavra)

            def jogo_forca():
                palavra="UVA"
                #escolher_palavra()

                tentativas = 7

                acertos=0
                erros=0

                acertos_letra=" "
                erros_letra=" "


                while acertos != len(palavra) and erros != tentativas:


                    for letra in palavra:
                        
                        if letra in acertos_letra:
                            print(letra,end="")
                        else:
                            print("_",end="")
                            
                    
                    print("\nLetras acertadas: ",acertos_letra)
                    print("Letras erradas: ",erros_letra)

                    letra =input("Digite a letra ").upper()

                    if letra.isalpha() and len(letra) == 1:

                        if letra in palavra:
                            
                            if letra not in acertos_letra:

                                acertos_letra = acertos_letra + letra

                                acertos = acertos + palavra.count(letra)
                        else:
                        
                            if letra not in erros_letra:  
                                erros_letra = erros_letra + letra
                                erros = erros + 1
                                print("Voce tem :", (tentativas-erros), "chances")
                    else:
                        print("letra invalida")

                print("Fim de jogo!")

                if acertos == len(palavra):
                    resultado= "Voce venceu"
                else:
                    resultado=" voce perdeu"
                    #print("palavra certa era ", palavra)

                return resultado

            result =jogo_forca()
            print(result)

            

            # o looping continua aqui, se caso o usuario inserir não eu quero que volte ao comeco do programa
            while True:
                opc=input("gostaria de enviar o resultado ao seu email : SIM / NAO ?").upper()





                if opc =="SIM":
                        
                        regex_email= r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$'

                        assunto= "Jogo da Forca"

                        corpo=result

                        remetente=input("digite o remetente")

                        regex_emailr= r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$'

                        if re.search(regex_emailr, remetente):

                            senha=input("digite a senha do remetente")
                        
                            while True:
                                destinatario=input("digite o email do destinatario ")

                                if re.search(regex_email, destinatario):

                                    email_enviar(remetente,corpo,destinatario,assunto,senha)
                                    
                                    break
                            
                                else:
                                    print("email invalido")

                            break
                        else:
                            print("remetente invalido")

                elif opc == "NAO":
                        print("Tenha um dia legal, obrigado por jogar :) ")
                        break
                        
                    

                elif opc != "SIM" or "NAO":
                    print("Resposta invalida,")
                

        elif opcao != "JOGAR" or "EMAIL":
            print("Invalido")
        


            
            
# Estrutura do Jogo



