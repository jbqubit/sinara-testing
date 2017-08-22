import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

dt = 2e-3
t = np.arange(2000)*dt
y = np.sin(2*np.pi*1*t)
y1 = np.clip(y, -1, .5)
b, a = signal.butter(1, 3*dt/2, "highpass", "digital", output='ba')
w, h = signal.freqz(b, a)
y2 = signal.lfilter(b, a, x=y1 )

fig = plt.figure()
plt.title('Digital filter frequency response')
ax1 = fig.add_subplot(111)

plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [rad/sample]')

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
plt.plot(w, angles, 'g')
plt.ylabel('Angle (radians)', color='g')
plt.grid()
plt.axis('tight')
plt.show()

# Plot the filter's frequency response, showing the critical points:

# b, a = signal.butter(4, 100, 'low', analog=True)
# w, h = signal.freqs(b, a)
# plt.semilogx(w, 20 * np.log10(abs(h)))
# plt.title('Butterworth filter frequency response')
# plt.xlabel('Frequency [radians / second]')
# plt.ylabel('Amplitude [dB]')
# plt.margins(0, 0.1)
# plt.grid(which='both', axis='both')
# plt.axvline(100, color='green') # cutoff frequency
# plt.show()