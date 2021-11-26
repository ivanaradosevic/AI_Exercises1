#7. Napiši program koji traži sequence malih slova povezanih s 'underscore'.
import re
stringac= "mala_slov Ima Ovdje neko_liko klkhkhs_hjhfjk_dhdh_fkjf"
x=re.findall(r"[a-z_]+_[a-z_]+", stringac)
print(x)
