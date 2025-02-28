# Ptsv1pushfundstransferMerchantDefinedInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The number you assign for as the key for your merchant-defined data field. Valid values are 0 to 100.  For example, to set or access the key for the 2nd merchant-defined data field in the array, you would reference merchantDefinedInformation[1].key.  For Mastercard Send: Name to be displayed in the reconciliation report for this disbursement. This value will appear as a header in the column name of the report.  | [optional] 
**value** | **str** | The value you assign for your merchant-defined data field.  For details, see merchant_defined_data1 field description in the Credit Card Services Using the SCMP API Guide.  Warning Merchant-defined data fields are not intended to and must not be used to capture personally identifying information. Accordingly, merchants are prohibited from capturing, obtaining, and/or transmitting any personally identifying information in or via the merchant-defined data fields. Personally identifying information includes, but is not limited to, address, credit card number, social security number, driver&#39;s license number, state-issued identification number, passport number, and card verification numbers (CVV, CVC2, CVV2, CID, CVN). In the event CyberSource discovers that a merchant is capturing and/or transmitting personally identifying information via the merchant-defined data fields, whether or not intentionally, CyberSource will immediately suspend the merchant&#39;s account, which will result in a rejection of any and all transaction requests submitted by the merchant after the point of suspension.  For Mastercard Send: Value to be displayed in the reconciliation report for this disbursement.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


