# Ptsv2paymentsPaymentInformationBankAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Account type.  Possible values:  - **C**: Checking.  - **G**: General ledger. This value is supported only on Wells Fargo ACH.  - **S**: Savings (U.S. dollars only).  - **X**: Corporate checking (U.S. dollars only).  | [optional] 
**number** | **str** | Account number.  When processing encoded account numbers, use this field for the encoded account number.  | [optional] 
**encoder_id** | **str** | Identifier for the bank that provided the customer&#39;s encoded account number.  To obtain the bank identifier, contact your processor.  For details, see &#x60;account_encoder_id&#x60; request-level field description in [Credit Card Services Using the SCMP API.](https://apps.cybersource.com/library/documentation/dev_guides/CC_Svcs_SCMP_API/html/)  | [optional] 
**check_number** | **str** | Check number.  Chase Paymentech Solutions - Optional. CyberSource ACH Service - Not used. RBS WorldPay Atlanta - Optional on debits. Required on credits. TeleCheck - Strongly recommended on debit requests. Optional on credits.  | [optional] 
**check_image_reference_number** | **str** | Image reference number associated with the check. You cannot include any special characters.  | [optional] 
**iban** | **str** | International Bank Account Number (IBAN) for the bank account. For some countries you can provide this number instead of the traditional bank account information. You can use this field only when scoring a direct debit transaction.  For all possible values, see the &#x60;bank_iban&#x60; field description in the _Decision Manager Using the SCMP API Developer Guide_ on the [CyberSource Business Center.](https://ebc2.cybersource.com/ebc2/) Click **Decision Manager** &gt; **Documentation** &gt; **Guides** &gt; _Decision Manager Using the SCMP API Developer Guide_ (PDF link).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


