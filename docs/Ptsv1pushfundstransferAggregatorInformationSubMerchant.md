# Ptsv1pushfundstransferAggregatorInformationSubMerchant

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID you assigned to your sub-merchant.  FDC Compass: This value must consist of uppercase characters.  Visa Platform Connect with Mastercard: String (15) FDC Compass: String (20)  | [optional] 
**name** | **str** | Sub-merchant&#39;s business name.  Visa Platform Connect With American Express, the maximum length of the sub-merchant name depends on the length of the aggregator name. The combined length for both values must not exceed 36 characters. The value for this field does not map to the TC 33 capture file5.  FDC Compass This value must consist of uppercase characters.  | [optional] 
**address1** | **str** | First line of the sub-merchant&#39;s street address.  Visa Platform Connect The value for this field does not map to the TC 33 capture file5.  FDC Compass This value must consist of uppercase characters.  | [optional] 
**locality** | **str** | Sub-merchant&#39;s city.  For processor-specific details, see submerchant_city request field description in Credit Card Services Using the SCMP API.  Visa Platform Connect The value for this field does not map to the TC 33 capture file5.  FDC Compass This value must consist of uppercase characters.  | [optional] 
**administrative_area** | **str** | Sub-merchant&#39;s state or province. See https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf  Visa Platform Connect The value for this field does not map to the TC 33 capture file.  FDC Compass This value must consist of uppercase characters.  | [optional] 
**postal_code** | **str** | Partial postal code for the sub-merchant&#39;s address.  For processor-specific details, see submerchant_postal_code request field description in Credit Card Services Using the SCMP API.  Visa Platform Connect The value for this field does not map to the TC 33 capture file5.  FDC Compass This value must consist of uppercase characters.  | [optional] 
**country** | **str** | Sub-merchant&#39;s country. Use the ISO Standard numeric Country Codes.  See https://developer.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf  Visa Platform Connect The value for this field does not map to the TC 33 capture file.  FDC Compass This value must consist of uppercase characters.  | [optional] 
**email** | **str** | Sub-merchant&#39;s email address.  CyberSource through VisaNet | With American Express, the value for this field corresponds to the following data in the TC 33 capture file:  - Record: CP01 TCRB - Position: 25-64 - Field: American Express Seller E-mail Address - Note The TC 33 Capture file contains information about the purchases and refunds that a merchant submits to CyberSource. CyberSource through VisaNet creates the TC 33 Capture file at the end of the day and sends it to the merchant&#39;s acquirer, who uses this information to facilitate end-of-day clearing processing with payment card companies.  | [optional] 
**phone_number** | **str** | Sub-merchant&#39;s telephone number.  Maximum length for procesors  Visa Platform Connect: 20 FDC Compass: 13  FDC Compass This value must consist of uppercase characters. Use one of these recommended formats: NNN-NNN-NNNN NNN-AAAAAAA  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


