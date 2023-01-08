import numbers
import os
import re
import nltk
import numpy
from unidecode import unidecode
import re
import string
import numpy as np

def fun_letra_A():

    diretorio = r"C:/Users/G/Documents/SEMESTRE 2022/ORI/hinos"   #insira aqui os vocabularios dos hinos
    os.chdir(diretorio)

    #função que remove os repetidos da lista
    def fun_remove_repetidos(vet):
        li = []
        for i in vet:
            if i not in li:
                li.append(i)
        li.sort()
        return li

    #função que coloca letrar em minusculo
    def fun_lower(frase):
        vet2 = []
        for i in frase:
            for j in i:
                vet2.append(unidecode(j).lower())
        return vet2

    def fun_car(frase):
        vet = []
        for i in frase:
            vet.append(i.replace(",", " ").replace(
                ".", " ").replace("\n", " ").replace("´"," ").replace("?"," ").replace("!"," ").replace("]"," ").replace("("," ").replace(")"," ").split())
        return fun_lower(vet)

    w = []

    #lendo todos os arquivos .txt do diretorio
    for arquivo in os.listdir():
        if arquivo.endswith(".txt"):
            file_path = f"{diretorio}\{arquivo}"
            with open(file_path, "r", encoding="utf8") as f:
                w.extend(f.readlines())

    #função que retira os carcteres especiais do arquivo e coloca as letras minusculas
    list = fun_car(w)

    #3) Grave o vocabulário em arquivo texto
    with open("C:/Users/G/Documents/SEMESTRE 2022/ORI/TP2_Géssica_Santos/vocab_hinos.txt", "w" , encoding="utf8") as f:
        vocabulario = fun_remove_repetidos(list)
        for i in vocabulario:
            print(i, file=f)


    print(vocabulario, "for debug - vocabulário  \n")
    print("\n")
    tam = len(vocabulario)
    print("Tamanho do vocabulario do documento é.." , tam)
    print("\n")

