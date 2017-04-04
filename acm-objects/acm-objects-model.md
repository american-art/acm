# acm-objects1.xml

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300264237`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/ulan/500305326`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _accession_duplicate_
From column: _table / tuple / Unfold: name / titaccessionno / Values_
``` python
return getValue("Values")
```

#### _row_uri_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_table_tuple_atom / content_
``` python
return "object/"+getValue("content")
```

#### _dimension_uri_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_table_tuple_atom / row_uri_
``` python
return "object/"+getValue("content")+"/dimension"
```

#### _time_uri_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_table_tuple_atom / dimension_uri_
``` python
return "object/"+getValue("content")+"/year"
```

#### _accession_uri_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_table_tuple_atom / time_uri_
``` python
return "object/"+getValue("content")+"/accession"
```

#### _url_uri_
From column: _table / tuple / Unfold: name / url / Values_
``` python
return getValue("Values")
```

#### _materials_uri_
From column: _table / tuple / Unfold: name / medmedium / Values_
``` python
return UM.uri_from_fields("thesauri/title/",getValue("Values"))
```

#### _title_uri_
From column: _table / tuple / Unfold: name / titmaintitle / Values_
``` python
return UM.uri_from_fields("thesauri/title/",getValue("Values"))
```

#### _material_uri_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_table_tuple_atom / row_uri_
``` python
return getValue("row_uri")+"/materials"
```

#### _physical_thing_uri_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_table_tuple_atom / material_uri_
``` python
return getValue("row_uri")+"/physical_thing"
```

#### _production_uri_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_table_tuple_atom / physical_thing_uri_
``` python
return getValue("row_uri")+"/production_uri"
```

#### _title_uri_main_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_table_tuple_atom / production_uri_
``` python
return getValue("row_uri")+"/title"
```

#### _title_duplicate_
From column: _table / tuple / Unfold: name / titmaintitle / Values_
``` python
return getValue("Values")
```

#### _acession_uri_
From column: _table / tuple / Unfold: name / titaccessionno / accession_duplicate_
``` python
return UM.uri_from_fields("object/",getValue("Values"))
```

#### _duplicate_title_uri_
From column: _table / tuple / Unfold: name / titmaintitle / title_uri_
``` python
return UM.uri_from_fields("thesauri/row_uri/",getValue("Values"))
```

#### _production_uri1_
From column: _table / tuple / Unfold: name / titmaintitle / title_uri_
``` python
return UM.uri_from_fields("production/",getValue("Values"))
```

#### _physical_thing_
From column: _table / tuple / Unfold: name / titmaintitle / production_uri1_
``` python
return UM.uri_from_fields("physical_thing/",getValue("Values"))
```

#### _dimension_uri1_
From column: _table / tuple / Unfold: name / titmaintitle / physical_thing_
``` python
return UM.uri_from_fields("dimension/",getValue("Values"))
```

#### _time_span_uri_
From column: _table / tuple / Unfold: name / titmaintitle / dimension_uri1_
``` python
return UM.uri_from_fields("time_span/",getValue("Values"))
```

#### _material_uri1_
From column: _table / tuple / Unfold: name / titmaintitle / time_span_uri_
``` python
return UM.uri_from_fields("material/",getValue("Values"))
```

#### _url_uri+123_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_table_tuple_atom / row_uri_
``` python
return "object/"+getValue("content")+"/url/"
```

#### _url_uri_1234_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_table_tuple_atom / row_uri_
``` python
return "object/"+getValue("content")+"/url"
```

#### _row_uri_new_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_Unfold: name_titaccessionno_Values_
``` python
if getValue("table_tuple_Glue_1_table_tuple_Unfold: name_titaccessionno_Values"):
    return 'object/'+SM.fingerprint_string(getValue("table_tuple_Glue_1_table_tuple_Unfold: name_titaccessionno_Values"))
else:
    return ""
```

#### _url_uri_new_
From column: _table / tuple / Glue_1 / Glue_1 / row_uri_new_
``` python
return 'object/'+SM.fingerprint_string(getValue("table_tuple_Glue_1_table_tuple_Unfold: name_titaccessionno_Values"))+'/url/'
```

#### _ProductionURI_
From column: _table / tuple / Glue_1 / Glue_1 / row_uri_new_
``` python
return getValue("row_uri_new")+"/production"
```

#### _MediumURI_
From column: _table / tuple / Glue_1 / Glue_1 / ProductionURI_
``` python
return getValue("row_uri_new")+"/medium"
```

#### _TimeSpanURI_
From column: _table / tuple / Glue_1 / Glue_1 / ProductionURI_
``` python
return getValue("row_uri_new")+"/timespan"
```

#### _Dimension_
From column: _table / tuple / Glue_1 / Glue_1 / MediumURI_
``` python
return getValue("row_uri_new")+"/dimension"
```

#### _OwnerURI_
From column: _table / tuple / Glue_1 / Glue_1 / row_uri_new_
``` python
return "http://data.americanartcollaborative.org/acm"
```

#### _OwnerLabel_
From column: _table / tuple / Glue_1 / Glue_1 / OwnerURI_
``` python
return "Amon Carter Museum of American Art"
```

#### _PrefIdURI_
From column: _table / tuple / Unfold: name / titaccessionno / accession_duplicate_
``` python
if getValue("Values"):
    return "object/"+SM.fingerprint_string(getValue("Values"))+"/id"
else:
    return ""
```


## Selections
#### _DEFAULT_TEST_
From column: _table / tuple / Glue_1 / Glue_1 / table_tuple_Glue_1_table_tuple_Unfold: name_medtechnique_Values_
<br>Operation: `Union`
``` python
return getValue("table_tuple_Glue_1_table_tuple_Unfold: name_titaccessionno_Values") == ''
```


## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _MediumURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _OwnerLabel_ | `rdfs:label` | `crm:E40_Legal_Body1`|
| _OwnerURI_ | `uri` | `crm:E40_Legal_Body1`|
| _PrefIdURI_ | `uri` | `crm:E42_Identifier1`|
| _ProductionURI_ | `uri` | `crm:E12_Production2`|
| _TimeSpanURI_ | `uri` | `crm:E52_Time-Span1`|
| _Values_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _Values_ | `rdf:value` | `crm:E35_Title1`|
| _Values_ | `rdfs:label` | `foaf:Document1`|
| _Values_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _Values_ | `rdfs:label` | `crm:E42_Identifier1`|
| _accession_duplicate_ | `rdf:value` | `crm:E42_Identifier1`|
| _row_uri_new_ | `uri` | `crm:E22_Man-Made_Object1`|
| _title_duplicate_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _title_uri_ | `uri` | `crm:E35_Title1`|
| _url_uri_ | `uri` | `foaf:Document1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production2` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production2`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P52_has_current_owner` | `crm:E40_Legal_Body1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300264237`|
| `crm:E35_Title1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E40_Legal_Body1` | `skos:exactMatch` | `http://vocab.getty.edu/ulan/500305326`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
