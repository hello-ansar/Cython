from matplotlib.pyplot import plot, show
from numpy import linspace, random, arange, exp, fft, dot, pi, sin
from time import time


def run():
    start_time = time()
    A = int(10)
    f = int(3)
    N = int(1000)
    t = linspace(0, 5, N)

    S = A * sin(2 * pi * f * t) + random.uniform(-2, 2, N)
    n = arange(N)
    k = n.reshape((N, 1))
    M = exp(-2j * pi * k * n / N)
    a = fft.fftfreq(N, 5 / N)
    F = dot(S, M)
    F[F < 100] = 0

    print('{0} секунд'.format(time() - start_time))
    # print("%s секунд" % (time() - start_time))

    plot(abs(a), F)
    show()


if __name__ == '__main__':
    run()