def fun_letra_B():
    # lendo o diretorio de documentos
    dir_doc = r"C:/Users/G/Documents/SEMESTRE 2022/ORI/hinos"   #inisra aqui o vocabulario dos hinos
    os.chdir(dir_doc)

    contador_docs = 0
    for arq in os.listdir(dir_doc):
        if arq.endswith(".txt"):  # se os arquivos forem .txt eu conto
            contador_docs += 1
    print("Quantidade de documentos do meu diretorio")
    print(contador_docs, "\n")

    # numero de documentos da minha coleção
    N = contador_docs

    aux1 = {}

    def f_repetidos(lista):  # função que remove os repetidos
        li = []
        unique_list = [i for n, i in enumerate(lista) if i not in lista[n + 1:]]
        for unique_result in unique_list:
            li.append(unique_result)
        print("Resultado da lista de documentos sem repetidos", "\n")
        return li

    def f_remove_char(wd):  # função que remove caracteres especiais
        wd = re.sub(r'W', ' ', wd)
        wd = re.sub('\'', ' ', wd)
        wd = ''.join(c for c in wd if c not in string.punctuation)
        wd = ''.join([c for c in wd if not c.isdigit()]).lower()
        return wd.split()

    dic = dict()  # dicionario dos documentos
    doc2vocab = dict()
    cont1 = []
    cont2 = {}
    docs = {}

    # percorendo cada arquivo do meu diretorio
    for arquivo in os.listdir():
        if arquivo.endswith(".txt"):
            file_path = f"{dir_doc}\{arquivo}"
            with open(file_path, 'r', encoding="utf8") as f:
                dicionario = f.read()
                dic[arquivo] = f_remove_char(dicionario)

    # crio um vocabulario com as palavras com os valores zerados
    with open("C:/Users/G/Documents/SEMESTRE 2022/ORI/vocab_hinos.txt", "r", encoding="utf8") as f:   #insira aqui o nome do vocabulario dos hinos
        vocabulario = {}
        for linha in f.readlines()[0:]:
            linha = linha.replace("\n", "")
            vocabulario[linha] = 0

    for i in vocabulario:
        for chave, valor in dic.items():
            if i in valor:
                vocabulario[i] += 1  # contando quantas vezes cada palavra apareceu em cada documento

    print("Valores de ni de cada palavra do vocabulario")
    print(vocabulario)
    print("\n")

    # percorrendo meu dicionario de documentos
    for keys, data in dic.items():
        doc2vocab.setdefault(keys, "0")
        for dado in data:
            if dado in vocabulario:
                cont1.append({keys: {dado: data.count(dado)}})
            else:
                cont1.append({keys: {dado: data.count(0)}})
            cont2 = cont1.copy()

    item = 0

    # variaveis para guardar o valor do tf e idf dos valores separadamente
    aux_tf = []
    list_tf = {}
    aux_idf = {}

    for item in f_repetidos(cont2):
        for chave, valor in item.items():
            for key, value in valor.items():  # percorro ele até entrar na primeira posição onde tem uma lista e cada valor é frequencia dos termos
                if value > 0:
                    tf = (numpy.log2(value)) + 1  # calculo do tf
                    print("doc", chave)
                    print("tf da palavra  " + key, end='  ')
                    print("{:.2f}".format(tf))
                    aux_tf.append({chave: {key: tf}})
                else:
                    aux_tf.append({chave: {key: 0}})
        list_tf = aux_tf.copy()

    print("\n")

    # percorro meu vocabulario com os valores de ni
    for key, value in vocabulario.items():
        if value > 0:
            aux = N / value
            idf = numpy.log2(aux)  # calculo o log da divisão de N por ni
            print("IDF da palavra  " + key, end='  ')
            print("{:.2f}".format(idf))
            aux_idf[key] = idf
        else:
            aux_idf[key] = 0

    print("\n")
    print("Valores de TF de cada documento\n")
    #print(list_tf)
    print("\n")
    print("Valores de IDF de cada documento\n")
    #print(aux_idf)

    list_tfidf = []
    aux_tdfidf = []
    for chaves in list_tf:  # percorrendo o valores de Tf de cada documento
        tfidf = []
        for i, j in chaves.items():  # percorro cada documento
            for k, v in j.items():  # entro na chave e valor de cada documento
                if v > 0 :
                    aux_tdfidf = v * aux_idf[k]  # multiplico o valor do tf daquele k (termo) * o idf na posição do mesmo termo
                    tfidf.append({k: aux_tdfidf})  # inserindo o termo e o valor calculado do tfidf dele
                else:
                    tfidf.append({k: 0})
        list_tfidf.append({i: tfidf})  # inserindo o documento daquele termo e o calculo

    with open("C:/Users/G/Documents/SEMESTRE 2022/ORI/tdf_idf_hinos.txt", "w" , encoding="utf8") as f:
        for i in list_tfidf:
            print(i, file=f)    #salvo os valores do tdf_idf em um txt

    print("\n")
    print("TDF X IDF dos documentos")

    for indice in list_tfidf:
        print(indice)

    print("\n")


    maior = 5
    palavra_maior = None
    doc_maior = None
    lis_valores = []
    for indi in list_tfidf:
        for ch, vl in indi.items():
            for valores in vl:
                for key, value in valores.items():
                       if (value) > maior:
                           maior = (value)
                           palavra_maior = key
                           doc_maior = ch
    print(f"O termo {palavra_maior}  e o documento {doc_maior} possuem o maior TDxIDF da coleção")          #O termo com o maior tfxidf








                        #lis_valores.append(value)

    #min = lis_valores[0]
    #max = lis_valores[2]


    #for i in lis_valores:
    #    if i > min and i > max:
     #       max = i
    #print(max)
    #print("^^^^Maior valor de tf x idf^^^^")





fun_letra_A()

fun_letra_B()
