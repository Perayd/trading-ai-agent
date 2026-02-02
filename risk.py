def position_size(balance, entry, stop, risk_pct):
    risk_amount = balance * risk_pct
    risk_per_unit = abs(entry - stop)
    size = risk_amount / risk_per_unit
    return round(size, 4)
