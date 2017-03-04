# acm-artist.xml

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300379842`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _artist_name_uri_
From column: _table / tuple / table / tuple / Unfold: name / namfullname / Values_
``` python
if getValue("Values") != "Unknown":
    return UM.uri_from_fields("thesauri/artist_name/",getValue("Values"))
else:
    return ""
```

#### _nationality_uri_
From column: _table / tuple / table / tuple / Unfold: name / bionationality / Values_
``` python
if getValue("Values"):
    return UM.uri_from_fields("thesauri/nationality/",getValue("Values"))
else:
    return ""
```

#### _row_uri_
From column: _table / tuple / table / tuple / Unfold: name / internalrecordnumber / Values_
``` python
return "artist/"+getValue("Values")
```

#### _birthdate_uri_
From column: _table / tuple / table / tuple / Unfold: name / Glue_1 / table_tuple_table_tuple_Unfold: name_biobirthearliestdate_Values_
``` python
return getValue("table_tuple_table_tuple_Unfold: name_internalrecordnumber_row_uri") +"/birth/date"
```

#### _birthplace_uri_
From column: _table / tuple / table / tuple / Unfold: name / biobirthplace / Values_
``` python
if getValue("Values"):
    return UM.uri_from_fields("thesauri/place/",getValue("Values"))
else:
    return ""
```

#### _deathplace_uri_
From column: _table / tuple / table / tuple / Unfold: name / biodeathplace / Values_
``` python
if getValue("Values"):
    return UM.uri_from_fields("thesauri/place/",getValue("Values"))
else:
    return ""
```

#### _GenderTypeURI_
From column: _table / tuple / table / tuple / Unfold: name / namsex / Values_
``` python
if getValue("Values"):
    return UM.uri_from_fields("thesauri/sex/",getValue("Values"))
else:
    return ""

```

#### _deathdate_uri_
From column: _table / tuple / table / tuple / Unfold: name / Glue_2 / table_tuple_table_tuple_Unfold: name_internalrecordnumber_row_uri_
``` python
return getValue("table_tuple_table_tuple_Unfold: name_internalrecordnumber_row_uri") + "/death/date"
```

#### _End_Existence1_uri_
From column: _table / tuple / table / tuple / Unfold: name / Glue_2 / deathdate_uri_
``` python
if getValue("table_tuple_table_tuple_Unfold: name_biodeathdate_Values"):
    return getValue("table_tuple_table_tuple_Unfold: name_internalrecordnumber_row_uri") + "/death"
else:
    return ""
```

#### _begin_existence1_uri_
From column: _table / tuple / table / tuple / Unfold: name / Glue_1 / birthdate_uri_
``` python
if getValue("table_tuple_table_tuple_Unfold: name_biobirthearliestdate_Values"):
    return  getValue("table_tuple_table_tuple_Unfold: name_internalrecordnumber_row_uri") +"/birth"
else:
    return ""
```

#### _name_duplicate_
From column: _table / tuple / table / tuple / Unfold: name / namfullname / Values_
``` python
return getValue("Values")
```

#### _GenderURI_
From column: _table / tuple / table / tuple / Unfold: name / namsex / GenderTypeURI_
``` python
if getValue("Values"):
    return "thesauri/gender"
else:
    return ""

```

#### _GenderURI_in_use_
From column: _table / tuple / table / tuple / Unfold: name / internalrecordnumber / row_uri_
``` python
if getValue("Values"):
    return getValue("row_uri")+"/gender"
else:
    return ""

```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _End_Existence1_uri_ | `uri` | `crm:E64_End_of_Existence1`|
| _GenderTypeURI_ | `uri` | `crm:E55_Type2`|
| _GenderURI_in_use_ | `uri` | `crm:E55_Type1`|
| _Values_ | `rdfs:label` | `crm:E74_Group1`|
| _Values_ | `rdfs:label` | `crm:E53_Place1`|
| _Values_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span2`|
| _Values_ | `rdfs:label` | `crm:E55_Type1`|
| _Values_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span2`|
| _Values_ | `rdfs:label` | `crm:E53_Place2`|
| _Values_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _Values_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _Values_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _Values_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _Values_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _artist_name_uri_ | `uri` | `crm:E82_Actor_Appellation1`|
| _begin_existence1_uri_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _birthdate_uri_ | `uri` | `crm:E52_Time-Span1`|
| _birthplace_uri_ | `uri` | `crm:E53_Place1`|
| _deathdate_uri_ | `uri` | `crm:E52_Time-Span2`|
| _deathplace_uri_ | `uri` | `crm:E53_Place2`|
| _name_duplicate_ | `rdfs:label` | `crm:E39_Actor1`|
| _nationality_uri_ | `uri` | `crm:E74_Group1`|
| _row_uri_ | `uri` | `crm:E39_Actor1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E55_Type1` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E64_End_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place2`|
| `crm:E74_Group1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300379842`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
