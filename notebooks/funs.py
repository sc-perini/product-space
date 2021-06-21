import pandas as pd
import numpy as np
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable
from math import ceil
import networkx as nx
import os
from scipy.stats import sem
# from community import community_louvain
from itertools import combinations
from sklearn.metrics import adjusted_rand_score
from random import Random
from copy import deepcopy
from json import loads, dumps
from collections import OrderedDict
from scipy.stats import ttest_rel

densities = np.arange(0, 1, 0.05)

def plot_matshow_per_period(data:pd.DataFrame, list_years, nro_df, save:bool=False):
    """
        Toma un dataframe con las proximidades por periodo y, para cada uno,
        plotea una matriz de proximidades.
        
        Atributos
        ---------
        
        data: pd.DataFrame
            Matriz con las proximidades. Debe contener solamente las columnas
            con las proxs y la columna que indica los periodos.
        
        list_years: 
            Lista que indica los periodos. 
        
        save: bool, default=False
            Indicador para guardar el gráfico o plotearlo.
            
    """
    fig = plt.figure(figsize=(15,5))
    for i, year in enumerate(list_years):
        if len(list_years) == 2:
            ax = plt.subplot(1,2,i+1)
            im = plt.matshow(data[year],fignum=False, cmap="magma")
            # create an axes on the right side of ax. The width of cax will be 5%
            # of ax and the padding between cax and ax will be fixed at 0.05 inch.
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            plt.colorbar(im, cax=cax)
            plt.title(f'Matriz de Proximidad: {year}')
            
        else:
            ax = plt.subplot(1,3,i+1)
            im = plt.matshow(data[year],fignum=False, cmap="magma")
            # create an axes on the right side of ax. The width of cax will be 5%
            # of ax and the padding between cax and ax will be fixed at 0.05 inch.
            divider = make_axes_locatable(ax)
            cax = divider.append_axes("right", size="5%", pad=0.05)
            plt.colorbar(im, cax=cax)
            plt.title(f'Matriz de Proximidad: {year}')
    if save:
            folder = os.path.abspath('.').replace('notebooks','figures')
            file_path = os.path.join(folder, f'heatmap_proximity_matrix_df{nro_df}.png')
            plt.savefig(file_path)
            plt.close()
            print(f'{file_path} guardado exitosamente.')
    else:
            plt.show()
    
def grafos_pordensidad_dict(proximity_matrix:pd.DataFrame, densities:list):
    """
        Toma un dataframe cuadrado (x,x) y una lista de densidades y devuelte
        un diccionario en el que cada densidad es la key y cada value es la
        matriz de adyacencia generada a partir de utilizar la densidad 
        correspondiente como umbral.
        
        Atributos
        ---------
        
        proximity_matrix: pd.DataFrame
            Matriz de proximidades.
            
        densities: list
            Lista de densidades para utilizar como umbrales.
            
        Returns
        -------
        
        Gs: dict
            Diccionario con las densidades como keys y las matrices de 
            adyacencia correspondientes como values.
            
    """
    # cantidad de filas de la matriz (es una matriz cuadrada, así que filas==columnas)
    n = proximity_matrix.shape[0]
    # máxima cantidad de links
    max_links = (n*n-n)//2 
    # conservo la mitad de la matriz ya que es simétrica (me quedo con triangulo inferior)
    tril_idx = np.tril_indices(n,-1) 
    # paso a una dimensión y ordeno
    sorted_proximities = sorted(proximity_matrix.values[tril_idx].flatten(),reverse=True)
    
    # genero grafos y los guardo en diccionario
    Gs = dict()
    for d in densities:
        # pruebo con distinto número de links en base a la densidad definida
        idx = int(d*max_links) 
        # calculo el umbral correspondiente a dicha densidad
        threshold = sorted_proximities[idx] 
        # armo grafos a distintos umbrales
        Gs[threshold] = nx.from_pandas_adjacency(proximity_matrix>=threshold) 
    return Gs

def plot_heatmap_by_density(data, densidad, list_years, save=False):
    fig = plt.figure(figsize=(10,4))
    for i, year in enumerate(list_years):
        for d in data[year].keys():
            densidad = round(densidad,3)
            if round(d,3) == densidad:
                plt.subplot(1,4,i+1)
                fig.suptitle(f'Densidad: {densidad}',fontsize=20)
                graph = data[year][d]
                sns.heatmap(nx.to_numpy_array(graph),cbar=False,cmap="Blues",square=True)
                plt.title(f'{year}')
    plt.tight_layout()
    plt.subplots_adjust(top=0.99)
    if save:
        folder = os.path.abspath('.').replace('notebooks','graphs')
        file_path = os.path.join(folder, f'heatmap_by_density_{densidad}.png')
        plt.savefig(file_path)
        plt.close()
        print(f'{file_path} guardado exitosamente.')
    else:
        plt.show()
