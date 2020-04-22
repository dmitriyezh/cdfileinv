#Программа для поиска части текста в нём по тегу и выборки её в новый файл

infile = "allinvo.inv"

tagList = ['CD_A','CD_Q','CD_H','CD_PR','CD_ZO','CD_ZH','CD_ACC','CD_CM','CD_E']

for y in tagList:

	with open(infile,"r", encoding = 'utf-8') as fin:
		with open("allinvo_"+y+".inv", "w", encoding = 'utf-8') as fout:                                                                                                                                     
		    lines = fin.read().split("\n")
		    i=0
		    while i<len(lines):
		        if "# "+y+" BEGIN" in lines[i]:
		            fout.write(lines[i].rstrip()+"\n")
		            i+=1
		            while i<len(lines) and "# "+y+" END" not in lines[i]:
		            	fout.write(lines[i].rstrip()+"\n")
		            	#print(i)
		            	i+=1
		            if "# "+y+" END" in lines[i]:
		            	fout.writelines("# "+y+" END"+"\n")
		        i+=1
print('работа завершена')
