# ACMAA_Media_data_final_AAC data set IRNs

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300026687`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _AccessionNo_
``` python
return "object/" + SM.fingerprint_string(getValue("AccessionNo"))
```

#### _UrlLabel_
From column: _ObjectRecordURL_
``` python
return getValue("ObjectRecordURL")
```

#### _CreditURI_
From column: _CreditLine_
``` python
if getValue("CreditLine"):
    return getValue("ObjectURI")+"/credit_line"
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _CreditLine_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _CreditURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _ObjectRecordURL_ | `uri` | `foaf:Document1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _UrlLabel_ | `rdfs:label` | `foaf:Document1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300026687`|
