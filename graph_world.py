'''A Dictionary Containing Chernaurs locations
along with connections between them. Graph Theory.'''

#New_Location = {"NAME":{"NEIGHBOUR

def add_location(graph):
    '''function to make entering new locations with all info easier'''
    name = str(input("Enter new location name:"))
    neighbours = int(input("Enter the number of neighbours it has:"))
    for num in range(neighbours):
        
                        
    
graph = { "NE Airfield": { "Berezino Industrial": {"distance":2, "direction": "SE"},
                           "Krasnostav": {"distance":1, "direction": "SW"}
                            },
          
          "Krasnostav": { "NE Airfield": {"distance":1, "direction": "NE"},
                          "Berezino Indsutrial": {"distance":3, "direction": "SE"},
                          "Dubrovka": {"distance":3, "direction":"S"},
                          "Black Mountain": {"distance":1, "direction":"SW"},
                          "Gvozdno": {"distance":2, "direction": "W"}
                          },
          
          "Devil's Castle": {"Gvozdno": {"distance":2, "direction":"NE"},
                             "Black Mountain": {"distance": 3, "direction":"E"},
                             "Dubrovka":{"distance": 4, "direction": "SE"},
                             "Gorka":{"distance": 4, "direction": "S"},
                             "Grishino": {"distance": 1, "direction": "SW"}
                             },

          "Gvozdno":        {"Krasnostav": {"distance":2, "direction":"NE"},
                             "Black Mountain": {"distance": 1, "direction":"E"},
                             "Dubrovka":{"distance": 3, "direction": "SE"},
                             "Devil's Castle":{"distance": 2, "direction": "W"}
                             },
          
          "Black Mountain": {"Krasnostav": {"distance":1, "direction":"NE"},
                             "Dubrovka":{"distance": 2, "direction": "S"},
                             "Devil's Castle":{"distance": 3, "direction": "SW"},
                             "Gvozdno": {"distance": 1, "direction":"W"}
                             },
          
          "Grishino":       {"NW Airfield": {"distance":1, "direction":"W"},
                             "Kabanino":{"distance": 2, "direction": "S"},
                             "Devil's Castle":{"distance": 1, "direction": "NE"}
                             },
          
          "Lopatino":       {"NW Airfield": {"distance":2, "direction":"E"},
                             "Vybor":{"distance": 1, "direction": "SE"},
                             "Pustoshka":{"distance": 2, "direction":"S"}
                             },
          
          "NW Airfield":    {"Grishino": {"distance":1, "direction":"E"},
                             "Kabanino": {"distance": 2, "direction":"S"},
                             "Vybor":{"distance": 2, "direction": "SW"},
                             "Lopatino":{"distance": 2, "direction": "W"}
                             },
          
          "Dubrovka":   { "Krasnostav": {"distance":3, "direction": "NE"},
                          "Black Mountain": {"distance":1, "direction":"SW"},
                          "Dubrovka": {"distance":3, "direction":"S"},
                          "Berezino Indsutrial": {"distance":3, "direction": "SE"},
                          "Gvozdno": {"distance":2, "direction": "W"}
                          },

          
          
        
    }
