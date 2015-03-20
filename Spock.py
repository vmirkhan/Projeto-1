nome=str(input("Digite seu nome para iniciar o jogo:"))
print("""O jogo é pedra-papel-tesoura-lagarto-spock.
Você, %s, jogará contra mim, o poderoso computador!"""%nome)
print("Digite suas escolhas com letras minusculas!")
from random import randint
n=randint(1,5)               #escolha do pc
if n==1:  
    escpc="pedra"
if n==2:
    escpc="papel"
if n==3:
    escpc="tesoura"
if n==4:
    escpc="lagarto"
if n==5:
    escpc="spock"
escus=str(input("Estou pronto!Faça sua escolha:"))     #escolha do usuario
escus=escus.lower()
print("Eu escolho %s"%escpc)
score_pc=0
score_us=0
while True:
    if escpc=="pedra" and (escus=="papel" or escus=="spock"):
        score_us=score_us+1
        score_pc=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        if score_us==3:
            print("Você me derrotou! Parabéns, %s"%nome)
            break
        print("Você venceu!Vamos denovo") 
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
             escpc="pedra"
        if n==2:
             escpc="papel"
        if n==3:
             escpc="tesoura"
        if n==4:
             escpc="lagarto"
        if n==5:
             escpc="spock"
        print("Eu escolho %s"%escpc)
    if escpc=="pedra" and (escus=="tesoura" or escus=="lagarto"):
        score_pc= score_pc+1
        score_us=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        if score_pc==3:
           print("Eu derrotei você, %s. Perdedor."%nome)
           break
        print("Eu venci!Vamos denovo.")
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
             escpc="pedra"
        if n==2:
             escpc="papel"
        if n==3:
             escpc="tesoura"
        if n==4:
             escpc="lagarto"
        if n==5:
             escpc="spock"
        print("Eu escolho %s"%escpc)
    if escpc=="papel" and (escus=="tesoura" or escus=="lagarto"):
        score_us= score_us+1
        score_pc=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        if score_us==3:
            print("Você me derrotou! Parabéns, %s"%nome)
            break
        print("Você venceu! Vamos denovo.") 
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
             escpc="pedra"
        if n==2:
             escpc="papel"
        if n==3:
             escpc="tesoura"
        if n==4:
             escpc="lagarto"
        if n==5:
             escpc="spock"
        print("Eu escolho %s"%escpc)
    if escpc=="papel" and (escus=="spock" or escus=="pedra"):
        score_pc=score_pc+1
        score_us=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        if score_pc==3:
           print("Eu derrotei você, %s. Perdedor."%nome)
           break
        print("Eu venci!Vamos denovo.")
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
             escpc="pedra"
        if n==2:
             escpc="papel"
        if n==3:
             escpc="tesoura"
        if n==4:
             escpc="lagarto"
        if n==5:
             escpc="spock"
        print("Eu escolho %s"%escpc)
    if escpc=="tesoura" and (escus=="spock" or escus=="pedra"):
        score_us=score_us+1
        score_pc=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        if score_us==3:
            print("Você me derrotou! Parabéns, %s"%nome)
            break
        print("Você venceu! Vamos denovo.") 
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
             escpc="pedra"
        if n==2:
             escpc="papel"
        if n==3:
             escpc="tesoura"
        if n==4:
             escpc="lagarto"
        if n==5:
             escpc="spock"
        print("Eu escolho %s"%escpc)
    if escpc=="tesoura" and (escus=="lagarto" or escus=="papel"):
        score_pc=score_pc+1
        score_us=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        if score_pc==3:
           print("Eu derrotei você, %s. Perdedor."%nome)
           break
        print("Eu venci!Vamos denovo.")
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
             escpc="pedra"
        if n==2:
             escpc="papel"
        if n==3:
             escpc="tesoura"
        if n==4:
             escpc="lagarto"
        if n==5:
             escpc="spock"
        print("Eu escolho %s"%escpc)
    if escpc=="lagarto" and (escus=="papel" or escus=="spock"):
        score_pc=score_pc+1
        score_us=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        if score_pc==3:
           print("Eu derrotei você, %s. Perdedor."%nome)
           break
        print("Eu venci!Vamos denovo.")
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
             escpc="pedra"
        if n==2:
             escpc="papel"
        if n==3:
             escpc="tesoura"
        if n==4:
             escpc="lagarto"
        if n==5:
             escpc="spock"
        print("Eu escolho %s"%escpc)
    if escpc=="lagarto" and (escus=="tesoura" or escus=="pedra"):
        score_us=score_us + 1
        score_pc=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        if score_us==3:
            print("Você me derrotou! Parabéns, %s"%nome)
            break
        print("Você venceu! Vamos denovo.") 
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
             escpc="pedra"
        if n==2:
             escpc="papel"
        if n==3:
             escpc="tesoura"
        if n==4:
             escpc="lagarto"
        if n==5:
             escpc="spock"
        print("Eu escolho %s"%escpc)
    if escpc=="spock" and (escus=="tesoura" or escus=="pedra"):
        score_pc=score_pc + 1
        score_us=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        if score_pc==3:
           print("Eu derrotei você, %s. Perdedor."%nome)
           break
        print("Eu venci!Vamos denovo.")
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
             escpc="pedra"
        if n==2:
             escpc="papel"
        if n==3:
             escpc="tesoura"
        if n==4:
             escpc="lagarto"
        if n==5:
             escpc="spock"
        print("Eu escolho %s"%escpc)
    if escpc=="spock" and (escus=="papel" or escus=="lagarto"):
        score_us=score_us + 1
        score_pc=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        if score_us==3:
            print("Você me derrotou! Parabéns, %s"%nome)
            break
        print("Você venceu! Vamos denovo.") 
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
             escpc="pedra"
        if n==2:
             escpc="papel"
        if n==3:
             escpc="tesoura"
        if n==4:
             escpc="lagarto"
        if n==5:
             escpc="spock"
        print("Eu escolho %s"%escpc)
    if escpc==escus:
        score_pc=0
        score_us=0
        print("Placar= PC %d X %d Usuario"%(score_pc,score_us))
        print("Empatou!Vamos denovo!")
        escus=str(input("Faça sua escolha:"))
        n=randint(1,5)               #escolha do pc
        if n==1:  
           escpc="pedra"
        if n==2:
           escpc="papel"
        if n==3:
           escpc="tesoura"
        if n==4:
           escpc="lagarto"
        if n==5:
           escpc="spock"
        print("Eu escolho %s"%escpc)
    

    
    


        
    

    
    