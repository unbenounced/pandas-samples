#You've been asked by Amazon to find the shipment_id and weight of the third heaviest shipment.
#Output the shipment_id, and total_weight for that shipment_id.
#In the event of a tie, do not skip ranks.

#eric
# Import your libraries
import pandas as pd

# Start writing code
ranked = amazon_shipment.groupby("shipment_id", as_index=False)["weight"].sum().reset_index()


ranked["weight_rank"] = ranked["weight"].rank(ascending=False)

ranked.loc[(ranked["weight_rank"] > 2) &(ranked["weight_rank"] < 4)][["shipment_id", "weight"]]

#strata
import pandas as pd
import numpy as np

shipment_weights = (
    amazon_shipment.groupby("shipment_id")["weight"]
    .sum()
    .to_frame("total_weight")
    .reset_index()
)
shipment_weights["rank"] = shipment_weights["total_weight"].rank(
    method="dense", ascending=False
)
result = shipment_weights[["shipment_id", "total_weight"]][
    shipment_weights["rank"] == 3
]

#solutions from other user
result = (
    amazon_shipment
    .groupby('shipment_id')['weight']
    .sum()
    .to_frame('total_weight')
    .reset_index()
    .assign(rank = lambda a: a['total_weight'].rank(method='dense',ascending=False))
    .query('rank == 3')
    .filter(items=['shipment_id','total_weight'])
    )

