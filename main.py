import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

print('Available regions ....')
available_region = client.describe_regions()
for available_region in ec2.instances.all():
    state = available_region.regions
    print(state)



def Main_menu(): #메인 메뉴 구성
    print('-----------------------------------------------------------')
    print('    1. list instance               2. available zones')
    print('    3. start instance              4. available regions')
    print('    5. stop instance               6. create instance')
    print('    7. reboot instance             8. list images')
    print('                                   99. quit')
    print('-----------------------------------------------------------')
    
#1번 기능 id list 출력
def list_instance(): 
    '''
    response = client.describe_instances(
        InstanceIds=[
            'i-07e66349b31807962', #master
            'i-0770e98d5789bd13a', #slave
        ]
    )
    print('Listing instances....')
    for instance in range(2):
        imageid = response.get('Reservations')[instance].get('Instances')[0].get('ImageId')
        id = response.get('Reservations')[instance].get('Instances')[0].get('InstanceId')
        type = response.get('Reservations')[instance].get('Instances')[0].get('InstanceType')
        state = response.get('Reservations')[instance].get('Instances')[0].get('State').get('Name')
        monitoring = response.get('Reservations')[instance].get('Instances')[0].get('Monitoring').get('State')
        print(f'[id] {id}, [AMI] {imageid}, [type] {type}, [state] {state}, [motinoring state] {monitoring}')
    print()
    '''
    for instance in ec2.instances.all():
        state = instance.state.get('Name')
        monitoring = instance.monitoring.get('State')
        print(f'[id]  {instance.instance_id} , [AMI]  {instance.image_id}, [type]  {instance.instance_type}, [state]  ', end='')
        print(state, end='')
        print(', [monitoring state]  ', end='')
        print(monitoring)
    print()
    
#2번 기능
def available_zones(): 
    print('available zones')
    
def start_instance(): #3번 기능 instance 시작
    idInput = input("Enter instance id: ")
    response = client.start_instances(InstanceIds=[idInput])
    print(f'Starting .... {idInput}')
    print(f'Successfully started instance  {idInput}\n')
        
def available_regions(): #4번 기능
    '''
    response = client.describe_regions(RegionNames=['us-east-2'])
    pr1 = response.get('Regions')[0].get('Endpoint')
    pr2 = response.get('Regions')[0].get('RegionName')
    print(f"Endpoint : {pr1}")
    print(f"RegionName : {pr2}\n")
    '''
    
    
    
def stop_instance(): #5번 기능 instance 중지
    idInput = input("Enter instance id: ")
    response = client.stop_instances(InstanceIds=[idInput])
    print(f'Successfully stop instance  {idInput}\n')

def create_instance(): #6번 기능
    print('create instance')

def reboot_instance(): #7번 기능 instance 재부팅
    idInput = input("Enter instance id: ")
    response = client.reboot_instances(InstanceIds=[idInput])
    print(f'Rebooting .... {idInput}')
    print(f'Successfully rebooted instance  {idInput}\n')
    
def list_images(): #8번 기능
    print('list images')

def exit():
    quit()

#while(True):
while(False):
    Main_menu()
    Num = int(input("Enter an integer: "))
    if Num == 1: #doneVV
        list_instance()
    elif Num == 2:
        available_zones()
    elif Num == 3: #doneVV
        start_instance()
    elif Num == 4: #done
        available_regions()
    elif Num == 5: #doneVV
        stop_instance()
    elif Num == 6:
        create_instance()
    elif Num == 7: #doneVV
        reboot_instance()
    elif Num == 8:
        list_images()
    elif Num == 99: #doneVV
        exit()
    else:
        print("Error\n")