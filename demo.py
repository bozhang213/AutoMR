import os
import pickle
import numpy as np
import pandas as pd
import settings
import Phase1_PSOSearch
import Phase2_Filter
import Phase3_RemoveRedundancy
from load_resulrs import *


if __name__ == '__main__':
    print("=====Start Inferring=====")
    print('start phase 1: searching ...')
    Phase1_PSOSearch.run_phase1()
    print('start phase 2: filtering ...')
    Phase2_Filter.run_phase2()
    print('start phase 3: redundancy removing ...')
    Phase3_RemoveRedundancy.run_phase3()

    print("=====Results=====")
    MRs_path = settings.output_path
    func_indices = settings.func_indices
    result_files = os.listdir(f"{MRs_path}/phase3")
    for result_file in result_files:
        print(f'result file is {result_file}')
        func_index = int(result_file[0:result_file.find('_')])
        MRs = load_phase3_results(f"{MRs_path}/phase3/{result_file}")
        for k, v in MRs.items():
            parameters_int = [int(e) for e in k.split("_")]
            NOI = parameters_int[0]
            MIR = parameters_int[1]
            MOR = parameters_int[2]
            DIR = parameters_int[3]
            DOR = parameters_int[4]

            map_relation = {1:"=", 2:">", 3:"<"}

            with open(f"{MRs_path}/{func_index}_{k}.html", 'w') as _file:
                _file.write(f'<p>func index is {func_index} </p>')
                _file.write(f'<p>Mode of Input Relation is "{map_relation[MIR]}" </p>')
                _file.write(f'<p>Mode of Output Relation is "{map_relation[MOR]}" </p>')
                _file.write(f'<p>Input Relation is: </p>')
                _file.write(v[0].to_html())
                _file.write(r"</br>")
                _file.write(f'<p>Output Relation is: </p>')
                _file.write(v[1].to_html())
