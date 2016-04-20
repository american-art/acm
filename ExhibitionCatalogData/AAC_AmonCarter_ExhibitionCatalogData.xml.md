## AAC_AmonCarter_ExhibitionCatalogData.xml

### PyTransforms
#### _CitedNameURI_
From column: _table / tuple / table / tuple / tuple / Unfold: name / namcitedname / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _FullNameURI_
From column: _table / tuple / table / tuple / tuple / Unfold: name / namfullname / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _ReferenceTypeURI_
From column: _table / tuple / table / tuple / table / tuple / Unfold: name / catreftype / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _ReferenceValueURI_
From column: _table / tuple / table / tuple / table / tuple / Unfold: name / catrefvalue / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _ReferenceNameURI_
From column: _table / tuple / table / tuple / table / tuple / Unfold: name / namcitedname / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _ReferenceFullNameURI_
From column: _table / tuple / table / tuple / table / tuple / Unfold: name / namfullname / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _TitleURI_
From column: _table / tuple / table / tuple / Unfold: name / cattitle / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _ReferenceNumberURI_
From column: _table / tuple / table / tuple / Unfold: name / internalreferencenumber / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _PublicationCityURI_
From column: _table / tuple / table / tuple / Unfold: name / catpublicationcity / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _PublicationDateURI_
From column: _table / tuple / table / tuple / Unfold: name / catpublicationdate / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _CitedNameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _FullNameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _PublicationCityURI_ | `uri` | `dct:Location1`|
| _PublicationDateURI_ | `uri` | `crm:E52_Time-Span1`|
| _ReferenceFullNameURI_ | `uri` | `crm:E39_Actor1`|
| _ReferenceNameURI_ | `uri` | `crm:E41_Appellation1`|
| _ReferenceNumberURI_ | `uri` | `crm:E42_Identifier1`|
| _ReferenceTypeURI_ | `uri` | `crm:E55_Type1`|
| _ReferenceValueURI_ | `uri` | `crm:E84_Information_Carrier1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E35_Title1` | `crm:P105_right_held_by` | `crm:E39_Actor2`|
| `crm:E35_Title1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E35_Title1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E35_Title1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E35_Title1` | `crm:P53_has_former_or_current_location` | `dct:Location1`|
| `crm:E39_Actor2` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E39_Actor2` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation2`|
| `crm:E55_Type1` | `crm:P137i_is_exemplified_by` | `crm:E39_Actor1`|
| `crm:E55_Type1` | `crm:P1_is_identified_by` | `crm:E41_Appellation1`|
| `crm:E55_Type1` | `crm:P1_is_identified_by` | `crm:E84_Information_Carrier1`|
