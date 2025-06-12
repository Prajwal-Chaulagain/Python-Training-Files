Students_list=[]
n = 1
while n < 3:
   Name = input("Enter the name:")
   Gender = input("Enter the gender (male or female):")
   Field=input("Enter the field:")
   Address=input("Enter the address:")
   obj = {"Name": Name, "Gender": Gender, "Field": Field, "Address": Address}
   Students_list.append(obj)
   n+=1
   
for item in Students_list:
    print("Name",item['Name'])
    print("Gender",item['Gender'])
    print("Field",item['Field'])
    print("Address",item['Address'])
    
    
    
    