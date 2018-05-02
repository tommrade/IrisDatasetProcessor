#!/usr/bin/python
# encoding: utf-8

from math import floor
import matplotlib.pyplot
import numpy

data_file = 'iris.data'
flower = [['num'], ['num'], ['num'], ['num'], []]
flower_component = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
flower_species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
how_many_columns = len(flower)

def load(file_to_read):
    table = [[] for i in range(how_many_columns)]
    file = open(file_to_read, "r")
    for line in file:
        if len(line) > 1:
            vector_of_expressions = line.split(',')
            for i in range(how_many_columns):
                expression = vector_of_expressions[i].strip()
                if 'num' in flower[i]:
                    expression = float(expression)
                table[i].append(expression)
    file.close()
    return table

def generalized_mean(characteristics_values_table, degree):
    characteristics_values_table = sorted(characteristics_values_table)
    result = 0.
    for i in characteristics_values_table:
        result += pow(i, degree)
    result = pow((result / len(characteristics_values_table)), (1. / degree))
    return result

def arithmetic_mean(characteristics_values_table):
    return generalized_mean(characteristics_values_table, 1)

def harmonic_mean(characteristics_values_table):
    return generalized_mean(characteristics_values_table, -1)

def geometric_mean(characteristics_values_table):
    characteristics_values_table = sorted(characteristics_values_table)
    result = 1.
    for i in characteristics_values_table:
        result *= i
    result = pow((result), (1. / len(characteristics_values_table)))
    return result

def quantile(characteristics_values_table, degree):
    characteristics_values_table = sorted(characteristics_values_table)
    how_many_elements = len(characteristics_values_table)
    element = floor(how_many_elements * degree)
    element = int(element)
    if 0.0 == degree:
        result = characteristics_values_table[0]
    elif how_many_elements % 2 or 1.0 == degree:
        result = characteristics_values_table[element - 1]
    else:
        result = (characteristics_values_table[element] + characteristics_values_table[element - 1]) / 2
    return result

def minimum(characteristics_values_table):
    characteristics_values_table = sorted(characteristics_values_table)
    return characteristics_values_table[0]

def lower_quartile(characteristics_values_table):
    return quantile(characteristics_values_table, 0.25)

def median(characteristics_values_table):
    return quantile(characteristics_values_table, 0.5)

def upper_quartile(characteristics_values_table):
    return quantile(characteristics_values_table, 0.75)

def maximum(characteristics_values_table):
    return quantile(characteristics_values_table, 1.0)

def minmax_difference(characteristics_values_table):
    return (maximum(characteristics_values_table) - minimum(characteristics_values_table))

def variance(characteristics_values_table, N):
    current_arithmetic_mean = arithmetic_mean(characteristics_values_table)
    result = 0.
    assert len(characteristics_values_table) == N
    for i in range(N):
        result += pow((characteristics_values_table[i] - current_arithmetic_mean), (2))
    result /= N
    return result

def standard_deviation(characteristics_values_table, N):
    return pow((variance(characteristics_values_table, N)), (0.5))

def kurtosis(characteristics_values_table, N):
    current_arithmetic_mean = arithmetic_mean(characteristics_values_table)
    result = 0.
    assert len(characteristics_values_table) == N
    for i in range(N):
        result += pow((characteristics_values_table[i] - current_arithmetic_mean), (4))
    result /= N
    result /= pow(standard_deviation(characteristics_values_table, N), 4)
    return result

table = load(data_file)
complete_table = table[0] + table[1] + table[2] + table[3]
complete_table = sorted(complete_table)

complete_matrix = [table[0], table[1], table[2], table[3]]
complete_matrix = numpy.asarray(complete_matrix)
matrix_setosa = complete_matrix[0:4, 0:50]  
matrix_versicolor = complete_matrix[0:4, 50:100]
matrix_virginica = complete_matrix[0:4, 100:150]

table_setosa = [[], [], [], []]
table_versicolor = [[], [], [], []]
table_virginica = [[], [], [], []]

for i in range(4):
    table_setosa[i] = matrix_setosa[i:(i+1), 0:50]
    table_setosa[i] = numpy.asarray(table_setosa[i]).reshape(-1)
    table_versicolor[i] = matrix_versicolor[i:(i+1), 0:50]
    table_versicolor[i] = numpy.asarray(table_versicolor[i]).reshape(-1)
    table_virginica[i] = matrix_virginica[i:(i+1), 0:50]
    table_virginica[i] = numpy.asarray(table_virginica[i]).reshape(-1)

