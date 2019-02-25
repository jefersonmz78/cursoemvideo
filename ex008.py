medida = float(input('Uma distância em metros: '))
dc = medida * 10
cm = medida * 100
mm = medida * 1000
km = medida * 10000
print('A media de a {}dc a {}cm corresponde a {:.0f}cm a {:.0f}mm e {} km '.format(medida,dc, cm, mm,km))