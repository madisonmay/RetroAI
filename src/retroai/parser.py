
from lark import Lark


retroai_parser = Lark(r"""
    WHERE: "where"
    CRITERIA: "less than" 
            | "more than" 
            | "is"
            | "is not"
            | ">" 
            | "<" 
            | "=" 
            | "<=" 
            | ">="
            | "!="

    COMPASS_DIRECTION: "north"
                      | "northeast"
                      | "east"
                      | "southeast"
                      | "south"
                      | "southwest"
                      | "west"
                      | "northwest"
    DIRECTIONAL_RELATIONSHIP: "right"
                            | "left"
                            | "above"
                            | "below"
    SPATIAL_RELATIONSHIP: "inside" 
                        | "outside" 
    ORDER_RELATIONSHIP: "before"
                      | "after"
    LENGTH: "length" 
    WIDTH: "width"
    HEIGHT: "height"
    UNIT: "px" 
        | "chars"
    AND: "and"
    OR: "or"
    ALPHANUMERIC: /[a-zA-Z0-9_]+/

    direction: "from"
             | DIRECTIONAL_RELATIONSHIP "of"
             | COMPASS_DIRECTION "of"
             | ORDER_RELATIONSHIP 
    criteria: CRITERIA
    number: NUMBER
    unit: UNIT
    conjunction: AND 
               | OR

    expr: candidate_pool WHERE filter

    relationship: criteria number unit direction?
    relationship_condition: relationship span_set
    length_condition: LENGTH criteria number unit
    size_condition: [WIDTH | HEIGHT] criteria number unit
    condition: relationship_condition | length_condition | size_condition 

    candidate_pool: span_set (conjunction span_set)*
    span_set: "'" ALPHANUMERIC "'"
    clause: "(" condition (conjunction condition)* ")"
    filter: [condition | clause] (conjunction [condition | clause])* 

    %import common.NUMBER -> NUMBER
    %import common.WS
    %ignore WS
    """, 
    start='expr'
)


def parse(s: str):
    return retroai_parser.parse(s)
