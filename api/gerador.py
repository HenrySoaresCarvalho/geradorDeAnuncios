from template import template
class Gerador():
    def __init__(self,nome):
        self.nome = nome
        self.template = template

    def gerar(self,anuncios):
        temp = ""
        for i in anuncios:
            temp = "•"+i["desc"] + "\n    " + temp
        
        arq=''
        for i in anuncios:
            arq = str(template(i['desc'],temp,i['sku'],i['pos'],i['comp'],i['larg'],i['alt'])) + "\n\n ======================================= \n\n" + str(arq)
            with open(self.nome,'w') as file:
                file.write(arq)

        