import numpy as np

Random_Integers = np.random.randint(1, 20, 20)
print("Random Integers :", Random_Integers)

Reshaping = Random_Integers.reshape((4,5))
print("Random Integers ater Reshaping :")
print(Reshaping)

Replacing_Max = np.where(Reshaping == np.amax(Reshaping, axis=1, keepdims=True), 0, Reshaping)
print("Random Integers ater replacing the maximum in each row by 0")
print(Replacing_Max)