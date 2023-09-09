# write your code here
person = {
    'name' : 'omar',
    'age' : 28,
    'hobbies' : ['reading', 'swimming', 'hiking', 'tennis']

}
print(person['name'])
print(person['age'])
person['age'] = 30
person['country'] = 'algeria'
print(len(person))
person['hobbies'].append('coding')
print(person)
def check_hobbies(person):
    if len(person['hobbies']) > 3:
        print('wow you are amazing')
    else:
        print(':)')
check_hobbies(person)

