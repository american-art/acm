## AAC_AmonCarter_ObjectData.xml

### PyTransforms
#### _CreditLineURI_
From column: _table / tuple / tuple / Unfold: name / acqcreditline / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _InternalRecordNumURI_
From column: _table / tuple / table / tuple / Unfold: name / internalrecordnumber / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _MediumURI_
From column: _table / tuple / Unfold: name / medmedium / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _ParentTitleURI_
From column: _table / tuple / Unfold: name / titparenttitle / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _MainTitleURI_
From column: _table / tuple / Unfold: name / titmaintitle / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _RoleURI_
From column: _table / tuple / Unfold: name / crerole_tab / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _MetricUnitURI_
From column: _table / tuple / Unfold: name / medunitmetric_tab / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _UrlURI_
From column: _table / tuple / Unfold: name / url / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _FormatURI_
From column: _table / tuple / Unfold: name / medformat / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _UnitURI_
From column: _table / tuple / Unfold: name / medunit_tab / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _MeasurementURI_
From column: _table / tuple / Unfold: name / medvalue_tab / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _EditionURI_
From column: _table / tuple / Unfold: name / ediedition / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _MediumTypeURI_
From column: _table / tuple / Unfold: name / medobjecttype / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _TechniqueURI_
From column: _table / tuple / Unfold: name / medtechnique / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _MetricMeasurementURI_
From column: _table / tuple / Unfold: name / medvaluemetric_tab / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _DateCreatedURI_
From column: _table / tuple / Unfold: name / credatecreated_tab / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _AccessionNumberURI_
From column: _table / tuple / Unfold: name / titaccessionno / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _CollectionNameURI_
From column: _table / tuple / Unfold: name / woracmcollectionname / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _MeasurementTypeURI_
From column: _table / tuple / Unfold: name / medtype_tab / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```

#### _CopyrightURI_
From column: _table / tuple / Unfold: name / refcopyright_tab / Values_
>``` python
if getValue("Values") == 'NULL':
    return " "
else:
    return getValue("Values")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AccessionNumberURI_ | `uri` | `crm:E73_Information_Object2`|
| _CollectionNameURI_ | `uri` | `crm:E78_Collection1`|
| _CopyrightURI_ | `uri` | `crm:E39_Actor2`|
| _CreditLineURI_ | `uri` | `crm:E39_Actor1`|
| _DateCreatedURI_ | `uri` | `crm:E65_Creation1`|
| _EditionURI_ | `uri` | `crm:E73_Information_Object1`|
| _FormatURI_ | `uri` | `crm:E29_Design_or_Procedure3`|
| _InternalRecordNumURI_ | `uri` | `crm:E35_Title1`|
| _MainTitleURI_ | `uri` | `crm:E35_Title1`|
| _MeasurementTypeURI_ | `uri` | `crm:E55_Type1`|
| _MeasurementURI_ | `uri` | `crm:E16_Measurement1`|
| _MediumTypeURI_ | `uri` | `crm:E29_Design_or_Procedure2`|
| _MediumURI_ | `uri` | `dct:PhysicalMedium1`|
| _MetricMeasurementURI_ | `uri` | `crm:E16_Measurement2`|
| _MetricUnitURI_ | `uri` | `crm:E58_Measurement_Unit2`|
| _ParentTitleURI_ | `uri` | `crm:E35_Title2`|
| _RoleURI_ | `uri` | `crm:E74_Group1`|
| _TechniqueURI_ | `uri` | `crm:E29_Design_or_Procedure1`|
| _UnitURI_ | `uri` | `crm:E58_Measurement_Unit1`|
| _UrlURI_ | `uri` | `crm:E84_Information_Carrier1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E16_Measurement1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E16_Measurement1` | `crm:P2_has_type` | `crm:E58_Measurement_Unit1`|
| `crm:E16_Measurement2` | `crm:P2_has_type` | `crm:E58_Measurement_Unit2`|
| `crm:E35_Title1` | `crm:P105_right_held_by` | `crm:E39_Actor2`|
| `crm:E35_Title1` | `crm:P106i_forms_part_of` | `crm:E35_Title2`|
| `crm:E35_Title1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E35_Title1` | `crm:P10_falls_within` | `crm:E78_Collection1`|
| `crm:E35_Title1` | `crm:P148_has_component` | `dct:PhysicalMedium1`|
| `crm:E35_Title1` | `crm:P148_has_component` | `crm:E73_Information_Object1`|
| `crm:E35_Title1` | `crm:P1_is_identified_by` | `crm:E84_Information_Carrier1`|
| `crm:E35_Title1` | `crm:P39i_was_measured_by` | `crm:E16_Measurement1`|
| `crm:E35_Title1` | `crm:P39i_was_measured_by` | `crm:E16_Measurement2`|
| `crm:E35_Title1` | `crm:P4_has_time-span` | `crm:E65_Creation1`|
| `crm:E35_Title1` | `crm:P51_has_former_or_current_owner` | `crm:E39_Actor1`|
| `crm:E35_Title1` | `crm:P67i_is_referred_to_by` | `crm:E73_Information_Object2`|
| `dct:PhysicalMedium1` | `crm:P32_used_general_technique` | `crm:E29_Design_or_Procedure1`|
| `dct:PhysicalMedium1` | `crm:P32_used_general_technique` | `crm:E29_Design_or_Procedure2`|
| `dct:PhysicalMedium1` | `crm:P32_used_general_technique` | `crm:E29_Design_or_Procedure3`|
