from unidecode import unidecode
import os

diretorio = r"C:/Users/G/Documents/SEMESTRE 2022/ORI/hinos"
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
            ".", " ").replace("\n", " ").replace("?"," ").replace("!"," ").replace("]"," ").replace("("," ").replace(")"," ").split())
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
with open("C:/Users/G/Documents/SEMESTRE 2022/ORI/vocab_hinos.txt", "w" , encoding="utf8") as f:
    vocabulario = fun_remove_repetidos(list)
    for i in vocabulario:
        print(i, file=f)

print(vocabulario, "for debug - vocabulário  \n")



with open("C:/Users/G/Documents/SEMESTRE 2022/ORI/voc.txt", "r" , encoding="utf8") as f:
    linha_doc = f.readlines()

#"print for debug do doc sem tratamento\n"
print(linha_doc , "for debug -- doc sem tratar\n")

var_aux = []
#removendo caracteres e colocando em minusculo
var_aux = fun_car(linha_doc)

doc_tratado = []

#removendo os repetidos do documento e colocando em ordem alfabetica
doc_tratado = fun_remove_repetidos(var_aux)
print(doc_tratado , "for debug -- doc tratado\n")


bag = []

for i in vocabulario:
    if i in doc_tratado:
        bag.append(1)
    else:
        bag.append(0)


print("\n")
print(bag)


