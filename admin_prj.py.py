#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
class restaurant:
  def __init__(self):
    self.foods={}
    self.food_id=len(self.foods)
  
 # admin functionality
  def food_items(self):
    self.Name=input("Enter food name:")
    self.Quantity=int(input("Enter the quantity:"))
    self.Price=int(input("Enter the food price:$"))
    self.Discount=int(input("enter the discount:%"))
    self.Stock=int(input("Enter the stock:kg"))
    self.item={"Name":self.Name,"Quantity":self.Quantity,"Price":self.Price,"Discount":self.Discount,"Stock":self.Stock}
    self.food_id=len(self.foods)+1
    self.foods[self.food_id]=self.item
    print(self.foods)
    with open("food_items.json","w") as f:
        json.dump(self.foods,f)
    print("Item added successfully")
    print("************************************************************************************************************")
    
  def remove_food_items(self):
    del self.foods[int(input("Enter the food_id you want to delete from menu"))]
    print("Remaining items are",self.foods)
    with open("food_items.json","w") as f:
        json.dump(self.foods,f)
    print("************************************************************************************************************")
      
                          
  def edit_food_items(self):
    f_id=int(input("Enter the food_id you want to edit"))     
    for i in self.foods[f_id]:
           self.foods[f_id][i]=input("Enter the data that you want to edit:")    
    print(self.foods)
    with open("food_items.json","w") as f:
           json.dump(self.foods,f)         
    print("food_item edited successfully")
    print("************************************************************************************************************")
    
  def view_food_items(self):
    print("list of all food items")
    for i in self.foods:
        print("food_id :" ,i,"\n**************************************")
        for j in self.foods[i]:
            print(j,":",self.foods[i][j])


    print("************************************************************************************************************")
    






x=restaurant()
x.food_items()
print("************************************************************************************************************")
x.food_items() 
print("************************************************************************************************************")    
x.food_items()
print("************************************************************************************************************")
x.remove_food_items()
print("************************************************************************************************************")
x.edit_food_items()   
print("************************************************************************************************************")
x.view_food_items()   
print("************************************************************************************************************")
    


# In[ ]:





# In[ ]:




