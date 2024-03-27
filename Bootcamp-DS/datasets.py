import yfinance as yf
import pandas as pd
import os 



list_paths = {
  "./datos_AAPL.csv": "AAPL",
  "./datos_SPY.csv": "SPY",
  "./datos_BTC-USD.csv": "BTC-USD",
}

for i in list_paths:
  
  if not os.path.exists(i):
    datos = yf.download(list_paths[i], start="2014-01-01", end="2024-03-01")
    datos.to_csv(f"datos_{list_paths[i]}.csv", index=True)
    
    dt_frame = pd.read_csv(i)
    if not os.path.exists("datasets.xlsx"):
      with pd.ExcelWriter("datasets.xlsx", engine='openpyxl') as writer:
        dt_frame.to_excel(writer, sheet_name=list_paths[i], index=True)
    else:
      with pd.ExcelWriter("datasets.xlsx", engine='openpyxl', mode='a') as writer:
        dt_frame.to_excel(writer, sheet_name=list_paths[i], index=True)
  else: 
    print("El archivo ya existe")
  
      
