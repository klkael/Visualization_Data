import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [1,3,5,2,4,6,8,7,3]
plt.plot(x,y)
plt.title('X vs Y')
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.grid(True)
plt.legend(['Garis XY'])
# plt.savefig('Chart.png') buat save chartnya
plt.show()
