numMetros =  float(input("Medida em metros: "))
km = numMetros /1000
hm = numMetros /100
dam = numMetros / 10
dm = numMetros * 10
cm = numMetros * 100
mm = numMetros * 1000
print('{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'. format(km,hm,dam,dm,cm,mm))