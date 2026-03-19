import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 50)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, x**2, color='pink')
ax1.set_title("Đồ thị $y = x^2$")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax2.plot(x, np.sqrt(x), color='black')
ax2.set_title("Đồ thị $y = \sqrt{x}$")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
plt.tight_layout()
plt.show()