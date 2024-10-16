import os
import configs as c
import fluxes as fl

ports_path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports")

def init_ports():
    ports = {"dfs-a": {
        "flux_name": "DFS-A",
        "sectors": {
            "SOUNDS": {
                "size": 0,
                "cells": {
                    0: {
                        "type": "EMPTY",
                        "value": None
                    }
                }
            },
            "PLAYER": {
                "size": 5,
                "cells": {
                    0: {
                        "type": "ADDR",
                        "value": [
                            {
                                "sector": "SOUNDS",
                                "address": 0
                            }
                        ]
                    },
                    1: {
                        "type": "INTEGER", # 0 : Play, 1 : Pause, 2 : Stop, 3 : Fade out, 4 : Set volume, 5 : Get volume, 6 : Is playing
                        "value": 0
                    },
                    2: {
                        "type": "BOOLEAN", # False : Done, True : Not done
                        "value": False
                    },
                    3: {
                        "type": "INTEGER", # Argument for Fade out and Set volume
                        "value": 0
                    },
                    4: {
                        "type": "INTEGER", # Result for Get volume (0 to 1) and Is playing (0 or 1)
                        "value": 0
                    }
                }
            }
        }
    }, "dfs-g": {
        "flux_name": "DFS-G",
        "sectors": {
            'INFO': {'size': 0, 'cells': {}},
            'FRAME': {'size': 1, 'cells': {
                0: {
                    "type": "STRING",
                    "value": "PATH"
                }
            }}
        }
    }, "dfs-i": {
        "flux_name": "DFS-I",
        "sectors": {}
    }, "dfs-s": {
        "flux_name": "DFS-S",
        "sectors": {
            "TRIGGERS": {
                "size": 0,
                "cells": { # Set boolean to 0 after trigger
                    0: {
                        "type": "BOOLEAN", # Stop all sounds
                        "value": 0
                    },
                    1: {
                        "type": "BOOLEAN", # Pause all sounds
                        "value": 0
                    },
                    2: {
                        "type": "BOOLEAN", # Unpause all sounds
                        "value": 0
                    }
                }
            }
        }
    }}
    
    for port, flux_trace in ports.items():
        port_path = os.path.join(ports_path, f"{port}.flx")
        f = open(port_path, "w+")
        f.close()
        port_flux = fl.FluxFile(port_path)        
        port_flux.write_file(port_path, port_flux.format(flux_trace))
    
    for _, __, files in os.walk(os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "data")):
        for file in files:
            path = os.path.join(c.DISPLAY_FOLDER_PATH, "ports", "data", file)
            l_path = path.lower().replace("\\", "/")
            try:
                os.remove(path)
            except:
                pass