# Загрузка данных из файла
data = np.loadtxt('accelerations.txt') 
dt = 1/104 # Шаг времени

# Инициализация переменных x = np.zeros(len(data))
y = np.zeros(len(data)) 
z = np.zeros(len(data)) 
vx = np.zeros(len(data)) 
vy = np.zeros(len(data)) 
vz = np.zeros(len(data))
# Вычисление скоростей и координат на каждом шаге 
for i in range(1, len(data)):
# Вычисление скоростей
    vx[i] = vx[i-1] + data[i, 0] * dt
    vy[i] = vy[i-1] + data[i, 1] * dt
    vz[i] = vz[i-1] + data[i, 2] * dt 
# Вычисление координат
    x[i] = x[i-1] + vx[i] * dt
    y[i] = y[i-1] + vy[i] * dt
    z[i] = z[i-1] + vz[i] * dt
# Вычисление итогового перемещения
displacement = np.sqrt(x[-1]**2 + y[-1]**2 + z[-1]**2) * 1000 
# в мм
print("Итоговое перемещение:", displacement, "мм")