from PyInquirer import style_from_dict, Token, Separator

style = style_from_dict({
  Token.Separator: '#cc5454',
  Token.QuestionMark: '#00ff00 bold',
  Token.Selected: '#cc5454',  # default
  Token.Pointer: '#00ff00 bold',
  Token.Instruction: '',  # default
  Token.Answer: '#f44336 bold',
  Token.Question: '',
})

questions = [
  {
    'type': 'list',
    'message': '데이터추출',
    'name': 'extract',
    'choices': [
      'test_data', 'oracle'
    ],
    'validate': lambda answer: 'You must choose at least one extract'
    if len(answer) == 0 else True
  }, 
  {
    'type': 'list',
    'message': '데이터적재',
    'name': 'loader',
    'choices': [
      'print', 'oracle'
    ],
    'validate': lambda answer: 'You must choose at least one loader'
    if len(answer) == 0 else True
  }
]
