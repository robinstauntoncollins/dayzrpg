'''A Python Class
A simple Python graph class to handle world graph and relationsips between areas'''
#from graph_world import graph
class World(object):
    def __init__(self, graph_dict=None):
        ''' initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used'''
            
        if graph_dict == None:
            graph_dict = {}

        self.__graph_dict = graph_dict
        
    def locations(self):
            """ returns the vertices of a graph """
            return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def connections(self, location):
        ''' returns list of connections of a particular vertice'''
        for k,v in self.__graph_dict[location].items():
            print(k,v.items())
        #return list(self.__graph_dict[location].keys())

    def add_location(self, location):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if location not in self.__graph_dict:
            self.__graph_dict[location] = {}
##            with open('graph_world.py', 'a') as file:
##                file.write(vertex)

    def add_connection(self, connection):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        connection = set(connection)
        location1 = connection.pop()
        if edge:
            # not a loop
            location2 = connection.pop()
        else:
            # a loop
            location2 = location1
        if location1 in self.__graph_dict:
            self.__graph_dict[location1].append(location2)
        else:
            self.__graph_dict[location1] = [location2]

    def __generate_connections(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        connections = []
        for location in self.__graph_dict:
            for neighbour in self.__graph_dict[location]:
                if {neighbour, location} not in connections:
                    connections.append({location, neighbour})
        return connections

if __name__ == "__main__":

    graph = { "NE Airfield": { "Krasnostav": {"distance":1, "direction": "SW"},
                           "Berezino Industrial": {"distance":2, "direction": "SE"}
                            },
          
          "Krasnostav": { "NE Airfield": {"distance":1, "direction": "NE"},
                          "Black Mountain": {"distance":1, "direction":"SW"},
                          "Dubrovka": {"distance":3, "direction":"S"},
                          "Berezino Indsutrial": {"distance":3, "direction": "SE"},
                          "Gvozdno": {"distance":2, "direction": "W"}
                          },
          
          "Devil's Castle": {"Gvozdno": {"distance":2, "direction":"NE"},
                             "Black Mountain": {"distance": 3, "direction":"E"},
                             "Dubrovka":{"distance": 4, "direction": "SE"},
                             "Gorka":{"distance": 4, "direction": "S"},
                             "Grishino": {"distance": 1, "direction": "SW"}
                             }                      
                    
    }

    Chernarus = World(graph)
    #Chernarus.connections("Krasnostav")
    #print("\n\n")
    #Chernarus.connections("NE Airfield")
    
    #locs = Chernarus.locations()
    #print(locs)
