import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import time
import scipy as sp


def choose_graph(mode):
    start = time.time()
    if mode == 1:
        graph = nx.DiGraph()
        df = pd.read_csv("soc-sign-bitcoinalpha.csv", header=None, names=["source", "target", "weight", "time"])
        del df["time"]  # time: t(del) < t(drop) < t(pop) --> συμφερει το del
        for i in range(len(df)):
            row = (df["source"][i], df["target"][i], df["weight"][i])
            graph.add_node(row[1])
            graph.add_node(row[2])
            graph.add_weighted_edges_from([row])
    elif mode == 2:
        df = pd.read_csv("com-amazon.ungraph.txt", sep="\t", header=None, names=["source", "target"])
        graph = nx.Graph()
        for i in range(len(df)):
            graph.add_node(df["source"][i])
            graph.add_node(df["target"][i])
            graph.add_edge(df["source"][i], df["target"][i])
    elif mode == 3:
        df = pd.read_csv("wiki-topcats.txt", sep=" ", header=None, names=["source", "target"])
        graph = nx.DiGraph()
        for i in range(len(df)):
            graph.add_node(df["source"][i])
            graph.add_node(df["target"][i])
            graph.add_edge(df["source"][i], df["target"][i])
    else:
        print("There are only 3 files to choose from. mode possible values are 1,2,3")
        graph = None
    print("Graph total time: ", time.time() - start)
    return graph


def graph_to_gexf(G, file_name):
    nx.write_gexf(G, file_name+".gexf")
    print("Graph successfully saved as .gexf file.")
    return


G = choose_graph(1)
# graph_to_gexf(G, graph1)

