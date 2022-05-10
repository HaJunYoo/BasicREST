import json

data = {}
data['Book'] = []
data['Book'].append({
    'Title': 'Python',
    'Authors': ['John','Bob'],
    'Date':'2013',
    'Publisher': 'Springer'
})
data['Book'].append({
    'Title': 'Information System',
    'Authors': ['Andrew','Martin'],
    'Date':'2014',
    'Publisher': 'Elsevier'
})
data['Book'].append({
    'Title': 'Database',
    'Authors': ['Edward','David'],
    'Date':'2016',
    'Publisher': 'Wiley'
})

with open('BookData.json', 'w') as outfile:
    json.dump(data, outfile)
    # Python의 객체를 JSON 문자열로 변환하기 위해서는 dumps() 함수를 사용
    # JSON 문자열을 Python의 객체로 변환하기 위해서는 loads() 함수
    # load() 함수: JSON 파일을 Python 객체로 불러오기
    # dump() 함수: Python 객체를 JSON 파일에 저장하기