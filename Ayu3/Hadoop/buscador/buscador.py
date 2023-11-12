import sys 
import re

dict = {
    "1":"https://es.wikipedia.org/wiki/mazda",
    "2":"https://es.wikipedia.org/wiki/nissan",
    "3":"https://es.wikipedia.org/wiki/toyota",
    "4":"https://es.wikipedia.org/wiki/mitsubishi",
    "5":"https://es.wikipedia.org/wiki/suzuki",
    "6":"https://es.wikipedia.org/wiki/bentley",
    "7":"https://es.wikipedia.org/wiki/ferrari",
    "8":"https://es.wikipedia.org/wiki/lamborghini",
    "9":"https://es.wikipedia.org/wiki/lotus",
    "10":"https://es.wikipedia.org/wiki/bugatti",
}

result = []

for line in sys.stdin:
    if(line.split()[0] == sys.argv[1]):
        # obtener ls
        aux=re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+',line)
        max = 0
        res = 0
        for tuple in aux[1:]:
            result.append(dict[str(eval(tuple)[0])])
            if eval(tuple)[1] > max:
                result.remove(dict[str(eval(tuple)[0])])
                max = eval(tuple)[1]
                res = eval(tuple)[0]
                result.insert(0, dict[str(res)])
try:
    for idx, value in enumerate(result):
        if idx == 0:
            print("Most coincidences ("+ str(idx+1)+ "): " + value)
            continue
        print(str(idx+1)+ ": " + value)
except:
    print("palabra no encontrada!")