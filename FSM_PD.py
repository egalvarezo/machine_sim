import pandas as pd1
import pd_sim as pd2

nombre_archivo = 'FSM_dosUnosSeguidos.csv'

data_frame1 = pd1.read_csv(nombre_archivo)
data_frame2 = pd2.read_csv(nombre_archivo)

print(data_frame1)
print(data_frame2)

print()

print(data_frame1.head())
#error print(data_frame2.head())

print()

print(data_frame1.tail())
#error print(data_frame2.tail())

print()

print(data_frame1.index)
#error print(data_frame2.index)

print()

print(data_frame1.describe())
#error print(data_frame2.describe())

print()

print(data_frame1.T)
print(data_frame2.T)
#error print(data_frame2.T())

print()

print(data_frame1.sort_index(axis=1, ascending=False))
#error print(data_frame2.sort_index(axis=1, ascending=False))

print()

print(data_frame1['Est_act'])
print(data_frame2['Est_act'])

print()

print(data_frame1[0:3])
print(data_frame2[0:3])

print()

print(data_frame1.loc[0])
#error print(data_frame2.loc[0])
#error print(data_frame2.loc(0))

print()

print(data_frame1.at[1, "Est_act"])
#error print(data_frame2.at[1, "Est_act")])
#error print(data_frame2.at(1, "Est_act"))

print()

print(data_frame1 > 0)
#error print(data_frame2 > 0)

print()

print(data_frame1.iloc[3])
#error print(data_frame2.iloc[3])
#error print(data_frame2.iloc(3))

print()

data_frame1_a=data_frame1.copy()
print(data_frame1_a)
#error data_frame2_a=data_frame2.copy()
#error print(data_frame2_a)

print()

data_frame1_a['Est_act'] = 0
print(data_frame1_a)
#data_frame2['Est_act'] = 0
#print(data_frame2)

print('Función negar -, Gerardo Muñoz')

print(-data_frame1)
print(-data_frame2)

print()
