from graphics import *
import time
import random
import pygame
import sys
from pygame.mixer import Sound

pygame.init()
ranking = open("ranking.txt", "a+")

print("Jogo: Ball vs Block")

###variaveis #
name = []
variavel = 0
vida = 0

tocar = 3
tocar2 = 3


verificar = True

c1 = True  #TRUE na primeria vez
c2 = True   #TRUE na primeira vez
c3 = True #True ever

ponto_pontoX = 0
ponto_pontoY = 0

### Checar destruicão dos blocos
checar_bloco1 = 0
checar_bloco2 = 0
checar_bloco3 = 0
checar_bloco4 = 0
checar_bloco5 = 0

vida_tela = 0

movimento = 0



tempo = 0.09

### BLOCOS MOVIMENTOS

velocidade_descidax = 0
velocidade_desciday = 5

vel_desc = 5

##ponto

pont=0


if True:

    tela1 = GraphWin("Start",300,450)
    tela1.setBackground("white")

    VS = Image(Point(150,120),"vs.png")
    VS.draw(tela1)

    SNAKE = Text(Point(95,35),"BALL")
    SNAKE.setSize(22)
    SNAKE.setOutline("black")
    SNAKE.setStyle("bold italic")
    SNAKE.draw(tela1)

    BLOCK = Text(Point(185,220),"BLOCK")
    BLOCK.setSize(22)
    BLOCK.setOutline("black")
    BLOCK.setStyle("bold italic")
    BLOCK.draw(tela1)

    START = Text(Point(150,300),"COMEÇAR")
    START.setSize(22)
    START.setOutline("black")
    START.draw(tela1)

    INST = Text(Point(150,370),"INSTRUÇÕES")
    INST.setSize(22)
    INST.setOutline("black")
    INST.draw(tela1)

    clique = tela1.getMouse()
    cliquex = clique.getX()
    cliquey = clique.getY()
    iniciar = 0



    ##Checa pra ver se clicou certo.
    if ( (cliquex > 0 and cliquex < 300) and (cliquey > 0 and cliquey < 265) )  or  ( ( (cliquex >0 and cliquex < 55) or (cliquex >245 and cliquex <300)) and (cliquey >265 and cliquey<345) )  or (   ((cliquex > 0 and cliquex < 45) or (cliquex > 255 and cliquex <300)) and (cliquey > 346 and cliquey < 385)) or ((cliquex >0 and cliquex < 300)  and (cliquey > 385 and cliquey <450)) :
        clique = tela1.getMouse()
        cliquex = clique.getX()
        cliquey = clique.getY()
    ##Tela Instruções
    if (cliquex > 45 and cliquex < 255) and ((cliquey > 346 and cliquey < 385)):
        print("Instruções")
        START.undraw()
        BLOCK.undraw()
        SNAKE.undraw()
        VS.undraw()
        tela1.close()  ##### Fecha janela START #

        Instruções = GraphWin("Ball VS Block: Instruções",300,500)
        Instruções.setBackground("black")

        I1 = Text(Point(150,50),"Instruções:")
        I1.setSize(22)
        I1.setOutline("white")
        I1.setStyle("italic")
        I1.draw(Instruções)

        I2 = Text(Point(150,150),"O objetivo do jogo é destuir o\nbloco com menor valor.  Use \nas teclas Direita e Esquerda\n para se mover.")
        I2.setOutline("white")
        I2.setSize(13)
        I2.draw(Instruções)

        I3 = Text(Point(150,275),"A velocidade aumenta de acordo\n com a vida e/ou tempo de jogo.")
        I3.setOutline("white")
        I3.setSize(13)
        I3.draw(Instruções)

        I4 = Text(Point(150,350),"Teclas Q e W alteram musicas.\nTecla E pausa a musica.")
        I4.setOutline("white")
        I4.setSize(13)
        I4.draw(Instruções)

        START = Text(Point(150,450),"COMEÇAR")
        START.setSize(22)
        START.setOutline("white")
        START.draw(Instruções)

        clique = Instruções.getMouse()
        cliquex = clique.getX()
        cliquey = clique.getY()
        iniciar = 1
        print(cliquex, cliquey)

        if ((cliquex>0 and cliquex <300) and (cliquey > 0 and cliquey < 432)) or ( (cliquex > 0 and cliquex<300) and (cliquey >466 and cliquey <500)) or (   ((cliquex > 0 and cliquex <72) or (cliquex >230 and cliquex < 300))  and ( cliquey >432 and cliquey <466)):
            clique = Instruções.getMouse()
            cliquex = clique.getX()
            cliquey = clique.getY()

        ## Tela Jogo
    if ((cliquex > 55 and cliquex < 245) and (cliquey > 265 and cliquey < 345)) or ((cliquex > 72 and cliquex < 230) and (cliquey > 432 and cliquey < 466)):
        if iniciar != 1:        
            print("s/ instr")
            START.undraw()
            BLOCK.undraw()
            SNAKE.undraw()
            VS.undraw()
            tela1.close()
        if iniciar == 1:
            print("c/ instr")
            START.undraw()
            I1.undraw()
            I2.undraw()
            I3.undraw()
            I4.undraw()
            Instruções.close()

        Jogo = GraphWin("Ball VS Block",300,450)
        Jogo.setBackground("black")
        Jogo.ligar_Buffer()

        while True:
            Jogo.flush()
            Jogo.update()
            movimento += 1

            if c1 == True:
                #### Blocos aparecem ####
                ##################### BLOCO 1 #####################################
                bloco1 = Rectangle(Point(0,10),Point(55,65))
                num_color = random.randint(1,5)
                if num_color == 1:
                    color = ("blue")
                elif num_color == 2:
                    color = ("green")
                elif num_color == 3:
                    color = ("red")
                elif num_color == 4:
                    color = ("yellow")
                else:
                    color = ("white")
                bloco1.setFill(color)
                bloco1.draw(Jogo)
                if vida >= 0 and vida <= 15:   
                    power1 = random.randint(1,5)       
                if vida > 16:
                    power1 = random.randint(5,10)

                if power1 == 0:
                    if vida >= 0 and vida <= 15:   
                        power1 = random.randint(1,5)       
                    if vida > 16:
                        power1 = random.randint(5,10)

                power_in_bloco1 = Text(Point(27.5,37.5),str(power1))
                power_in_bloco1.setOutline("black")
                power_in_bloco1.setStyle("bold")
                power_in_bloco1.setSize(14)
                power_in_bloco1.draw(Jogo)

                power_in_bloco11 = Text(Point(27.5,15),str(power1))
                power_in_bloco11.setOutline("White")
                power_in_bloco11.setStyle("bold")
                power_in_bloco11.setSize(14)
                power_in_bloco11.draw(Jogo)

                    ##################### BLOCO 2 #####################################
                bloco2 = Rectangle(Point(60,10),Point(115,65))
                num_color = random.randint(1,5)
                if num_color == 1:
                    color = ("blue")
                elif num_color == 2:
                    color = ("green")
                elif num_color == 3:
                    color = ("red")
                elif num_color == 4:
                    color = ("yellow")
                else:
                    color = ("white")
                bloco2.setFill(color)
                bloco2.draw(Jogo)                
                if vida >= 0 and vida <= 15:   
                    power2 = random.randint(1,5)       
                if vida > 16:
                    power2 = random.randint(5,10)    

                if power2 == 0:
                    if vida >= 0 and vida <= 15:   
                        power2 = random.randint(1,5)       
                    if vida > 16:
                        power2 = random.randint(5,10)
                power_in_bloco2 = Text(Point(87.5,37.5),str(power2))
                power_in_bloco2.setOutline("black")
                power_in_bloco2.setStyle("bold")
                power_in_bloco2.setSize(14)
                power_in_bloco2.draw(Jogo)

                power_in_bloco22 = Text(Point(87.5,15),str(power2))
                power_in_bloco22.setOutline("white")
                power_in_bloco22.setStyle("bold")
                power_in_bloco22.setSize(14)
                power_in_bloco22.draw(Jogo)

                ##################### BLOCO 3 #####################################
                bloco3 = Rectangle(Point(120,10),Point(175,65))
                num_color = random.randint(1,5)
                if num_color == 1:
                    color = ("blue")
                elif num_color == 2:
                    color = ("green")
                elif num_color == 3:
                    color = ("red")
                elif num_color == 4:
                    color = ("yellow")
                else:
                    color = ("white")
                bloco3.setFill(color)
                bloco3.draw(Jogo)     
                if vida >= 0 and vida <= 15:   
                    power3 = random.randint(1,5)       
                if vida > 16:
                    power3 = random.randint(5,10)  
                if power3 == 0:
                    if vida >= 0 and vida <= 15:   
                        power3 = random.randint(1,5)       
                    if vida > 16:
                        power3 = random.randint(5,10)   
                power_in_bloco3 = Text(Point(147.5,37.5),str(power3))
                power_in_bloco3.setOutline("black")
                power_in_bloco3.setStyle("bold")
                power_in_bloco3.setSize(14)
                power_in_bloco3.draw(Jogo)

                power_in_bloco33 = Text(Point(147.5,15),str(power3))
                power_in_bloco33.setOutline("white")
                power_in_bloco33.setStyle("bold")
                power_in_bloco33.setSize(14)
                power_in_bloco33.draw(Jogo)

                ##################### BLOCO 4 #####################################
                bloco4 = Rectangle(Point(180,10),Point(235,65))
                num_color = random.randint(1,5)
                if num_color == 1:
                    color = ("blue")
                elif num_color == 2:
                    color = ("green")
                elif num_color == 3:
                    color = ("red")
                elif num_color == 4:
                    color = ("yellow")
                else:
                    color = ("white")
                bloco4.setFill(color)
                bloco4.draw(Jogo)                
                if vida >= 0 and vida <= 15:   
                    power4 = random.randint(1,5)       
                if vida > 16:
                    power4 = random.randint(5,10) 
                if power4 == 0:
                    if vida >= 0 and vida <= 15:   
                        power4 = random.randint(1,5)       
                    if vida > 16:
                        power4 = random.randint(5,10)
                power_in_bloco4 = Text(Point(207.5,37.5),str(power4))
                power_in_bloco4.setOutline("black")
                power_in_bloco4.setStyle("bold")
                power_in_bloco4.setSize(14)
                power_in_bloco4.draw(Jogo)

                power_in_bloco44 = Text(Point(207.5,15),str(power4))
                power_in_bloco44.setOutline("white")
                power_in_bloco44.setStyle("bold")
                power_in_bloco44.setSize(14)
                power_in_bloco44.draw(Jogo)

                ##################### BLOCO 5 #####################################
                bloco5 = Rectangle(Point(240,10),Point(295,65))
                num_color = random.randint(1,5)
                if num_color == 1:
                    color = ("blue")
                elif num_color == 2:
                    color = ("green")
                elif num_color == 3:
                    color = ("red")
                elif num_color == 4:
                    color = ("yellow")
                else:
                    color = ("white")
                bloco5.setFill(color)
                bloco5.draw(Jogo)
                if vida >= 0 and vida <= 15:   
                    power5 = random.randint(1,5)       
                if vida > 16:
                    power5 = random.randint(5,10) 
                if power5 == 0:
                    if vida >= 0 and vida <= 15:   
                        power5 = random.randint(1,5)       
                    if vida > 16:
                        power5 = random.randint(5,10) 

                power_in_bloco5 = Text(Point(267.5,37.5),str(power5))
                power_in_bloco5.setOutline("black")
                power_in_bloco5.setStyle("bold")
                power_in_bloco5.setSize(14)
                power_in_bloco5.draw(Jogo)

                power_in_bloco55 = Text(Point(267.5,15),str(power5))
                power_in_bloco55.setOutline("white")
                power_in_bloco55.setStyle("bold")
                power_in_bloco55.setSize(14)
                power_in_bloco55.draw(Jogo)

                checar_bloco1 = 0
                checar_bloco2 = 0
                checar_bloco3 = 0
                checar_bloco4 = 0
                checar_bloco5 = 0

                c1 = False
            
            if c2 == True:
                ### "VIDA" ##
                vida = 5
                vd = Text(Point(150,430),"Vidas: "+str(vida))
                vd.setOutline("white")
                vd.draw(Jogo)

                #### "BOLA" ###
                cabeça = Circle(Point(150,300),10)
                cabeça.setFill("white")
                cabeça.draw(Jogo)
                local_cabeca_X = cabeça.getCenter().getX()
                local_cabeca_Y = cabeça.getCenter().getY()

                c2 = False

            print("Pontuacao:"+str(pont))

            tecla = Jogo.checkKey_Buffer()
            update()
            if len(tecla) > 0 and "Right" in tecla:
                if local_cabeca_X >= 290:
                    cabeça.move(0,0)
                else:
                    cabeça.move(10,0)

            if len(tecla) > 0 and "Left" in tecla:
                if local_cabeca_X <= 10:
                    cabeça.move(0,0)
                else:
                    cabeça.move(-10,0)
                
            if len(tecla) > 0 and "q" in tecla:
                if tocar2 == 1:
                    pygame.mixer.pause()                
                audio = pygame.mixer.Sound("musica1.wav")
                audio.play()
                tocar = 1
            
            if len(tecla) > 0 and "w" in tecla:
                if tocar == 1:
                    pygame.mixer.pause()                
                audio = pygame.mixer.Sound("musica2.wav")
                audio.play()
                tocar2 = 1

            if len(tecla) > 0 and "e" in tecla:
                pygame.mixer.pause()                

            if c3 == True: ### MOVIMENTOS DOS BLOCOS E PEGA LOCAL DELES#####
                bloco1.move(velocidade_descidax,velocidade_desciday)
                power_in_bloco1.move(velocidade_descidax,velocidade_desciday)

                bloco2.move(velocidade_descidax,velocidade_desciday)
                power_in_bloco2.move(velocidade_descidax,velocidade_desciday)

                bloco3.move(velocidade_descidax,velocidade_desciday)
                power_in_bloco3.move(velocidade_descidax,velocidade_desciday)

                bloco4.move(velocidade_descidax,velocidade_desciday)
                power_in_bloco4.move(velocidade_descidax,velocidade_desciday)

                bloco5.move(velocidade_descidax,velocidade_desciday)
                power_in_bloco5.move(velocidade_descidax,velocidade_desciday)

                localBloco1Y = bloco1.getCenter().getY()
                localBloco2Y = bloco2.getCenter().getY()
                localBloco3Y = bloco3.getCenter().getY()
                localBloco4Y = bloco4.getCenter().getY()
                localBloco5Y = bloco5.getCenter().getY()

            local_cabeca_X = cabeça.getCenter().getX() #LOCAL DA CABECA##
            time.sleep(tempo)  ##???????????????##

            if localBloco1Y and localBloco2Y and localBloco3Y and localBloco4Y and localBloco5Y >= 390: ### SE BLOCOS SAIREM DA TELA APAGA E INICA C1 NOVAMENTE, PARA QUE SEJAM DESENHANOS DNV########### 
                bloco1.undraw()
                power_in_bloco1.undraw()
                power_in_bloco11.undraw()

                bloco2.undraw()
                power_in_bloco2.undraw()
                power_in_bloco22.undraw()

                bloco3.undraw()
                power_in_bloco3.undraw()
                power_in_bloco33.undraw()

                bloco4.undraw()
                power_in_bloco4.undraw()
                power_in_bloco44.undraw()

                bloco5.undraw()
                power_in_bloco5.undraw()
                power_in_bloco55.undraw()

                c1 = True

            ## Checa posicão do bloco, da cobra; Vê se bloco do lado já foi destruido.  Caso sim, desconsidera, caso não destroi bloco e soma pontuaćão. DA GAME OVER.
            ## BLOCO 1 ##
            if (localBloco1Y >= 260.5 and localBloco1Y <= 275.5) and (local_cabeca_X >= 0 and local_cabeca_X <= 55) and (checar_bloco2 == 0):
                if vida >= power1:
                    vida = vida - power1
                    vd.setText("Vidas: "+str(vida))
                    bloco1.undraw()
                    power_in_bloco1.undraw()
                    pont = pont + power1
                    power1 = 0
                    checar_bloco1 = 1
                    power_in_bloco11.undraw()
                
                if vida < power1:
                    vida = vida - power1
                    vd.setText("Vidas: "+str(vida))
                    fim = Text(Point(150,215),"Game Over")
                    fim.setOutline("white")
                    fim.setStyle("bold")
                    fim.setSize(20)
                    fim.draw(Jogo)


             ## BLOCO 2 ##
            ## BLOCO 2 ##
            if (localBloco2Y >= 260.5 and localBloco2Y <= 275.5) and (local_cabeca_X >= 60 and local_cabeca_X <= 115) and (checar_bloco1 == 0 and checar_bloco3 == 0):
                if vida >= power2:
                    vida = vida - power2
                    vd.setText("Vidas: "+str(vida))
                    bloco2.undraw()
                    power_in_bloco2.undraw()
                    power_in_bloco22.undraw()
                    pont = pont + power2
                    power2 = 0
                    checar_bloco2 = 1

                if vida < power2:
                    vida = vida - power2
                    vd.setText("Vidas: "+str(vida))
                    fim = Text(Point(150,215),"Game Over")
                    fim.setOutline("white")
                    fim.setStyle("bold")
                    fim.setSize(20)
                    fim.draw(Jogo)
            ## BLOCO 3 ##
            if (localBloco3Y >= 260.5 and localBloco3Y <= 275.5) and (local_cabeca_X >= 120 and local_cabeca_X <= 175) and (checar_bloco2 == 0 and checar_bloco4 == 0):
                if vida >= power3:
                    vida = vida - power3
                    vd.setText("Vidas: "+str(vida))
                    bloco3.undraw()
                    power_in_bloco3.undraw()
                    power_in_bloco33.undraw()
                    pont = pont + power3
                    power3 = 0
                    checar_bloco3 = 1

                if vida < power3:
                    vida = vida - power3
                    vd.setText("Vidas: "+str(vida))
                    fim = Text(Point(150,215),"Game Over")
                    fim.setOutline("white")
                    fim.setStyle("bold")
                    fim.setSize(20)
                    fim.draw(Jogo)
            ## BLOCO 4 ##
            if (localBloco4Y >= 260.5 and localBloco4Y <= 275.5) and (local_cabeca_X >= 180 and local_cabeca_X <= 235) and (checar_bloco3 == 0 and checar_bloco5 == 0):
                if vida >= power4:
                    vida = vida - power4
                    vd.setText("Vidas: "+str(vida))
                    bloco4.undraw()
                    power_in_bloco4.undraw()
                    power_in_bloco44.undraw()
                    pont = pont + power4
                    power4 = 0
                    checar_bloco4 = 1

                if vida < power4:
                    vida = vida - power4
                    vd.setText("Vidas: "+str(vida))
                    fim = Text(Point(150,215),"Game Over")
                    fim.setOutline("white")
                    fim.setStyle("bold")
                    fim.setSize(20)
                    fim.draw(Jogo)
            ## BLOCO 5 ##
            if (localBloco5Y >= 260.5 and localBloco5Y <= 275.5) and (local_cabeca_X >= 240 and local_cabeca_X <= 300) and (checar_bloco4 == 0):
                if vida >= power5:
                    vida = vida - power5
                    vd.setText("Vidas: "+str(vida))
                    bloco5.undraw()
                    power_in_bloco5.undraw()
                    power_in_bloco55.undraw()
                    pont = pont + power5
                    power5 = 0
                    checar_bloco5 = 1
                    

                if vida < power5:
                    vida = vida - power5
                    vd.setText("Vidas: "+str(vida))
                    fim = Text(Point(150,215),"Game Over")
                    fim.setOutline("white")
                    fim.setStyle("bold")
                    fim.setSize(20)
                    fim.draw(Jogo)
                   
                    
            if vida < 0:
                c = Text(Point(150,170),"Pontuacão: "+str(pont))
                c.setOutline("white")
                c.setStyle("bold")
                c.setSize(20)
                c.draw(Jogo)
                time.sleep(1.5)
                Jogo.desligar_Buffer()
                Jogo.close()

                salvar = GraphWin("Snake VS Block - Salvar Pontuaćão",300,450)
                salvar.setBackground("black")
                c = Text(Point(150,50),"Pontuacão: "+str(pont))
                c.setOutline("white")
                c.setStyle("bold")
                c.setSize(20)
                c.draw(salvar)

                I1 = Text(Point(150,150),"Digite seu nome:")
                I1.setSize(20)
                I1.setOutline("white")
                I1.setStyle("italic")
                I1.draw(salvar)

                I2 = Text(Point(150,185),"No fim, clique Enter para confirmar.")
                I2.setSize(13)
                I2.setOutline("white")
                I2.setStyle("italic")
                I2.draw(salvar)

                tecla = salvar.getKey()
                name.append(tecla)
                x = 80
                while tecla != "Return":
                    Nome = Text(Point(x,215),tecla)
                    Nome.setSize(25)
                    Nome.setOutline("white")
                    Nome.setStyle("italic")
                    Nome.draw(salvar)
                    x += 15
                    tecla = salvar.getKey()                        
                    if tecla == "space":
                        tecla = "_"
                    if tecla == "BackSpace":
                        Nome.undraw()
                        x += -30
                        tecla = ""
                        name.pop()
                    if tecla != "Return":
                        name.append(tecla)
                        if tecla == "":
                            name.pop()
                print(name)
                ranking.write("\nNome: " + str(name) + "/ Pontuacão: "+str(pont)+"\n")

                rec = Text(Point(150,300), "Jogar Novamente? (Y/N)")
                rec.setSize(18)
                rec.setOutline("white")
                rec.setStyle("italic")
                rec.draw(salvar)
                restart = salvar.getKey()

                if restart == "y" or restart == "Y" :
                    I1.undraw()
                    I2.undraw()
                    Nome.undraw()
                    rec.undraw()
                    salvar.close()


                    time.sleep(1)
                    pont = 0
                    movimento = 0

                    fim.undraw()
                    c.undraw()
                    vd.undraw()
                    bloco1.undraw()
                    power_in_bloco1.undraw()
                    power_in_bloco11.undraw()
                    bloco2.undraw()
                    power_in_bloco2.undraw()
                    power_in_bloco22.undraw()
                    bloco3.undraw()
                    power_in_bloco3.undraw()
                    power_in_bloco33.undraw()
                    bloco4.undraw()
                    power_in_bloco4.undraw()
                    power_in_bloco44.undraw()
                    bloco5.undraw()
                    power_in_bloco5.undraw()
                    power_in_bloco55.undraw()

                    checar_bloco1 = 0
                    checar_bloco2 = 0
                    checar_bloco3 = 0
                    checar_bloco4 = 0
                    checar_bloco5 = 0

                    name = []


                    cabeça.undraw()
                    c1 = True
                    c2 = True
                    pygame.mixer.pause()

                    Jogo = GraphWin("Snake VS Block",300,450)
                    Jogo.setBackground("black")
                    Jogo.ligar_Buffer()

                if restart == "n" or restart == "N":
                    sys.exit()

            if checar_bloco1 or checar_bloco2 or checar_bloco3 or checar_bloco4 or checar_bloco5 == 1:
                if vida_tela == 0:
                    x = random.randint(10,290)
                    y = random.randint(50,80)
                    c = Circle(Point(x,y),15)
                    c.setFill("#993399")
                    c.draw(Jogo)
                    p = random.randint(1,5)
                    t = Text(Point(x,y),str(p))
                    t.draw(Jogo)

                    vida_tela = 1

                    
            if vida_tela == 1:
                c.move(0,vel_desc)
                t.move(0,vel_desc)
                ponto_pontoX = c.getCenter().getX()
                ponto_pontoY = c.getCenter().getY()
                
                local_cabeca_X_1 = local_cabeca_X - 12
                local_cabeca_X_2 = local_cabeca_X + 12

                local_cabeca_Y_1 = local_cabeca_Y - 14
                local_cabeca_Y_2 = local_cabeca_Y + 14


                if (local_cabeca_X_1 <= ponto_pontoX and ponto_pontoX <= local_cabeca_X_2) and (local_cabeca_Y_1 <= ponto_pontoY and ponto_pontoY <= local_cabeca_Y_2):
                    vida = vida + p
                    vd.setText("Vidas: "+str(vida))
                    c.undraw()
                    t.undraw()
                    vida_tela = 0

                if ponto_pontoY > 390:
                    c.undraw()
                    t.undraw()
                    vida_tela = 0

            if movimento <=60:
                tempo = 0.09
                velocidade_desciday = 5
                vel_desc = 5
            if movimento >= 61 and movimento <= 150:
                tempo = 0.08
                velocidade_desciday = 6
                vel_desc = 6
            if movimento >= 151 and movimento <= 220:
                tempo = 0.07
                velocidade_desciday = 7
                vel_desc = 7
            if movimento >= 221 and movimento <= 280:
                tempo = 0.06
                velocidade_desciday = 8
                vel_desc = 8
            if movimento >= 281 and movimento < 499:
                tempo = 0.05
                velocidade_desciday = 9
                vel_desc = 9
            if movimento >=500 and movimento < 999:
                tempo = 0.04
                velocidade_desciday = 11
                vel_desc = 11
            if movimento >= 1000:
                tempo = 0.04
                velocidade_desciday = 13
                vel_desc = 13