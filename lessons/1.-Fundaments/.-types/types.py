text: str = 'Hi mom!'
integer: int = 1
double: float = 1.0

# Python does not check type safety
integer: int = 1.0
double: float = '1.0'

# Types are also implied, meaning that there's no inmediate difference to these lines
text: str = 'Typed'
text = '"Un"Typed'
