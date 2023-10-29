def towerofhanoi(n,from_rod,to_rod,aux_rod):
    if n==1:
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        move_disks(from_rod,to_rod)
        return
    towerofhanoi(n-1,from_rod,aux_rod,to_rod)
    move_disks(from_rod,to_rod)
    towerofhanoi(n-1,aux_rod,to_rod,from_rod)
def move_disks(from_rod,to_rod):
    disk=rods[from_rod].pop()
    rods[to_rod].append(disk)
    print_rods_state()
def print_rod_state(rod_name,disks):
    print(rodname,":",disks)
def print_rods_state():
    for rod_name,disks in rods.items():
        print_rod_state(rod_name,disks)
    print()    
n=int(input("enter no.of rods"))
rods={
       'A':list(range(n,0,-1)),
       'B':[],
       'C':[]
}
print_rods_state()
towerofhanoi(n,'A','C','B')       
     
               
        
                 










