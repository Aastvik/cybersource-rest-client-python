# PtsV2PaymentsPost201ResponsePaymentInsightsInformationResponseInsights

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Categorization of response message from processor  Possible Values: - &#x60;APPROVED&#x60; - &#x60;ISSUER_WILL_NEVER_APPROVE&#x60; - &#x60;ISSUER_CANT_APPROVE_AT_THIS_TIME&#x60; - &#x60;ISSUER_CANT_APPROVE_WITH_THESE_DETAILS&#x60; - &#x60;GENERIC_ERROR&#x60; - &#x60;OTHERS&#x60; - &#x60;MATCH_NOT_FOUND&#x60;  | [optional] 
**category_code** | **str** | Categorization Code of response message from processor  Possible Values: - &#x60;01&#x60; : Issuer Will Never Approve - &#x60;02&#x60; : Issuer Can&#39;t Approve at this Time - &#x60;03&#x60; : Issuer Can&#39;t Approve with these Details - &#x60;04&#x60; : Generic Error - &#x60;98&#x60; : Others - &#x60;99&#x60; : Payment Insights Response Category Match Not Found  | [optional] 
**processor_raw_name** | **str** | Raw name of the processor used for the transaction processing, especially useful during acquirer swing to see which processor transaction settled with  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


