import pandas as pd
chipotle = pd.read_csv('./chipotle.tsv', sep='\t')
chipotle.head()

chipotle.item_name.value_counts()
chipotle.choice_description.groupby(by=chipotle['item_name']).count()
chipotle.quantity.groupby(by=chipotle['item_name']).count()
chipotle.item_name.groupby(by=chipotle['order_id']).count()
