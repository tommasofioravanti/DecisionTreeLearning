class DataSet:
    """A data set for a machine learning problem. It has the following fields:
    d.examples   A list of examples. Each one is a dictionary of attribute values.

    d.attrs      A list of integers to index into an example, so example[attr] 
                 gives a value. Normally the same as range(len(d.examples[0])).

    d.attrnames  A dictionary that identifies {attr: attrname,..}  for all d.attrs.

    d.target     The attribute that a learning algorithm will try to predict.
                 By default the final attribute.
    d.inputs     The list of attrs without the target.
    
    d.values     A dictionary that identifies every possible value for all d.attrs {attr: [value1,value2,..]}."""

    def __init__(self, name = '', examples = None, inputs = None, attributes = None, target = None, attrnames=None, values=None):
        self.name = name
        self.examples = examples
        self.target = target
        self.values = values
        self.inputs = inputs

        if attributes is None and self.examples is not None:
            attributes = list(range(len(self.examples[0])))
        self.attributes = attributes

        if isinstance(attrnames, str):
            self.attrnames = attrnames.split()
        else:
            self.attrnames = attrnames or attributes