import catboost.datasets
import pandas as pd
import os




def main():
    train,test = catboost.datasets.titanic()
    names = ['Pclass','Sex','Age']
    os.chdir('./datasets')
    train[names].to_csv('train.csv')
    test[names].to_csv('test.csv')
if __name__ == "__main__":
    main()