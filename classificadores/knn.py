import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


data = pd.read_csv('../base_de_dados/iris.data')

# Pré-processamento dos dados
data = data.dropna()  # Remover linhas com valores ausentes

# Separar as features (características) e o target (alvo)
X = data.drop('class', axis=1)
y = data['class']

# Dividir os dados em conjunto de treinamento e conjunto de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)

# Criar o modelo kNN e treiná-lo
k = 7  # Número de vizinhos
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = knn.predict(X_test)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)

print('Acurácia: {:.2%}'.format(accuracy))
