import vk_api
import loaderconfig
import json
import os

def auth_handler():
    """ 
    При двухфакторной аутентификации вызывается эта функция.
    """
    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True
    return key, remember_device

def stop_f(items):
    print (items)
    
def main():
    data = loaderconfig.get_data()
    login, password = data["vk"]["login"], data["vk"]["password"]
    vk_session = vk_api.VkApi(
    login, password,
    auth_handler=auth_handler
    )
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
    
    tools = vk_api.VkTools(vk_session)
    vk_app = vk_session.get_api()
    # print(vk_app.wall.post(message='Hello vk_api!'))
    
    group_id = int(data["vk"]["group_id"])
    wall = tools.get_all("wall.get", 100, {"owner_id": group_id})
    
    print('Posts count:', wall['count'])
    
    with open(r"wall_asp.txt","a") as f:
        f.write(json.dumps(wall))

if __name__ == '__main__':
    main()