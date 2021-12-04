import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

def Main_menu(): #메인 메뉴 구성
    print('---------------------------------------------------------------')
    print('      1. list instance               2. available zones')
    print('      3. start instance              4. available regions')
    print('      5. stop instance               6. create instance')
    print('      7. reboot instance             8. list images')
    print('                                     99. quit')
    print('---------------------------------------------------------------')
    
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
    
#2번 기능 zone 찾기
def available_zones(): 
    available_zone = client.describe_availability_zones()
    count_num = 0
    for i in range(1000):
        try:
            if available_zone.get('AvailabilityZones')[i].get('RegionName').find("-") != -1:
                count_num = count_num + 1
        except:
            continue
    print('Available Zones ....')
    for i in range(count_num):  
        RegionName = available_zone.get('AvailabilityZones')[i].get('RegionName')
        ZoneName = available_zone.get('AvailabilityZones')[i].get('ZoneName')
        ZoneId = available_zone.get('AvailabilityZones')[i].get('ZoneId')
        print(f'[id]  {ZoneId}, [region]  {RegionName}, [zone]  {ZoneName}')
    #print(available_zone) #디버깅

#3번 기능 instance 시작
def start_instance():
    idInput = input("Enter instance id: ")
    response = client.start_instances(InstanceIds=[idInput])
    print(f'Starting .... {idInput}')
    print(f'Successfully started instance  {idInput}\n')

#4번 기능 regions 찾기
def available_regions(): 
    '''
    response = client.describe_regions(RegionNames=['us-east-2'])
    pr1 = response.get('Regions')[0].get('Endpoint')
    pr2 = response.get('Regions')[0].get('RegionName')
    print(f"Endpoint : {pr1}")
    print(f"RegionName : {pr2}\n")
    '''
    available_region = client.describe_regions()
    count_num = 0
    for i in range(1000):
        try:
            if available_region.get('Regions')[i].get('Endpoint').find("-") != -1:
                count_num = count_num + 1
        except:
            continue
    print('Available regions ....')
    for i in range(count_num):  
        endpoint = available_region.get('Regions')[i].get('Endpoint')
        regionname = available_region.get('Regions')[i].get('RegionName')
        print(f'[region]  {regionname}, [endpoint]  {endpoint}')
    #print(available_region) #디버깅
    
#5번 기능 instance 중지
def stop_instance():
    idInput = input("Enter instance id: ")
    response = client.stop_instances(InstanceIds=[idInput])
    print(f'Successfully stop instance  {idInput}\n')

#6번 기능 instance 생성
def create_instance():
    idInput = str(input("Enter ami id:  "))
    response = ec2.create_instances(ImageId=idInput, MaxCount=1, MinCount=1, InstanceType='t2.micro')
    print(f'Successfully started EC2 instance {response[0].instance_id} based on AMI {idInput}\n')

#7번 기능 instance 재부팅
def reboot_instance(): 
    idInput = input("Enter instance id: ")
    response = client.reboot_instances(InstanceIds=[idInput])
    print(f'Rebooting .... {idInput}')
    print(f'Successfully rebooted instance  {idInput}\n')

#8번 기능 image 리스트
def list_images(): 
    find_image = client.describe_images(Owners=['self'])
    for image in find_image['Images']:
        print('[ImageID] ' + image['ImageId'], end='')
        print(', [Name] ' + image['Name'], end='')
        print(', [Owner] '+ image['OwnerId'])
    print()

#메인 메뉴 실행
while(True):
    Main_menu()
    Num = int(input("Enter an integer: "))
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
        quit()
    else:
        print("Error occur. Try again another number\n")