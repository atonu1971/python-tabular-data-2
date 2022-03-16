#! /usr/bin/env python3

import pandas as pd 
import matplotlib.pyplot as plt
from scipy import stats

iris_df = pd.read_csv("iris.csv")

setosa = iris_df[iris_df.species == "Iris_setosa"]
versicolor = iris_df[iris_df.species == "Iris_versicolor"]
virginica = iris_df[iris_df.species == "Iris_virginica"]

species = [setosa, versicolor, virginica]

def get_regression_plot(species)
    """
    Parameters
    -------------------------------
    species: pandas.core.frame.DataFrame
        A dataframe containing morphological measurements for a given species.
    Returns
    -------------------------------
    A scatterplot .png file showing the data with the regression of the x & y 
    variables plotted onto them.
    """
    x = species.petal_length_cm
    y = species.sepal_length_cm
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept   
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("petal_v_sepal_length_regress.png")
    return 

    #for taxon in species:
    #    get_regression_plot(taxon)

if __name__ == '__main__':
  


    dataframe = pd.read_csv("iris.csv")
    versicolor = dataframe[dataframe.species == "Iris_versicolor"]
    virginica = dataframe[dataframe.species == "Iris_virginica"]
    setosa = dataframe[dataframe.species == "Iris_setosa"]

    x1 = versicolor.petal_length_cm
    y1 = versicolor.sepal_length_cm
    x2 = virginica.petal_length_cm
    y2 = virginica.sepal_length_cm
    x3 = setosa.petal_length_cm
    y3 = setosa.sepal_length_cm

    result1 = get_regression_line(x1, y1)
    result2 = get_regression_line(x2, y2)
    result3 = get_regression_line(x3, y3)
    plt.savefig("all_species_together.png")
    plt.close('all')
    quit()
