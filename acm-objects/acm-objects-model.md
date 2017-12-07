# acm-objects1.xml

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300264237`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300312355`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300179869`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300055547`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `"http://vocab.getty.edu/ulan/500305326"`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _table / tuple / Unfold: name / titaccessionno / Values_
``` python
x = getValue("Values")
x = SM.alpha_numeric(SM.ascii_chars(x)).lower()
y = list(x.split())
y = '_'.join(y)
return "object/" + y
```

#### _TitleURI_
From column: _table / tuple / Unfold: name / titmaintitle / Values_
``` python
objecturi = getValueFromNestedColumnByIndex("Unfold: name", "titaccessionno/ObjectURI", getRowIndex())
if getValue("Values"):
    return UM.uri_from_fields(objecturi+"/", getValue("Values"))
else:
    return ""
```

#### _TitleLabel_
From column: _table / tuple / Unfold: name / titmaintitle / Values_
``` python
if getValue("Values"):
    return getValue("Values")
else:
    return ""
```

#### _Acc_No_URI_
From column: _table / tuple / Unfold: name / titaccessionno / Values_
``` python
return getValue("ObjectURI")+"/acc_no"
```

#### _MediumURI_
From column: _table / tuple / Unfold: name / medmedium / Values_
``` python
objecturi = getValueFromNestedColumnByIndex("Unfold: name", "titaccessionno/ObjectURI", getRowIndex())
if getValue("Values"):
    return objecturi + "/medium"
else:
    return ""
```

#### _Values_
From column: _table / tuple / Unfold: name / url / Values_
``` python
return getValue("Values")
```

#### _UrlURI_
From column: _table / tuple / Unfold: name / url / Values_
``` python
if getValue("Values"):
    return getValue("Values")
else:
    return ""
```

#### _StartDate_
From column: _table / tuple / Unfold: name / credatecreated_tab / Values_
``` python
if getValue("Values"):
    return getValue("Values")+"-01-01"
else:
    return ""
```

#### _EndDate_
From column: _table / tuple / Unfold: name / credatecreated_tab / StartDate_
``` python
if getValue("Values"):
    return getValue("Values")+"-31-12"
else:
    return ""
```

#### _DateLabel_
From column: _table / tuple / Unfold: name / credatecreated_tab / Values_
``` python
if getValue("Values"):
    return getValue("Values")
else:
    return ""
```

#### _ProductionURI_
From column: _table / tuple / Unfold: name / titaccessionno / ObjectURI_
``` python
date = getValueFromNestedColumnByIndex("Unfold: name", "credatecreated_tab/Values", getRowIndex())
if date:
    return getValue("ObjectURI")+"/production"
else:
    return ""
```

#### _TimespanURI_
From column: _table / tuple / Unfold: name / credatecreated_tab / Values_
``` python
productionuri = getValueFromNestedColumnByIndex("Unfold: name", "titaccessionno/ProductionURI", getRowIndex())
if getValue("Values"):
    return productionuri+"/timespan"
else:
    return ""
```

#### _ClassificationURI_
From column: _table / tuple / Unfold: name / medobjecttype / Values_
``` python
objecturi = getValueFromNestedColumnByIndex("Unfold: name", "titaccessionno/ObjectURI", getRowIndex())
if getValue("Values"):
    return objecturi+"/classification"
else:
    return ""
```

#### _TypeURI_
From column: _table / tuple / Unfold: name / medobjecttype / ClassificationURI_
``` python
if getValue("Values"):
    return UM.uri_from_fields("thesauri/classification/",getValue("Values"))
else:
    return ""
```

#### _RightsURI_
From column: _table / tuple / Unfold: name / refcopyright_tab / Values_
``` python
objecturi = getValueFromNestedColumnByIndex("Unfold: name", "titaccessionno/ObjectURI", getRowIndex())
if getValue("Values"):
    return objecturi+"/rights"
else:
    return ""
```

#### _ArtistURI_
From column: _table / tuple / content_Aggregation3_
``` python
return "artist/"+getValue("content_Aggregation3").split(';')[1]
```

#### _OwnerURI_
From column: _table / tuple / Unfold: name / titaccessionno / ObjectURI_
``` python
return "http://data.cartermuseum.org"
```

#### _OwnerLabel_
From column: _table / tuple / Unfold: name / titaccessionno / OwnerURI_
``` python
return "The Amon Carter"
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Acc_No_URI_ | `uri` | `crm:E42_Identifier1`|
| _ArtistURI_ | `uri` | `crm:E39_Actor1`|
| _ClassificationURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _DateLabel_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _EndDate_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _MediumURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _OwnerLabel_ | `rdfs:label` | `crm:E40_Legal_Body1`|
| _OwnerURI_ | `uri` | `crm:E40_Legal_Body1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _RightsURI_ | `uri` | `crm:E33_Linguistic_Object2`|
| _StartDate_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _TimespanURI_ | `uri` | `crm:E52_Time-Span1`|
| _TitleLabel_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _TypeURI_ | `uri` | `crm:E55_Type1`|
| _UrlURI_ | `uri` | `foaf:Document1`|
| _Values_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _Values_ | `rdf:value` | `crm:E35_Title1`|
| _Values_ | `rdfs:label` | `foaf:Document1`|
| _Values_ | `rdfs:label` | `crm:E55_Type1`|
| _Values_ | `rdf:value` | `crm:E42_Identifier1`|
| _Values_ | `rdf:value` | `crm:E33_Linguistic_Object2`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor1`|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `http://vocab.getty.edu/aat/300179869`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object2`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P52_has_current_owner` | `crm:E40_Legal_Body1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300264237`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300055547`|
| `crm:E35_Title1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E40_Legal_Body1` | `skos:exactMatch` | `http://vocab.getty.edu/ulan/500305326`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300312355`|
