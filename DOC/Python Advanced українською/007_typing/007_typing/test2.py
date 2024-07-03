from typing import NewType, Union


UserId = NewType('UserId', int)
AccountId = NewType('AccountId', str)
ProfileId = NewType('ProfileId', str)
ComplexId = NewType('ComplexId', Union[int, str])

some_id = UserId(522135)


def find_account(entity_id: AccountId):
    return f'{entity_id}'


def find_profile(entity_id: ProfileId):
    return f'{entity_id}'


def my_convert(obj1: ComplexId):
    return f'{obj1}'


id1: AccountId = AccountId('123')
id2: ProfileId = ProfileId('234')

print(find_account(id1))
print(find_profile(id2))
print(my_convert(id1))
print(find_profile(id1))
