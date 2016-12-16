# AAC_AmonCarter_ArtistData.xml

## Add Column

## Add Node/Literal
#### Literal Node: `aat:300404670`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `aat:300379842`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`

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
return UM.uri_from_fields("thesauri/artist_name/",getValue("Values"))
```

#### _nationality_uri_
From column: _table / tuple / table / tuple / Unfold: name / bionationality / Values_
``` python
return UM.uri_from_fields("thesauri/nationality/",getValue("Values"))
```

#### _row_uri_
From column: _table / tuple / table / tuple / Unfold: name / internalrecordnumber / Values_
``` python
return "object/"+getValue("Values")
```

#### _birthdate_uri_
From column: _table / tuple / table / tuple / Unfold: name / Glue_1 / table_tuple_table_tuple_Unfold: name_biobirthearliestdate_Values_
``` python
return  getValue("table_tuple_table_tuple_Unfold: name_internalrecordnumber_row_uri") +"/birthdate/" + getValue("table_tuple_table_tuple_Unfold: name_biobirthearliestdate_Values")
```

#### _birthplace_uri_
From column: _table / tuple / table / tuple / Unfold: name / biobirthplace / Values_
``` python
return UM.uri_from_fields("thesauri/birthplace/",getValue("Values"))
```

#### _deathplace_uri_
From column: _table / tuple / table / tuple / Unfold: name / biodeathplace / Values_
``` python
return UM.uri_from_fields("thesauri/deathplace/",getValue("Values"))
```

#### _sex_uri_
From column: _table / tuple / table / tuple / Unfold: name / namsex / Values_
``` python
return UM.uri_from_fields("thesauri/sex/",getValue("Values"))

```

#### _deathdate_uri_
From column: _table / tuple / table / tuple / Unfold: name / Glue_2 / table_tuple_table_tuple_Unfold: name_internalrecordnumber_row_uri_
``` python
return getValue("table_tuple_table_tuple_Unfold: name_internalrecordnumber_row_uri") + "/deathdate/"+ getValue("table_tuple_table_tuple_Unfold: name_biodeathdate_Values")
```

#### _name_duplicate_
From column: _table / tuple / table / tuple / Unfold: name / namfullname / Values_
``` python
return getValue("Values")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Values_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _Values_ | `rdfs:label` | `crm:E74_Group1`|
| _Values_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _Values_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _Values_ | `rdfs:label` | `crm:E53_Place2`|
| _Values_ | `skos:prefLabel` | `crm:E55_Type1`|
| _Values_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _Values_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span2`|
| _Values_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _Values_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span2`|
| _Values_ | `rdfs:label` | `crm:E53_Place1`|
| _artist_name_uri_ | `uri` | `crm:E82_Actor_Appellation1`|
| _birthdate_uri_ | `uri` | `crm:E52_Time-Span1`|
| _birthplace_uri_ | `uri` | `crm:E53_Place1`|
| _deathdate_uri_ | `uri` | `crm:E52_Time-Span2`|
| _deathplace_uri_ | `uri` | `crm:E53_Place2`|
| _name_duplicate_ | `rdfs:label` | `crm:E39_Actor1`|
| _nationality_uri_ | `uri` | `crm:E74_Group1`|
| _row_uri_ | `uri` | `crm:E39_Actor1`|
| _sex_uri_ | `uri` | `crm:E55_Type1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place1`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E64_End_of_Existence1` | `crm:P7_took_place_at` | `crm:E53_Place2`|
| `crm:E74_Group1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300379842`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
