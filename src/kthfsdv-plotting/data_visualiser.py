import numpy as np
import matplotlib
matplotlib.use('Agg') # setting Non GUI
import matplotlib.pyplot as plt

class DataVisualiser:
    def __init__(self, t_range, dt=0.01):
        self.t_range = t_range
        self.dt = dt
        self.t_values = np.arange(t_range[0], t_range[1], dt)
        self.h_values = self.calculate_h(self.t_values)

    def lambda_t(self, t):
        return 5 * np.sin(2 * np.pi * 1 * t)

    def calculate_h(self, t):
        return 3 * np.pi * np.exp(-self.lambda_t(t))

    def plot_data(self, filename='plot.png'):
        plt.figure(figsize=(10, 6))
        plt.plot(self.t_values, self.h_values, label='h(t) = $3\pi e^{-\lambda(t)}$')
        plt.title('Function Visualisation')
        plt.xlabel('Time (t)')
        plt.ylabel('h(t)')
        plt.legend()
        plt.grid(True)
        plt.savefig(filename)  # save PNG
        print(f'Plot saved as {filename}')

if __name__ == '__main__':
    visualiser = DataVisualiser(t_range=(0, 2), dt=0.01)
    visualiser.plot_data('function_visualisation.png')