import calendar
from pathlib import Path

meses_ano =list(calendar.month_name[1::])
#print(meses_ano)
dias_semana =list(calendar.day_name[0::])
#print(dias_semana)


for i, meses in enumerate(meses_ano):
   for dias in dias_semana:
       Path(f'2022/{i+1}-{meses}/{dias}' ).mkdir(parents=True, exist_ok=True)
