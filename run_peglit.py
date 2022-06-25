#!/ usr/bin/env python

# This scritp is for peg linker calculate using peglit
# Rference: https://github.com/sshen8/peglit
# Author: Hongjiang Liu

import pandas as pd
import peglit
import numpy as np
import os
import time
#import threading
import multiprocessing

# *****************************
# *         Variables         *
# *****************************
# Allowed CPU Threads
THREAD_NUM = 4
# Sepcifiy the input file
INPUT_FILE = './peg_example.csv'
# 输出文件
OUTPUT_FILE = './peg_linker_result.csv'
# motif
MOTIF = "CGCGGTTCTATCTAGTTACGCGTTAAACCAACTAGAA"


# *****************************
# *       Function body       *
# *****************************

def calculate_peg(nrow):
	start_time = time.time()
	print("row %s is running." % (nrow + 1))
	global df
	spacer_sig =  str(df.iat[nrow,0])
	scaffold_sig =  str(df.iat[nrow,1])
	tem_sig =  str(df.iat[nrow,2])
	pbs_sig =  str(df.iat[nrow,3])
	peg_results = peglit.pegLIT(seq_spacer=spacer_sig, seq_scaffold=scaffold_sig, seq_template=tem_sig,seq_pbs=pbs_sig, seq_motif=MOTIF)
	end_time = time.time()
	print("row", (nrow + 1), "time cost:", end_time - start_time , "s, peg:", peg_results)
	return peg_results


if __name__ == "__main__":
	#Read in the file
	df = pd.read_csv(INPUT_FILE)

	print("Using %s threads." % THREAD_NUM)
	print("Input file is: %s, %s rows in total." % (INPUT_FILE, len(df)))
	print("Output will be saved in: %s." % OUTPUT_FILE)

	cores = THREAD_NUM
	pool = multiprocessing.Pool(processes=cores)
	tasks = np.arange(6000,len(df),1)
	# parallel calculation
	results = pool.map(calculate_peg,tasks)
	pool.close()
	pool.join()
	df['link'] = results
	#Write the result
	df.to_csv(OUTPUT_FILE,index=False)
	print(results)
	print("Done! Output is saved in %s." % OUTPUT_FILE)

