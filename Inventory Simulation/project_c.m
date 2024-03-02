% IE630M Assignment
% Roll no.: 190260039	Name: Shah Heetak Jayesh 
% Roll no.: 19D100011	Name: Modi Shivkumar Ashokbhai		
% Topic 1	Option C

function [] = project_c(M, L, factor1)  % Takes input as value of M, L and level of factor 1 i.e. 1 for level 1 and 2 for level 2.
                                        % Gives output as fill rate and mean monthly cost
infinity = 10000000000;                 % 1 unit time is 0.01 monnth
lambda = 15;
orderCost = 60;
costOfItem = 5;
rushOrderCost = 120;
rushCostOfItem = 12;
f = 0;
b = 0;
t1 = infinity;
t2 = infinity;
t3 = infinity;
i = M;
cost = 0;
q1 = 0;
q2 = 0;
X = exprnd(1/lambda);
if X < 0.01
    t3 = 0;
end
if X >= 0.01
    t3 = (round(100*X));
end
Y = rand;
if Y < 0.5 || Y == 0.5
    demand = 1;
end
if Y > 0.5 && (Y < 0.75 || Y == 0.75)
    demand = 2;
end
if Y > 0.75 && (Y < 0.875 || Y == 0.875)
    demand = 3;
end
if Y > 0.875 && (Y < 1 || Y == 1)
    demand = 4;
end 
if factor1 == 1
    for t0=0:11200
        if t0 == 1200
            cost = 0;
        end
        if t0 == t1
            i = (i + q1);
            q1 = 0;
            t1 = infinity;
        end
        if t0 == t2
            i = i + q2;
            q2 = 0;
            t2 = infinity;
        end
        if t0 == t3
            if i < demand
                if i > 0
                    f = f + i;
                    b = b + demand - i; 
                end
                if i < 0
                    b = b + demand;
                end
                i = i - demand;
                cost = cost - (i*4);
            end
            if i > demand || i == demand
                i = i - demand;
                f = f + demand;
            end
            X = exprnd(1/lambda);
            if X < 0.01
                t3 = t0 + 1;
            end
            if X >= 0.01
                t3 = t0 + (round(100*X));
            end
            Y = rand;
            if Y < 0.5 || Y == 0.5
                demand = 1;
            end
            if Y > 0.5 && (Y < 0.75 || Y == 0.75)
                demand = 2;
            end
            if Y > 0.75 && (Y < 0.875 || Y == 0.875)
                demand = 3;
            end
            if Y > 0.875 && (Y < 1 || Y == 1)
                demand = 4;
            end 
        end
        if mod(t0,100) == 0
            if i < 0 || i == 0
                Y = rand;
                Y = Y*0.15;
                t1 = t0 + 100*(round(Y,2) + 0.1);
                q1 = M - i;
                cost = cost + rushOrderCost + (rushCostOfItem * q1);
            end
            if i < L && q1 == 0
                Y = rand;
                t2 = t0 + 100*(round(Y,2) + 0.25);
                q2 = M - i;
                cost = cost + orderCost + (costOfItem * q2);
            end
            cost = cost + i;%Holding Cost.
        end
    end
end
if factor1 == 2
    for t0=0:11199
        if t0 == 1200
            cost = 0;
            %cost1 = cost1 + (cost - cost2);
            %disp(cost1)
            %disp(cost - cost2)
        end
        if t0 == t1
            %disp(i)
            i = (i + q1);
            q1 = 0;
            t1 = infinity;
        end
        if t0 == t2
            %disp(i)
            i = i + q2;
            q2 = 0;
            t2 = infinity;
        end
        if t0 == t3
            if i < demand
                if i > 0
                    f = f + i;
                    b = b + demand - i; 
                end
                if i < 0
                    b = b + demand;
                end
                i = i - demand;
                cost = cost - (i*4);
            end
            if i > demand || i == demand
                i = i - demand;
                f = f + demand;
            end
            X = exprnd(1/lambda);
            if X < 0.01
                t3 = t0 + 1;
            end
            if X >= 0.01
                t3 = t0 + (round(100*X));
            end
            Y = rand;
            if Y < 0.5 || Y == 0.5
                demand = 1;
            end
            if Y > 0.5 && (Y < 0.75 || Y == 0.75)
                demand = 2;
            end
            if Y > 0.75 && (Y < 0.875 || Y == 0.875)
                demand = 3;
            end
            if Y > 0.875 && (Y < 1 || Y == 1)
                demand = 4;
            end 
        end
        if i < 0 || i == 0 && q1 == 0
            Y = rand;
            %disp(Y)
            Y = Y*0.15;
            t1 = t0 + 100*(round(Y,2) + 0.1);
            q1 = M - i;
            cost = cost + rushOrderCost + (rushCostOfItem * q1);
        end
        if i < L-1 && q1 == 0 && q2 == 0
            Y = rand;
            %disp(Y)
            t2 = t0 + 100*(round(Y,2) + 0.25);
            q2 = M - i;
            cost = cost + 90 + (costOfItem * q2);
        end
        if mod(t0, 100) == 0
            cost = cost + i;               %Holding Cost.
        end
    end  
end
fill_rate = (f*100)/(f+b);
mean_cost = cost/100;
disp(fill_rate)
disp(mean_cost)
end