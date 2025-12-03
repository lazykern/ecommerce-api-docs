## Summary
We're making some changes to the API logic in [Get Order Detail](get-order-detail) to address common issues around the different `name`-related parameters.
## Impact
|  |  |
| --- | --- |
| Impacted market(s) | * Brazil (BR) <br> * Mexico (MX) |
| Impacted version(s) | * 202309 (and later) |
## Changes
### Get Order Detail
Currently, when buyers place an order, they provide a `first_name` and `last_name` that are returned in the `recipient_address` response for Get Order Detail. The two parameters are additionally concatenated to return the `name` field:
| `first_name` | `last_name` | `name` |
| --- | --- | --- |
| John | Doe | John Doe |

For the **BR** and **MX** markets, buyers will now only need to provide a single `name`, and the API logic will synchronize this into the `first_name` field as well, leaving the `last_name` field empty:
| `first_name` | `last_name` | `name` |
| --- | --- | --- |
| John Doe |  | John Doe |

We are hoping this will remove some confusion around the difference(s) between these three fields.
## Next steps
Since this is only a logic change, please ensure your logic is still compatible. There are no new or deprecated parameters that need to be supported.