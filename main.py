import api
import json

if __name__ == '__main__':
    resp = api.Request_Data('http://api.tianapi.com/ncov/index', '2020-05-28').Get_Info()
    resp_dict = json.loads(resp)
    print(resp_dict)
    # print(resp_json['type'])
