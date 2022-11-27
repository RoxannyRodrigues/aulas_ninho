

Frutas= [
    'maça', 'melancia', 'maça',  'goiaba',
    'maça', 'melancia', 'goiaba',
    'maça',  'uva', 'goiaba',
    'uva', 'melancia', 'uva', 'goiaba',
    'maça', 'uva', 'goiaba'
]

from collections import Counter
contagem_frutas = Counter(Frutas)
total_igual = contagem_frutas.most_common(4)
print(total_igual)