for j in range(4):
    print '===\nSpecies: %s, component: %s:' % (flower_species[0], flower_component[j])
    print '\nMean:'
    print 'arithmetic: %f' % arithmetic_mean(table_setosa[j])
    print 'harmonic: %f' % harmonic_mean(table_setosa[j])
    print 'geometric: %f' % geometric_mean(table_setosa[j])
    print '\nquantils:'
    print 'minimum: %f' % minimum(table_setosa[j])
    print '1st quartile: %f' % lower_quartile(table_setosa[j])
    print 'median: %f' % median(table_setosa[j])
    print '3rd quartile: %f' % upper_quartile(table_setosa[j])
    print 'maximum: %f' % maximum(table_setosa[j])
    print '\nMisc:'
    print 'range: %f' % minmax_difference(table_setosa[j])
    print 'variance: %f' % variance(table_setosa[j], len(table_setosa[j]))
    print 'standard deviation: %f' % standard_deviation(table_setosa[j], len(table_setosa[j]))
    print 'kurtosis: %f' % kurtosis(table_setosa[j], len(table_setosa[j]))
    print ''
    
for j in range(4):
    print '===\nSpecies: %s, component: %s:' % (flower_species[1], flower_component[j])
    print '\nMean:'
    print 'arithmetic: %f' % arithmetic_mean(table_versicolor[j])
    print 'harmonic: %f' % harmonic_mean(table_versicolor[j])
    print 'geometric: %f' % geometric_mean(table_versicolor[j])
    print '\nquantils:'
    print 'minimum: %f' % minimum(table_versicolor[j])
    print '1st quartile: %f' % lower_quartile(table_versicolor[j])
    print 'median: %f' % median(table_versicolor[j])
    print '3rd quartile: %f' % upper_quartile(table_versicolor[j])
    print 'maximum: %f' % maximum(table_versicolor[j])
    print '\nMisc:'
    print 'range: %f' % minmax_difference(table_versicolor[j])
    print 'variance: %f' % variance(table_versicolor[j], len(table_versicolor[j]))
    print 'standard deviation: %f' % standard_deviation(table_versicolor[j], len(table_versicolor[j]))
    print 'kurtosis: %f' % kurtosis(table_versicolor[j], len(table_versicolor[j]))
    print ''
    
for j in range(4):
    print '===\nSpecies: %s, component: %s:' % (flower_species[2], flower_component[j])
    print '\nMean:'
    print 'arithmetic: %f' % arithmetic_mean(table_virginica[j])
    print 'harmonic: %f' % harmonic_mean(table_virginica[j])
    print 'geometric: %f' % geometric_mean(table_virginica[j])
    print '\nquantils:'
    print 'minimum: %f' % minimum(table_virginica[j])
    print '1st quartile: %f' % lower_quartile(table_virginica[j])
    print 'median: %f' % median(table_virginica[j])
    print '3rd quartile: %f' % upper_quartile(table_virginica[j])
    print 'maximum: %f' % maximum(table_virginica[j])
    print '\nMisc:'
    print 'range: %f' % minmax_difference(table_virginica[j])
    print 'variance: %f' % variance(table_virginica[j], len(table_virginica[j]))
    print 'standard deviation: %f' % standard_deviation(table_virginica[j], len(table_virginica[j]))
    print 'kurtosis: %f' % kurtosis(table_virginica[j], len(table_virginica[j]))
    print ''
 
matplotlib.pyplot.figure(1)
points_sepal_setosa = matplotlib.pyplot.scatter(matrix_setosa[1], matrix_setosa[0], c=['r'], s=100)
points_sepal_versicolor = matplotlib.pyplot.scatter(matrix_versicolor[1], matrix_versicolor[0], c=['g'], s=100)
points_sepal_virginica = matplotlib.pyplot.scatter(matrix_virginica[1], matrix_virginica[0], c=['b'], s=100)
matplotlib.pyplot.xlabel(flower_component[1])
matplotlib.pyplot.ylabel(flower_component[0])
matplotlib.pyplot.legend((points_sepal_setosa, points_sepal_versicolor, points_sepal_virginica),
                         (flower_species[0], flower_species[1], flower_species[2]),
                         scatterpoints=1, loc='lower left', ncol=3, fontsize=8)
 
matplotlib.pyplot.figure(2)
points_petal_setosa = matplotlib.pyplot.scatter(matrix_setosa[3], matrix_setosa[2], c=['c'], s=100)
points_petal_versicolor = matplotlib.pyplot.scatter(matrix_versicolor[3], matrix_versicolor[2], c=['m'], s=100)
points_petal_virginica = matplotlib.pyplot.scatter(matrix_virginica[3], matrix_virginica[2], c=['y'], s=100)
matplotlib.pyplot.xlabel(flower_component[3])
matplotlib.pyplot.ylabel(flower_component[2])
matplotlib.pyplot.legend((points_petal_setosa, points_petal_versicolor, points_petal_virginica),
                         (flower_species[0], flower_species[1], flower_species[2]),
                         scatterpoints=1, loc='lower left', ncol=3, fontsize=8)
 
matplotlib.pyplot.show()
