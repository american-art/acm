## AAC_AmonCarter_ArtistData.xml

### PyTransforms
#### _InternalRecordURI_
From column: _table / tuple / table / tuple / Unfold: name / internalrecordnumber / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _FullNameURI_
From column: _table / tuple / table / tuple / Unfold: name / namfullname / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _NationalityURI_
From column: _table / tuple / table / tuple / Unfold: name / bionationality / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _EarliestBirthURI_
From column: _table / tuple / table / tuple / Unfold: name / biobirthearliestdate / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _BirthDateURI_
From column: _table / tuple / table / tuple / Unfold: name / biobirthdate / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _LatestBirthURI_
From column: _table / tuple / table / tuple / Unfold: name / biobirthlatestdate / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _BirthPlaceURI_
From column: _table / tuple / table / tuple / Unfold: name / biobirthplace / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _EarliestDeathURI_
From column: _table / tuple / table / tuple / Unfold: name / biodeathearliestdate / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _DeathDateURI_
From column: _table / tuple / table / tuple / Unfold: name / biodeathdate / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _LatestDeathURI_
From column: _table / tuple / table / tuple / Unfold: name / biodeathlatestdate / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _DeathLocationURI_
From column: _table / tuple / table / tuple / Unfold: name / biodeathplace / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _EthnicityURI_
From column: _table / tuple / table / tuple / Unfold: name / bioethnicity / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _SexURI_
From column: _table / tuple / table / tuple / Unfold: name / namsex / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _SummaryURI_
From column: _table / tuple / table / tuple / Unfold: name / summarydata / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _LabelURI_
From column: _table / tuple / table / tuple / Unfold: name / biolabel / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BirthDateURI_ | `uri` | `crm:E67_Birth2`|
| _BirthPlaceURI_ | `uri` | `dct:Location1`|
| _DeathDateURI_ | `uri` | `crm:E69_Death2`|
| _DeathLocationURI_ | `uri` | `dct:Location2`|
| _EarliestBirthURI_ | `uri` | `crm:E67_Birth1`|
| _EarliestDeathURI_ | `uri` | `crm:E69_Death1`|
| _EthnicityURI_ | `uri` | `crm:E74_Group2`|
| _FullNameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _InternalRecordURI_ | `uri` | `crm:E39_Actor1`|
| _LabelURI_ | `uri` | `crm:E15_Identifier_Assignment1`|
| _LatestBirthURI_ | `uri` | `crm:E67_Birth3`|
| _LatestDeathURI_ | `uri` | `crm:E69_Death3`|
| _NationalityURI_ | `uri` | `crm:E74_Group1`|
| _SexURI_ | `uri` | `crm:E74_Group3`|
| _SummaryURI_ | `uri` | `crm:E82_Actor_Appellation2`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P100i_died_in` | `crm:E52_Time-Span8`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group2`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group3`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E15_Identifier_Assignment1`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation2`|
| `crm:E39_Actor1` | `crm:P53_has_former_or_current_location` | `dct:Location1`|
| `crm:E39_Actor1` | `crm:P53_has_former_or_current_location` | `dct:Location2`|
| `crm:E39_Actor1` | `crm:P98i_was_born` | `crm:E52_Time-Span7`|
| `crm:E52_Time-Span7` | `crm:P4i_is_time-span_of` | `crm:E67_Birth1`|
| `crm:E52_Time-Span7` | `crm:P4i_is_time-span_of` | `crm:E67_Birth2`|
| `crm:E52_Time-Span7` | `crm:P4i_is_time-span_of` | `crm:E67_Birth3`|
| `crm:E52_Time-Span8` | `crm:P4i_is_time-span_of` | `crm:E69_Death1`|
| `crm:E52_Time-Span8` | `crm:P4i_is_time-span_of` | `crm:E69_Death2`|
| `crm:E52_Time-Span8` | `crm:P4i_is_time-span_of` | `crm:E69_Death3`|
