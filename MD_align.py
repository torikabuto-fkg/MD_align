import os
import subprocess

# ディレクトリのルートパス
base_dir = ""
subdirs = ["", "", "", ""]  

# 各サブディレクトリで処理を実行
for subdir in subdirs:
    for run in ["run_1", "run_2", "run_3"]:
        # ファイルパスの設定
        production_dir = os.path.join(base_dir, subdir, "production", run)
        input_file_fit = os.path.join(production_dir, "prod1nj3_nowat.xtc")
        input_file_set = os.path.join(production_dir, "prod0_align.pdb")
        output_file_xtc = os.path.join(production_dir, "prod1_align.xtc")
        index_file = os.path.join(production_dir, "index.ndx")
        
        # コマンドを順番に実行
        try:
            cmd = f"gmx_mpi trjconv -f {input_file_fit} -o {output_file_xtc} -s {input_file_set} -n {index_file} -fit rot+trans"
            process1 = subprocess.run(cmd, shell=True, input="C-alpha\nProtein\n", text=True, check=True)
            print(f"Executed: {cmd}")
            
        
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

print("All tasks completed.")
