import numbers
import os
import re
import nltk
import numpy
from unidecode import unidecode
import re
import string
import numpy as np

#lendo o diretorio de documentos
dir_doc = r"C:/Users/G/Documents/SEMESTRE 2022/ORI/docs/"
os.chdir(dir_doc)

contador_docs = 0
for arq in os.listdir(dir_doc):
    if arq.endswith(".txt"):        #se os arquivos forem .txt eu conto
        contador_docs += 1
print("Quantidade de documentos do meu diretorio")
print(contador_docs, "\n")


#numero de documentos da minha coleção
N = contador_docs

aux1 = {}
def f_repetidos(lista):  #função que remove os repetidos
    li = []
    unique_list = [i for n, i in enumerate(lista) if i not in lista[n + 1:]]
    for unique_result in unique_list:
        li.append(unique_result)
    print("Resultado da lista de documentos sem repetidos" , "\n")
    return li

def f_remove_char(wd): #função que remove caracteres especiais
    wd = re.sub(r'W', ' ', wd)
    wd = re.sub('\'', ' ', wd)
    wd = ''.join(c for c in wd if c not in string.punctuation)
    wd = ''.join([c for c in wd if not c.isdigit()]).lower()
    return wd.split()

dic = dict() #dicionario dos documentos
doc2vocab = dict()
cont1 = []
cont2 = {}
docs = {}

#percorendo cada arquivo do meu diretorio
for arquivo in os.listdir():
    if arquivo.endswith(".txt"):
        file_path = f"{dir_doc}\{arquivo}"
        with open (file_path, 'r', encoding="utf8") as f:
            dicionario = f.read()
            dic[arquivo] = f_remove_char(dicionario)

#crio um vocabulario com as palavras com os valores zerados
with open("C:/Users/G/Documents/SEMESTRE 2022/ORI/TP2/vocab.txt", "r" , encoding="utf8") as f:
    vocabulario = {}
    for linha in f.readlines()[0:]:
        linha = linha.replace("\n", "")
        vocabulario[linha] = 0


for i in vocabulario:
    for chave, valor in dic.items():
        if i in valor:
            vocabulario[i] += 1         #contando quantas vezes cada palavra apareceu em cada documento

print("Valores de ni de cada palavra do vocabulario")
print(vocabulario)
print("\n")


#percorrendo meu dicionario de documentos
for keys, data in dic.items():
    doc2vocab.setdefault(keys,"0")
    for dado in data:
        if dado in vocabulario:
            cont1.append({keys:{dado:data.count(dado)}})
        else:
            cont1.append({keys: {dado: data.count(0)}})
        cont2 = cont1.copy()



item = 0

#variaveis para guardar o valor do tf e idf dos valores separadamente
aux_tf = []
list_tf = {}
aux_idf = {}


for item in f_repetidos(cont2):
   for chave, valor in item.items():
       for key, value in valor.items(): #percorro ele até entrar na primeira posição onde tem uma lista e cada valor é frequencia dos termos
           tf = (numpy.log2(value)) + 1   #calculo do tf
           print("doc" , chave)
           print("tf da palavra  " + key, end='  ')
           print("{:.2f}".format(tf))
           aux_tf.append({chave:{key:tf}})
   list_tf = aux_tf.copy()

print("\n")

#percorro meu vocabulario com os valores de ni
for key, value in vocabulario.items():
        if value > 0:
            aux = N / value
            idf = numpy.log2(aux)   #calculo o log da divisão de N por ni
            print("IDF da palavra  " + key, end='  ')
            print("{:.2f}".format(idf))
            aux_idf[key] = idf
        else:
            aux_idf[key] = 0


print("\n")
print("Valores de TF de cada documento\n")
print(list_tf)
print("\n")
print("Valores de IDF de cada documento\n")
print(aux_idf)


list_tfidf = []
aux_tdfidf = []
for chaves in list_tf:  #percorrendo o valores de Tf de cada documento
    tfidf = []
    for i, j in chaves.items(): #percorro cada documento
        for k , v in j.items():     #entro na chave e valor de cada documento
            aux_tdfidf = v * aux_idf[k]     #multiplico o valor do tf daquele k (termo) * o idf na posição do mesmo termo
            tfidf.append({k:aux_tdfidf})    #inserindo o termo e o valor calculado do tfidf dele
    list_tfidf.append({i:tfidf})    #inserindo o documento daquele termo e o calculo

print("\n")
print("TDF X IDF dos documentos")
for indice in list_tfidf:
        print(indice)












