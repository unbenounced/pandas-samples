# Count how many claims submitted in December 2021 are still pending. A claim is pending when it has neither an acceptance nor rejection date.

# eric 
import pandas as pd
cvs_claims.loc[(cvs_claims['date_accepted'].isna()) & (cvs_claims['date_rejected'].isna()) & (cvs_claims['date_submitted'].dt.to_period("M") == '2021-12')]["claim_id"].count()

# strata
filtered_claims = cvs_claims[(pd.to_datetime(cvs_claims['date_submitted']).dt.to_period('M') == '2021-12') & (cvs_claims['date_accepted'].isna()) & (cvs_claims['date_rejected'].isna())]
result = filtered_claims.shape[0]