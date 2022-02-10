from ontotools.normalize import normalize, get_topbraid_metadata


content = """# baseURI: https://w3id.org/tern/ontologies/tern/
# imports: http://datashapes.org/dash
# imports: http://qudt.org/schema/qudt/
# imports: http://rdfs.org/ns/void
# imports: http://www.w3.org/2002/07/owl#
# imports: http://www.w3.org/2004/02/skos/core#
# imports: http://www.w3.org/2006/time#
# imports: http://www.w3.org/ns/dcat#
# imports: http://www.w3.org/ns/prov#
# imports: http://www.w3.org/ns/sosa/
# imports: http://www.w3.org/ns/ssn/
# imports: https://raw.githubusercontent.com/w3c/sdw/gh-pages/ssn-extensions/rdf/ssn-ext.ttl
# imports: https://w3id.org/tern/ontologies/loc/
# imports: https://w3id.org/tern/ontologies/org/
# imports: https://w3id.org/tern/ontologies/sd/
# prefix: tern

@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix doap: <http://usefulinc.com/ns/doap#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <https://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix ssn: <http://www.w3.org/ns/ssn/> .
@prefix tern: <https://w3id.org/tern/ontologies/tern/> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://rs.tdwg.org/dwc/terms/materialSampleID>
  a rdf:Property ;
  rdfs:comment "An identifier for the MaterialSample (as opposed to a particular digital record of the material sample). In the absence of a persistent global unique identifier, construct one from a combination of identifiers in the record that will most closely make the materialSampleID globally unique." ;
  rdfs:isDefinedBy <http://rs.tdwg.org/dwc/terms/> ;
  rdfs:label "material sample ID" ;
.
sosa:isSampleOf
  a owl:TransitiveProperty ;
."""


def test_normalize_changed_true():
    _, changed = normalize(content)
    print(_)
    assert changed


def test_normalize_changed_false():
    content = """# imports: http://datashapes.org/dash
# imports: http://qudt.org/schema/qudt/
# imports: http://rdfs.org/ns/void
# imports: http://www.w3.org/2002/07/owl#
# imports: http://www.w3.org/2004/02/skos/core#
# imports: http://www.w3.org/2006/time#
# imports: http://www.w3.org/ns/dcat#
# imports: http://www.w3.org/ns/prov#
# imports: http://www.w3.org/ns/sosa/
# imports: http://www.w3.org/ns/ssn/
# imports: https://raw.githubusercontent.com/w3c/sdw/gh-pages/ssn-extensions/rdf/ssn-ext.ttl
# imports: https://w3id.org/tern/ontologies/loc/
# imports: https://w3id.org/tern/ontologies/org/
# imports: https://w3id.org/tern/ontologies/sd/
# prefix: tern
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sosa: <http://www.w3.org/ns/sosa/>

<http://rs.tdwg.org/dwc/terms/materialSampleID>
    a rdf:Property ;
    rdfs:label "material sample ID" ;
    rdfs:comment "An identifier for the MaterialSample (as opposed to a particular digital record of the material sample). In the absence of a persistent global unique identifier, construct one from a combination of identifiers in the record that will most closely make the materialSampleID globally unique." ;
    rdfs:isDefinedBy <http://rs.tdwg.org/dwc/terms/> ;
.

sosa:isSampleOf
    a owl:TransitiveProperty ;
.

"""
    _, changed = normalize(content)
    assert not changed


def test_topbraid_metadata():
    metadata = get_topbraid_metadata(content)
    assert metadata == """# baseURI: https://w3id.org/tern/ontologies/tern/
# imports: http://datashapes.org/dash
# imports: http://qudt.org/schema/qudt/
# imports: http://rdfs.org/ns/void
# imports: http://www.w3.org/2002/07/owl#
# imports: http://www.w3.org/2004/02/skos/core#
# imports: http://www.w3.org/2006/time#
# imports: http://www.w3.org/ns/dcat#
# imports: http://www.w3.org/ns/prov#
# imports: http://www.w3.org/ns/sosa/
# imports: http://www.w3.org/ns/ssn/
# imports: https://raw.githubusercontent.com/w3c/sdw/gh-pages/ssn-extensions/rdf/ssn-ext.ttl
# imports: https://w3id.org/tern/ontologies/loc/
# imports: https://w3id.org/tern/ontologies/org/
# imports: https://w3id.org/tern/ontologies/sd/
# prefix: tern"""