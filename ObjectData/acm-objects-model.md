# AAC_AmonCarter_ObjectData.xml

## Add Column

## Add Node/Literal
#### Literal Node: `aat:300312355`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
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
| _Values_ | `skos:prefLabel` | `crm:E57_Material1`|
| _Values_ | `rdf:value` | `crm:E35_Title1`|
| _Values_ | `crm:P91_has_unit` | `crm:E54_Dimension1`|
| _Values_ | `rdfs:label` | `foaf:Document1`|
| _Values_ | `rdf:value` | `crm:E54_Dimension1`|
| _Values_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _Values_ | `rdfs:label` | `crm:E42_Identifier1`|
| _accession_duplicate_ | `rdf:value` | `crm:E42_Identifier1`|
| _accession_uri_ | `uri` | `crm:E42_Identifier1`|
| _dimension_uri_ | `uri` | `crm:E54_Dimension1`|
| _material_uri_ | `uri` | `crm:E57_Material1`|
| _physical_thing_uri_ | `uri` | `crm:E18_Physical_Thing1`|
| _production_uri_ | `uri` | `crm:E12_Production2`|
| _row_uri_ | `uri` | `crm:E22_Man-Made_Object1`|
| _time_uri_ | `uri` | `crm:E52_Time-Span1`|
| _title_uri_ | `uri` | `crm:E35_Title1`|
| _url_uri_ | `uri` | `foaf:Document1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production2` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E18_Physical_Thing1` | `crm:P43_has_dimension` | `crm:E54_Dimension1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production2`|
| `crm:E22_Man-Made_Object1` | `crm:P46_is_composed_of` | `crm:E18_Physical_Thing1`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
