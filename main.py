import boto3

client = boto3.client('ec2')

print("Which one do you want to stop?\n")
print("1: Master            2: Slave")
Num = int(input())

if Num == 1:
    response = client.stop_instances(
        InstanceIds=[
            'i-07e66349b31807962',
        ],
    )
    print('Done!\n\n')
elif Num == 2:
    response = client.stop_instances(
        InstanceIds=[
            'i-0770e98d5789bd13a',
        ],
    )
    print('Done!\n\n')


def Main_menu(): #메인 메뉴 구성
    print('-------------------------------------------------\n')
    print('  1. list instance       2. available zones\n')
    print('  3. start instance      4. available regions\n')
    print('  5. stop instance       6. create instance\n')
    print('  7. reboot instance     8. list images\n')
    print('                         99. quit\n')
    print('-------------------------------------------------')
    

def list_instance(): #1번 기능 id list 출력
    response = client.start_instances(
        InstanceIds=[
            'i-07e66349b31807962', #master
            'i-0770e98d5789bd13a', #slave
        ],
    )
    for i in range(2):
        pr = response.get('StartingInstances')[i].get('InstanceId')
        print(pr)
    print('\n\n')

def available_zones(): #2번 기능
    print('available zones')
    
def start_instance(): #3번 기능 instance 시작
    print("Which one do you want to start?\n")
    print("1: Master & Slave     2: Slave")
    Num = int(input())

    if Num == 1:
        response = client.start_instances(
            InstanceIds=[
                'i-07e66349b31807962', #master
            ],
        )
        print('Done!\n\n')
    elif Num == 2:
        response = client.start_instances(
            InstanceIds=[
                'i-0770e98d5789bd13a', #slave
            ],
        )
        print('Done!\n\n')

def available_regions():
    print('available regions')

def stop_instance(): #5번 기능 instance 시작
    print("Which one do you want to stop?\n")
    print("1: Master            2: Slave")
    Num = int(input())

    if Num == 1:
        response = client.stop_instances(
            InstanceIds=[
                'i-07e66349b31807962', #master
            ],
        )
        print('Done!\n\n')
    elif Num == 2:
        response = client.stop_instances(
            InstanceIds=[
                'i-0770e98d5789bd13a', #slave
            ],
        )
        print('Done!\n\n')

def create_instance():
    print('create instance')

def reboot_instance():
    print('7. reboot instance')
    
def list_images():
    print('list images')

def exit():
    quit()

#while(True):
while(False):
    Main_menu()
    Num = int(input())
    if Num == 1:
        list_instance()
    elif Num == 2:
        available_zones()
    elif Num == 3:
        start_instance()
    elif Num == 4:
        available_regions()
    elif Num == 5:
        stop_instance()
    elif Num == 6:
        create_instance()
    elif Num == 7:
        reboot_instance()
    elif Num == 8:
        list_images()
    elif Num == 99:
        exit()
    else:
        print("Error\n")