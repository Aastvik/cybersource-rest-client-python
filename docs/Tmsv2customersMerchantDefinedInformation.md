# Tmsv2customersMerchantDefinedInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The number you assign as the name for your merchant-defined data or secure field. Possible Values are data1 to data4 and sensitive1 to sensitive4  For example, to set the name for merchant-defined data 2 field, you would reference merchantDefinedInformation[x].name as data2 Possible Values: - data1 - data2 - data3 - data4 - sensitive1 - sensitive2 - sensitive3 - sensitive4  | [optional] 
**value** | **str** | The value you assign for your merchant-defined data field.  **Warning** Merchant-defined data fields are not intended to and must not be used to capture personally identifying information. Accordingly, merchants are prohibited from capturing, obtaining, and/or transmitting any personally identifying information in or via the merchant-defined data fields. Personally identifying information includes, but is not limited to, address, credit card number, social security number, driver&#39;s license number, state-issued identification number, passport number, and card verification numbers (CVV, CVC2, CVV2, CID, CVN). In the event it is discovered a merchant is capturing and/or transmitting personally identifying information via the merchant-defined data fields, whether or not intentionally, the merchant&#39;s account will immediately be suspended, which will result in a rejection of any and all transaction requests submitted by the merchant after the point of suspension.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


