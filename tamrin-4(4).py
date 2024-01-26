class matab:
    patients = {}
    visit_time = {}
    lst_visit = []
    def __init__(self):
       pass
    def add_Patient(self,id,name,familyname,age,height,weight):
        self.id = id
        self.name = name
        self.familyname = familyname
        self.age = age
        self.height = height
        self.weight = weight
        if self.id in matab.patients.keys():
            print('error: this ID already exists')
            return
        elif self.age < 0:
            print("error: invalid age")
            return
        elif self.height < 0:
            print('error: invalid height')
            return
        elif self.weight < 0:
            print('error: invalid weight')
            return
        else:
            print('patient added successfully') 
            matab.patients[self.id] = [self.name, self.familyname, self.age, self.height, self.weight]
    def display_patient(self,id):
        self.id = id
        if int(self.id) not in matab.patients.keys():
            print('error: invalid ID')
        else:
            print(f'''patient name: {matab.patients[self.id][0]}
patient family name: {matab.patients[self.id][1]}
patient age: {matab.patients[self.id][2]}
patient height: {matab.patients[self.id][3]}
patient weight: {matab.patients[self.id][4]}'''
            )
    def add_visit(self,id,time):
        self.id = id
        self.time = time
        if self.id not in matab.patients.keys():
            print('error: invalid id')
        elif self.time < 9 or self.time > 18:
            print('error: invalid time')
        elif self.time in matab.lst_visit:
            print('error: busy time')
        else:
            if self.id in matab.visit_time.keys():
                matab.visit_time[self.id].append(self.time)
                print('visit added successfully!')
            else:   
                print('visit added successfully!')
                matab.visit_time[self.id] = [self.time]
                for i in matab.visit_time[self.id]:
                    matab.lst_visit.append(i)
    def delete_patient(self,id):
        self.id = id
        if int(self.id) in matab.patients.keys():
            matab.patients[int(self.id)] = ''
            if int(self.id) in matab.patients.keys():
                matab.visit_time[int(self.id)] = ''
            print('patient deleted successfully!')
        else:
            print('error: invalid id')
    def display_visit_list(self):
        print('SCHEDULE:')
        if len(matab.visit_time.keys()) > 0:
            for i in matab.visit_time.keys():
                for j in matab.visit_time[i]:
                    print(f'{j}:00 {matab.patients[i][0]} {matab.patients[i][1]}')
while True:
    p = matab()
    try:
        entry = input().split()
        if entry[0] == 'exit':
            break
        if entry[0] == 'add' and entry[1] == 'patient':
            p.add_Patient(int(entry[2]),entry[3],entry[4],int(entry[5]),int(entry[6]),int(entry[7]))
        elif entry[0] == 'display' and entry[1] == 'patient':
            p.display_patient(int(entry[2]))
        elif entry[0] == 'add' and entry[1] == 'visit':
            p.add_visit(int(entry[2]),int(entry[3]))
        elif entry[0] == 'delete' and entry[1] == 'patient':
            p.delete_patient(entry[2])
        elif entry[0] == 'display' and entry[1] == 'visit' and entry[2] == 'list':
            p.display_visit_list()
        else:
            print('invalid command')
    except:
        print('invalid command')