#este programa devera extrair informaçoes  Faça um Banco de dados:
#Conjunto de registros armazenados em um arquivo
##-localização
##-edição

#extração de informações:
#-listagens (que satisfaçam algum critério)
#-informações globais(menor,maior,média,quantidades)

##por nome
##leitura de arquivo
#escrita de arquivo

#Tudo isso dentro de funções.
#Para entregar no CEAD até o dia 28/03
def quantidades():#le a quantidade de alunos
    arquivo=input("insira o nome do arquivo")
    newfile=open(arquivo +'.txt','r')
    lines=newfile.readlines()
    print(len(lines))
def nomesdosalunos():#le o nome dos alunos
    list=[]
    completlist=[]
    arquivo=input("insira o nome do arquivo")#le o arquivo
    newfile=open(arquivo +'.txt','r')
    lines=newfile.readlines()
    for i in range(len(lines)):#retira o \n da string com o rstrip function
        list.append(lines[i].rstrip('\n'))
        completlist.append(list[i].split(','))

    for y in range(len(completlist)):#le o arquivo em posiçao de forma de matriz
        print(completlist[y][0])
def maiormedia():
    todasmedias=[]
    list=[]
    completlist=[]
    arquivo=input("insira o nome do arquivo")#le o arquivo
    newfile=open(arquivo +'.txt','r')
    lines=newfile.readlines()
    for i in range(len(lines)):#retira o \n da string com o rstrip function
        list.append(lines[i].rstrip('\n'))
        completlist.append(list[i].split(','))
    for i in range(len(completlist)):#o for percorre a completilist que e a lista com todoas a as medias e so percorre aonde fica somente as notas e faz as medias
        todasmedias.append((float(completlist[i][1])+float(completlist[i][2]))/2)
    maior=todasmedias[0]
    for i in todasmedias:#da a maior media
        if maior<i:
            maior=i
            melhoraluno=todasmedias.index(maior)
    print('O Aluno com maior nota é  '+ completlist[melhoraluno][0] +' com a média : ' , maior)

def menormedia():
    todasmedias=[]
    list=[]
    completlist=[]
    arquivo=input("insira o nome do arquivo")#le o arquivo
    newfile=open(arquivo +'.txt','r')
    lines=newfile.readlines()
    for i in range(len(lines)):#retira o \n da string com o rstrip function
        list.append(lines[i].rstrip('\n'))
        completlist.append(list[i].split(','))
    for i in range(len(completlist)):#o for percorre a completilist que e a lista com todoas a as medias e so percorre aonde fica somente as notas e faz as medias
        todasmedias.append((float(completlist[i][1])+float(completlist[i][2]))/2)
    menor=todasmedias[0]
    for i in todasmedias:# da a menor media
        if menor>i:
            menor=i
            melhoraluno=todasmedias.index(menor)
    print('O Aluno com menor nota é  '+ completlist[melhoraluno][0] +' com a média : ' , menor)

def alunoespecifico():
    list=[]
    completlist=[]
    arquivo=input("insira o nome do arquivo")#le o arquivo
    newfile=open(arquivo +'.txt','r')
    lines=newfile.readlines()
    for i in range(len(lines)):#retira o \n da string com o rstrip function
        list.append(lines[i].rstrip('\n'))
        completlist.append(list[i].split(','))
    name= str(input('Insira o nome do aluno desejado'))
    for i in range(len(completlist)):
        if completlist[i][0]==name:
            print('O aluno',completlist[i][0],'possui a media com',(float(completlist[i][1])+float(completlist[i][2]))/2)
def newfiles():#cria um novo arquivo

    nomeArquivo = input('Digite o nome do arquivo que deseja criar:')
    novo=open(nomeArquivo+'.txt','w')
    novo.close()
def escreverarquivo():
    nome=str(input('digite o nome'))
    nota1=str(input('digite a nota1'))
    nota2=str(input('digite a nota 2'))
    arquivo=input("insira o nome do arquivo")#le o arquivo
    newfile=open(arquivo +'.txt','a')
    newfile.write(nome+','+nota1+','+nota2+'\n')

def alterarinformaçao():
    list=[]
    completlist=[]
    name=str(input('digite o nome do aluno desejado que queira alterar '))
    arquivo=input("insira o nome do arquivo")#le o arquivo
    newfile=open(arquivo +'.txt','r+')
    lines=newfile.readlines()
    for i in range(len(lines)):#retira o \n da string com o rstrip function
        list.append(lines[i].rstrip('\n'))
        completlist.append(list[i].split(','))
    for i in range(len(completlist)):
        if completlist[i][0]==name:
            completlist[i][1]=str(input('altere a nota1'))
            completlist[i][2]=str(input('altera a nota2'))
    for i in range(len(completlist)):
        newfile.write(completlist[i],"")









print('Trabalho de programaçao')
print("1- NOMES DOS ALUNOS;2-MAIOR MEDIA;3-MENOR MEDIA;4-ENCONTRAR ALUNO E MEDIA ;(EXTRAIR INFORMAÇOES")
print("(OPERAÇOES):5- NOVO ARQUIVO;6-PREECHER ARQUIVO,7- EDITAR AS INFORMAÇOES DO ALUNO;8-ORDENAR EM ORDEM ALFABETICA")
print("0-SAIR DO PROGRAMA")
aviso="INSIRA A OPÇAO "
escolha=(int(input(aviso)))
while escolha!=0:
    if escolha==1:
        nomesdosalunos()
    elif escolha==2:
        maiormedia()
    elif escolha==3:
        menormedia()
    elif escolha==4:
        alunoespecifico()
    elif escolha==5:
        newfiles()
    else:
        print("funçao desconhecida")
    escolha=int(input(aviso))

