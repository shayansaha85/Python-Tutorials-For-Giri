
cols = "firstname,lastname"
row1 = "giri,s"
row2 = "shayan,saha"
row3 = "saket,bihari"

content = cols +"\n"+row1+"\n"+row2+"\n"+row3+"\n"

file = open("names.csv", "w")
file.write(content)
file.close()