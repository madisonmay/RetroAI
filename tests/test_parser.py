from lark import Tree, Token

from retroai import parse

def test_parser():
    parsed = parse("'date_regex' where less than 5 px from 'date_keyphrase'")
    print(parsed.pretty())
    assert isinstance(parsed, Tree)

def test_conjunctions():
    parsed = parse(
        "'date' where less than 100 px southeast of 'date_keyphrase' "
        "or less than 50 chars from 'date_keyphrase'"
    )
    print(parsed.pretty())
    assert isinstance(parsed, Tree)

def test_clause():
    parsed = parse(
        "'price' where less than 100 px southeast of 'due_date_keyphrase' "
        "or (less than 50 chars from 'due_date_keyphrase' and more than 50 chars from 'invoice_date_keyphrase')"
    )
    print(parsed.pretty())
    assert isinstance(parsed, Tree)

def test_mix_and_match_conditions():
    parsed = parse(
        "'title' where width > 100 px and length > 10 chars"
    )
    print(parsed.pretty())
    assert isinstance(parsed, Tree)