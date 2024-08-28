import numpy as np
import matplotlib.pyplot as plt

#Lista de valores
valores = [47.3, 12.8, 63.5, 29.1, 54.7, 18.2, 37.6, 82.4, 66.9, 41.2, 95.8, 23.7, 57.1, 34.6, 25.1]

#Média
media = np.mean(valores)

#Mediana
mediana = np.median(valores)

#Variância populacional e amostral
variancia_pop = np.var(valores)
variancia_amostral = np.var(valores, ddof=1)

#Desvio padrão populacional e amostral
desvio_pop = np.std(valores)
desvio_amostral = np.std(valores, ddof=1)

#Coeficiente de variação populacional e amostral
coef_var_pop = (desvio_pop / media) * 100
coef_var_amostral = (desvio_amostral / media) * 100

#Quartis
quartis = np.percentile(valores, [25, 50, 75])

#Histograma
plt.hist(valores, bins=5, edgecolor='k')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma')
plt.show()

#Box plot
plt.boxplot(valores)
plt.ylabel('Valores')
plt.title('Box Plot')
plt.show()

#Resultados
print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Variância Populacional: {variancia_pop}")
print(f"Variância Amostral: {variancia_amostral}")
print(f"Desvio Padrão Populacional: {desvio_pop}")
print(f"Desvio Padrão Amostral: {desvio_amostral}")
print(f"Coeficiente de Variação Populacional: {coef_var_pop}%")
print(f"Coeficiente de Variação Amostral: {coef_var_amostral}%")
print(f"Quartis (Q1, Q2, Q3): {quartis}")
