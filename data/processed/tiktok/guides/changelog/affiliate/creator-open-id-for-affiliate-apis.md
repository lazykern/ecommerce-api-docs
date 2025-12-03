# Summary
This week, we'll be introducing the new **Creator Open ID**, a privacy-preserving identifier used in Affiliate Open APIs. Instead of exposing the plain creator ID (restricted by our privacy policy), we'll instead provide a **pseudonymous, non-reversible** Creator Open ID to external partners.

<span style="color: #D83931">❗ </span><span style="color: #D83931"><strong>Important</strong></span><span style="color: #D83931">: The </span><span style="color: #D83931"><strong>Creator Open ID</strong></span><span style="color: #D83931"> will be implemented with a new version of our Affiliate APIs (202509). For the time being, we will continue to support plain creator IDs simultaneously, but announce a deprecation timeline soon. Please stay tuned for our official communication on the full migration plan!</span>
# Impact
|  |  |
| --- | --- |
| Impacted market(s) | * United States (US) - Local and cross-border <br> * United Kingdom (UK) - Local and cross-border <br> * Southeast Asia (SEA)- Local and cross-border |
| Impacted version(s) | * 202509 (and later) |
# What's new?
The new Creator Open ID seeks to:
– Enable partners to reference creators safely.
– Keep raw, personally identifiable IDs protected and out of external systems.

Creator Open IDs will be **unique per app**, meaning:
– If the **same creator** is accessed by **two different apps**, each app sees a **different** Creator Open ID.
– If **two different sellers** access the **same creator within the same app**, they see the **same** Creator Open ID. 
# Next steps
– Treat the **Creator Open ID** as the **sole primary key** for creators in all Open API integrations.
– **Do not** attempt to map to or persist plain creator IDs.
– **Do not** assume Creator Open IDs can be joined **across apps**; mappings are app-local.
– Expect the ID to be **stable over time within a given app** (barring announced platform changes).