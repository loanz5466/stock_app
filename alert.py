# -*- coding: utf-8 -*-
# 觸底提醒系統（可切換規則）
from datetime import datetime

# === 規則選擇（改這裡就能換） ===
RULE = 'prev_mid_touch'      # 可選：'prev_mid_touch' / 'percent_drawdown' / 'below_level'

# === 參數（依規則需要調整） ===
TOLERANCE = 0.005            # 前一根中值的緩衝：0.5%（避免差一點點沒提醒）
DRAWDOWN_PCT = 0.05          # 自近期高點的回檔%：5% 就提醒
LEVEL = 60                   # 自訂關鍵價（不是
