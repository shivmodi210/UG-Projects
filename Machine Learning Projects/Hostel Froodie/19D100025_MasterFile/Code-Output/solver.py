from pulp import *

def mess_plan(menu_items,meal_weights,weight,goal,CalPD):
    
    problem_name="Meal_plan"
    if goal=="G":
        prob= pulp.LpProblem(problem_name,LpMinimize)
    else:    
        prob= pulp.LpProblem(problem_name,LpMaximize)
    decision_var=[]
    # decision variables
    for i in range(len(menu_items)):
        variable=str('x'+str(i+1))
        if menu_items[i][0].split(",")[0]=="None":
            variable=pulp.LpVariable(str(variable),lowBound=0,upBound=0,cat='Integer')
        elif menu_items[i][0].split(",")[0]!="Roti" and menu_items[i][0].split(",")[0]!="Bread-Butter":
            variable=pulp.LpVariable(str(variable),lowBound=0,upBound=3,cat='Integer')
        else:
            variable=pulp.LpVariable(str(variable),lowBound=0,upBound=7,cat='Integer')
        decision_var.append(variable)

        
    
    total=""
    # objective function
    for i in range(len(menu_items)):
        expr=menu_items[i][-1][-1]*decision_var[i]/meal_weights[i]  
#        expr=menu_items[i][-1][-1]*decision_var[i]/meal_weights[i]**2   for second solution
        total+=expr
        
    prob += total
    
    #constraints
    # nutritional value wise constraint
    for j in range(3):
        total=""
        for i in range(len(menu_items)):
            expr=menu_items[i][-1][j+1]*decision_var[i]
            total+=expr
        if j==1:
            prob+=(total<=2.5*weight)
            prob+=(total>=0.5*weight)            
        if j==0:    
            prob+=(total<=2*weight)
            prob+=(total>=1*weight)
        if j==2:    
            prob+=(total<=CalPD)
            prob+=(total>=0.95*CalPD)
    
    #meal wise distribution constraint
    i=0
    total=""
    while menu_items[i][0].split(",")[-1]=="Breakfast":   
        expr=menu_items[i][-1][3]*decision_var[i]
        total+=expr
        i+=1
    
    prob+=(total<=0.3*CalPD)
    prob+=(total>=0.25*CalPD)
    
    
    total=""
    while menu_items[i][0].split(",")[-1]=="Lunch":     
        expr=menu_items[i][-1][3]*decision_var[i]
        total+=expr
        i+=1
    prob+=(total<=0.3*CalPD)
    prob+=(total>=0.25*CalPD)
    total=""
    while menu_items[i][0].split(",")[-1]=="Tiffin":     
        expr=menu_items[i][-1][3]*decision_var[i]
        total+=expr
        i+=1
    prob+=(total<=0.15*CalPD)
    prob+=(total>=0.1*CalPD)
    total=""
    while menu_items[i][0].split(",")[-1]=="Dinner":     
        expr=menu_items[i][-1][3]*decision_var[i]
        total+=expr
        i+=1
        if(i>=len(menu_items)):
            break
    
    prob+=(total<=0.3*CalPD)
    prob+=(total>=0.25*CalPD)
    #meal wise weight distribution constraint
    i=0
    total=""
    while menu_items[i][0].split(",")[-1]=="Breakfast":   
        expr=menu_items[i][-1][-1]*decision_var[i]
        total+=expr
        i+=1
    
    prob+=(total<=15*weight)
    prob+=(total>=5*weight)
    
    
    total=""
    while menu_items[i][0].split(",")[-1]=="Lunch":     
        expr=menu_items[i][-1][-1]*decision_var[i]
        total+=expr
        i+=1
    prob+=(total<=15*weight)
    prob+=(total>=5*weight)
    total=""
    while menu_items[i][0].split(",")[-1]=="Tiffin":     
        expr=menu_items[i][-1][-1]*decision_var[i]
        total+=expr
        i+=1
    prob+=(total<=15*weight)
    prob+=(total>=5*weight)
    total=""
    while menu_items[i][0].split(",")[-1]=="Dinner":     
        expr=menu_items[i][-1][-1]*decision_var[i]
        total+=expr
        i+=1
        if(i>=len(menu_items)):
            break
    
    prob+=(total<=15*weight)
    prob+=(total>=5*weight)
    
    #food likeability constraints
    #milk juice constraints
    total=""
    expr = decision_var[0]+decision_var[1]+decision_var[20]
    total+=expr
    prob+=(total<=1)
    #banana bhurji omlette constraint
    total=""
    expr = decision_var[2]+decision_var[3]+decision_var[4]+decision_var[5]
    total+=expr
    prob+=(total<=3)
    #bread-butter and jam constraints
    total=""
    expr = decision_var[8]+decision_var[9]
    total+=expr
    prob+=(total<=decision_var[7])
    # vegetable roti rice constraint    
    total=""
    expr = decision_var[13]+decision_var[14]+decision_var[15]
    total+=expr
    prob+=(total<=(0.67*decision_var[17]+decision_var[16]))
    prob+=(total>=(0.33*decision_var[17]+decision_var[16]))
    #bread-butter and jam constraints
    total=""
    expr = decision_var[24]
    total+=expr
    prob+=(total<=decision_var[23])
    # vegetable roti rice constraint    
    total=""
    expr = decision_var[26]+decision_var[27]+decision_var[29]
    total+=expr
    prob+=(total<=(0.67*decision_var[31]+decision_var[28]+decision_var[32]))
    prob+=(total>=(0.33*decision_var[31]+decision_var[28]+decision_var[32]))
    #fruit constraint
    total=""
    expr = decision_var[35]+decision_var[34]
    total+=expr
    prob+=(total<=2)
    
    prob.solve()
    output=[]
    for i in range(len(menu_items)):
        output.append(0)
    for i, v in enumerate(prob.variables()):
        val=int(v.name[1:])
        output[val-1]=([menu_items[val-1][0],v.varValue])
    return output

def preferance(pref,food_item_weights,food_menu):
    food_item_weights_user={}
    for i in range(len(food_menu[0])):
        if food_menu[0][i]!="Weekly":
            total=0
            for j in range(len(pref)):
                total+=pref[j][i]
            if total!=0:
                var=food_menu[2][i]+","+food_menu[1][i]
                food_item_weights_user[var]=total/28
            else:
                var=food_menu[2][i]+","+food_menu[1][i]
                food_item_weights_user[var]=0.01
        else:
            for j in range(7):
                total=0
                for k in range(4):
                    total+=pref[7*k+j][i]
                if total!=0:
                    var=food_menu[j+2][i]+","+food_menu[1][i]
                    food_item_weights_user[var]=total/4
                else:
                    var=food_menu[j+2][i]+","+food_menu[1][i]
                    food_item_weights_user[var]=0.01
            
    return food_item_weights_user

