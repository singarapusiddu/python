import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm, poisson

def plot_binomial(n, p):
    x = np.arange(0, n + 1)
    y = binom.pmf(x, n, p)
    plt.bar(x, y, color='skyblue', edgecolor='black')
    plt.title(f'Binomial Distribution (n={n}, p={p})')
    plt.xlabel('Number of Successes')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()

def plot_normal(mu, sigma):
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y = norm.pdf(x, mu, sigma)
    plt.plot(x, y, color='green')
    plt.title(f'Normal Distribution (μ={mu}, σ={sigma})')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.show()

def plot_poisson(lam):
    x = np.arange(0, np.ceil(lam + 4*lam**0.5))
    y = poisson.pmf(x, lam)
    plt.bar(x, y, color='lightcoral', edgecolor='black')
    plt.title(f'Poisson Distribution (λ={lam})')
    plt.xlabel('Number of Events')
    plt.ylabel('Probability')
    plt.grid(True)
    plt.show()

def main():
    print("Select a distribution to plot probabilities:")
    print("1. Binomial Distribution")
    print("2. Normal Distribution")
    print("3. Poisson Distribution")

    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        n = int(input("Enter number of trials (n): "))
        p = float(input("Enter probability of success (p): "))
        plot_binomial(n, p)

    elif choice == '2':
        mu = float(input("Enter mean (μ): "))
        sigma = float(input("Enter standard deviation (σ): "))
        plot_normal(mu, sigma)

    elif choice == '3':
        lam = float(input("Enter lambda (λ): "))
        plot_poisson(lam)

    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
