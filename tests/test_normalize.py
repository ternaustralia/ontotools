from ontotools.normalize import normalize


def test_normalize_changed_true():
    content = """# baseURI: https://example.com/ontology/

<https://example.com/ontology/Class_1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2000/01/rdf-schema#Class> .
<https://example.com/ontology/Class_1> <http://www.w3.org/2000/01/rdf-schema#label> "Class 1" .
<https://example.com/ontology/Class_1> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.w3.org/2002/07/owl#Class> .
<https://example.com/ontology/Class_1_1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2000/01/rdf-schema#Class> .
<https://example.com/ontology/Class_1_1> <http://www.w3.org/2000/01/rdf-schema#label> "Class 1_1" .
<https://example.com/ontology/Class_1_1> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <https://example.com/ontology/Class_1> .
<https://example.com/ontology/Class_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2000/01/rdf-schema#Class> .
<https://example.com/ontology/Class_2> <http://www.w3.org/2000/01/rdf-schema#label> "Class 2" .
<https://example.com/ontology/Class_2> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.w3.org/2002/07/owl#Class> .    
    """
    _, changed = normalize(content)
    assert changed


def test_normalize_changed_false():
    content = """# baseURI: https://example.com/ontology/
<https://example.com/ontology/Class_1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2000/01/rdf-schema#Class> .
<https://example.com/ontology/Class_1> <http://www.w3.org/2000/01/rdf-schema#label> "Class 1" .
<https://example.com/ontology/Class_1> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.w3.org/2002/07/owl#Class> .
<https://example.com/ontology/Class_1_1> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2000/01/rdf-schema#Class> .
<https://example.com/ontology/Class_1_1> <http://www.w3.org/2000/01/rdf-schema#label> "Class 1_1" .
<https://example.com/ontology/Class_1_1> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <https://example.com/ontology/Class_1> .
<https://example.com/ontology/Class_2> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2000/01/rdf-schema#Class> .
<https://example.com/ontology/Class_2> <http://www.w3.org/2000/01/rdf-schema#label> "Class 2" .
<https://example.com/ontology/Class_2> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://www.w3.org/2002/07/owl#Class> ."""

    _, changed = normalize(content)
    assert not changed
