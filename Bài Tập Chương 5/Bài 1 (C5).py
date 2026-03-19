from matplotlib import pyplot as plt
categories =['Xuất Sắc','Giỏi','Trung Bình','Yếu','Kém']
values = [6,10,12,4,1]
plt.bar(categories,values,color="skyblue")
plt.title("Kết Quả Học Tập Của Lớp")
plt.xlabel("Học Lực Của Lớp")
plt.ylabel("Số Lượng Học Sinh")
plt.show()