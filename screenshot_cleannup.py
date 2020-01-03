#!/usr/local/bin/python3
import os
import shutil
from pathlib import Path
import shutil

# 前準備
# 1. スクリーンショット格納ディレクトリに当該スクリプトを配置している
# 2. 同ディレクトリに、以下の名前のディレクトリが作成してある
# ディレクトリ名：archives

# 作業ディレクトリ
p = Path(".")

# 移動先ディレクトリ
archives_dir = Path("./archives")
print(archives_dir.resolve())

for f in p.glob("スクリーン*png"):
    # ファイルの移動開始
    src_path = f.resolve()
    dst_path = archives_dir.resolve() / f
    shutil.move(src_path, dst_path)
