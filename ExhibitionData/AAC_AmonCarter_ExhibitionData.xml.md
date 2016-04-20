## AAC_AmonCarter_ExhibitionData.xml

### PyTransforms
#### _ExhibitionNameURI_
From column: _table / tuple / table / tuple / Unfold: name / namfullname / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _ExhibitionRecordURI_
From column: _table / tuple / table / tuple / Unfold: name / internalrecordnumber / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    getValue("Values")
```

#### _ExhibitTitleURI_
From column: _table / tuple / Unfold: name / eveeventtitle / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    getValue("Values")
```

#### _CompletionDateURI_
From column: _table / tuple / Unfold: name / datcompletiondate / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    getValue("Values")
```

#### _CommencementDateURI_
From column: _table / tuple / Unfold: name / datcommencementdate / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _CommencementDateURI_ | `uri` | `crm:E52_Time-Span2`|
| _CompletionDateURI_ | `uri` | `crm:E52_Time-Span1`|
| _ExhibitTitleURI_ | `uri` | `crm:E78_Collection1`|
| _ExhibitionNameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _ExhibitionRecordURI_ | `uri` | `crm:E39_Actor1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E78_Collection1` | `crm:P109_has_current_or_former_curator` | `crm:E39_Actor1`|
| `crm:E78_Collection1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E78_Collection1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
