user={
    'ferit':{
    'age':21,
    'gender':'male',
    'job':'developer'
    }
    ,'mary':{
        'age':19,
        'gender':'female',
        'job':'nurse'
    },
    'carl':{
        'age':25,
        'gender':'male',
        'job':'teacher'
    }
    }

print(user['mary'])
print(user['carl']['age'])
print(user['carl']['job'])

user['jesus']={
    'age':23,
    'gender':'male',

    'educations': {
        'primary school':'havarik',
        'high school':['muradiye analdolu','şehit tahsin barutçu anadolu'],
        'university':'medeniyet'
    }
}

print(user['jesus'])