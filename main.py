import os

#qemu-system-x86_64 -enable-kvm -cpu host -m 2G -boot d storage.qcow2 
#qemu-img create -f qcow2 storage.qcow2 1G
# todo: create yaml/json file holding saved commands. show presets on startup

def create_img():
    try:
        #storage_name = "storage"
        #storage_size = "1G"
        print("Name the storage:")
        storage_name = str(input("> "))
        print("How large (G):")
        storage_size = int(input("> "))
        img_command = ("qemu-img create -f qcow2 "+ str(storage_name)+".qcow2 " + str(storage_size)+"G")
        print(img_command)
        confirm = str(input("does this look right (y/n) \n> "))
        if confirm == 'y':
            os.system(img_command)
        if confirm == 'n':
            img_command = "echo 0"
            create_img()
    except TypeError:
        os.system("clear")
        print("invald input. (TypeError)")
        create_img()
def run_headless():

    iso_name = str(input("iso name: "))
    run_headless_command = ("qemu-system-x86_64 -enable-kvm -cpu host -m 2G -boot d "+ str(iso_name)) 
    print(run_headless_command)
    
    confirm = str(input("does this look right (y/n) \n> "))
    if confirm == 'y':
        os.system(run_headless_command)
    if confirm == 'n':
        run_headless_command = "echo 0"
        run()

def main():
    while True:
        print("""1) Create img
        2) Run iso (without storage)
        3) Run vm
        4) Exit
        """)

        menu = int(input("> "))
        if menu == 1:
            create_img()
        elif menu == 2:
            run_headless()
        elif menu == 3:
            run()
        elif menu == 4:
            os.system("clear")
            exit()
        else:
            print("?")
main()
