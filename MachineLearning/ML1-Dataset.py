#Trining Dataset75% Testing Dataset 25%
from sklearn import datasets
#Iris Dataset
iris_dataset = datasets.load_iris()
#MNIST Dataset
digit_dataset = datasets.load_digits()
print(digit_dataset['target_names'])