import json

def convert_zeppelin_to_jupyter(zeppelin_path, jupyter_path):
    with open(zeppelin_path, 'r', encoding='utf-8-sig') as f:
        zep_data = json.load(f)
    
    cells = []
    
    for paragraph in zep_data.get('paragraphs', []):
        text = paragraph.get('text', '')
        if not text.strip():
            continue
            
        lines = text.split('\n')
        if lines[0].startswith('%md'):
            cell_type = 'markdown'
            source = [line + '\n' for line in lines[1:]]
        elif lines[0].startswith('%pyspark') or lines[0].startswith('%python'):
            cell_type = 'code'
            source = [line + '\n' for line in lines[1:]]
        else:
            # Maybe %angular or others, keep as markdown to be safe
            cell_type = 'markdown'
            source = [line + '\n' for line in lines]
            
        # Clean trailing newlines in source for each line isn't needed, but remove the last \n from last element
        if source and source[-1].endswith('\n'):
            source[-1] = source[-1][:-1]
            
        cell = {
            "cell_type": cell_type,
            "metadata": {},
            "source": source
        }
        
        if cell_type == 'code':
            cell["execution_count"] = None
            cell["outputs"] = []
            
        cells.append(cell)
        
    jupyter_data = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    with open(jupyter_path, 'w', encoding='utf-8') as f:
        json.dump(jupyter_data, f, indent=2, ensure_ascii=False)

convert_zeppelin_to_jupyter('/Users/kotori/Documents/RL_Multi_floor_maze/Multi_Floor_Maze.json', '/Users/kotori/Documents/RL_Multi_floor_maze/Multi_Floor_Maze.ipynb')
