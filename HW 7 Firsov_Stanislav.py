import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def harmonic_oscillator(t, state):
    y, v = state
    return [v, -y]

try:
    y0 = float(input("Initial position y(0) [default 1.0]: ") or 1.0)
    v0 = float(input("Initial velocity v(0) [default 0.0]: ") or 0.0)
    t_end = float(input("Integration time (0 to t) [default 10.0]: ") or 10.0)
except ValueError:
    print("Invalid input. Using default values.")
    y0, v0, t_end = 1.0, 0.0, 10.0

sol = solve_ivp(harmonic_oscillator, [0, t_end], [y0, v0],
                t_eval=np.linspace(0, t_end, 1000))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.plot(sol.t, sol.y[0], label='Position')
ax1.plot(sol.t, sol.y[1], label='Velocity')
ax1.set_xlabel('Time')
ax1.set_ylabel('Value')
ax1.set_title('Time Domain')
ax1.legend()
ax1.grid()

ax2.plot(sol.y[0], sol.y[1])
ax2.set_xlabel('Position')
ax2.set_ylabel('Velocity')
ax2.set_title('Phase Portrait')
ax2.grid()

plt.tight_layout()
plt.show()
