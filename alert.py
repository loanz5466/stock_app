# -*- coding: utf-8 -*-
# 觸底提醒系統（可切換規則）
from datetime import datetime

# === 規則選擇（改這裡就能換） ===
RULE = 'prev_mid_touch'      # 可選：'prev_mid_touch' / 'percent_drawdown' / 'below_level'

# === 參數（依規則需要調整） ===
TOLERANCE = 0.005            # 前一根中值的緩衝：0.5%（避免差一點點沒提醒）
DRAWDOWN_PCT = 0.05          # 自近期高點的回檔%：5% 就提醒
LEVEL = 60                   # 自訂關鍵價（不是 50，想用多少就填多少）

# === 觀察清單（先手動填；之後可接資料來源）===
# price：現價（暫時手填）
# prev_high / prev_low：前一根K棒的高低（你習慣的日/週/月自己選一個）
# recent_high：近期高點（用於回檔%規則）
watchlist = [
    {'symbol': '2408.TW', 'price': 61.0, 'prev_high': 69.4, 'prev_low': 63.6, 'recent_high': 80.0},
    # 再加別的：{'symbol':'2002.TW', 'price': 33.5, 'prev_high': 34.2, 'prev_low': 32.8, 'recent_high': 35.0},
]

# === 規則實作 ===
def alert_prev_mid(price, prev_high, prev_low, tol):
    mid = (prev_high + prev_low) / 2.0
    hit = price <= mid * (1 + tol)   # 觸碰中值或略高於中值(緩衝)就提醒
    msg = f'觸碰前一根中值 {mid:.2f}（含緩衝 {tol*100:.1f}%）'
    return hit, msg

def alert_percent_drawdown(price, recent_high, pct):
    target = recent_high * (1 - pct)
    hit = price <= target
    msg = f'自近期高點 {recent_high:.2f} 回檔 {pct*100:.1f}%（門檻 {target:.2f}）'
    return hit, msg

def alert_below_level(price, level):
    hit = price <= level
    msg = f'價格低於自訂關鍵價 {level:.2f}'
    return hit, msg

RULES = {
    'prev_mid_touch': lambda s: alert_prev_mid(s['price'], s['prev_high'], s['prev_low'], TOLERANCE),
    'percent_drawdown': lambda s: alert_percent_drawdown(s['price'], s['recent_high'], DRAWDOWN_PCT),
    'below_level':     lambda s: alert_below_level(s['price'], LEVEL),
}

# === 執行 ===
print('🔔 觸底提醒系統啟動', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print('使用規則：', RULE)

for s in watchlist:
    ok, reason = RULES[RULE](s)
    status = '🚨 提醒' if ok else '✅ 正常'
    print(f"{s['symbol']}: {status} | 現價 {s['price']:.2f} | {reason}")
