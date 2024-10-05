import pandas as pd

ganancias={"enero":35000,"febrero":20350,"marzo":42370}
miserie=pd.Series(ganancias, index=["enero","febrero"])

print(miserie)