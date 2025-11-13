import os
import pymol
from pymol import cmd

# ディレクトリパスの定義
base_dir = os.path.expanduser('')
# variantsの名前がディレクトリ名に対応している。
variants = ["", "", "", ""] 
runs = ['run_1', 'run_2', 'run_3']

# アライメントしたい先の構造を以下で指定
target_pdb = os.path.join(base_dir, '.pdb')

# PyMOLをヘッドレスモードで起動
pymol.finish_launching(['pymol', '-cq'])  # '-cq' は PyMOL をコマンドラインモードで起動し、GUI を無効にします

# ターゲットPDBをロード
cmd.load(target_pdb, 'target')

# すべての変異体と実行ごとにアラインメントを行う
for variant in variants:
    for run in runs:
        pdb_path = os.path.join(base_dir, variant, run, 'prod0_nowat_renum.pdb')
        if os.path.exists(pdb_path):
            # PDBファイルをロード
            pdb_name = f"{variant}_{run}"
            cmd.load(pdb_path, pdb_name)
            
            # アラインメントを実行
            cmd.align(pdb_name, 'target')
            
            # アラインメントされたPDBを保存
            aligned_pdb_path = os.path.join(base_dir, variant, run, 'prod0_align.pdb')
            cmd.save(aligned_pdb_path, pdb_name)
            
            # アラインメント結果をクリア
            cmd.delete(pdb_name)

# PyMOLを終了
cmd.quit()
